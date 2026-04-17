import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# load workout data into variable
data = pd.read_csv("data/workouts.csv")
data["start_time"] = pd.to_datetime(data["start_time"])
data["end_time"] = pd.to_datetime(data["end_time"])
print(data.dtypes)

#subset data to only useful data 
revisedData = ["title","start_time","end_time","exercise_title","superset_id","set_index","set_type","weight_lbs","reps"]
print(data[revisedData])
print(data.sort_values("start_time", ascending=True))
