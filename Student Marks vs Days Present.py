import numpy as np
import plotly.express as ps
import csv


def getDataSource(data_path):
    marks = []
    present = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            marks.append(float(row["Marks"]))
            present.append(float(row["Present"]))
    return {"x": marks, "y": present}


def setup():
    data_path = "Student Marks vs Days Present.csv"
    data_source = getDataSource(data_path)
    findcoreRelation(data_source)


def findcoreRelation(data_source):
    coreRelation = np.corrcoef(data_source["x"], data_source["y"])
    print("coreRelation between Marks and days present sales is:",
          coreRelation[0, 1])


setup()
