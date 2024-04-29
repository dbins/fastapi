from workout_api.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat,UUID4

class CentroTreinamento(BaseSchema):
	nome: Annotated[str, Field(descritpion="Nome da Centro de Treinamento", example="CT King", max_length=50)]
	endereco: Annotated[str, Field(descritpion="Endereço da Centro de Treinamento", example="Rua Castro Alves 10", max_length=100)]
	proprietario: Annotated[str, Field(descritpion="Proprietário da Centro de Treinamento", example="Bins", max_length=50)]
	
class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço da Centro de Treinamento', example='Rua Castro Alves 10', max_length=100)]
    proprietario: Annotated[str, Field(description='Proprietário da Centro de Treinamento"', example='Bins', max_length=50)]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]    