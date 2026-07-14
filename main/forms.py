from django import forms
from .models import Blog, Contact, Comment

class BlogsForm(forms.ModelForm):    
    class Meta:
        # model name from .models
        model = Blog
        
        # fields to be captured in the form
        fields = ['title', 'content'] 
        
        #form widgets with attributes
        widgets ={
            'title': forms.TextInput(attrs={
                'class':'w-full bg-background/50 border border-white/10 rounded-xl px-md py-sm focus:border-primary focus:ring-1 focus:ring-primary outline-none transition-all text-on-surface',
                'placeholder': 'Blog Post title....',
                'required': True
            }),
            
            'content': forms.Textarea(attrs={
                'class':'w-full bg-background/50 border border-white/10 rounded-xl px-md py-sm focus:border-primary focus:ring-1 focus:ring-primary outline-none transition-all text-on-surface',
                'placeholder': 'Blog Post Content....',
                'required': True
            })
        }
        

class ContactsForm(forms.ModelForm):
    class Meta:
        # define model name from .models
        model = Contact
        
        # fields to be captured in the form
        fields = ['name', 'email','message']
        
        #form widgets with attributes
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'w-full bg-background/50 border border-white/10 rounded-xl px-md py-sm focus:border-primary focus:ring-1 focus:ring-primary outline-none transition-all text-on-surface',
                'placeholder': 'John Janny',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class':'w-full bg-background/50 border border-white/10 rounded-xl px-md py-sm focus:border-primary focus:ring-1 focus:ring-primary outline-none transition-all text-on-surface',
                'placeholder': 'johnjann@gmail.com',
                'required': True
            }),
            'message':forms.Textarea(attrs={
                'class':'w-full bg-background/50 border border-white/10 rounded-xl px-md py-sm focus:border-primary focus:ring-1 focus:ring-primary outline-none transition-all text-on-surface',
                'placeholder': 'How do we help you',
                'required': True
            })
        }
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','content']
        
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'w-full bg-slate-800/60 border border-slate-700 rounded-xl px-5 py-4 focus:border-blue-500 focus:ring-2 focus:ring-blue-500 outline-none',
                'required': True,
                'placeholder': 'enter your name',
                'min_length':3
            }),
            'content':forms.Textarea(attrs={
                'class': 'w-full bg-slate-800/60 border border-slate-700 rounded-xl px-5 py-4 resize-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500 outline-none',
                'placeholder': 'Your thought...',
                'required': True,
                'min_length':5
                
            })
        }