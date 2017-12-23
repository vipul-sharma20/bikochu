from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from twitter import views

urlpatterns = [
    url(r'^tweets/$', views.TweetList.as_view(), name='tweet_search'),
    url(r'^$', views.Home.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
