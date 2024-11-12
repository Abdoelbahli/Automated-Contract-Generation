import streamlit as st
from docxtpl import DocxTemplate
from pathlib import Path
from io import BytesIO
import os
from contract_loader import extract_contract_data
from validation_checks import check_completeness, validate_contract_data

# Define template path
template_file = "contract_template.docx"
template_path = os.path.join(os.path.dirname(__file__), "templates", template_file)

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
            # Debug path
            st.write(f"Template path: {template_path}")
            
            # Check if file exists
            if not os.path.exists(template_path):
                st.error(f"Template not found at: {template_path}")
                st.stop()
            
            # Load and process template
            doc = DocxTemplate(template_path)
            
            # Process dates
            contract_data["start_date"] = contract_data["start_date"].strftime("%Y-%m-%d")
            contract_data["end_date"] = contract_data["end_date"].strftime("%Y-%m-%d")
            
            # Render the template with the data
            doc.render(contract_data)
            
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
            st.error(f"Error generating contract: {str(e)}")
            st.error(f"Current working directory: {os.getcwd()}")
            st.error(f"Files in current directory: {os.listdir('.')}")
            if os.path.exists("templates"):
                st.error(f"Files in templates directory: {os.listdir('templates')}")
