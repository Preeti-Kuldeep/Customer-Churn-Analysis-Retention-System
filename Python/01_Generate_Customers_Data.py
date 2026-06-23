import pandas as pd
import random
from datetime import datetime, timedelta

# Sample data
first_names = [
    "Rahul", "Priya", "Amit", "Sneha", "Karan",
    "Neha", "Arjun", "Pooja", "Rohit", "Anjali",
    "Vikas", "Meera", "Sanjay", "Kavya", "Manoj",
    "Divya", "Nikhil", "Riya", "Akash", "Shreya",
    "Aditya", "Isha", "Rakesh", "Tanya", "Siddharth",
    "Ananya", "Vivek", "Sanya", "Raghav","Aarav",
]

last_names = [
    "Sharma", "Patel", "Kumar", "Reddy", "Singh",
    "Gupta", "Mehta", "Verma", "Jain", "Desai",
    "Chopra", "Kapoor", "Malhotra", "Bhatia", "Agarwal",
    "Choudhary", "Saxena", "Nair", "Joshi", "Bansal",
    "Chatterjee", "Rao", "Iyer", "Dutta", 
]

cities = [
    "Mumbai", "Pune", "Delhi", "Bangalore",
    "Hyderabad", "Chennai", "Ahmedabad",
    "Kolkata", "Jaipur", "Lucknow"
]

data = []

for i in range(1, 501):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    customer_name = f"{first_name} {last_name}"
    age = random.randint(18, 65)
    gender = random.choice(["Male", "Female"])
    city = random.choice(cities)

    email = f"{first_name.lower()}.{last_name.lower()}{i}@gmail.com"
    phone_number = f"9{random.randint(100000000, 999999999)}"

    joining_date = (
        datetime(2021, 1, 1)
        + timedelta(days=random.randint(0, 1800))
    ).strftime("%Y-%m-%d")

    data.append([
        1000 + i,
        customer_name,
        age,
        gender,
        city,
        email,
        phone_number,
        joining_date
    ])

df = pd.DataFrame(
    data,
    columns=[
        "customer_id",
        "customer_name",
        "age",
        "gender",
        "city",
        "email",
        "phone_number",
        "joining_date"
    ]
)

df.to_csv(
    r"C:\Users\Preeti\OneDrive\Desktop\Customer-Churn-Analysis-Retention-System\Data\customers.csv",
    index=False
)

print("500 customer records generated successfully.")