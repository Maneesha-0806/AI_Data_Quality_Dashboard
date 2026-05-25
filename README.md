# AI-Powered Data Quality Monitoring Dashboard

An intelligent and automated data quality analysis tool built using Python, Streamlit, and AI-powered insights.

This dashboard helps users upload CSV or Excel datasets, automatically detect data quality issues, visualize problems, generate AI-driven insights, and download cleaned datasets and reports.

---

# Features

## File Upload Support

- Upload CSV files
- Upload Excel files (.xlsx)
- Handles large datasets

---

## Automated Data Quality Checks

### Missing Value Detection

- Detect missing/null values
- Column-wise missing value analysis
- Missing value visualizations

### Duplicate Detection

- Identify duplicate rows
- Calculate duplicate percentage

### Outlier Detection

- Detect outliers using IQR method
- Numeric column analysis

### Inconsistency Detection

- Detect inconsistent text formatting
- Identify data irregularities

---

## Data Quality Score

- Automatic data quality scoring system
- Interactive gauge visualization
- Quality score out of 100

---

## AI-Powered Insights

Generate intelligent dataset insights using Groq LLMs:

- Executive summaries
- Business insights
- Data quality observations
- Trend analysis
- Recommendations

Fallback local insights are generated when AI API is unavailable.

---

## Interactive Visualizations

- Missing value bar charts
- Correlation heatmaps
- Quality score gauge chart
- Interactive Plotly charts

---

# Tech Stack

| Technology | Purpose               |
| ---------- | --------------------- |
| Python     | Core programming      |
| Streamlit  | Interactive dashboard |
| Pandas     | Data processing       |
| Plotly     | Data visualizations   |
| Groq API   | AI-generated insights |
| OpenPyXL   | Excel file handling   |

---

# Future Enhancements

- PDF report generation
- Automatic data cleaning actions
- Chat with dataset feature
- Data drift detection
- Multi-file batch processing
- Power BI integration
- User authentication
- Cloud deployment

---
