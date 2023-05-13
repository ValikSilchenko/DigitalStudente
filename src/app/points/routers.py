from requests import get

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends, APIRouter

from src.app.database import get_async_session
from src.app.points.models import *

router = APIRouter(tags=["points"], prefix="/point")


@router.get("/category/{category_str}", status_code=200)
async def get_points_by_category(category_str: str, session: AsyncSession = Depends(get_async_session)):
    query = select(category).filter(category.c.name.ilike(category_str.lower()))
    result = await session.execute(query)
    categories = list(map(lambda x: dict(x), result.mappings().all()))

    if categories:
        query = select(category_establishment.c.establishment_id).where(
            category_establishment.c.category_id.in_([categories[i]["id"] for i in range(len(categories))]))
        result = await session.execute(query)
        points = list(map(lambda x: x[0], result.all()))

        query = select(
            establishment.c.coords, establishment.c.name, establishment.c.address, establishment.c.website
        ).filter(establishment.c.id.in_(points))
        result = await session.execute(query)

        data = list(map(lambda x: dict(x), result.mappings().all()))
        for d in data:
            d["coords"] = list(map(float, d["coords"].split(';')))
            d["category"] = categories[0]["name"]

        return data


@router.get("/search", status_code=200)
async def get_points_by_search(search_query: str, session: AsyncSession = Depends(get_async_session)):
    query = select(establishment).filter(establishment.c.name.ilike(f"%{search_query.lower()}%"))
    result = await session.execute(query)
    data = list(result.mappings().all())

    if data:
        return data

    query = select(establishment).filter(establishment.c.address.ilike(f"%{search_query.lower()}%"))
    result = await session.execute(query)
    data = list(result.mappings().all())

    return data
