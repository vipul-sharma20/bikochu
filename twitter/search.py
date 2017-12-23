import dateutil.parser

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search

connections.create_connection()


class TweetIndex(DocType):
    user = Text(analyzer='default')
    tweet = Text(analyzer='default')
    created_at = Date()

    class Meta:
        index = 'tweet-index'


class ElasticTweet(object):
    def __init__(self, *args, item_count=100, **kwargs):
        self.s = Search()
        self.item_count = item_count

    def search(self, query):
        if query.get('start_date') or query.get('end_date'):
            date_range = {}
            if query.get('start_date'):
                date_range['from'] = dateutil.parser.parse(query['start_date'])
            if query.get('end_date'):
                date_range['to'] = dateutil.parser.parse(query['end_date'])
            self.s = self.s.filter(
                            'range',
                            created_at=date_range)
        if query.get('user'):
            self.s = self.s.filter('match', user=query['user'])
        if query.get('q'):
            self.s = self.s.filter('match', tweet=query['q'])

        return self._clean(self.s[0:self.item_count].execute())

    def _clean(self, tweets):
        return [tweet.to_dict() for tweet in tweets]

