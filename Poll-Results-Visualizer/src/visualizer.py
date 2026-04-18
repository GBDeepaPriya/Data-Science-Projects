# src/visualizer.py

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


def bar_chart(counts):

    plt.figure(figsize=(8, 5))

    counts.plot(
        kind="bar"
    )

    plt.title("Product Preference Count")

    plt.xlabel("Product")

    plt.ylabel("Votes")

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/bar_chart.png"
    )

    plt.close()


def pie_chart(counts):

    plt.figure(figsize=(6, 6))

    counts.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.ylabel("")

    plt.title("Product Distribution")

    plt.savefig(
        "outputs/charts/pie_chart.png"
    )

    plt.close()


def region_chart(region_df):

    region_df.plot(
        kind="bar",
        stacked=True,
        figsize=(10, 6)
    )

    plt.title(
        "Region-wise Product Preference"
    )

    plt.xlabel("Region")

    plt.ylabel("Votes")

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/region_chart.png"
    )

    plt.close()


def wordcloud_chart(df):

    text = " ".join(

        df["Feedback"]
        .astype(str)
        .tolist()

    )

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(text)

    plt.figure(figsize=(10, 5))

    plt.imshow(wordcloud)

    plt.axis("off")

    plt.title("Feedback Word Cloud")

    plt.savefig(
        "outputs/charts/wordcloud.png"
    )

    plt.close()