# Database Design

## Database Name

customer_churn_db

## Database Overview

The Customer Churn Analysis & Retention System uses a relational database to store customer information, subscription details, payment transactions, and complaint records.

The database is designed to support customer churn analysis, KPI reporting, revenue analysis, and customer retention strategies.

## Main Tables

1. Customers
2. Subscriptions
3. Payments
4. Complaints

## Table 1: Customers

### Purpose

Stores customer master information.

### Columns

| Column Name   | Data Type    | Description                |
| ------------- | ------------ | -------------------------- |
| customer_id   | INT          | Unique customer identifier |
| customer_name | VARCHAR(100) | Customer full name         |
| age           | INT          | Customer age               |
| gender        | VARCHAR(10)  | Customer gender            |
| city          | VARCHAR(50)  | Customer city              |
| joining_date  | DATE         | Customer joining date      |

### Primary Key

customer_id

### Validation Rules

#### customer_id

* Must be unique
* Cannot be NULL
* Positive integer only

#### customer_name

* Cannot be NULL
* Maximum length: 100 characters

#### age

* Minimum value: 18
* Maximum value: 80

#### gender

Allowed values:

* Male
* Female
* Other

#### city

* Cannot be NULL

#### joining_date

* Cannot be a future date

## Table 2: Subscriptions

### Purpose

Stores customer subscription and plan information.

### Columns

| Column Name         | Data Type     | Description                    |
| ------------------- | ------------- | ------------------------------ |
| subscription_id     | INT           | Unique subscription identifier |
| customer_id         | INT           | Customer reference             |
| plan_type           | VARCHAR(50)   | Subscription plan              |
| monthly_fee         | DECIMAL(10,2) | Monthly subscription fee       |
| contract_type       | VARCHAR(20)   | Monthly or Yearly contract     |
| start_date          | DATE          | Subscription start date        |
| end_date            | DATE          | Subscription end date          |
| subscription_status | VARCHAR(20)   | Active or Churned              |

### Primary Key

subscription_id

### Foreign Key

customer_id → Customers(customer_id)

## Table 3: Payments

### Purpose

Stores customer payment transactions.

### Columns

| Column Name  | Data Type     | Description               |
| ------------ | ------------- | ------------------------- |
| payment_id   | INT           | Unique payment identifier |
| customer_id  | INT           | Customer reference        |
| amount       | DECIMAL(10,2) | Payment amount            |
| payment_date | DATE          | Date of payment           |

### Primary Key

payment_id

### Foreign Key

customer_id -> Customers(customer_id)

## Table 4: Complaints

### Purpose

Stores customer complaints and service issues.

### Columns

| Column Name      | Data Type   | Description                 |
| ---------------- | ----------- | --------------------------- |
| complaint_id     | INT         | Unique complaint identifier |
| customer_id      | INT         | Customer reference          |
| complaint_type   | VARCHAR(50) | Type of complaint           |
| complaint_date   | DATE        | Date complaint was raised   |
| complaint_status | VARCHAR(20) | Complaint status            |

### Primary Key

complaint_id

### Foreign Key

customer_id -> Customers(customer_id)

## Table Relationships

### Customers -> Subscriptions

Relationship Type: 1 : Many

One customer can have multiple subscriptions.

### Customers -> Payments

Relationship Type: 1 : Many

One customer can make multiple payments.

### Customers -> Complaints

Relationship Type: 1 : Many

One customer can raise multiple complaints.

## Database Relationship Summary

Customers (1) ---- (M) Subscriptions

Customers (1) ---- (M) Payments

Customers (1) ---- (M) Complaints
