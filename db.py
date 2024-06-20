# from sqlalchemy import create_engine, text
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# db_url = os.getenv('SQLALCHEMY_DATABASE_URI')
# print(db_url)

# # Create an engine
# engine = create_engine(db_url)

# # Connect to the database
# with engine.connect() as connection:
#     result = connection.execute(text("SELECT version();"))
#     for row in result:
#         print(row)
