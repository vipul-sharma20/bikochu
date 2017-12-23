from django.core.urlresolvers import reverse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TweetPaginator
from .search import ElasticTweet


class Home(APIView):
    def get(self, request):
        return Response(dict(search_api=reverse('tweet_search'),
                             get_auth_token=reverse('token_auth')))


class TweetList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        query = dict(
                    q=request.query_params.get('q', None),
                    user=request.query_params.get('user', None),
                    start_date=request.query_params.get('start_date', None),
                    end_date=request.query_params.get('end_date', None),
                )
        elastic_object = ElasticTweet()
        tweets = elastic_object.search(query)
        paginator = TweetPaginator()
        result_page = paginator.paginate_queryset(tweets, request)

        return paginator.get_paginated_response(result_page)

