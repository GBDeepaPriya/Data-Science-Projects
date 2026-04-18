# src/report_generator.py

def generate_report(
    summary,
    file_path="outputs/reports/climate_report.txt"
):
    """
    Generate climate report file.
    """

    with open(
        file_path,
        "w"
    ) as f:

        f.write(
            "CLIMATE TREND ANALYSIS REPORT\n"
        )

        f.write(
            "=============================\n\n"
        )

        for key, value in summary.items():

            line = f"{key}: {value}\n"

            f.write(line)

    print(
        "Report Generated Successfully!"
    )