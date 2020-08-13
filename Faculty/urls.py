from django.urls import path
from Faculty import views


urlpatterns=[
        

         path('index/',views.index,name="index"),
         path('register/',views.register,name="register"),
         path('about/',views.about,name="about"),
         path('signup/',views.signup,name="signup"),
         path('show/',views.show,name="show"),
         path('edit/<int:id>',views.edit,name="edit"),
         path('delete/<int:id>',views.delete,name="delete"),

   ]