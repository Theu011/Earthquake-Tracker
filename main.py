import pandas as pd
import plotly.express as px


token = open("D:\My Python Stuffs\earthquakeTracker/mapbox_token.txt").read()  # you will need your own token
earthquakes_7days = pd.read_csv("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv")
marker_size = earthquakes_7days['mag'].abs() / 50


fig = px.scatter_mapbox(earthquakes_7days,
                        title="Earthquakes around the World in the past week",
                        lat="latitude",
                        lon="longitude",
                        hover_name="magType",
                        hover_data=["place", "mag", "time"],
                        color_discrete_sequence=["fuchsia"],
                        zoom=1.5,
                        height=720,
                        size=marker_size
                        )
fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, title_x=0.5, title_y=0.95, title_font_color="white")
fig.show()
