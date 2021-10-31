from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 100,null = True, blank = True)
    description = models.CharField(max_length =100)
    icon = models.CharField(max_length = 100)

    def __str__(self,):
        return self.name



class Post(models.Model):
    STATUS_CHOICES=(('Draft','Draft'),('Published','Published'),)
    title=models.CharField(max_length=250)
    date=models.DateField(auto_now=True)
    content=RichTextField(blank=True,null=True)
    slug=models.SlugField()
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='Draft')
    category=models.ManyToManyField(Category,related_name='category')
    image=models.ImageField(upload_to='images/',blank=True)
    likes=models.ManyToManyField(User,related_name='likes',blank=True)
    author=models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def total_like(self):
        return self.likes.count()


    
class comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)  
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    datetime=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('datetime',)
    def __str__(self):
        return f'comment by: {self.user} on {self.post}'