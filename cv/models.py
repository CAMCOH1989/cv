from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table, text, ForeignKey, Boolean, UniqueConstraint


def get_column_names(constraint, table) -> str:
    return "_".join([
        column.name for column in constraint.columns.values()
    ])


convention = {
    "all_column_names": get_column_names,
    "ix": "ix__%(all_column_names)s",
    "uq": "uq__%(table_name)s__%(all_column_names)s",
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    "fk": "fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s",
    "pk": "pk__%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

guests_table = Table(
    "guests",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("ip", String),
    Column("user_agent", String),
    Column("visit_datetime", String),
    Column("os", String),
)

skills_table = Table(
    "skills",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("skill_name", String),
    Column("skill_weight", Integer),
)


class Tables:
    guests = guests_table
