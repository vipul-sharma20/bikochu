from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views

from twitter import urls as twitter_urls


urlpatterns = [
    # Examples:
    url(r'^', include(twitter_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token, name='token_auth'),
]
