import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("api_key")

st.title("Weather App")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):

    if city:


        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()


        if response.status_code == 200:

            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]
            wind = data["wind"]["speed"]

            st.success(f"Weather in {city}")

            st.write(f"Temperature: {temp} °C")
            st.write(f"Condition: {weather.title()}")
            st.write(f"Humidity: {humidity}%")
            st.write(f"Wind Speed: {wind} m/s")

        else:
            st.error("City not found!")

    else:
        st.warning("Please enter a city name.")