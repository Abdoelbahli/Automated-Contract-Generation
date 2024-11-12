import streamlit as st
from docxtpl import DocxTemplate
from pathlib import Path
from io import BytesIO
import os
from contract_loader import extract_contract_data
from validation_checks import check_completeness, validate_contract_data
from datetime import datetime

# Define template path
current_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(current_dir, "templates", "Contract_template.docx")

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
            # Load template
            doc = DocxTemplate(template_path)
            
            # Create a copy of contract_data to avoid modifying the original
            template_data = contract_data.copy()
            
            # Format dates properly
            if isinstance(template_data["start_date"], datetime):
                template_data["start_date"] = template_data["start_date"].strftime("%Y-%m-%d")
            
            if isinstance(template_data["end_date"], datetime):
                template_data["end_date"] = template_data["end_date"].strftime("%Y-%m-%d")
            
            # Render the template with the formatted data
            doc.render(template_data)
            
            # Create a BytesIO object to store the document
            doc_io = BytesIO()
            doc.save(doc_io)
            doc_io.seek(0)
            
            # Offer the document for download
            st.download_button(
                label="Download Contract",
                data=doc_io,
                file_name="generated_contract.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        except Exception as e:
            st.error("Error generating contract. Please try again.")
