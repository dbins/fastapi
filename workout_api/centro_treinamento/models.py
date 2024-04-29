from datetime import datetime
from sqlalchemy import DateTime, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel

class CentroTreinamentoModel(BaseModel):
    __tablename__ = "centros_treinamento"
    pk_id: Mapped[int]= mapped_column(Integer, primary_key= True)
    nome:Mapped[str] = mapped_column(String(50), unique=True, nullable= False)
    endereco:Mapped[str] = mapped_column(String(100), nullable= False)
    proprietario:Mapped[str] = mapped_column(String(50), nullable= False)
    created_at:Mapped[datetime] = mapped_column(DateTime, nullable= False)
    atleta:Mapped["AtletaModel"] = relationship(back_populates = "centro_treinamento")