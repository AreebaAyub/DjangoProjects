from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Destination(models.Model):
    username=models.CharField(max_length=80)
    password=models.TextField()
    email=models.TextField()
    #img=models.ImageField()

class Comment(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    #reply=models.ForeignKey('self', null=True, related_name='replies',on_delete=models.PROTECT, blank=True )
    content=models.TextField(max_length=160, null=True)
    #replies=models.TextField(max_length=160)
    timestamp=models.DateTimeField(auto_now_add=True)

    def getAllReplies(self):
        if Reply.objects.filter(comment = self).exists():
            return Reply.objects.filter(comment = self)
        else:
            return False

    def __str__(self):
        return '{}'.format(str(self.user.username),self.content)

class Reply(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    comment=models.ForeignKey(Comment,on_delete=models.PROTECT)
    body=models.TextField(max_length=160, null=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(str(self.user.username),self.body)

class PostAnn(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    #reply=models.ForeignKey('self', null=True, related_name='replies',on_delete=models.PROTECT, blank=True )
    content=models.TextField(max_length=160, null=True)
    #replies=models.TextField(max_length=160)
    timestamp=models.DateTimeField(auto_now_add=True)





    
