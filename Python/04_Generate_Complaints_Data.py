import pandas as pd
import random
from datetime import datetime, timedelta

# Load customer data
customers = pd.read_csv(
    r"C:\Users\Preeti\OneDrive\Desktop\Customer-Churn-Analysis-Retention-System\Data\customers.csv"
)

complaint_types = [
    "Billing Issue",
    "Network Issue",
    "Technical Problem",
    "Service Outage",
    "Poor Customer Support",
    "Payment Failure",
    "Plan Change Request"
]

statuses = [
    "Open",
    "In Progress",
    "Resolved",
    "Closed"
]

complaints = []
complaint_id = 4001

# Generate 1-3 complaints for some customers
for _, row in customers.iterrows():

    customer_id = row["customer_id"]

    # About 70% customers will have complaints
    if random.random() < 0.70:

        for _ in range(random.randint(1, 3)):

            complaint_date = (
                datetime(2021, 1, 1)
                + timedelta(days=random.randint(0, 1500))
            )

            complaints.append([
                complaint_id,
                customer_id,
                random.choice(complaint_types),
                complaint_date.strftime("%Y-%m-%d"),
                random.choice(statuses)
            ])

            complaint_id += 1

complaints_df = pd.DataFrame(
    complaints,
    columns=[
        "complaint_id",
        "customer_id",
        "complaint_type",
        "complaint_date",
        "complaint_status"
    ]
)

complaints_df.to_csv(
    r"C:\Users\Preeti\OneDrive\Desktop\Customer-Churn-Analysis-Retention-System\Data\complaints.csv",
    index=False
)

print(f"{len(complaints_df)} complaint records generated successfully.")