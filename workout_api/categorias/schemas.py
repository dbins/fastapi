from workout_api.contrib.schemas import BaseSchema
from pydantic import UUID4, Field
from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat



class Categoria(BaseSchema):
	nome: Annotated[str, Field(descritpion="Nome da Categoria", example="Scale", max_length=10)]

class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', example='Scale', max_length=10)]


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]