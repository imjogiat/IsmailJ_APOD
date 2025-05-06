import os
import streamlit as st
import requests
import datetime

# """Create a webpage that displays a daily astronomy picture
# and some text description"""

todays_date = str(datetime.datetime.now())
todays_date = (todays_date.split(" "))[0]

st.title("Daily Astronomy Picture")
st.subheader(todays_date)

#Use NASA OpenAPI for picture and info- api.nasa.gov
#Use APOD- Astronomy Picture of the Day

#Get URL for API and API Key
API_URL = "https://api.nasa.gov/planetary/apod?api_key=Cft5PQZwn41ltKlASwEFtUtjeoCLKyzyONQ4HYez"
API_key = "Cft5PQZwn41ltKlASwEFtUtjeoCLKyzyONQ4HYez"

#download the picture of the day
response = requests.get(API_URL)
astro_content = response.json()
astro_desc = astro_content["explanation"]

print(astro_content["url"])

st.video(astro_content["url"])

st.write(astro_desc)



# with open ("astro_img.jpg", "wb") as astro_pic:
#     print(type(astro_content["hdurl"]))
#     print(astro_content["hdurl"])
    # astro_pic.write(astro_content["url"])
    