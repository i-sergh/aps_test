from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.exceptions import RequestValidationError

from search.router import router as search_router
from pages.router import router as pages_router

app = FastAPI(
    title = 'DocSearch'
    )

app.mount('/static', StaticFiles(directory='pages/static'), name='static')
app.mount('/icons', StaticFiles(directory='pages/static/icons/'), name='icons')
app.include_router(search_router)
app.include_router(pages_router)

@app.get('/')
async def start_page():
    return RedirectResponse("/pages/")

@app.exception_handler(404)
async def custom_handler(request, e):
    return RedirectResponse("/pages/")

@app.exception_handler(RequestValidationError)
async def custom_422_handler(request, e):
    return RedirectResponse("/pages/")
