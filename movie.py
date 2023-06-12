from string import whitespace, punctuation, digits
import os

import httpx
from dotenv import load_dotenv

load_dotenv()

TMDB_KEY = os.getenv('TMDB_KEY')

def get_movie_by_id(id):
    url = f'https://api.themoviedb.org/3/movie/{id}?api_key={TMDB_KEY}&language=en-US'
    response = httpx.get(url)
    if response.status_code == 200:
        my_movie = response.json()
    else:
        return
    return my_movie


def movie_details(movie):
    title, year = movie['title'], movie['release_date'].split('-')[0]
    rating, release_date = movie['vote_average'], movie['release_date']
    runtime = movie['runtime']
    hours = runtime // 60
    minutes = runtime - hours * 60

    movie_genres = [genre['name'] for genre in movie['genres']]
    categories = ', '.join(movie_genres)

    return f"{title} ({year})\n{rating * 10}%\n{release_date}\n{categories} \n⌚{hours}:{minutes}"




punctuation = punctuation.replace('-','')

def validate(word: str) -> bool:
    """
    Validate a word to see if it does not cointain whitespace, puncuations and digits
    :param word: Word to validate.
    :return: True if valid, False if not.
    """
    for char in word:
        if char in digits:
            print('Invalid word, no words contain digits! Try again.')
            return False
        if char in whitespace:
            print('Invalid word, no whitepsace allowed. Try again.')
            return False
        if char in punctuation:
            print('Invalid word, no punctuation allowed. Try again.')
            return False
    return True


def movie_search(movie: str):
    movie = movie.replace(' ', '-')
    if validate(movie):
        url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_KEY}&language=en-US&query={movie}&page=1&include_adult=false'
    else:
        return None
    response = httpx.get(url)
    if not response.status_code == httpx.codes.OK:
        response.raise_for_status()
    my_movie = response.json()
    movie_id = my_movie['results'][0]['id']
    my_movie = get_movie_by_id(movie_id)
    return my_movie
