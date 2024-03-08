from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("./data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME"]]
@app.route("/")
def home():
  return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
  filename = f"./data_small/TG_STAID{str(station).zfill(6)}.txt"
  df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
  date_formatted = date[0:3] + '-' + date[4:5] + "-" + date[6:]
  temperature = df.loc[df['    DATE'] == date_formatted]['   TG'].squeeze() / 100
  temperature = 23
  return {
    "station": station,
    "date": date,
    "temperature": temperature
  }

@app.route("/api/v1/<station>")
def all_data(station):
  filename = f"./data_small/TG_STAID{str(station).zfill(6)}.txt"
  df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
  result = df.to_dict(orient='records')
  return result


@app.route("/api/v1/yearly/<station>/<year>")
def all_yearly_data(station, year):
  filename = f"./data_small/TG_STAID{str(station).zfill(6)}.txt"
  df = pd.read_csv(filename, skiprows=20)
  df["    DATE"] = df["    DATE"].astype(str)
  result = df[df["    DATE"].str.startswith((str(year)))].to_dict(orient='records')
  return result





if __name__ == "__main__":
  app.run(debug=True, port=5000)