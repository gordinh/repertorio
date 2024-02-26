import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import pandas_datareader as data 
import yfinance as yf
from keras.models import load_model
import streamlit as st
from sklearn.preprocessing import MinMaxScaler


startDate = '2010-01-01'
endDate = '2023-10-31'

st.title('Stock Trend Prediction') 
user_input = st.text_input('Enter Stock Ticker', 'AAPL') #Add a validation for the ticker

df = yf.download(user_input, startDate, endDate) # make dynamic with any user input

# Describing Data
st.subheader('Data from 2010 - 2023')
st.write(df.describe())


# Visualizations
st.subheader('Closing price vs Time chart')
fig = plt.figure(figsize=(12, 6))
plt.plot(df.Close, 'b')
st.pyplot(fig)

# Moving Avg
st.subheader('Closing price vs Time chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize=(12, 6))
plt.plot(ma100, 'r')
plt.plot(df.Close, 'b')
st.pyplot(fig)

# Moving Avg
st.subheader('Closing price vs Time chart with 100MA and 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(12, 6))
plt.plot(ma100, 'r')
plt.plot(ma200, 'g')
plt.plot(df.Close, 'b')
st.pyplot(fig)

# Splitting Data into Training and Testing

data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])


# Scaling
scaler = MinMaxScaler(feature_range=(0, 1))

data_training_array = scaler.fit_transform(data_training)

# Load model
model = load_model('./keras_model.h5')

# Testing
past_100_days = data_training.tail(100)
final_df = pd.concat([past_100_days, data_testing], ignore_index=True)

input_data = scaler.fit_transform(final_df)
x_test = [input_data[i-100:i] for i in range(100, input_data.shape[0])]
y_test = [input_data[i, 0] for i in range(100, input_data.shape[0])]

x_test, y_test = np.array(x_test), np.array(y_test)

# Prediction
y_predicted = model.predict(x_test)

scale_factor = 1/scaler.scale_
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor

# Final Visualization
st.subheader('Predictions vs Original')
fig2 = plt.figure(figsize=(12, 6))
plt.plot(y_test, 'b', label = 'Original Price')
plt.plot(y_predicted, 'r', label = 'Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)