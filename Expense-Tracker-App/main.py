from src.data_generator import generate_expense_data
from src.data_cleaning import clean_data
from src.analysis import (
    category_analysis,
    monthly_trends,
    spending_patterns
)
from src.visualization import (
    plot_category,
    plot_monthly,
    plot_pie
)
from src.insights import generate_insights

def run_pipeline():

    print("Generating Data...")
    generate_expense_data()

    print("Cleaning Data...")
    clean_data()

    print("Running Analysis...")
    category_analysis()
    monthly_trends()
    spending_patterns()

    print("Creating Visualizations...")
    plot_category()
    plot_monthly()
    plot_pie()

    print("Generating Insights...")
    generate_insights()

if __name__ == "__main__":
    run_pipeline()