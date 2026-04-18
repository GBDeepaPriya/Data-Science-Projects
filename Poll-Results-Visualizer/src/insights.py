# src/insights.py

def generate_insights(summary_df):

    top_product = summary_df.index[0]

    top_percentage = summary_df.iloc[0][
        "Percentage"
    ]

    insight_text = f"""
    Poll Results Summary

    Most Preferred Product:
    {top_product}

    Market Share:
    {top_percentage:.2f}%

    """

    output_path = "outputs/reports/summary_report.txt"

    with open(output_path, "w") as f:

        f.write(insight_text)

    print("Insights generated")