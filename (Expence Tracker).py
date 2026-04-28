import pandas as pd
import matplotlib.pyplot as plt
import os

def track_expenses():
    filename = 'expenses.csv'
    
    # Create file if it doesn't exist
    if not os.path.isfile(filename):
        df = pd.DataFrame(columns=['Date', 'Category', 'Amount'])
        df.to_csv(filename, index=False)

    print("--- Personal Expense Tracker ---")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Rent, Bills, Fun): ")
    amount = float(input("Enter amount: "))

    # Append new data
    new_data = pd.DataFrame([[date, category, amount]], columns=['Date', 'Category', 'Amount'])
    new_data.to_csv(filename, mode='a', header=False, index=False)
    
    # Generate Visualization
    df = pd.read_csv(filename)
    summary = df.groupby('Category')['Amount'].sum()
    
    summary.plot(kind='pie', autopct='%1.1f%%', title="Spending by Category")
    plt.ylabel('')
    plt.savefig('expense_report.png')
    print("Expense saved! Report generated as 'expense_report.png'.")

if __name__ == "__main__":
    track_expenses()