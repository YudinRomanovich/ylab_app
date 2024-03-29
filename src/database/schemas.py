from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class MenuCreate(BaseModel):
    model_config = ConfigDict()

    title: str
    description: str


class MenuInfo(BaseModel):
    model_config = ConfigDict()

    submenus_count: int
    dishes_count: int


class MenuRead(BaseModel):
    model_config = ConfigDict()

    id: UUID
    title: str
    description: str
    submenus_count: int
    dishes_count: int


class MenuUpdate(BaseModel):
    model_config = ConfigDict()

    title: str | None
    description: str | None


class SubmenuCreate(BaseModel):
    model_config = ConfigDict()

    title: str
    description: str


class SubmenuRead(BaseModel):
    model_config = ConfigDict()

    id: UUID
    title: str
    description: str
    dishes_count: int


class SubmenuUpdate(BaseModel):
    model_config = ConfigDict()

    title: str | None
    description: str | None


class DishCreate(BaseModel):
    model_config = ConfigDict()

    title: str
    description: str
    price: Decimal


class DishUpdate(BaseModel):
    model_config = ConfigDict()

    title: str
    description: str
    price: Decimal


class DishRead(BaseModel):
    model_config = ConfigDict()

    id: UUID
    title: str
    description: str
    price: Decimal
