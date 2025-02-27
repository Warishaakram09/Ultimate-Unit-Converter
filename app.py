import streamlit as st
import matplotlib.pyplot as plt

def convert_units(value, from_unit, to_unit):
    conversions = {
        "Kilometers to Miles": value * 0.621371,
        "Miles to Kilometers": value / 0.621371,
        "Meters to Feet": value * 3.28084,
        "Feet to Meters": value / 3.28084,
        "Kilograms to Pounds": value * 2.20462,
        "Pounds to Kilograms": value / 2.20462,
        "Grams to Ounces": value * 0.035274,
        "Ounces to Grams": value / 0.035274,
        "Celsius to Fahrenheit": (value * 9/5) + 32,
        "Fahrenheit to Celsius": (value - 32) * 5/9,
        "Celsius to Kelvin": value + 273.15,
        "Kelvin to Celsius": value - 273.15
    }
    return conversions.get(f"{from_unit} to {to_unit}", "Invalid Conversion")

st.set_page_config(page_title="💜 Ultimate Unit Converter 💜", page_icon="🔄", layout="wide")

# Custom CSS for full background change
st.markdown(f"""
    <style>
        body {{ background-color: #6a11cb; color: white; }}
        .main {{ background-color: #6a11cb; padding: 30px; border-radius: 15px; }}
        .sidebar .sidebar-content {{ background: #6a11cb; color: white; padding: 20px; font-size: 18px; }}
        .stButton>button {{ background: #6a11cb; color: white; border-radius: 8px; padding: 10px; font-size: 16px; }}
        .stButton>button:hover {{ background: #521d9b; }}
        h1 {{ color: white; text-align: center; font-size: 40px; font-weight: bold; text-transform: uppercase; }}
        .footer-text {{ text-align: center; color: #d1a3ff; font-size: 20px; font-weight: bold; }}
    </style>
""", unsafe_allow_html=True)

# Sidebar with engaging elements
st.sidebar.markdown("""
    <h1>🚀 Quick Convert</h1>
    <p>🔹 Convert units instantly & easily!</p>
    <p>🔹 Keep track of recent conversions</p>
    <p>🔹 Reset history anytime</p>
    <p>📢 Give your feedback to improve the app!</p>
    <p>📊 View detailed conversion statistics</p>
""", unsafe_allow_html=True)

# Conversion Statistics Chart
def plot_conversion_chart():
    labels = ["Length", "Weight", "Temperature", "Volume", "Speed", "Area", "Time"]
    values = [10, 8, 6, 7, 5, 4, 3]  # Example data
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color='#9b59b6')
    plt.xlabel("Conversion Types")
    plt.ylabel("Usage Count")
    plt.title("Most Used Conversion Types")
    st.sidebar.pyplot(plt)

if st.sidebar.button("📊 View Stats"):
    st.sidebar.success("Here are your conversion statistics:")
    plot_conversion_chart()

# Feedback Section
feedback = st.sidebar.text_area("💬 Share Your Feedback")
if st.sidebar.button("Submit Feedback ✅"):
    st.sidebar.success("Thank you for your feedback! 💜")

# Main Content
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("💜 Ultimate Unit Converter 💜")

conversion_type = st.selectbox("Select Conversion Type:", ["Length", "Weight", "Temperature", "Volume", "Speed", "Area", "Time"])
unit_options = {
    "Length": ["Kilometers", "Miles", "Meters", "Feet", "Centimeters", "Inches"],
    "Weight": ["Kilograms", "Pounds", "Grams", "Ounces", "Tons"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Volume": ["Liters", "Milliliters", "Gallons", "Cups", "Cubic Meters"],
    "Speed": ["Kilometers per hour", "Miles per hour", "Meters per second"],
    "Area": ["Square Meters", "Square Kilometers", "Hectares", "Acres"],
    "Time": ["Seconds", "Minutes", "Hours", "Days", "Weeks"]
}

from_unit = st.selectbox("From:", unit_options[conversion_type])
to_unit = st.selectbox("To:", unit_options[conversion_type])
value = st.number_input("Enter Value:", min_value=0.0, step=0.1)

if st.button("Convert 🚀"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"🎉 {value} {from_unit} = {result} {to_unit} 🎉")

st.markdown(f"""
    <hr>
    <p class='footer-text'>🚀 Created with Passion by <span style='color:#d1a3ff;'>Warisha Akram</span> 🚀</p>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
