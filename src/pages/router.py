from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix='/pages',
    tags=["Pages"]
)

templates = Jinja2Templates(directory='pages/templates')

@router.get('/')
def get_start_page(request: Request):
    return templates.TemplateResponse('base.html', 
                                        {'request': request,})
