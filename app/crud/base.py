from odmantic import Model, ObjectId
from odmantic.session import AIOSession
from pydantic import BaseModel
from typing import Generic, TypeVar, Type
from fastapi.encoders import jsonable_encoder


ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, db: AIOSession, *, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**jsonable_encoder(obj_in))
        return await db.save(db_obj)

    async def get(self, db: AIOSession, *, id: ObjectId) -> ModelType | None:
        return await db.find_one(self.model, self.model.id == id)

    async def get_multi(self, db: AIOSession) -> list[ModelType]:
        return await db.find(self.model)
