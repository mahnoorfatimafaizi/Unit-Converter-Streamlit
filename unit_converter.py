import streamlit as st

# Custom CSS for the app
st.markdown(
    """
    <style>
    /* General app styling */
    .stApp {
        color: rgb(255, 255, 255);  /* White background */
        background-color: rgb(0, 0, 0);                  /* Black text */
        text-align: center;                    /* Center-align text */
        font-family: 'Courier New', monospace; /* Monospace font */
    }

    


    </style>
    """,
    unsafe_allow_html=True
)

# App title and description
st.title("🚀 Unit Converter 🚀")
st.write("Convert units with ease! 🌟")


# Radio button for conversion type
conversion_type = st.radio(
    "Select the conversion type: ",
    ["Kilometers to Miles", "Miles to Kilometers", "Celsius to Fahrenheit", "Fahrenheit to Celsius"]
)

# Input for value to convert
value = st.number_input("Enter the value to convert: ")

# Conversion logic
if conversion_type == "Kilometers to Miles":
    miles = value * 0.621371
    st.write(f"{value} kilometers is equal to {miles} miles.")
elif conversion_type == "Miles to Kilometers":
    kilometers = value / 0.621371
    st.write(f"{value} miles is equal to {kilometers} kilometers.")
elif conversion_type == "Celsius to Fahrenheit":
    fahrenheit = value * 9/5 + 32
    st.write(f"{value} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
elif conversion_type == "Fahrenheit to Celsius":
    celsius = (value - 32) * 5/9
    st.write(f"{value} degrees Fahrenheit is equal to {celsius} degrees Celsius.")


st.write("Thank you for using the app! 🌟")



