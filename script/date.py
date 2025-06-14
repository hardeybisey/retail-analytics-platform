import numpy as np
import pandas as pd

# Define date range
start_date = "2020-01-01"
end_date = "2030-12-31"
dates = pd.date_range(start=start_date, end=end_date, freq="D")

# Create DataFrame
df = pd.DataFrame({"full_date": dates})

# Basic columns
df["date_key"] = df["full_date"].dt.strftime("%Y%m%d").astype(int)
df["day_of_week"] = df["full_date"].dt.weekday + 1  # Monday=1
df["day_num_in_month"] = df["full_date"].dt.day
df["day_num_overall"] = (df["full_date"] - pd.to_datetime(start_date)).dt.days + 1
df["day_name"] = df["full_date"].dt.day_name()
df["day_abbrev"] = df["full_date"].dt.strftime("%a")
df["weekday_flag"] = df["day_of_week"].apply(lambda x: "Y" if x <= 5 else "N")

# Week-related columns
df["week_num_in_year"] = df["full_date"].dt.isocalendar().week
df["week_num_overall"] = (
    (df["full_date"] - pd.to_datetime(start_date)).dt.days // 7
) + 1
df["week_begin_date"] = df["full_date"] - pd.to_timedelta(
    df["full_date"].dt.weekday, unit="D"
)
df["week_begin_date_key"] = df["week_begin_date"].dt.strftime("%Y%m%d").astype(int)

# Month-related columns
df["month"] = df["full_date"].dt.month
df["month_num_overall"] = ((df["full_date"].dt.year - 2020) * 12) + df["month"]
df["month_name"] = df["full_date"].dt.strftime("%B")
df["month_abbrev"] = df["full_date"].dt.strftime("%b")

# Quarter and year
df["quarter"] = df["full_date"].dt.quarter
df["year"] = df["full_date"].dt.year
df["yearmo"] = df["full_date"].dt.strftime("%Y%m")

# Fiscal logic (assuming fiscal year starts in April)
df["fiscal_month"] = (df["month"] - 4) % 12 + 1
df["fiscal_quarter"] = ((df["fiscal_month"] - 1) // 3) + 1
df["fiscal_year"] = np.where(df["month"] >= 4, df["year"], df["year"] - 1)

# Flags and lag features
df["last_day_in_month_flag"] = (
    df["full_date"] == (df["full_date"] + pd.offsets.MonthEnd(0))
).apply(lambda x: "Y" if x else "N")
df["same_day_year_ago"] = df["full_date"] - pd.DateOffset(years=1)

# Reorder and finalise
cols = [
    "date_key",
    "full_date",
    "day_of_week",
    "day_num_in_month",
    "day_num_overall",
    "day_name",
    "day_abbrev",
    "weekday_flag",
    "week_num_in_year",
    "week_num_overall",
    "week_begin_date",
    "week_begin_date_key",
    "month",
    "month_num_overall",
    "month_name",
    "month_abbrev",
    "quarter",
    "year",
    "yearmo",
    "fiscal_month",
    "fiscal_quarter",
    "fiscal_year",
    "last_day_in_month_flag",
    "same_day_year_ago",
]

date_dim = df[cols]

date_dim.to_csv("date_dimension_2020_2030.csv", index=False)
