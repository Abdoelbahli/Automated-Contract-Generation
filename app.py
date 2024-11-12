import streamlit as st
from docxtpl import DocxTemplate
from pathlib import Path
from io import BytesIO
import os

# Define constants and helper functions at the top of the file
TEMPLATE_PATH = Path(__file__).parent / "templates" / "contract_template.docx"

def load_contract_template():
    """Load the contract template file."""
    try:
        if not TEMPLATE_PATH.exists():
            st.error(f"Template file not found at: {TEMPLATE_PATH}")
            return None
        return DocxTemplate(str(TEMPLATE_PATH))
    except Exception as e:
        st.error(f"Error loading template: {str(e)}")
        return None

def generate_contract(contract_data):
    """Generate a contract from template and data."""
    try:
        template = load_contract_template()
        if template is None:
            return None
            
        template.render(contract_data)
        
        # Create a BytesIO object to store the document
        doc_io = BytesIO()
        template.save(doc_io)
        doc_io.seek(0)
        return doc_io
    except Exception as e:
        st.error(f"Error generating contract: {str(e)}")
        return None

# Streamlit app main code
def main():
    st.title("Contract Generation and Validation")
    
    # Add navigation
    option = st.sidebar.selectbox(
        "Choose a function",
        ("Contract Validation", "Contract Generation", "Contract Insights")
    )

    if option == "Contract Validation":
        # Your existing validation code
        template = load_contract_template()
        if template is None:
            st.stop()
        # Rest of your validation code...

    elif option == "Contract Generation":
        # Your contract generation code
        pass

    elif option == "Contract Insights":
        # Your insights code
        pass

if __name__ == "__main__":
    main()
