import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load workout data into variable
data = pd.read_csv("data/workouts.csv")
#convert start_time and end_time columns from str to datetime datatypes
data["start_time"] = pd.to_datetime(data["start_time"])
data["end_time"] = pd.to_datetime(data["end_time"])

#create volume column 
data["set_volume"] = data["weight_lbs"] * data["reps"]
#subset data to only useful data 
revisedData = ["title","start_time","end_time","exercise_title","weight_lbs","reps","set_volume"]
print(data[revisedData].sort_values("start_time", ascending=True))


#set the start_time as the index
revisedData2 = data[revisedData]
revisedData2.groupby(["start_time","exercise_title"])[["weight_lbs","reps","set_volume"]]
