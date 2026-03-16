import ollama
import pandas as pd
import os

def ask_question(question: str):
    filepath = "data/expenses.xlsx"
    if not os.path.exists(filepath):
        return "No expense data found. Please add some expenses first."

    df = pd.read_excel(filepath)
    
    # Convert data to string summary for the AI
    data_summary = df.to_string(index=False)
    
    prompt = f"""
You are a personal finance assistant.
Answer the question based ONLY on the expense data below.
Be concise and specific. Use ₹ for amounts.

Expense Data:
{data_summary}

Question: {question}
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0}
    )

    return response['message']['content']