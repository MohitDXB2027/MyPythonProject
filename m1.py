import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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
            # Create PDF using reportlab
            pdf_filename = "carbon_footprint_report.pdf"
            c = canvas.Canvas(pdf_filename, pagesize=letter)
            
            # Add Title to PDF
            c.setFont("Helvetica", 16)
            c.drawString(200, 750, "Carbon Footprint Report")
            
            # Add the details to the PDF
            c.setFont("Helvetica", 12)
            c.drawString(50, 700, f"Monthly Electricity Bill: {electricity_bill} EUR")
            c.drawString(50, 675, f"Monthly Gas Bill: {gas_bill} EUR")
            c.drawString(50, 650, f"Monthly Fuel Bill: {fuel_bill} EUR")
            c.drawString(50, 625, f"Calculated Carbon Footprint: {carbon_footprint:.2f} kg CO2 per year")
            
            # Save the PDF
            c.save()
            
            # Provide the option to download the PDF
            st.download_button("Download PDF", pdf_filename)
    else:
        st.error("Please enter valid bills for all fields.")
