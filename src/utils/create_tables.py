import psycopg2
from config import load_db_config
from typing import List

def execute_sql_commands(commands: List[str], connection):
    """Execute multiple SQL commands"""
    with connection.cursor() as cursor:
        for command in commands:
            cursor.execute(command)

def create_tables(connection: psycopg2.extensions.connection):
    """Create tables in the PostgreSQL database"""
    commands = [
        """
        CREATE TABLE IF NOT EXISTS artist (
            id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            type VARCHAR(255),
            genres VARCHAR(255),
            popularity INTEGER
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS album (
            id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255),
            artist_id TEXT [],
            album_type VARCHAR(255),
            release_date DATE,
            total_tracks INTEGER,
            available_markets TEXT [],
            disc_number INTEGER
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS songs (
            id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255),
            duration_ms INTEGER,
            popularity INTEGER,
            album_id VARCHAR(255),
            type VARCHAR(255),
            track_number INTEGER,
            available_markets TEXT [],
            explicit BOOLEAN,
            is_local BOOLEAN,
            FOREIGN KEY (album_id) REFERENCES album(id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS activity (
            id SERIAL PRIMARY KEY,
            played_at TIMESTAMP,
            song_id VARCHAR(255),
            FOREIGN KEY (song_id) REFERENCES songs(id)
        )
        """
    ]

    try:
        execute_sql_commands(commands, connection)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def main():
    try:
        config = load_db_config()
        with psycopg2.connect(**config) as conn:
            create_tables(conn)
    except psycopg2.DatabaseError as e:
        print(f"Database Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
