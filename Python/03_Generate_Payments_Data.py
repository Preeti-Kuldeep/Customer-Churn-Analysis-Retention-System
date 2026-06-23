import pandas as pd
import random
from datetime import datetime, timedelta

# Load subscriptions data
subscriptions = pd.read_csv(
    r"C:\Users\Preeti\OneDrive\Desktop\Customer-Churn-Analysis-Retention-System\Data\subscriptions.csv"
)

payments = []
payment_id = 3001

for _, row in subscriptions.iterrows():

    customer_id = row["customer_id"]
    monthly_fee = row["monthly_fee"]

    # Generate 8 to 15 payments per customer
    number_of_payments = random.randint(8, 15)

    for _ in range(number_of_payments):

        payment_date = (
            datetime(2021, 1, 1)
            + timedelta(days=random.randint(0, 1500))
        )

        payments.append([
            payment_id,
            customer_id,
            monthly_fee,
            payment_date.strftime("%Y-%m-%d")
        ])

        payment_id += 1

payments_df = pd.DataFrame(
    payments,
    columns=[
        "payment_id",
        "customer_id",
        "amount",
        "payment_date"
    ]
)

payments_df.to_csv(
    r"C:\Users\Preeti\OneDrive\Desktop\Customer-Churn-Analysis-Retention-System\Data\payments.csv",
    index=False
)

print(f"{len(payments_df)} payment records generated successfully.")