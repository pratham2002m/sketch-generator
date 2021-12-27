from django.conf import settings
from django.urls import path
from django.conf.urls import url 
from django.views.static import serve
from . import views

urlpatterns = [
    path('',views.gallery , name='gallery'),
    # path('photo/<int:pk>/',views.photo , name='photo'),
    # path('delete/<int:pk>/',views.delete , name='delete'),
    # url(f'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    # path('add/',views.add , name='add'),
]