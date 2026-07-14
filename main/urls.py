from django.urls import path
from . import views

#regist the app urls
urlpatterns = [
    path('',views.index,name='index'),
    path('skills/',views.skills, name='skills'),
    path('blog/', views.blog,name='blog'),
    path('post/<int:id>/details', views.single_blog,name="details"),
    path('new/', views.create_blog,name='new'),
    path('post/<int:id>/edit', views.edit_post,name="edit"),
    path('post/<int:id>/delete', views.delete_post,name="delete"),
    path('contact/', views.contact, name='contact'),
    path('comment/<int:id>/comment',views.comment,name="comment"),

]
