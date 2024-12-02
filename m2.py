import Streamlit as st; # type: ignore
from io import BytesIO;
from reportlab.pdfgen import canvas # type: ignore

# Function to calculate the carbon footprint
def calculate_carbon_footprint(electricity_bill, gas_bill, fuel_bill) :
 carbon_footprint = (electricity_bill * 12 * 0.00005) + (gas_bill * 12 * 0.0053) + (fuel_bill * 12 * 2.32)
 return carbon_footprint

st.title('Carbon FootPrint Calculator')

electricity_bill = st.number_input('Enter your average monthly electricity bill in euros', min_vaalue=0.0, format="%.2f")
gas_bill = st.number_input('enter your average monthly natural gas bill in euros' , min_value=0.0, format="%.2f")
fuel_bill = st.number_input('Enter your average monthly fuel bill for transportation in euros', min_value=0.0, format="%.2f")

if st.button('Calculate Carbon FootPrint'):
    

  if electricity_bill and gas_bill and fuel_bill:
    carbon_footprint = calculate_carbon_footprint(electricity_bill, gas_bill, fuel_bill)
st.write(f"Your estimated carbon footprint is: {carbon_footprint:.2f} kg CO2 per year.")

def create_simple_pdf():
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    
    # Add content to the PDF
    c.drawString(100, 750, "Simple PDF Report")
    c.drawString(100, 725, "This is a sample PDF created using Streamlit and ReportLab.")
    c.drawString(100, 700, "Enjoy generating PDFs easily!")
    
    # Save the PDF to the buffer
    c.save()
    buffer.seek(0)
    return buffer

# Streamlit app
st.title("Simple PDF Generator")

if st.button("Generate Simple PDF"):
    pdf_buffer = create_simple_pdf()
    st.download_button(
        label="Download PDF",
        data=pdf_buffer,
        file_name="simple_report.pdf",
        mime="application/pdf"
    )
