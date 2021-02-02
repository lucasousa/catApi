import sqlalchemy


metadata = sqlalchemy.MetaData()


cats = sqlalchemy.Table(
    "cats",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("breed", sqlalchemy.String),
    sqlalchemy.Column("location_of_origin", sqlalchemy.String),
    sqlalchemy.Column("coat_length", sqlalchemy.String),
    sqlalchemy.Column("body_type", sqlalchemy.String),
    sqlalchemy.Column("pattern", sqlalchemy.String),
)