# 📊 Aggregation & Grouping in SQL

> **Learning Goal:** Learn how to summarize millions of rows into meaningful insights using aggregate functions and GROUP BY.

---

## 1️⃣ Aggregate Functions

Aggregate functions perform a calculation on a set of values and return a single value.

| Function | Description | Example |
|----------|-------------|---------|
| `COUNT()` | Number of rows | `COUNT(*)` |
| `SUM()` | Total sum | `SUM(amount)` |
| `AVG()` | Average value | `AVG(amount)` |
| `MIN()` | Smallest value | `MIN(date)` |
| `MAX()` | Largest value | `MAX(amount)` |

```sql
-- Total Revenue
SELECT SUM(amount) AS total_revenue FROM transactions;

-- Average Transaction Value
SELECT AVG(amount) AS avg_ticket_size FROM transactions;
```

---

## 2️⃣ GROUP BY: The SQL Powerhouse

`GROUP BY` allows you to group rows that have the same values in specified columns.

**Example: Revenue by Store**
```sql
SELECT store, SUM(amount) AS store_revenue
FROM transactions
GROUP BY store
ORDER BY store_revenue DESC;
```

**Example: Category-wise Sales Performance**
```sql
SELECT category, COUNT(txn_id) AS total_orders, AVG(amount) AS avg_price
FROM transactions
GROUP BY category
ORDER BY total_orders DESC;
```

---

## 3️⃣ HAVING: Filtering Groups

`WHERE` filters rows *before* grouping. `HAVING` filters groups *after* aggregation.

```sql
-- Find categories with more than 50 orders
SELECT category, COUNT(*) as order_count
FROM transactions
GROUP BY category
HAVING order_count > 50;
```

---

## 📅 Common Use Case: Monthly Trends

SQL is excellent for time-series aggregation.

```sql
SELECT month, SUM(amount) as monthly_revenue
FROM transactions
GROUP BY month
ORDER BY month;
```

---

## 🧠 Quick Check Questions

1. What is the difference between `COUNT(*)` and `COUNT(column_name)`? (Hint: Think about NULLs).
2. Write a query to find the maximum `amount` spent in a single transaction.
3. How do you find the number of transactions per payment method?
4. When would you use `HAVING` instead of `WHERE`?

---

*Next Topic → [Joining Tables](./04_SQL_Joins.md)*
