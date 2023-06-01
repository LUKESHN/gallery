from django.urls import path
from .import views
urlpatterns=[
    path('',views.home_view.as_view(),name='home'),
    path('register/',views.register_view.as_view(),name="register"),
    path('signout/',views.signout_view,name='signout'),
    path('gallery/',views.gallery_view.as_view(),name='gallery'),
    path('addimage/',views.addimage_view.as_view(),name='addimage'),
    path('cat/<int:id>/',views.Cat_view.as_view(),name='cat'),
    path('myupload/',views.myupload_view.as_view(),name='myupload'),
    
    

]
