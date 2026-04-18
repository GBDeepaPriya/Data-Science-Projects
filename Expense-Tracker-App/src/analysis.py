import pandas as pd

def category_analysis():

    df = pd.read_csv(
        "data/processed_expense_data.csv"
    )

    category_total = df.groupby(
        "category"
    )["amount"].sum()

    category_total.to_csv(
        "outputs/category_summary.csv"
    )

    print("\nCategory Summary:")
    print(category_total)

def monthly_trends():

    df = pd.read_csv(
        "data/processed_expense_data.csv"
    )

    monthly_total = df.groupby(
        ["year", "month"]
    )["amount"].sum()

    monthly_total.to_csv(
        "outputs/monthly_trends.csv"
    )

    print("\nMonthly Trends:")
    print(monthly_total)

def spending_patterns():

    df = pd.read_csv(
        "data/processed_expense_data.csv"
    )

    weekend_spending = df.groupby(
        "is_weekend"
    )["amount"].sum()

    weekend_spending.to_csv(
        "outputs/weekend_spending.csv"
    )

    print("\nWeekend Spending:")
    print(weekend_spending)

if __name__ == "__main__":

    category_analysis()
    monthly_trends()
    spending_patterns()