import streamlit as st
from docxtpl import DocxTemplate
from pathlib import Path
from io import BytesIO
import os
from validation_checks import validate_contract_data

# Define template path
TEMPLATE_PATH = Path(__file__).parent / "templates" / "contract_template.docx"

# Set page title
st.title("Contract Generation and Validation")

# Add navigation
option = st.sidebar.selectbox(
    "Choose a function",
    ("Contract Generation", "Contract Validation", "Contract Insights")
)

if option == "Contract Generation":
    st.header("Contract Generation")
    st.write("Fill in the contract details below:")

    # Contract form inputs
    contract_data = {
        "client_name": st.text_input("Client Name"),
        "project_name": st.text_input("Project Name"),
        "start_date": st.date_input("Start Date"),
        "end_date": st.date_input("End Date"),
        "contract_value": st.number_input("Contract Value", min_value=0.0),
        "payment_terms": st.text_area("Payment Terms"),
        "scope_of_work": st.text_area("Scope of Work")
    }

    if st.button("Generate Contract"):
        try:
            # Debug: Print the template path
            st.write(f"Looking for template at: {TEMPLATE_PATH}")
            
            # Check if template exists
            if not TEMPLATE_PATH.exists():
                st.error(f"Template file not found at: {TEMPLATE_PATH}")
                st.stop()
            
            # Load template - use the actual path, not the string "TEMPLATE_PATH"
            template = DocxTemplate(TEMPLATE_PATH)  # Changed this line
            
            # Convert dates to string format
            contract_data["start_date"] = contract_data["start_date"].strftime("%Y-%m-%d")
            contract_data["end_date"] = contract_data["end_date"].strftime("%Y-%m-%d")
            
            # Render template
            template.render(contract_data)
            
            # Save to BytesIO
            doc_io = BytesIO()
            template.save(doc_io)
            doc_io.seek(0)
            
            # Offer download
            st.download_button(
                label="Download Contract",
                data=doc_io,
                file_name="generated_contract.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            
        except Exception as e:
            st.error(f"Error generating contract: {str(e)}")
            # Debug: Print more
