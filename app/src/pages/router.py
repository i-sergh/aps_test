from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from search.router import get_last_twenty_results, get_by_id

router = APIRouter(
    prefix='/pages',
    tags=["Pages"]
)

templates = Jinja2Templates(directory='pages/templates')

@router.get('/')
def get_start_page(request: Request):
    return templates.TemplateResponse('base.html', 
                                        {'request': request,})


@router.get('/search/')
def get_search_page(request: Request, results=Depends(get_last_twenty_results)):
    """ print(results) """
    return templates.TemplateResponse('search.html', 
                                        {'request': request,
                                        'results': results})

@router.get('/search/{id}')
def get_search_page(request: Request, results=Depends(get_by_id)):
    """ print(results) """
    return templates.TemplateResponse('search.html', 
                                        {'request': request,
                                        'results': results})