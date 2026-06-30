-- ===============================================
-- CUSTOMER CHURN ANALYSIS & RETENTION SYSTEM
-- MODULE 1 : CUSTOMER ANALYSIS
-- ===============================================

USE customer_churn_db;

-- ===============================================
-- 1. Total Customers
-- How many customers does the company have?
-- ===============================================

SELECT COUNT(*) AS Total_Customers
FROM customers;

-- ===============================================
-- 2. Customers by City
-- Which cities have the highest number of customers?
-- ===============================================

SELECT
    city,
    COUNT(*) AS Total_Customers
FROM customers
GROUP BY city
ORDER BY Total_Customers DESC;

-- ===============================================
-- 3. Customers by Gender
-- What is the gender distribution of customers?
-- ===============================================

SELECT
    gender,
    COUNT(*) AS Total_Customers
FROM customers
GROUP BY gender;

-- ===============================================
-- 4. Average Customer Age
-- What is the average age of customers?
-- ===============================================

SELECT
    ROUND(AVG(age),2) AS Average_Age
FROM customers;

-- ===============================================
-- 5. Youngest and Oldest Customer
-- What is the age range of customers?
-- ===============================================

SELECT
    MIN(age) AS Youngest_Customer,
    MAX(age) AS Oldest_Customer
FROM customers;

-- ===============================================
-- 6. Customers by Age Group
-- Business Question:
-- Which age group has the highest number of customers?
-- ===============================================

SELECT
    CASE
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 45 THEN '36-45'
        WHEN age BETWEEN 46 AND 55 THEN '46-55'
        ELSE '56+'
    END AS Age_Group,

    COUNT(*) AS Total_Customers
FROM customers
GROUP BY Age_Group
ORDER BY Total_Customers DESC;

-- ----------------------------------------------------------
-- Query 7 : Customers Joined by Year
-- Business Question : How many customers joined each year?
-- Functions Used :
-- YEAR()   - Extracts the year from a date.
-- COUNT()  - Counts customers.
-- GROUP BY - Groups customers by year.
-- ----------------------------------------------------------

SELECT
    YEAR(joining_date) AS Joining_Year,
    COUNT(*) AS Total_Customers
FROM customers
GROUP BY YEAR(joining_date)
ORDER BY Joining_Year;

-- ----------------------------------------------------------
-- Query 8 : Customers Joined by Month
-- Business Question : Which month has the highest customer registrations?
-- Functions Used :
-- MONTHNAME() - Returns the month name.
-- MONTH()     - Returns the month number for proper sorting.
-- COUNT()     - Counts customers.
-- GROUP BY    - Groups customers by month.
-- ----------------------------------------------------------

SELECT
    MONTHNAME(joining_date) AS Month_Name,
    COUNT(*) AS Total_Customers
FROM customers
GROUP BY
    MONTH(joining_date),
    MONTHNAME(joining_date)
ORDER BY MONTH(joining_date);

-- ----------------------------------------------------------
-- Query 9 : Top 5 Cities by Customers
-- Business Question : Which are the top 5 cities with the highest customers?
-- Functions Used :
-- COUNT()  - Counts customers.
-- GROUP BY - Groups customers by city.
-- ORDER BY - Sorts the result.
-- LIMIT    - Restricts the output to 5 rows.
-- ----------------------------------------------------------

SELECT
    city,
    COUNT(*) AS Total_Customers
FROM customers
GROUP BY city
ORDER BY Total_Customers DESC
LIMIT 5;

-- ----------------------------------------------------------
-- Query 10 : Gender Percentage
-- Business Question : What percentage of customers are Male and Female?
-- ----------------------------------------------------------
SELECT
    gender,
    COUNT(*) AS Total_Customers,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM customers),
        2
    ) AS Percentage
FROM customers
GROUP BY gender;

-- ----------------------------------------------------------
-- Query 11 : Customers Joined in the Last 2 Years
-- Business Question : How many customers joined in the last 2 years?
-- Functions Used :
-- CURDATE() - Returns the current system date.
-- INTERVAL  - Subtracts a specific time period from a date.
-- WHERE     - Filters rows based on a condition.
-- ----------------------------------------------------------

SELECT
    customer_id,
    customer_name,
    city,
    joining_date
FROM customers
WHERE joining_date >= CURDATE() - INTERVAL 2 YEAR
ORDER BY joining_date;