import sqlalchemy

metadata = sqlalchemy.MetaData()

metro = sqlalchemy.Table(
    "metros",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, sqlalchemy.Sequence("metros_id_seq", metadata=metadata),
                      primary_key=True, nullable=False),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR(20), nullable=False),
    sqlalchemy.Column("coords", sqlalchemy.VARCHAR(21), nullable=False),
    sqlalchemy.Column("closed", sqlalchemy.Boolean, nullable=False, default=False),
)

university = sqlalchemy.Table(
    "universities",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, sqlalchemy.Sequence("universities_id_seq", metadata=metadata),
                      primary_key=True, nullable=False),
    sqlalchemy.Column("full_name", sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column("address", sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column("metro", sqlalchemy.Integer, sqlalchemy.ForeignKey("metros.id"), nullable=False),
    sqlalchemy.Column("web_site", sqlalchemy.VARCHAR(40), nullable=False),
    sqlalchemy.Column("coords", sqlalchemy.VARCHAR(21), nullable=False)
)

showroom = sqlalchemy.Table(
    "showrooms",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, sqlalchemy.Sequence("showrooms_id_seq", metadata=metadata),
                      primary_key=True, nullable=False),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR(40), nullable=False),
    sqlalchemy.Column("address", sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column("coords", sqlalchemy.VARCHAR(21), nullable=False),
    sqlalchemy.Column("website", sqlalchemy.VARCHAR(40)),
    sqlalchemy.Column("phone", sqlalchemy.VARCHAR(12)),
    sqlalchemy.Column("description", sqlalchemy.VARCHAR),
)

museum = sqlalchemy.Table(
    "museums",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, sqlalchemy.Sequence("museums_id_seq", metadata=metadata)
                      , primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR(40), nullable=False),
    sqlalchemy.Column("address", sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column("coords", sqlalchemy.VARCHAR(21), nullable=False),
    sqlalchemy.Column("website", sqlalchemy.VARCHAR(40)),
    sqlalchemy.Column("phone", sqlalchemy.VARCHAR(12))
)

wifi_zone = sqlalchemy.Table(
    "wifi_zones",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, sqlalchemy.Sequence("wifi_zones_id_seq", metadata=metadata),
                      primary_key=True),
    sqlalchemy.Column("wifi_name", sqlalchemy.VARCHAR(20), nullable=False),
    sqlalchemy.Column("coords", sqlalchemy.VARCHAR(21), nullable=False),
    sqlalchemy.Column("coverage", sqlalchemy.Integer, nullable=False),
)

category = sqlalchemy.Table(
    "categories",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, sqlalchemy.Sequence("categories_id_seq", metadata=metadata),
                      primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR(60), nullable=False)
)

establishment = sqlalchemy.Table(
    "establishments",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, sqlalchemy.Sequence("establishments_id_seq", metadata=metadata),
                      primary_key=True),
    sqlalchemy.Column("coords", sqlalchemy.VARCHAR(21), nullable=False),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR(60), nullable=False),
    sqlalchemy.Column("address", sqlalchemy.VARCHAR, nullable=False),
    sqlalchemy.Column("website", sqlalchemy.VARCHAR)
)

category_establishment = sqlalchemy.Table(
    "category_establishment",
    metadata,
    sqlalchemy.Column("category_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("categories.id"), nullable=False,
                      primary_key=True),
    sqlalchemy.Column("establishment_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("establishments.id"), nullable=False,
                      primary_key=True)
)
