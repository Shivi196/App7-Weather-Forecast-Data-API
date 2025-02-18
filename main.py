import streamlit as st
import plotly.express as px
from backend import get_data

# Add title,text_input,slider,selectbox & subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days",min_value=1,max_value=5,help="Select the number of forecasted days")
option = st.selectbox("Select data to view",options=("Temperature","Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place: #This means if place is not null and user entered value there then only run below code otherwise not

    try: #Why use try except :  in order to replace the error when place doesn't exist with the keyerror instead showing the original error code to user
        # Get the temperature/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature_data = [dict["main"]["temp"] / 10 for dict in filtered_data]  # check for list comprehension topic for this to understand
            date = [dict["dt_txt"] for dict in filtered_data]

            # Create a temperature plot
            figure = px.line(x=date, y=temperature_data, labels={"x":"Dates","y":"Temperatures(C)"})
            st.plotly_chart(figure)

        if option == "Sky":

            images = {"Clouds": "cloud_images/cloud.png",
                      "Clear": "cloud_images/clear.png",
                      "Rain":"cloud_images/rain.png",
                      "Snow": "cloud_images/snow.png"}
            sky_conditions_data = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions_data]
            st.image(image_paths, width=115)
    except KeyError:
        st.write(f"Sorry {place} doesn't exist..Try entering different place ")