from django.contrib import admin
from .models import Skill, Blog,Contact,Comment

# Register the Skills, Blogs  and Contacts models 
@admin.register(Blog)
class BlogsAdmin(admin.ModelAdmin):
    #display the following fields
    list_display = ['title','created_at'] 
    
    #search with the defined field
    search_fields = ['title']
    
@admin.register(Skill)
class SkillsAdmin(admin.ModelAdmin):
    #display the following fields
    list_display = ['title','description', 'years_of_experience']
    
    #search with the defined field
    search_fields = ['title']
    
@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    #display the following fields
    list_display = ['name','email','message']
    
    #search with the defined field
    search_fields = ['name', 'email']
    
@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    #display the following fields
    list_display = ['name','email','message']
    
    #search with the defined field
    search_fields = ['name', 'email']
    
