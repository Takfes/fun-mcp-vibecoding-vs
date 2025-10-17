#!/usr/bin/env python3
"""
load_pokemon_data.py

Minimal utilities to download the Pokemon CSV and load it directly into a database
using pandas.to_sql and the SQLAlchemy engine provided by `db_helper.get_sqlalchemy_engine`.

Public functions:
  - download_pokemon_dataframe(url: str) -> pandas.DataFrame
  - load_dataframe_to_db(df: pandas.DataFrame, db_type: str, table_name: str = 'pokemon')

This module does not write the CSV to disk.
"""

from typing import Optional
import logging
from io import StringIO

import pandas as pd
import requests

from db_helper import get_sqlalchemy_engine

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Default dataset URL (change if you have another source)
DEFAULT_POKEMON_CSV = "https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv"


def download_pokemon_dataframe(
    url: str = DEFAULT_POKEMON_CSV,
) -> Optional[pd.DataFrame]:
    """Download the CSV from `url` and return a pandas DataFrame.

    Returns None on failure.
    """
    try:
        logger.info(f"Downloading Pokemon CSV from {url}")
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        csv_text = resp.text
        df = pd.read_csv(StringIO(csv_text))
        logger.info(
            f"Downloaded CSV with {len(df)} rows and columns: {list(df.columns)}"
        )
        return df
    except Exception as e:
        logger.error(f"Failed to download or parse CSV: {e}")
        return None


def _prepare_dataframe_for_db(df: pd.DataFrame) -> pd.DataFrame:
    """Lightweight normalization to match the 'pokemon' table schema used earlier.

    - rename columns where necessary
    - coerce numeric columns
    - ensure boolean for 'Legendary'
    """
    df = df.copy()
    mapping = {
        "#": "pokemon_id",
        "Name": "name",
        "Type 1": "type1",
        "Type 2": "type2",
        "Total": "total",
        "HP": "hp",
        "Attack": "attack",
        "Defense": "defense",
        "Sp. Atk": "sp_atk",
        "Sp. Def": "sp_def",
        "Speed": "speed",
        "Generation": "generation",
        "Legendary": "legendary",
    }

    df = df.rename(columns=mapping)
    if "type2" in df.columns:
        df["type2"] = df["type2"].where(pd.notnull(df["type2"]), None)

    if "legendary" in df.columns:
        df["legendary"] = df["legendary"].astype(bool)

    # Coerce numeric columns
    for col in [
        "pokemon_id",
        "total",
        "hp",
        "attack",
        "defense",
        "sp_atk",
        "sp_def",
        "speed",
        "generation",
    ]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def load_dataframe_to_db(
    df: pd.DataFrame,
    db_type: str,
    table_name: str = "pokemon",
    if_exists: str = "append",
) -> bool:
    """Load a pandas DataFrame into the database using pandas.to_sql and SQLAlchemy engine.

    Returns True on success, False otherwise.
    """
    try:
        engine = get_sqlalchemy_engine(db_type)
    except Exception as e:
        logger.error(f"Could not create SQLAlchemy engine: {e}")
        return False

    df_prepared = _prepare_dataframe_for_db(df)

    try:
        # Use DataFrame.to_sql with the engine
        df_prepared.to_sql(
            name=table_name,
            con=engine,
            if_exists=if_exists,
            index=False,
            method="multi",
        )
        logger.info(f"Inserted {len(df_prepared)} rows into {db_type}.{table_name}")
        return True
    except Exception as e:
        logger.error(f"Failed to insert DataFrame to {db_type}: {e}")
        return False


if __name__ == "__main__":
    # Simple CLI: download and load into Postgres and MySQL (if available)
    df = download_pokemon_dataframe()
    if df is None:
        raise SystemExit(1)

    # Try Postgres
    try:
        ok = load_dataframe_to_db(df, "postgresql", if_exists="replace")
        if not ok:
            logger.error("Loading into Postgres failed")
    except Exception:
        logger.exception("Postgres load raised")

    # Try MySQL
    try:
        ok = load_dataframe_to_db(df, "mysql", if_exists="replace")
        if not ok:
            logger.error("Loading into MySQL failed")
    except Exception:
        logger.exception("MySQL load raised")
