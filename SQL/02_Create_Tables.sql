CREATE TABLE customers(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(100) NOT NULL,
age INT,
gender VARCHAR(10),
city VARCHAR(50) NOT NULL,
joining_date DATE
);

CREATE TABLE subscriptions(
subscription_id INT PRIMARY KEY,
customer_id INT,
plan_type VARCHAR(50),
monthly_fee DECIMAL(10,2),
contract_type VARCHAR(20),
start_date DATE,
end_date DATE,
subscription_status VARCHAR(20),

FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE payments(
payment_id INT PRIMARY KEY,
customer_id INT,
amount DECIMAL(10,2),
payment_date DATE,

FOREIGN KEY (customer_id ) REFERENCES CUSTOMERS(customer_id)
);

CREATE TABLE complaints(
complaint_id INT PRIMARY KEY,
customer_id INT,
complaint_type VARCHAR(50),
complaint_date DATE,
complaint_status VARCHAR(20),

FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

