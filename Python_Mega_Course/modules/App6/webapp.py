import streamlit as st
import plotly.express as px
from datetime import datetime
from backend import get_data

def transform_date(d):
  date_transformed = datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
  return date_transformed.strftime("%d/%m %H:%M")

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days.")
option = st.selectbox("Select data to view",
                       ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
  try:
    filtered_data = get_data(place=place, forecast_days=days)
  
    if option == 'Temperature':
      temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
      dates = [dict["dt_txt"] for dict in filtered_data]
      figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (ºC)"})
      st.plotly_chart(figure_or_data=figure)

    if option == 'Sky':
      images = {
        "Clear": "images/clear.png",
        "Clouds": "images/cloud.png",
        "Rain": "images/rain.png",
        "Snow": "images/snow.png"
      }
      sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
      description = [transform_date(dict["dt_txt"]) + ' ' + dict["weather"][0]["description"].title() for dict in filtered_data]
      image_paths = [images[condition] for condition in sky_conditions]
      st.image(image_paths, caption=description, width=200)
  except KeyError:
    st.write("This city doesn't exists.")