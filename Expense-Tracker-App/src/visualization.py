import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

def plot_category():

    df = pd.read_csv(
        "data/processed_expense_data.csv"
    )

    category_total = df.groupby(
        "category"
    )["amount"].sum().reset_index()

    plt.figure(figsize=(10,6))

    sns.barplot(
        x="category",
        y="amount",
        data=category_total
    )

    plt.xticks(rotation=45)

    plt.title("Category-wise Spending")

    plt.tight_layout()

    plt.savefig(
        "outputs/category_chart.png"
    )

    plt.show()

def plot_monthly():

    df = pd.read_csv(
        "data/processed_expense_data.csv"
    )

    monthly_total = df.groupby(
        ["year", "month"]
    )["amount"].sum().reset_index()

    plt.figure(figsize=(12,6))

    sns.lineplot(
        x="month",
        y="amount",
        data=monthly_total
    )

    plt.title("Monthly Spending Trend")

    plt.savefig(
        "outputs/monthly_chart.png"
    )

    plt.show()

def plot_pie():

    df = pd.read_csv(
        "data/processed_expense_data.csv"
    )

    category_total = df.groupby(
        "category"
    )["amount"].sum()

    plt.figure(figsize=(8,8))

    plt.pie(
        category_total,
        labels=category_total.index,
        autopct="%1.1f%%"
    )

    plt.title("Expense Distribution")

    plt.savefig(
        "outputs/pie_chart.png"
    )

    plt.show()

if __name__ == "__main__":

    plot_category()
    plot_monthly()
    plot_pie()