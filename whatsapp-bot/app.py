from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    quotes = ['quote' in incoming_msg or 'إقتباس' in incoming_msg]
    cats = ['cat' in incoming_msg or 'قط' in incoming_msg]
    if quotes:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if cats:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()
