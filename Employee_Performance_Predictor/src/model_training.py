import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def split_data(df):

    X = df.drop("Performance_Level", axis=1)

    y = df["Performance_Level"]

    # Save feature order
    joblib.dump(
        list(X.columns),
        "models/feature_columns.pkl"
    )

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


def train_model(X_train, y_train):

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model


def save_model(model):

    joblib.dump(
        model,
        "models/performance_model.pkl"
    )

    print("Model saved!")