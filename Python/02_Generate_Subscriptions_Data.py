import pandas as pd
import random
from datetime import datetime, timedelta

# Load customer data
customers = pd.read_csv(
    r"C:\Users\Preeti\OneDrive\Desktop\Customer-Churn-Analysis-Retention-System\Data\customers.csv"
)

subscriptions = []

for i, customer_id in enumerate(customers["customer_id"], start=1):

    plan_type = random.choice(["Basic", "Standard", "Premium"])

    if plan_type == "Basic":
        monthly_fee = 499
    elif plan_type == "Standard":
        monthly_fee = 699
    else:
        monthly_fee = 999

    contract_type = random.choice(["Monthly", "Yearly"])

    start_date = (
        datetime(2021, 1, 1)
        + timedelta(days=random.randint(0, 1200))
    )

    # 20% churn rate
    status = random.choices(
        ["Active", "Churned"],
        weights=[80, 20],
        k=1
    )[0]

    if status == "Churned":
        end_date = start_date + timedelta(days=random.randint(30, 600))
        end_date = end_date.strftime("%Y-%m-%d")
    else:
        end_date = "2099-12-31"  # Placeholder for active subscriptions

    subscriptions.append([
        2000 + i,
        customer_id,
        plan_type,
        monthly_fee,
        contract_type,
        start_date.strftime("%Y-%m-%d"),
        end_date,
        status
    ])

df = pd.DataFrame(
    subscriptions,
    columns=[
        "subscription_id",
        "customer_id",
        "plan_type",
        "monthly_fee",
        "contract_type",
        "start_date",
        "end_date",
        "subscription_status"
    ]
)

df.to_csv(
    r"C:\Users\Preeti\OneDrive\Desktop\Customer-Churn-Analysis-Retention-System\Data\subscriptions.csv",
    index=False
)

print("500 subscription records generated successfully.")