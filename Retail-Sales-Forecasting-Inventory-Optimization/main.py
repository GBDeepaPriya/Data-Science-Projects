"""
Updated Main Pipeline
"""

from src.data_generation import generate_synthetic_data
from src.data_preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.visualization import (
    plot_sales_trend,
    plot_category_sales
)

from src.forecasting_model import (
    train_forecasting_model,
    generate_forecast
)

from src.inventory_optimizer import (
    calculate_inventory
)

from src.model_evaluation import (
    plot_actual_vs_predicted
)


def run_pipeline():

    print("STEP 1: Generate Data")
    generate_synthetic_data()

    print("STEP 2: Preprocess Data")
    preprocess_data()

    print("STEP 3: Feature Engineering")
    create_features()

    print("STEP 4: Visualization")
    plot_sales_trend()
    plot_category_sales()

    print("STEP 5: Train Model")
    train_forecasting_model()

    print("STEP 6: Generate Forecast")
    generate_forecast()

    print("STEP 7: Inventory Optimization")
    calculate_inventory()

    print("STEP 8: Model Evaluation")
    plot_actual_vs_predicted()

    print("Pipeline Completed Successfully.")


if __name__ == "__main__":
    run_pipeline()