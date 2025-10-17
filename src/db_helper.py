#!/usr/bin/env python3
"""
db_helper.py

Minimal helper returning an SQLAlchemy Engine configured from environment
variables so it can be passed directly to pandas.read_sql(engine, sql).

Public function:
    get_sqlalchemy_engine(db_type: str) -> sqlalchemy.Engine

Supported db_type values: 'postgresql', 'mysql'
"""

import os
from urllib.parse import quote_plus

from sqlalchemy import create_engine


def get_sqlalchemy_engine(db_type: str):
    """
    Build and return an SQLAlchemy Engine for the requested database type.

    Args:
        db_type: 'postgresql' or 'mysql'

    Returns:
        sqlalchemy.Engine

    Raises:
        ValueError: if db_type is unsupported
    """
    if db_type == "postgresql":
        user = os.getenv("POSTGRES_USER", "pokemon_user")
        password = os.getenv("POSTGRES_PASSWORD", "pokemon_pass")
        host = os.getenv("POSTGRES_HOST", "localhost")
        port = os.getenv("POSTGRES_PORT", "5432")
        db = os.getenv("POSTGRES_DB", "pokemon_db")

        # Use psycopg2 driver via SQLAlchemy
        password_quoted = quote_plus(password)
        url = f"postgresql+psycopg2://{user}:{password_quoted}@{host}:{port}/{db}"

    elif db_type == "mysql":
        user = os.getenv("MYSQL_USER", "pokemon_user")
        password = os.getenv("MYSQL_PASSWORD", "pokemon_pass")
        host = os.getenv("MYSQL_HOST", "localhost")
        port = os.getenv("MYSQL_PORT", "3306")
        db = os.getenv("MYSQL_DATABASE", "pokemon_db")

        # Use pymysql driver via SQLAlchemy
        password_quoted = quote_plus(password)
        url = f"mysql+pymysql://{user}:{password_quoted}@{host}:{port}/{db}?charset=utf8mb4"

    else:
        raise ValueError(f"Unsupported database type: {db_type}")

    # create_engine will lazily connect; pool_pre_ping helps with stale connections
    engine = create_engine(url, pool_pre_ping=True)
    return engine
