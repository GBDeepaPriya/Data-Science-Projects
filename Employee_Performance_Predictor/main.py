"""
main.py
"""

from src.data_generation import (
    generate_employee_data
)

from src.data_preprocessing import (
    clean_data,
    save_cleaned_data
)

from src.eda import perform_eda

from src.feature_engineering import (
    encode_features,
    scale_features
)

from src.model_training import (
    split_data,
    train_model,
    save_model
)

from src.evaluation import (
    evaluate_model
)


def run_pipeline():

    print("Starting Pipeline...")

    # Generate data

    df = generate_employee_data()

    df.to_csv(
        "data/raw/employee_data.csv",
        index=False
    )

    # Clean data

    df = clean_data(df)

    save_cleaned_data(df)

    # EDA

    perform_eda(df)

    # Feature engineering

    df = encode_features(df)
    df = scale_features(df)

    # Train model

    X_train, X_test, y_train, y_test = split_data(df)

    model = train_model(
        X_train,
        y_train
    )

    save_model(model)

    # Evaluate model

    evaluate_model(
        model,
        X_test,
        y_test
    )

    print("Pipeline Completed!")


if __name__ == "__main__":

    run_pipeline()