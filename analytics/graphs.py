import pandas as pd
import matplotlib.pyplot as plt
import os

def load_expenses():
    filepath = "data/expenses.xlsx"
    if not os.path.exists(filepath):
        return None
    return pd.read_excel(filepath)

def category_pie_chart():
    df = load_expenses()
    if df is None or df.empty:
        return None
    
    fig, ax = plt.subplots()
    category_totals = df.groupby('category')['amount'].sum()
    ax.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%')
    ax.set_title("Spending by Category")
    return fig

def monthly_bar_chart():
    df = load_expenses()
    if df is None or df.empty:
        return None
    
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.strftime('%b %Y')
    
    fig, ax = plt.subplots()
    monthly_totals = df.groupby('month')['amount'].sum()
    monthly_totals.plot(kind='bar', ax=ax, color='steelblue')
    ax.set_title("Monthly Spending")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def top_expenses_chart():
    df = load_expenses()
    if df is None or df.empty:
        return None
    
    fig, ax = plt.subplots()
    top = df.nlargest(5, 'amount')[['description', 'amount']]
    ax.barh(top['description'], top['amount'], color='coral')
    ax.set_title("Top 5 Expenses")
    ax.set_xlabel("Amount (₹)")
    plt.tight_layout()
    return fig