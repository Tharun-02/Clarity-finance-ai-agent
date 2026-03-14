import pandas as pd
import os

def save_expenses(expense_list: list):
    filepath = "data/expenses.xlsx"
    os.makedirs("data", exist_ok=True)

    if os.path.exists(filepath):
        df_existing = pd.read_excel(filepath)
    else:
        df_existing = pd.DataFrame(columns=['date','description','amount','category','payment_method'])

    df_new = pd.DataFrame(expense_list)
    df_final = pd.concat([df_existing, df_new], ignore_index=True)
    df_final.to_excel(filepath, index=False)
    return df_final