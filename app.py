from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GIPHY_API_KEY = 'sAzPy5iBanJn2pl3bIl4auMNppcZ2pLC'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    query = request.args.get('query')
    url = 'https://api.giphy.com/v1/gifs/search'
    params = {
        'api_key': GIPHY_API_KEY,
        'q': query,
        'limit': 5,
        'rating': 'g',
        'lang': 'en'
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return f"Erro na API do Giphy: {response.status_code}"

    data = response.json()
    gifs = [
        gif['images']['original']['url']
        for gif in data['data']
    ]

    return render_template('results.html', gifs=gifs, query=query)


if __name__ == '__main__':
    app.run(debug=True)
