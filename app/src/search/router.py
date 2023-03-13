from fastapi import APIRouter, Depends

from sqlalchemy import select, delete, desc
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from search.utils import get_ids_by_string_from_elastic

from search.models import documents_tb




router = APIRouter(
    prefix='/search',
    tags=['Search'],
)


@router.get('/get-twenty')
async def get_last_twenty_results(session: AsyncSession = Depends(get_async_session)):
    """Возвращает последние - по дате публикации - 20 постов. \nОтсортированы по-убыванию"""
    query = select(documents_tb).order_by(desc(documents_tb.c.created_date)).limit(20)
    result = await session.execute(query)
    data = [list(val)  for val in result.all()]
    return {'code': 200, 'status':'success', 
             'data': data}

@router.get('/')
async def get_twenty_results_by_string(req:str, session: AsyncSession = Depends(get_async_session)):
    """"""
    elastic_id_result = get_ids_by_string_from_elastic(req)
    query = select(documents_tb).filter(documents_tb.c.id.in_(elastic_id_result)).order_by(desc(documents_tb.c.created_date)).limit(20)
    result = await session.execute(query)
    data = [list(val)  for val in result.all()]
    return {'code': 200, 'status':'success', 
             'data': data}



@router.delete('/delete')
async def delete_document_by_id (id:int, session: AsyncSession = Depends(get_async_session)):
    """Удаляет пост по id"""
    query = delete(documents_tb).where(documents_tb.c.id == id)
    await session.execute(query)
    await session.commit()
    return {'code': 200, 'status':'success'}

@router.get('/id/')
async def get_by_id (id:int, session: AsyncSession = Depends(get_async_session)):
    """Возвращает пост по id"""
    query = select(documents_tb).where(documents_tb.c.id == id)
    result = await session.execute(query)
    data = [list(val)  for val in result.all()]
    return {'code': 200, 'status':'success', 
            'data': data}
        
