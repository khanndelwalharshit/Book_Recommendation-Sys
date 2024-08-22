from sqlalchemy import create_engine

def get_database_connection():
    # Replace with your actual database URL
    engine = create_engine('sqlite:///books.db')
    connection = engine.connect()
    return connection
