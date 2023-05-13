from requests import get

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends, APIRouter

from src.app.database import get_async_session
from src.app.points.models import *

router = APIRouter(tags=["points"], prefix="/point")


# @router.get("/")
async def fill_db(session: AsyncSession = Depends(get_async_session)):
    url = "https://search-maps.yandex.ru/v1"
    key = "2710dda6-0302-439d-b682-aaf0e1e642f4"
    params = {"text": "", "type": "biz", "lang": "ru_RU", "apikey": key, "ll": "59.942668,30.315871",
              "spn": "0.100000,0.020000", "results": 500}

    categories = ["кафе", "кофейня", "ресторан", "копицентр", "столовая", "коворкинг", "фастфуд", "бар"]

    for category_ in categories:
        params["text"] = category_

        response = get(url, params=params)

        res = response.json()
        # print(res)

        for element in res["features"]:
            coords: str = ';'.join(map(str, element["geometry"]["coordinates"]))
            name = element["properties"]["CompanyMetaData"]["name"]
            address = element["properties"]["CompanyMetaData"]["address"]
            website = None
            if "url" in element["properties"]["CompanyMetaData"]:
                website = element["properties"]["CompanyMetaData"]["url"]

            el_categories = list(map(lambda x: x["name"], element["properties"]["CompanyMetaData"]["Categories"]))

            if website is None:
                statement = insert(establishment).values(name=name, coords=coords, address=address,
                                                         ).returning(establishment)
            else:
                statement = insert(establishment).values(name=name, coords=coords, address=address,
                                                         website=website).returning(establishment)
            result = await session.execute(statement)
            establishment_data = dict(result.mappings().one())

            for el_category in el_categories:
                query = select(category).where(category.c.name == el_category)
                result = await session.execute(query)
                data = result.mappings().all()
                if not data:
                    statement = insert(category).values(name=el_category).returning(category)
                    result = await session.execute(statement)
                    data = dict(result.mappings().all()[0])
                else:
                    data = dict(data[0])

                statement = insert(category_establishment).values(category_id=data["id"],
                                                                  establishment_id=establishment_data["id"])
                await session.execute(statement)

    await session.commit()


@router.get("/category/{category_str}", status_code=200)
async def get_point_by_category(category_str: str, session: AsyncSession = Depends(get_async_session)):
    query = select(category.c.id).filter(category.c.name.ilike(category_str.lower()))
    result = await session.execute(query)
    categories = list(map(lambda x: x[0], result.all()))

    if categories:
        query = select(category_establishment.c.establishment_id).where(
            category_establishment.c.category_id.in_(categories))
        result = await session.execute(query)
        points = list(map(lambda x: x[0], result.all()))

        query = select(
            establishment.c.coords, establishment.c.name, establishment.c.address, establishment.c.website
        ).filter(establishment.c.id.in_(points))
        result = await session.execute(query)

        data = list(map(lambda x: dict(x), result.mappings().all()))
        for d in data:
            d["coords"] = list(map(float, d["coords"].split(';')))

        return data

    @router.get("/metro/{metro_str}", status_code=200)
    async def get_point_by_metro(metro_str: str, session: AsyncSession = Depends(get_async_session)):
        query = select(metro.c.id).filter(metro.c.name.ilike(metro_str.lower()))
        result = await session.execute(query)
        metros = list(map(lambda x: x[0], result.all()))

        for d in metros:
            d["coords"] = list(map(float, d["coords"].split(';')))
        return metros

    @router.get("/metro/{metro_str}", status_code=200)
    async def get_point_by_metro(metro_str: str, session: AsyncSession = Depends(get_async_session)):
        query = select(metro.c.id).filter(metro.c.name.ilike(metro_str.lower()))
        result = await session.execute(query)
        metros = list(map(lambda x: x[0], result.all()))

        for d in metros:
            d["coords"] = list(map(float, d["coords"].split(';')))
        return metros

    @router.get("/museum/{museum_str}", status_code=200)
    async def get_point_by_museum(museum_str: str, session: AsyncSession = Depends(get_async_session)):
        query = select(museum).filter(museum.c.name.ilike(museum_str.lower()))
        result = await session.execute(query)
        museums = list(map(lambda x: dict(x), result.mappings().all()))

        for d in museums:
            d["coords"] = list(map(float, d["coords"].split(';')))

        return museums

    @router.get("/university/{university_str}", status_code=200)
    async def get_point_by_university(university_str: str, session: AsyncSession = Depends(get_async_session)):
        query = select(university).filter(university.c.name.ilike(university_str.lower()))
        result = await session.execute(query)
        universities = list(map(lambda x: dict(x), result.mappings().all()))

        for d in universities:
            d["coords"] = list(map(float, d["coords"].split(';')))

        return universities