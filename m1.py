import streamlit as st
from fpdf import FPDF

# Function to calculate the carbon footprint
def calculate_carbon_footprint(electricity_bill, gas_bill, fuel_bill):
    carbon_footprint = (electricity_bill * 12 * 0.00005) + (gas_bill * 12 * 0.0053) + (fuel_bill * 12 * 2.32)
    return carbon_footprint

# Streamlit app interface
st.title('Carbon Footprint Calculator')

# Inputs for bills
electricity_bill = st.number_input('Enter your average monthly electricity bill in euros', min_value=0.0, format="%.2f")
gas_bill = st.number_input('Enter your average monthly natural gas bill in euros', min_value=0.0, format="%.2f")
fuel_bill = st.number_input('Enter your average monthly fuel bill for transportation in euros', min_value=0.0, format="%.2f")

# Calculate the carbon footprint when button is clicked
if st.button('Calculate Carbon Footprint'):
    if electricity_bill and gas_bill and fuel_bill:
        carbon_footprint = calculate_carbon_footprint(electricity_bill, gas_bill, fuel_bill)
        st.write(f"Your estimated carbon footprint is: {carbon_footprint:.2f} kg CO2 per year.")
        
        # Button to download the PDF report
        if st.button('Generate PDF Report'):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(200, 10, 'Carbon Footprint Report', ln=True, align='C')
            pdf.ln(10)

            pdf.set_font('Arial', '', 12)
            pdf.cell(200, 10, f'Monthly Electricity Bill: {electricity_bill} EUR', ln=True)
            pdf.cell(200, 10, f'Monthly Gas Bill: {gas_bill} EUR', ln=True)
            pdf.cell(200, 10, f'Monthly Fuel Bill: {fuel_bill} EUR', ln=True)
            pdf.cell(200, 10, f'Calculated Carbon Footprint: {carbon_footprint:.2f} kg CO2 per year', ln=True)

            # Save PDF to a file
            pdf.output("carbon_footprint_report.pdf")

            # Let the user download the PDF
            st.download_button("Download PDF", "carbon_footprint_report.pdf")
    else:
        st.error("Please enter valid bills for all fields.")
