import pandas as pd

def generate_insights():

    df = pd.read_csv(
        "data/processed_expense_data.csv"
    )

    total_spent = df["amount"].sum()
    avg_spent = df["amount"].mean()

    highest_category = df.groupby(
        "category"
    )["amount"].sum().idxmax()

    print("\n===== INSIGHTS =====")

    print(
        f"Total Spending: ₹{round(total_spent,2)}"
    )

    print(
        f"Average Expense: ₹{round(avg_spent,2)}"
    )

    print(
        f"Highest Spending Category: {highest_category}"
    )

    # Overspending Detection
    overspending = df[df["amount"] > df["budget"]]

    print(
        f"Overspending Instances: {len(overspending)}"
    )

if __name__ == "__main__":
    generate_insights()