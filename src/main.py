from fastapi import FastAPI

from search.router import router as search_router

app = FastAPI(
    title = 'DocSearch'
    )

app.include_router(search_router)

@app.get('/')
def hello():
    return {'Hello': 'world!'}

