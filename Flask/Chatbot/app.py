from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

app = Flask(__name__)

MONGODB_PASS = os.environ.get('mongoDBPASS')
chatbot = ChatBot(
    'Ron Obvious', 
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter', 
    database_uri='mongodb+srv://admin:'+ MONGODB_PASS +'@cluster0-62hvi.gcp.mongodb.net/test?retryWrites=true&w=majority')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train('chatterbot.corpus.english')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == '__main__':
    app.run(debug=True)
