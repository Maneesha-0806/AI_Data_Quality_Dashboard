def duplicate_summary(df):

    duplicates = df.duplicated().sum()

    duplicate_percent = (
        duplicates / len(df)
    ) * 100

    return duplicates, duplicate_percent