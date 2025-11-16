import psycopg2
from api_request import mock_fetch_data

def connect_to_db():
    print("Connecting to the PostgreSQL database...")
    try:
        conn = psycopg2.connect(
            host="localhost",
            port = 5000,
            password="db_password",
            user="db_user",
            dbname="db",
        )
        return conn

    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        raise

def create_table(conn):
    print("Creating weather_data table if it doesn't exist...")
    
    try:
        cursor = conn.cursor()
        create_table_query = """
    CREATE SCHEMA IF NOT EXISTS dev;
    CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
        id SERIAL PRIMARY KEY,
        city TEXT,
        weather FLOAT,
        wind_speed FLOAT,
        time TIMESTAMP,
        weather_description TEXT,
        temperature FLOAT,
        inserted_at TIMESTAMP DEFAULT NOW(),
        utc_offset FLOAT   
    );
    """
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        print("Table was created.")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
        raise

conn = connect_to_db()
create_table(conn)

        