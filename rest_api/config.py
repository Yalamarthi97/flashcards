import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = f"""postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}@{os.environ["POSTGRES_DATABASE_HOST"]}:{os.environ["PORT"]}/{os.environ["PORT"]}"""
