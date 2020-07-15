from django.db import models
import random 
from django.conf import settings

User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
class Tweet(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User,null = True, on_delete=models.CASCADE) #many users can have many tweets | models.Cascade = if user deleted, all his tweet will be too
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(max_length=150, blank=True, null=True)
    image  = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    #def __str__(self):
    #    return self.content 

    class Meta():
        ordering = ['-id']  # - devant id pour ordre décroissant pour avoir les nouveaux tweet en haut

    @property
    def is_retweet(self):
        return self.parent != None


    def serialize(self):
        '''
        Now useless
        '''
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0,500),
        }
