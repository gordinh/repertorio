import requests
import streamlit as st


# Prepare API key and API url
api_key = "aVfct7J39j5ehMlDXbgBZkBXcNBOp3OOsCNW6nhQ"
api_url = "https://api.nasa.gov/planetary/apod?" \
          f"api_key={api_key}"

# Get the request data as a dictionary
response_metadata = requests.get(url=api_url)
data = response_metadata.json()

# Extract the image title, url and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download image
image_filepath = "img.png"
response_image = requests.get(image_url)
with open(image_filepath, 'wb') as file:
  file.write(response_image.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)