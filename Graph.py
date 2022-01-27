import plotly.express as ps
import csv

with open("Student Marks vs Days Present.csv") as f:

    df = csv.DictReader(f)
    fig = ps.scatter(df, x="Present", y="Marks")
    fig.show()
