from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

movies = [
    {"id": 1,
    "title": "The Substance",
    "overview": "'Tú, pero mejor en todos los sentidos'",
    "year": "2024",
    "rating": 7.2,
    "category": "Ciencia Ficción"},
    {"id": 2,
    "title": "The Fall: El sueño de Alexandria",
    "overview": "Hollywood, años veinte. Tras una desafortunada caída, un especialista en secuencias de acción es ingresado en un hospital",
    "year": "2006",
    "rating": 7.0,
    "category": "Fantástico"},

    {"id": 3,
    "title": "Aftersun",
    "overview": "Sophie reflexiona sobre la alegría compartida y la melancolía privada de unas vacaciones que hizo con su padre 20 años atrás",
    "year": "2022",
    "rating": 7.2,
    "category": "Drama"}
]

@app.get('/', tags=['Home'])
def home():
    return "Hola, mundo!"

@app.get('/movies', tags=['Home'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['Home'])
def get_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    return []

@app.get('/movies/', tags=['Home'])
def get_movie_by_category(category: str, year: int):
    for movie in movies:
        if movie['category'] == category:
            return movie
    return []