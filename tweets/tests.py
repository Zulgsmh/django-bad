from django.test import TestCase
from .models import Tweet
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User =  get_user_model()

# Create your tests here.
class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cfe', password='somepassword')
        Tweet.objects.create(content='mytweet1', user = self.user)
        Tweet.objects.create(content='mytweet2', user = self.user)
        Tweet.objects.create(content='mytweet3', user = self.user)

    
    def testTweetCreated(self):
        tweet_obj = Tweet.objects.create(content='mytweet2', user = self.user)
        self.assertEqual(tweet_obj.id, 4)
        self.assertEqual(tweet_obj.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username , password=self.user.password)
        return client 




