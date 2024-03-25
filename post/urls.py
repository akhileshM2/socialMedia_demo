from django.urls import path,include
from. import views
urlpatterns = [path('create/',views.create_post,name="create_post"),
               path("feed/",views.feed,name="feed"),
               path('like/',views.like_post,name="like")]

