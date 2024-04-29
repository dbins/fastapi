from uuid import uuid4
from datetime import datetime
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.centro_treinamento.models import CentroTreinamentoModel

from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select
from fastapi_pagination import Page, LimitOffsetPage
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import exc

router = APIRouter()

@router.post(
    '/', 
    summary='Criar um novo Centro de treinamento',
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    db_session: DatabaseDependency, 
    centro_treinamento_in: CentroTreinamentoIn = Body(...)
) -> CentroTreinamentoOut:
    
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(created_at=datetime.utcnow(), **centro_treinamento_out.model_dump())
    try:
       db_session.add(centro_treinamento_model)
       await db_session.commit()
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER, 
            detail=f'Já existe um Centro de Treinamento cadastrado com o nome {centro_treinamento_in.nome}'
        ) 

    return centro_treinamento_out
    
#Rota sem paginação    
#@router.get(
#    '/', 
#    summary='Consultar todos os centros de treinamento',
#    status_code=status.HTTP_200_OK,
#    response_model=list[CentroTreinamentoOut],
#)
#async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
#    centros_treinamento_out: list[CentroTreinamentoOut] = (
#        await db_session.execute(select(CentroTreinamentoModel))
#    ).scalars().all()
    
#    return centros_treinamento_out
@router.get(
    '/', 
    summary='Consultar todos os centros de treinamento',
    status_code=status.HTTP_200_OK,
    response_model=LimitOffsetPage[CentroTreinamentoOut],
)
async def query(db_session: DatabaseDependency) -> Page[CentroTreinamentoOut]:
    centros_treinamento_out = await paginate(db_session, select(CentroTreinamentoModel))  
    return centros_treinamento_out


@router.get(
    '/{id}', 
    summary='Consulta um centro de treinamento pelo id',
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def get(id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    centro_treinamento_out: CentroTreinamentoOut = (
        await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))
    ).scalars().first()

    if not centro_treinamento_out:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Centro de treinamento não encontrado no id: {id}'
        )
    
    return centro_treinamento_out