# 📈 Sales Trend Analysis

> **Learning Goal:** Learn how to spot patterns, seasonality, and growth in time-series retail data.

---

## 📅 Why Time Matters

In retail, a single number (Total Sales) isn't enough. We need to know:
- Are we growing month-over-month?
- Do we sell more on weekends?
- Is there a holiday spike?

---

## 1️⃣ Seasonality and Cyclical Patterns

**Seasonality** refers to fluctuations that repeat over a specific period (e.g., higher sales during Diwali or New Year).

- **Week-over-Week (WoW)**: Catching weekend surges.
- **Month-over-Month (MoM)**: Tracking general business healthy.
- **Year-over-Year (YoY)**: The gold standard. "Did we do better this December than last December?"

---

## 2️⃣ Moving Averages (Smoothing)

Daily sales data is often "noisy" (zig-zagging). Analysts use **moving averages** to smooth out the noise and see the real trend.

**Example: 7-Day Moving Average**
It averages the last 7 days of sales. This removes the "weekend spike" effect and shows if the sales line is generally going up or down.

```python
# Pandas Example
df['rolling_sales'] = df['amount'].rolling(window=7).mean()
```

---

## 3️⃣ Performance Benchmarking

Comparing a store's performance against a target or against the previous period.

- **Positive Growth**: "Sales up 15% due to Summer Sale."
- **Flat Growth**: "No change. Need more promotions."
- **Negative Growth**: "Down 10%. Competitor opened nearby?"

---

## 💡 Industry Case: The "Mid-Month Dip"

Many Indian retailers see a dip in sales around the 15th–20th of the month.
- **Observation**: Salaries are running low.
- **Insight**: Customers are waiting for the next paycheck.
- **Business Decision**: Launch "Budget Week" or "Flash Sales" during the 15th–20th to stimulate demand.

---

## 🧠 Quick Check Questions

1. What is the difference between MoM and YoY growth?
2. Why is a rolling average better than raw daily data for identifying trends?
3. If sales were ₹5,000 in January and ₹6,000 in February, what is the MoM growth %?
4. Look at the `transactions` data. Is there a specific month where sales peak?

---

*Next Topic → [Customer Insights & Segmentation](./03_Customer_Insights.md)*
