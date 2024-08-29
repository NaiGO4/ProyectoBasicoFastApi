from fastapi import FastAPI

app = FastAPI()

movie = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
        {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]

@app.get('/', tags=['Inicio'])
async def root():
    return('Hola mundo utilizando FastAPI')



@app.get('/movies', tags=['Cine'])
async def get_movies():
    return movie

@app.get('/movies/{id}', tags=['Cine'])
async def get_movie(id: int):
    for m in movie:
        if m['id'] == id:
            return m
    return {"error": "Película no encontrada"}  


@app.get('/movies', tags=['Cine'])
async def get_movie_by_category(category:str, year: str):
    for m in movie:
        if m['category'] == id:
            return movie
    return[]