import sqlalchemy

metadata = sqlalchemy.MetaData()

university = sqlalchemy.Table(
    "universities",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, sqlalchemy.Sequence("universities_id_seq", metadata=metadata),
                      primary_key=True, nullable=False),
    sqlalchemy.Column("full_name", sqlalchemy.text, nullable=False),
    sqlalchemy.Column("address", sqlalchemy.text, nullable=False),
    sqlalchemy.Column("metro", sqlalchemy.Integer, sqlalchemy.ForeignKey("metro"), nullable=False),
    sqlalchemy.Column("web_site", sqlalchemy.VARCHAR(40), nullable=False),
    sqlalchemy.Column("coords", sqlalchemy.VARCHAR(21), nullable=False)
)

showroom = sqlalchemy.Table(
    "showrooms",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, sqlalchemy.Sequence("showrooms_id_seq", metadata=metadata),
                      primary_key=True, nullable=False),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR(40), nullable=False),
    sqlalchemy.Column("address", sqlalchemy.text, nullable=False),
    sqlalchemy.Column("coords", sqlalchemy.VARCHAR(21), nullable=False),
    sqlalchemy.Column("website", sqlalchemy.VARCHAR(40)),
    sqlalchemy.Column("phone", sqlalchemy.VARCHAR(12)),
    sqlalchemy.Column("description", sqlalchemy.text),
)


metro = sqlalchemy.Table(
    "metros",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, sqlalchemy.Sequence("metros_id_seq", metadata=metadata),
                      primary_key=True, nullable=False),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR(20), nullable=False),
    sqlalchemy.Column("coords", sqlalchemy.VARCHAR(21), nullable=False),
    sqlalchemy.Column("closed", sqlalchemy.Boolean, nullable=False, default=False),
)


museum = sqlalchemy.Table(
    "museums",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, sqlalchemy.Sequence("museums_id_seq", metadata=metadata)
                      , primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR(40), nullable=False),
    sqlalchemy.Column("address", sqlalchemy.text, nullable=False),
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