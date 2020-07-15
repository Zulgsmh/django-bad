from . import views
from django.urls import path
from django.conf.urls import url

'''
CLIENT
BASE ENDPOINT /tweets/api/
'''
app_name='tweets'
urlpatterns = [
    path('', views.home_tweet, name='IndexTweet'),
    path('<int:tweet_id>', views.tweet_detail_view),
    path('all', views.tweet_list_view),
    path('api/all', views.tweet_list_view),
    path('api/create_tweet', views.tweet_create_view),
    path('api/action', views.tweet_action_view),
    path('api/<int:tweet_id>/delete', views.tweet_delete_view),
    
]

