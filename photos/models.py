from io import BytesIO
from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField, IntegerField, NullBooleanField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

from django.core.files.base import ContentFile
from PIL import Image
import numpy as np
# import cv2

# Create your models here.

class Category(models.Model) : 
    name = CharField(max_length=50,null=True,blank=True)
    
    class Meta : 
        ordering = ['name']
    
    def __str__(self) :
        return self.name


class Photos(models.Model) : 
    name = CharField(max_length=50)
    category = ForeignKey(Category , on_delete=SET_NULL , null=True)
    image = ImageField(null=False,blank=False)
    type = IntegerField(verbose_name = "Convert", null=True , blank=True)
    
    class Meta : 
        ordering = ["category"]
        
    
    def save(self,*args,**kwargs) :
          
        pil_img = Image.open(self.image)
        cv_img = np.array(pil_img)
        
        cartoon = cv_img
        
        
    #     #      Sketch 
    #     # print(self.type)    
    #     # print(type(self.type)) 
        
    #     cartoon = cv2.resize(cartoon,(594,456))
        
    #     if self.type == '1' : 
            
    #         grey = cv2.cvtColor(cv_img , cv2.COLOR_RGB2GRAY)
    #         invert = 250 - grey
    #         blurred = cv2.GaussianBlur(invert , (21,21),0)
    #         invertedblurred = 255 - blurred
            
    #         cartoon = cv2.divide(grey , invertedblurred, scale=250.0)

    #     #      Cartoonify
    #     elif self.type == '2' :   
            
    #         grey = cv2.cvtColor(cv_img,cv2.COLOR_BGR2GRAY)
    #         grey = cv2.medianBlur(grey , 5)
    #         edges = cv2.adaptiveThreshold(grey , 255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 5 , 9)

    #         color = cv2.bilateralFilter(cv_img ,50,20,20)
    #         cartoon = cv2.bitwise_and(color , color ,mask=edges )

    #         grey = cv2.cvtColor(cv_img , cv2.COLOR_RGB2GRAY)
    #         invert = 250 - grey
    #         blurred = cv2.GaussianBlur(invert , (21,21),0)
    #         invertedblurred = 255 - blurred
    #         cartoon = cv2.divide(cartoon , cv2.cvtColor(invertedblurred,cv2.COLOR_GRAY2BGR), scale=250.0)


                    
      
        
     
        
        im_pil = Image.fromarray(cartoon)
        
        buffer = BytesIO()
        im_pil.save(buffer,format='png')
        image_png = buffer.getvalue()

        self.image.save(str(self.image),ContentFile(image_png),save = False)
        
        super().save(*args,**kwargs)
    
    def __str__(self) :
        return self.name
    