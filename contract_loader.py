#contract_loader.py
from docxtpl import DocxTemplate
from io import BytesIO

def extract_contract_data(uploaded_file):
    """Extract data from uploaded contract file"""
    try:
        # Read the uploaded file into a BytesIO object
        bytes_data = BytesIO(uploaded_file.getvalue())
        
        # Load the document
        doc = DocxTemplate(bytes_data)
        
        # Extract the context data (assuming it's stored in the document's context)
        contract_data = {
            "client_name": "",
            "project_name": "",
            "start_date": "",
            "end_date": "",
            "contract_value": "",
            "payment_terms": "",
            "scope_of_work": ""
        }
        
        # Here you would add logic to extract the actual values from the document
        # For now, we're returning an empty dictionary with the expected structure
        
        return contract_data
        
    except Exception as e:
        raise Exception(f"Error extracting contract data: {str(e)}")
