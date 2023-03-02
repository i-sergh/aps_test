from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from search.router import router as search_router
from pages.router import router as pages_router

app = FastAPI(
    title = 'DocSearch'
    )

app.mount('/static', StaticFiles(directory='pages/static'), name='static')
app.include_router(search_router)
app.include_router(pages_router)

@app.get('/')
def hello():
    return {'Hello': 'world!'}

