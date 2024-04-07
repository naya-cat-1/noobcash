from flask import Flask, request, jsonify
from transformers import pipeline

pipe1 = pipeline('summarization', model='chiakya/Bert-chinese-Summarization')
pipe2 = pipeline("text-classification", model="hw2942/bert-base-chinese-finetuning-financial-news-sentiment-v2")
app = Flask(__name__)


@app.route('/api/summarization', methods=['GET'])
def summarization():
    word = request.args.get('info')
    if word == None:
        return ''
    return pipe1(word)


@app.route('/api/sentiment', methods=['GET'])
def sentiment():
    word = request.args.get('info')
    if word == None:
        return ''
    return pipe2(word)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
