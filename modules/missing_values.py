def missing_value_summary(df):    
    missing = df.isnull().sum()
    missing_percent = (
        df.isnull().sum() / len(df)
    ) * 100
    summary = {
        "Missing Count": missing,
        "Missing Percentage": missing_percent
    }
    return summary