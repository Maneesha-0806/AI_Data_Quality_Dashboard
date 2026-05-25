import os

from groq import Groq

from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_local_insights(df):

    insights = []

    rows, cols = df.shape

    insights.append(
        f"The dataset contains {rows} rows and {cols} columns."
    )

    missing = df.isnull().sum()

    high_missing = missing[missing > 0]

    if len(high_missing) > 0:

        insights.append(
            "Missing values detected:"
        )

        for col, val in high_missing.items():

            insights.append(
                f"- {col}: {val} missing values"
            )

    duplicates = df.duplicated().sum()

    insights.append(
        f"Duplicate rows: {duplicates}"
    )

    numeric_cols = df.select_dtypes(
        include='number'
    ).columns

    for col in numeric_cols:

        mean = round(df[col].mean(), 2)

        insights.append(
            f"Average {col}: {mean}"
        )

    return "\n".join(insights)


def generate_ai_insights(df):

    local_insights = generate_local_insights(df)

    try:

        summary = f"""
        Dataset Shape: {df.shape}

        Columns:
        {list(df.columns)}

        Missing Values:
        {df.isnull().sum().to_dict()}

        Statistical Summary:
        {df.describe(include='all').to_string()}

        Local Insights:
        {local_insights}
        """

        prompt = f"""
        Analyze this dataset and generate:

        1. Executive Summary
        2. Business Insights
        3. Data Quality Problems
        4. Trends and Patterns
        5. Recommendations

        Dataset:
        {summary}
        """

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3,

            max_tokens=700
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"""
Groq API unavailable.

Showing local insights instead.

Error:
{str(e)}

-----------------------------------

{local_insights}
"""