import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


# References the credentials specified in the .env file
CSV_URL = os.getenv("CSV_URL")
DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")

# Sets up SQLAlchemy engine that allows python to interact with the postgres database.
engine = create_engine(f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{PG_HOST}:{PG_PORT}/{POSTGRES_DB}")

# creates a full path to a file named annual-enterprise.csv that is located inside a directory represented by the variable DOWNLOAD_DIR
# N/B: Using os.path.join ensures this code works across different operating systems without worrying about path separators.
file_path = os.path.join(DOWNLOAD_DIR, "annual-enterprise.csv")

print("Downloading CSV file")
os.system(f"curl -L {CSV_URL} -o {file_path}")

print("Reading CSV into Pandas")
df = pd.read_csv(file_path)

print("Loading into Postgres")
df.to_sql("staging_enterprise", engine, if_exists="replace", index=False)

print("Data successfully loaded to staging_enterprise table.")