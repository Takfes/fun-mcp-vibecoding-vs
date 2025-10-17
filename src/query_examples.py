#!/usr/bin/env python3
"""
Query Example Script

This script demonstrates how to use the `get_sqlalchemy_engine` function from the `db_helper` module
along with `pandas.read_sql` to execute a simple SQL query (`SELECT COUNT(*) AS total_count FROM pokemon`)
against a specified database (PostgreSQL or MySQL).

Usage:
    python src/query_examples.py --db postgresql
    python src/query_examples.py --db mysql

Arguments:
    --db: Specify the database type to connect to ('postgresql' or 'mysql').

Returns:
    Prints the total count of records in the 'pokemon' table.

Note:
    Ensure that the database connection details are correctly configured in `db_helper.py`.
"""

import pandas as pd

from db_helper import get_sqlalchemy_engine

db_type = "postgresql"  # or "mysql"

query = "SELECT * FROM pokemon"
engine = get_sqlalchemy_engine("postgresql")
df = pd.read_sql(query, con=engine)
