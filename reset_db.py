import sys
from subprocess import call

import os
from sqlalchemy import create_engine


def run_migrations():
    root_connection_url = "mysql://root@localhost:3306/devday"

    print("******************************")
    print("Reseting DB")
    print("******************************")
    reset_migrations = [
        "DROP DATABASE devday",
        "CREATE DATABASE devday",
        "DROP USER 'test'@'%%'",
        "CREATE USER test@'%%' IDENTIFIED BY 'test'",
        "GRANT ALL ON devday.* TO 'test'@'%%'"
    ]

    engine = create_engine(root_connection_url)
    with engine.connect() as con:
        for statement in reset_migrations:
            con.execute(statement)


if __name__ == "__main__":
    run_migrations()
    call(["alembic", "-c", "devday_api/alembic.ini", "upgrade", "head"])
