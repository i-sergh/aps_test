from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from search.router import get_last_twenty_results, get_twenty_results_by_string

router = APIRouter(
    prefix='/pages',
    tags=["Pages"]
)

templates = Jinja2Templates(directory='pages/templates')

@router.get('/')
async  def get_start_page(request: Request):
    """Возвращает стартовую страницу"""
    return templates.TemplateResponse('base.html', 
                                        {'request': request,})


@router.get('/search/')
async  def get_search_page(request: Request, results=Depends(get_last_twenty_results)):
    """Возвращает страницу с 20-ю последними постами"""
    return templates.TemplateResponse('search.html', 
                                        {'request': request,
                                        'results': results})

@router.get('/search/{req}')
async def get_search_page(request: Request, results=Depends(get_twenty_results_by_string)):
    """Возвращает страницу с постом по введенной строке"""
    return templates.TemplateResponse('search.html', 
                                        {'request': request,
                                        'results': results})