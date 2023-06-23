import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import folium
from streamlit_folium import folium_static
import pandas as pd

def main():
    st.set_page_config(
        page_title="Dengue Vision: Your AI Powered Outbreak Oracle",
        page_icon="🦟",
        layout="centered",
        initial_sidebar_state="collapsed",
    )
    st.title("Dengue Vision: Your AI Powered Outbreak Oracle")
    page = st.sidebar.selectbox("Page", ["Form", "Result"])

    if page == "Form":
        show_form()
    elif page == "Result":
        show_result()

def show_form():
    image = Image.open("dengue.png")
    st.image(image, caption="", use_column_width=True)
    st.header("Input the given fields or upload a csv file which has the given input fields as columns:")
    with st.form(key="my_form"):
        input_fields = []
        input_field_names = ["AI", "AI 2ND LAST MONTH", "BI", "BI 2ND LAST MONTH", "CI", "CI 2ND LAST MONTH", "HI", "HI 2ND LAST MONTH", "HUMIDITY MEAN 2ND LAST MONTH", "HUMIDITY MEAN LAST MONTH", "HUMIDITY STD 2ND LAST MONTH", "HUMIDITY STD LAST MONTH",  "LAST MONTH CASES"]
        for i in input_field_names:
            input_field = st.text_input(f"{i}")
            input_fields.append(input_field)

        csv_upload = st.file_uploader("Upload a CSV file")
        
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Perform any necessary processing with the form data
            # You can access the input values using the input_fields list

            # Redirect to the result page after form submission
            st.experimental_set_query_params(page="Result")
            
        if csv_upload is not None:
            # Read the uploaded CSV file
            df = pd.read_csv(csv_upload)
            # Perform processing with the uploaded data
            # You can access the data using the 'df' DataFrame

            # Redirect to the result page after file upload
            st.experimental_set_query_params(page="Result")

def show_result():
    st.header("Dengue Prediction Result:")
    st.write("The result is <insert prediction results here>")

    # Additional styles and designs
    st.markdown(
        """
        <style>
        body {
            background-color: #F2F4F6;
        }
        .stMarkdown p {
            color: #1f618d;
            font-size: 18px;
            line-height: 1.5;
        }
        .form-header {
            background-color: #3498DB;
            color: white;
            padding: 10px;
            border-radius: 5px;
        }
        .result-section {
            background-color: #F9E79F;
            padding: 20px;
            margin-top: 30px;
            border-radius: 5px;
        }
        .result-title {
            color: #E74C3C;
            text-align: center;
            font-size: 24px;
        }
        .result-text {
            color: #ffffff;
            font-size: 16px;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<p>This is some additional styled text.</p>", unsafe_allow_html=True)
    
    m = folium.Map(location=[23.6850, 90.3563], zoom_start=7)

    # Add markers for the cities with numbers on them
    cities = ['Dhaka', 'Chittagong', 'Rajshahi']
    numbers = [10, 5, 8]
    for city, number in zip(cities, numbers):
        marker = folium.Marker(
            location=get_coordinates(city),
            popup=f"{city}: {number}",
            icon=folium.Icon(color='red', icon='info-sign')
        )
        marker.add_to(m)

    # Generate the HTML for the map and display it in Streamlit
    folium_static(m)
    
def get_coordinates(city):
    # You can use a geocoding service or a predefined dictionary to get the coordinates of the cities
    coordinates = {
        'Dhaka': [23.8103, 90.4125],
        'Chittagong': [22.3475, 91.8123],
        'Rajshahi': [24.3740, 88.6042]
    }
    return coordinates.get(city, [0, 0])


if __name__ == "__main__":
    main()
