def detect_inconsistencies(df):

    inconsistencies = {}

    for col in df.select_dtypes(include='object'):

        unique_values = df[col].dropna().unique()

        lower_values = [
            str(v).lower()
            for v in unique_values
        ]

        if len(lower_values) != len(set(lower_values)):
            inconsistencies[col] = "Case inconsistency detected"

    return inconsistencies