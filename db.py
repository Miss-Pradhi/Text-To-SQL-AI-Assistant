from sqlalchemy import create_engine, text
from faker import Faker
import random

engine = create_engine("sqlite:///enterprise.db")
fake = Faker()

def init_db():
    with engine.connect() as conn:

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY,
            name TEXT,
            city TEXT
        )
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS sales(
            id INTEGER PRIMARY KEY,
            product TEXT,
            region TEXT,
            amount INTEGER,
            customer_id INTEGER
        )
        """))

        count = conn.execute(text("SELECT COUNT(*) FROM sales")).fetchone()[0]

        if count == 0:

            cities = ["Pune","Mumbai","Delhi","Nagpur","Bangalore"]
            products = ["Laptop","Phone","Tablet","Monitor","Keyboard"]

            # 20 customers
            for i in range(1,21):
                conn.execute(text("""
                INSERT INTO customers VALUES (:id,:name,:city)
                """),{
                    "id":i,
                    "name":fake.first_name(),
                    "city":random.choice(cities)
                })

            # 50 sales rows
            for i in range(1,51):
                conn.execute(text("""
                INSERT INTO sales VALUES (:id,:product,:region,:amount,:cid)
                """),{
                    "id":i,
                    "product":random.choice(products),
                    "region":random.choice(cities),
                    "amount":random.randint(10000,90000),
                    "cid":random.randint(1,20)
                })

        conn.commit()