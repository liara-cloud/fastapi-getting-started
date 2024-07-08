from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_USER="sa"
DB_NAME="myj"
DB_HOST="bromo.liara.cloud"
DB_PORT=31726
DB_PASS="Lr0nm5zjaYwVTSgb6MKCJCWD"

SQLALCHEMY_DATABASE_URL = (
    f"mssql+pyodbc://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False},  # only needed for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
