import pandas as pd

from magpie.utils import clean_and_convert_json, get_proficiency_by_skill


def main():

    # question 1
    print(
        """
        ------------------------------------------------------------
        Output a time series CSV
        1. Consumes raw data (data.json)
        2. Validates / cleanses raw data
        3. Outputs to a time series in ascending order in a CSV (time-series.json)
        ------------------------------------------------------------
        """
    )

    print(clean_and_convert_json("data/data.json", "data/time-series.json"))

    # question 2
    print(
        """
        ------------------------------------------------------------
        Output a proficiency by skill CSV
        1. Consumes raw data (data.json)
        2. Validates / cleanses raw data
        3. Consume skills (skills.json) and proficiency (proficiency.json)
        4. For each skill, calculate the number of records.
        5. For each skill, calculate the average proficiency.
        6. Output to a CSV a report of skill, number of records, average proficiency.
        ------------------------------------------------------------
          """
    )
    skill_report = get_proficiency_by_skill(
        "data/time-series.json", "data/skill_report.csv"
    )

    # question 3
    print(
        """
        ------------------------------------------------------------
        Visualize results
        Using the output from part 2 (Create a proficiency by skill report) develop a visualization with 3
        dimensions - skill, size (number of records), and proficiency (average proficiency). Choose any
        visualization technology of your choice. You can add a graph in a spreadsheet, develop a web page, or
        use a cloud visualization tool.
        Create a README file so we know how to install and run your app, and please include any additional
        information we should know about your app, or links to any external resources, like visualization
        platforms. Push your code to a public repo and email dshoaf@magpie.org a link to your branch.
        Time limit: 90 minutes.
        ------------------------------------------------------------
        """
    )
    visualize_results(skill_report)


def visualize_results(skill_report: pd.DataFrame):
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    st.set_page_config(page_title="Category A & K Analysis", layout="wide")
    st.title("Category A & K Analysis Dashboard")

    df = pd.DataFrame(skill_report)

    st.sidebar.header("Visualization Settings")
    chart_type = st.sidebar.selectbox(
        "Select Chart Type", ["Bar Chart", "Dual Axis Chart", "Side by Side"]
    )

    st.subheader("Data")
    st.dataframe(df, use_container_width=True)

    st.subheader("Visualization")

    if chart_type == "Bar Chart":
        # Create two separate bar charts
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        # Count chart
        sns.barplot(x="skill", y="count", data=df, ax=ax1, palette="Blues")
        ax1.set_title("Count by Skill")
        ax1.set_ylabel("Count")

        # Average chart
        sns.barplot(x="skill", y="avg_proficiency", data=df, ax=ax2, palette="Greens")
        ax2.set_title("Average by Skill")
        ax2.set_ylabel("Average")

        st.pyplot(fig)

    elif chart_type == "Dual Axis Chart":
        fig, ax1 = plt.subplots(figsize=(10, 6))

        # Plot count bars
        sns.barplot(
            x="skill",
            y="count",
            data=df,
            ax=ax1,
            alpha=0.7,
            color="blue",
            label="Count",
        )
        ax1.set_ylabel("count", color="blue")
        ax1.tick_params(axis="y", labelcolor="blue")

        # Create second y-axis
        ax2 = ax1.twinx()

        # Plot average bars (as line with markers)
        ax2.plot(
            ax1.get_xticks(),
            df["avg_proficiency"],
            marker="o",
            color="green",
            linewidth=2,
            markersize=10,
            label="Average",
        )
        ax2.set_ylabel("Average", color="green")
        ax2.tick_params(axis="y", labelcolor="green")

        # Add legend
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

        plt.title("Count and Average Proficiency by Skill")
        plt.tight_layout()
        st.pyplot(fig)

    elif chart_type == "Side by Side":
        # Melt the DataFrame for easier plotting
        df_melted = pd.melt(
            df,
            id_vars=["skill"],
            value_vars=["count", "avg_proficiency"],
            var_name="Metric",
            value_name="Value",
        )

        # Create a grouped bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x="skill", y="Value", hue="Metric", data=df_melted, ax=ax)

        plt.title("Count and Average by Category")
        plt.ylabel("Value")
        plt.legend(title="Metric")

        st.pyplot(fig)

    # Add a section for insights
    st.subheader("Insights")
    col1, col2 = st.columns(2)

    with col1:
        st.info(
            f"""
        **Category A Insights:**
        - Count: {df.loc[df["skill"] == 'A', "count"].values[0]}
        - Average: {df.loc[df["skill"] == 'A', "avg_proficiency"].values[0]}
        - {df.loc[df["skill"] == 'A', "count"].values[0] / df["count"].sum():.1%} of total count
        """
        )

    with col2:
        st.info(
            f"""
        **Category K Insights:**
        - Count: {df.loc[df["skill"] == 'K', "count"].values[0]}
        - Average: {df.loc[df["skill"] == 'K', "avg_proficiency"].values[0]}
        - {df.loc[df["skill"] == 'K', "count"].values[0] / df["count"].sum():.1%} of total count
        """
        )

    # Add file uploader for users to upload their own data
    st.subheader("Upload Your Own Data")
    st.write("Upload a CSV file with columns: `skill`, `count`, `avg_proficiency`")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        user_df = pd.read_csv(uploaded_file)
        st.write("Your uploaded data:")
        st.dataframe(user_df)

        # Add code to visualize the uploaded data here
        st.write("Visualization of your data will appear here")
        # Similar visualization code as above but using user_df instead of df


if __name__ == "__main__":
    main()
