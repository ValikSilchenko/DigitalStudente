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
    params = {"text": "", "lang": "ru_RU", "apikey": key,
              "results": 200}

    categories = ["кафе", "кофейня", "ресторан", "копицентр", "столовая", "коворкинг", "фастфуд", "бар"]

    for category_ in categories:
        params["text"] = category_ + " СПб"

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


# @router.get("/")
async def fill_db(session: AsyncSession = Depends(get_async_session)):
    url = "https://spb-classif.gate.petersburg.ru/api/v2/datasets/139/versions/latest/data/569"
    key = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhU1RaZm42bHpTdURYcUttRkg1SzN5UDFhT0FxUkhTNm9OendMUExaTXhFIn0.eyJleHAiOjE3Nzg1Nzk1NDgsImlhdCI6MTY4Mzg4NTE0OCwianRpIjoiMzhhMDBkMTgtM2ZlNy00NTMxLTljOTItYWNlZmYxYjZkMWVlIiwiaXNzIjoiaHR0cHM6Ly9rYy5wZXRlcnNidXJnLnJ1L3JlYWxtcy9lZ3MtYXBpIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjI1N2VkYTUxLWYxOTUtNDY5OS1hMDU4LWVlYTQ5MzNlYjVjMiIsInR5cCI6IkJlYXJlciIsImF6cCI6ImFkbWluLXJlc3QtY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImM1ZWMzZmYxLThiNzktNDA4Yy1hZDU5LTgwNTdmMWM3MGRkNyIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiLyoiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtZWdzLWFwaSIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiJjNWVjM2ZmMS04Yjc5LTQwOGMtYWQ1OS04MDU3ZjFjNzBkZDciLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiLQktCw0LvQtdC90YLQuNC9INCh0LjQu9GM0YfQtdC90LrQviIsInByZWZlcnJlZF91c2VybmFtZSI6Ijc1MTg2YzE5ZjgwMjZiOTEyYTViNWU4MGM1Njc1M2MxIiwiZ2l2ZW5fbmFtZSI6ItCS0LDQu9C10L3RgtC40L0iLCJmYW1pbHlfbmFtZSI6ItCh0LjQu9GM0YfQtdC90LrQviJ9.1F-8jVx-43NM6KkVrJPLDTKGbg3N5LnLu7-uC8DvupIyeOtvbNMN_KtFzVyM8waE21Hl74sFX5Fhl-WzETvM5ongV5xWm-wXTiIQUSNdl3GtWxEKtRL-KvXs-P-UqcEJqz2FQm3YVq_r-wXNPbR3ZIYysMXCJaqhZ9BXCQWc6SjLS8TTZ1hu_WuLvepVxnHp5FH8-eeoFnztdncuLNh2Dkz3IYfQzJTRDkm01a9voXKflTrRp2_Qj8ePf3JQy3DlgZCvHLEuyyILJMdQ7KtoD5EHWvrEhcyJhpxZf7iPaVtC0iaugeVZk80d78m0YO51m9SHHZb7JLAjg6STlmBGsw"
    params = {"per_page": 100}
    headers = {"accept": "application/json", "Authorization": key}

    response = get(url, headers=headers, params=params)

    res = response.json()

    for element in res["results"]:
        coords: str = ';'.join(map(str, element["coord"]))
        name: str = element["name"]

        address = element["address_manual"]
        website = None
        if "www" in element:
            website = element["www"]

        el_categories = ["музей"]

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
