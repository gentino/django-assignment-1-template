from django.db import models



#create Skills model  with the defined fields
class Skill(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    proficiency =models.IntegerField(help_text='Skill up from 0 - 100')
    years_of_experience = models.IntegerField(help_text='Value from 0 and above')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

#create Blogs model  with the defined fields
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def  __str__(self):
         return self.title
#comment model with defined fields

class Comment(models.Model):
    owner=models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

#create Contacts model  with the defined fields
class  Contact(models.Model):
    name=models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)