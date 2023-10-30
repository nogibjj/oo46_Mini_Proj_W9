import pandas as pd


def read_dataset():
    df = pd.read_csv("dsets/car_sales_data.csv")
    return df


df = read_dataset()


def top_salesperson():
    top_salespersons = df["Salesperson"].value_counts().head(5)
    return top_salespersons


def most_sold_make():
    msc = df["Car Make"].value_counts()
    return msc


def most_sold_model():
    msm = df["Car Model"].value_counts()
    return msm


def desc_stats():
    return df.describe()
