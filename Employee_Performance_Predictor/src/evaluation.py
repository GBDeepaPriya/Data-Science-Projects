"""
evaluation.py
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


def evaluate_model(
        model,
        X_test,
        y_test
):

    y_pred = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    print("Accuracy:", accuracy)

    report = classification_report(
        y_test,
        y_pred
    )

    print(report)

    # Save metrics

    with open(
        "outputs/metrics.txt",
        "w"
    ) as f:

        f.write(
            f"Accuracy: {accuracy}\n\n"
        )

        f.write(report)

    # Save predictions

    pd.DataFrame({

        "Actual": y_test,
        "Predicted": y_pred

    }).to_csv(
        "outputs/predictions.csv",
        index=False
    )

    # Confusion Matrix

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d"
    )

    plt.title(
        "Confusion Matrix"
    )

    plt.savefig(
        "images/confusion_matrix.png"
    )

    plt.close()

    # Feature Importance

    if hasattr(
        model,
        "feature_importances_"
    ):

        importances = model.feature_importances_

        indices = np.argsort(
            importances
        )[::-1]

        features = X_test.columns

        plt.figure(
            figsize=(12, 8)
        )

        sns.barplot(

            x=importances[indices],
            y=features[indices]

        )

        plt.title(
            "Feature Importance"
        )

        plt.tight_layout()

        plt.savefig(
            "images/feature_importance.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    return accuracy