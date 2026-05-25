def detect_outliers(df):

    numeric_cols = df.select_dtypes(include=['number']).columns

    outlier_summary = {}

    for col in numeric_cols:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers = df[
            (df[col] < lower) |
            (df[col] > upper)
        ]

        outlier_summary[col] = len(outliers)

    return outlier_summary