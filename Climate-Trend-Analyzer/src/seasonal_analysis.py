# src/seasonal_analysis.py

from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt


def seasonal_decomposition(
    df,
    column,
    freq=365
):
    """
    Perform seasonal decomposition.
    """

    df = df.set_index("date")

    result = seasonal_decompose(
        df[column],
        model="additive",
        period=freq
    )

    result.plot()

    plt.savefig(
        f"outputs/plots/{column}_seasonal_decomposition.png"
    )

    plt.show()

    return result