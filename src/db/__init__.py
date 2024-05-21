from sqlalchemy import create_engine, text


def init_db():
    user = 'postgres'
    password = 'postgres'
    host = 'postgres'
    port = '5432'
    database = 'postgres'
    return create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}", echo=True)

def execute_query(query, query_params):
    db = init_db()

    with db.connect() as connection:
        connection.execute(text(query), query_params)
        connection.commit()

def execute_and_fetch_query(query, query_params):
    db = init_db()

    with db.connect() as connection:
        rows = connection.execute(text(query), query_params)
        connection.commit()

    result = []
    for row in rows:
        result.append(row._asdict())

    return result
