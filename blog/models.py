from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    
    date_created = models.DateTimeField(default=timezone.now) 
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_posts', blank=True)
    gaming_image = models.ImageField(upload_to='gaming', blank=True, null=True)

    class Meta:
        ordering = ['-date_created']

    def comment_count(self):
        return self.comment_set.all().count() 

    def comments(self):
            return self.comment_set.all()

    def __str__(self):
        return self.title
    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()
    
  
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)


    def __str__(self):
        return self.content
