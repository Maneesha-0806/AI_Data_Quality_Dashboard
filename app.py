import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from modules.missing_values import missing_value_summary
from modules.duplicates import duplicate_summary
from modules.outliers import detect_outliers
from modules.scoring import calculate_quality_score
from modules.ai_insights import generate_ai_insights
from modules.inconsistency import detect_inconsistencies


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Data Quality Dashboard",
    layout="wide"
)

st.title(
    "AI-Powered Data Quality Monitoring Dashboard"
)


# -----------------------------------
# FILE UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)


# -----------------------------------
# MAIN APPLICATION
# -----------------------------------

if uploaded_file is not None:

    try:

        # -----------------------------------
        # READ FILE
        # -----------------------------------

        if uploaded_file.name.endswith(".csv"):

            try:
                df = pd.read_csv(
                    uploaded_file,
                    encoding="utf-8"
                )

            except UnicodeDecodeError:

                try:
                    df = pd.read_csv(
                        uploaded_file,
                        encoding="latin1"
                    )

                except:

                    df = pd.read_csv(
                        uploaded_file,
                        encoding="cp1252"
                    )

        else:

            df = pd.read_excel(uploaded_file)

        st.success(
            "File uploaded successfully!"
        )

        # -----------------------------------
        # DATA PREVIEW
        # -----------------------------------

        st.subheader("Dataset Preview")

        st.dataframe(df.head())

        # -----------------------------------
        # DATASET OVERVIEW
        # -----------------------------------

        st.subheader("Dataset Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Rows",
            df.shape[0]
        )

        col2.metric(
            "Columns",
            df.shape[1]
        )

        col3.metric(
            "Missing Values",
            df.isnull().sum().sum()
        )

        # -----------------------------------
        # MISSING VALUES
        # -----------------------------------

        summary = missing_value_summary(df)

        st.subheader(
            "Missing Value Analysis"
        )

        st.write(summary)

        # -----------------------------------
        # DUPLICATE ANALYSIS
        # -----------------------------------

        duplicates, duplicate_percent = (
            duplicate_summary(df)
        )

        st.subheader(
            "Duplicate Analysis"
        )

        st.write(
            f"Duplicate Rows: {duplicates}"
        )

        st.write(
            f"Duplicate Percentage: {duplicate_percent:.2f}%"
        )

        # -----------------------------------
        # OUTLIER DETECTION
        # -----------------------------------

        outliers = detect_outliers(df)

        st.subheader(
            "Outlier Detection"
        )

        st.write(outliers)

        # -----------------------------------
        # INCONSISTENCY DETECTION
        # -----------------------------------

        inconsistencies = (
            detect_inconsistencies(df)
        )

        st.subheader(
            "Inconsistency Detection"
        )

        st.write(inconsistencies)

        # -----------------------------------
        # DATA QUALITY SCORE
        # -----------------------------------

        quality_score = calculate_quality_score(
            df,
            df.isnull().sum(),
            duplicates,
            outliers,
            inconsistencies
        )

        st.subheader(
            "Data Quality Score"
        )

        st.metric(
            "Quality Score",
            f"{quality_score}/100"
        )

        # -----------------------------------
        # GAUGE CHART
        # -----------------------------------

        gauge_fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=quality_score,

            title={
                'text': "Data Quality Score"
            },

            gauge={

                'axis': {
                    'range': [0, 100]
                },

                'bar': {
                    'color': "darkblue"
                },

                'steps': [

                    {
                        'range': [0, 50],
                        'color': "red"
                    },

                    {
                        'range': [50, 75],
                        'color': "orange"
                    },

                    {
                        'range': [75, 100],
                        'color': "green"
                    }
                ]
            }
        ))

        st.plotly_chart(
            gauge_fig,
            use_container_width=True
        )

        # -----------------------------------
        # MISSING VALUE VISUALIZATION
        # -----------------------------------

        missing_df = pd.DataFrame({

            "Column": df.columns,

            "Missing": df.isnull().sum()

        })

        missing_fig = px.bar(

            missing_df,

            x="Column",

            y="Missing",

            title="Missing Values by Column"

        )

        st.plotly_chart(
            missing_fig,
            use_container_width=True
        )

        # -----------------------------------
        # CORRELATION HEATMAP
        # -----------------------------------

        numeric_df = df.select_dtypes(
            include='number'
        )

        if not numeric_df.empty:

            corr = numeric_df.corr()

            heatmap_fig = px.imshow(

                corr,

                text_auto=True,

                title="Correlation Heatmap"

            )

            st.plotly_chart(
                heatmap_fig,
                use_container_width=True
            )

        # -----------------------------------
        # AI REPORT
        # -----------------------------------

        st.subheader(
            "AI Insights"
        )

        if st.button(
            "Generate AI Report"
        ):

            with st.spinner(
                "Generating AI Report..."
            ):

                insights = generate_ai_insights(df)

                st.write(insights)

        # -----------------------------------
        # DOWNLOAD CLEANED DATA
        # -----------------------------------

        st.subheader(
            "Download Cleaned Dataset"
        )

        csv = df.to_csv(index=False)

        st.download_button(

            label="Download CSV",

            data=csv,

            file_name="cleaned_data.csv",

            mime="text/csv"
        )

    except Exception as e:

        st.error(
            f"Error processing file: {e}"
        )

else:

    st.info(
        "Please upload a CSV or Excel file to begin analysis."
    )