def calculate_quality_score(
    df,
    missing,
    duplicates,
    outliers,
    inconsistencies
):

    total_cells = df.shape[0] * df.shape[1]

    missing_penalty = (
        missing.sum() / total_cells
    ) * 40

    duplicate_penalty = (
        duplicates / len(df)
    ) * 30

    outlier_penalty = (
        sum(outliers.values()) / total_cells
    ) * 20

    inconsistency_penalty = (
        len(inconsistencies) / df.shape[1]
    ) * 10

    score = 100 - (
        missing_penalty +
        duplicate_penalty +
        outlier_penalty +
        inconsistency_penalty
    )

    return round(max(score, 0), 2)