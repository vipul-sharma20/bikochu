bikochu
=======

REST API built in Django/Python for searching tweets
live demo at: [http://50.116.0.97](http://50.116.0.97)
see bottom of this document for more details on the live demo.

Project name: [reference](http://naruto.wikia.com/wiki/Bik%C5%8Dch%C5%AB_Search_Mission)

How to run?
-----------

### Clone ###
* `git clone https://github.com/vipul-sharma20/bikochu.git`
* `cd bikochu`

### Virtual Environment ###
* `sudo pip install virtualenv`
     * Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default, so you may have pip already.
     * If you don't have pip installed, visit here to see steps to install virtualenv: [https://virtualenv.readthedocs.org/en/latest/installation.html](https://virtualenv.readthedocs.org/en/latest/installation.html)
* `mkdir ~/.env/ && virtualenv -p python3 ~/.env/bikochu/`
* `source ~/.env/bikochu/bin/activate`

### Install Requirements ###
* `pip install -r requirements.txt` (wait till the requirements are installed)
* Install elasticsearch: [doc](https://www.elastic.co/guide/en/elasticsearch/reference/current/_installation.html#_installation_example_with_tar)

### Running ###
* `python manage.py makemigrations`
* `python manage.py migrate`

#### Run Test (Optional) ####
* `python manage.py test`

* `python manage.py runserver` This will run the application on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

API
---

### Authentication ###
This API supports token based authentication.

* Token based authentication example: `curl -X GET http://127.0.0.1:8000/ 'Authorization: Token <token>'`

In this project every request requires to authenticated.

#### Obtaining auth token ####
You can generate token by making POST request to `/api-token-auth/` and sending
`username` and `password` of registered user in POST body

* **`/api-token-auth/`**
* **Request Type:** POST
* **POST body:**
    * `username`: username
    * `password`: password

### Search ###
* **`/tweets/`**
* **Request Type:** GET
* **GET parameters:**
    * `user`: author of the tweet
    * `q`: query string to match against tweets
    * `start_date`: start date for time range filtering (isoformat)
    * `end_date`: end date for time range filtering (isoformat)
* Returns paginated response

#### Example ####
Suppose the token for a user _bruce_ is `c13a415a575338f7384d248934ad5e31ab957ab3`

* `curl -X GET http://127.0.0.1:8000/tweets/ -H 'Authorization: Token 9c37e6922466000bf87f6842b94400eec0ab42f1'`
* `http://127.0.0.1:8000/tweets?user=isabelldonovan4`
* `http://127.0.0.1:8000/tweets?user=isabelldonovan4&start_date=2017-12-28T07:53:40.387948`
* `http://127.0.0.1:8000/tweets?q=bitcoin&end_date=2017-12-28T07:53:40.387948`

#### Sample Response ####

    {
            "count": 30,
            "next": "?page=2",
            "previous": "?page=1",
            "tweets": [
            {
                "user": "mickeytrader",
                "tweet": "RT @ORACLEofETH: WOW better buy the other coins now before the big #BitcoinCash dump!\n\nIf  \"Bitcoin Cash\" hits $0 in the next 24 hrs...\nIll…",
                "created_at": "2017-12-21T08:19:27"
            },
            {
                "user": "EasyStockMarket",
                "tweet": "RT @ETMarkets: It was a year for #bitcoin #technology #stocks and the power consolidation of China's Xi Jinping.\nhttps://t.co/FHTgusbS0m",
                "created_at": "2017-12-21T08:19:32"
            },
            {
                "user": "ardellamatthe10",
                "tweet": "RT @ico_report: The Largest Channel about ICO in Telegram https://t.co/QFLFhyLrUQ\n💯 ICO Reports &amp; Crypto News🤘  \n📅 Сalendar &amp; Analytics🔥\n🚀…",
                "created_at": "2017-12-21T08:19:32"
            },
            {
                "user": "cryptotangle",
                "tweet": "RT @binarybits: Satoshi Nakamoto envisioned bitcoin as a currency for \"small casual transactions.\" Skyrocketing fees are making that imposs…",
                "created_at": "2017-12-21T08:19:30"
            },
            {
                "user": "Coca_Cola_lite",
                "tweet": "RT @SteveKnebworth: Openbazaar is to eBay as Bitcoin is to PayPal.\n\nhttps://t.co/UIBaZOd8PK",
                "created_at": "2017-12-21T08:19:33"
            }
        ]
    }

Next Steps?
-----------

#### NOTE ####

* For fetching and dumping tweets in elasticsearch, I used the Twitter streaming API
    * script used: [https://gist.github.com/vipul-sharma20/6f0bbe21d8d74a94f97d18a483205c26](https://gist.github.com/vipul-sharma20/6f0bbe21d8d74a94f97d18a483205c26)
    * tweets with keywords = ['bitcoin', 'ethereum', 'litecoin', 'ripple', 'cryptocurrency', 'the']
* Elasticsearch is on the same instance using 1GB of heap size

## Test it live ##

* Sample Postman collection with test user: [https://www.getpostman.com/collections/8439771b3600285fc05f](https://www.getpostman.com/collections/8439771b3600285fc05f)
* There exists a user on production environment
    * username: `test`
    * password: `test`
* Get auth token by:
    * POST `http://50.116.0.97:8000/api-token-auth/` with `username` and `password` in body
    * You can use auth token generated from production for above created user: `3749627cfc80e9e9fe3473f275db4479292fe93f`
* Make request:
    * Example: `curl -X GET http://50.116.0.97:8000/tweets/ -H 'Authorization: Token 3749627cfc80e9e9fe3473f275db4479292fe93f'`

