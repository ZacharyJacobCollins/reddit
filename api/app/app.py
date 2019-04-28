from flask import Flask
import urllib

app = Flask(__name__)


# Environment
app.config.update(
    REDDIT_SECRET=SECRET
)

@app.route('/')

def hello_world():
    ie >>> import urllib
       >>> a = (('p',1),('p',2), ('p', 3))
       >>> urllib.urlencode(a)
       'p=1&p=2&p=3'

    client_id = ''
    response_type = ''
    redirect_uri = ''
    duration = ''
    scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'


    redirect = """https://www.reddit.com/api/v1/authorize?client_id=CLIENT_ID&response_type=TYPE&
    &redirect_uri=URI&duration=DURATION&scope=scopes"""


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='1337')
