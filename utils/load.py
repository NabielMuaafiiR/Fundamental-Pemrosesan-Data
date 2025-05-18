from sqlalchemy import create_engine
import pandas as pd

def load_to_postgresql(df, table_name='products'):
    try:
        # Ganti info berikut sesuai konfigurasi PostgreSQL
        username = 'developer'
        password = 'nabiel123'
        host = 'localhost'
        port = '5432'
        database = 'productsdb'

        # Buat engine SQLAlchemy
        engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

        # Simpan ke database (replace jika sudah ada)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data berhasil disimpan ke PostgreSQL table '{table_name}'.")

    except Exception as e:
        print(f"Gagal menyimpan ke PostgreSQL: {e}")

def load_to_csv(df, filename):
    df.to_csv(filename, index=False)
