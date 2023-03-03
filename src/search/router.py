from fastapi import APIRouter, Depends

from sqlalchemy import select, delete, desc
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from search.models import documents_tb
from search.schemas import Document  # ??


router = APIRouter(
    prefix='/search',
    tags=['Search'],
)


@router.get('/')
async def get_last_twenty_results(session: AsyncSession = Depends(get_async_session)):
    query = select(documents_tb).order_by(desc(documents_tb.c.created_date)).limit(20)
    result = await session.execute(query)
    data = [list(val)  for val in result.all()]
    return {'code': 200, 'status':'success', 
             'data': data}

@router.delete('/delete')
async def delete_document_by_id (id:int, session: AsyncSession = Depends(get_async_session)):
    query = delete(documents_tb).where(documents_tb.c.id == id)
    await session.execute(query)
    await session.commit()
    return {'code': 200, 'status':'success'}

    
