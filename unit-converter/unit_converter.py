import streamlit as st

def convert_units(value, unit_from, unit_to):
    # Define conversion factors
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
        # Add more conversions if needed
    }

    # Create a key for the conversion
    key = f"{unit_from}_{unit_to}"
    
    # Check if the conversion is supported
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return None  # Return None for unsupported conversions

# Streamlit UI
st.title("Unit Converter")

value = st.number_input("Enter the value to convert:", min_value=1.0, step=1.0)

unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    if result is not None:
        st.write(f"Converted value: {result:.4f} {unit_to}")
    else:
        st.write("Conversion not supported for the selected units.")