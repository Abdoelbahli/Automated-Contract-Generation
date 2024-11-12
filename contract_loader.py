#contract_loader.py
import re
from docx import Document

def read_contract_file(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def extract_service_provider(text):
    pattern = r"Service Provider:\s*(.*?)\s*Address:"
    match = re.search(pattern, text, re.DOTALL)
    result = match.group(1).strip() if match and match.group(1).strip() != "" else "Missing"
    return result

def extract_provider_address(text):
    pattern = r"Service Provider:\s*(?:.*?\s*)Address:\s*(.*?)(?=\s*Contact Email:|$)"
    match = re.search(pattern, text, re.DOTALL)
    address = match.group(1).strip() if match else ""
    return address if address else "Missing"

def extract_provider_email(text):
    pattern = r"Contact Email:\s*(\S+@\S+\.\S+)"
    match = re.search(pattern, text)
    email = match.group(1).strip() if match else ""
    return email if email else "Missing"

def extract_client_email(text):
    pattern = r"Client:.*?Contact Email:\s*(.*?)(?=\s*(?:\d\. Services Provided|$))"
    match = re.search(pattern, text, re.DOTALL)
    email = match.group(1).strip() if match else ""
    return email if email else "Missing"

def extract_client_name(text):
    pattern = r"Client:\s*(.*?)\s*(?:Address:|Contact Email:|$)"
    match = re.search(pattern, text, re.DOTALL)
    name = match.group(1).strip() if match else ""
    return name if name else "Missing"

def extract_client_address(text):
    pattern = r"Client:.*?Address:\s*(.*?)(?=\s*Contact Email:|$)"
    match = re.search(pattern, text, re.DOTALL)
    address = match.group(1).strip() if match else ""
    return address if address else "Missing"

def extract_service_description(text):
    pattern = r"1\.\s*Services Provided\s*The Service Provider agrees to provide the following services to the Client:\s*(.*?)(?=2\.\s*Payment Terms|$)"
    match = re.search(pattern, text, re.DOTALL)
    service_description = match.group(1).strip() if match else ""
    return service_description if service_description else "Missing"

def extract_payment_amount(text):
    pattern = r"amount of\s*\$?\s*(\d+(\.\d{2})?)"
    match = re.search(pattern, text)
    payment_amount = match.group(1).strip() if match else ""
    return payment_amount if payment_amount else "Missing"

def extract_payment_terms(text):
    pattern = r"2\.\s*Payment Terms\s*(.*?)(?=\n3\.\s*Contract Duration|$)"
    match = re.search(pattern, text, re.DOTALL)
    payment_terms = match.group(1).strip() if match else ""
    if "payment schedule:" in payment_terms:
        payment_terms = payment_terms.split("payment schedule:")[1].strip()
        payment_terms = re.sub(r"\n3\..*", "", payment_terms, flags=re.DOTALL).strip()
    return payment_terms if payment_terms else "Missing"

def extract_termination_conditions(text):
    pattern = r"4\.\s*Termination\s*(.*?)(?=5\.\s*Confidentiality|$)"
    match = re.search(pattern, text, re.DOTALL)
    termination_conditions = match.group(1).strip() if match else ""
    if termination_conditions:
        # Remove the "under the following conditions:" if it exists
        termination_conditions = termination_conditions.split("conditions:")[-1].strip()
        # Remove any section headers that come after the conditions
        termination_conditions = re.sub(r"\n5\..*", "", termination_conditions, flags=re.DOTALL).strip()
        # Remove any leading bullet points or spaces
        termination_conditions = re.sub(r"^-?\s*•?\s*", "", termination_conditions, flags=re.MULTILINE).strip()
    return termination_conditions if termination_conditions else "Missing"

def extract_governing_law(text):
    pattern = r"6\.\s*Governing Law\s*This Agreement will be governed by and construed in accordance with the laws of\s*(.*?)(?=\n\d+\.\s|7\.\s*Signatures|$)"
    match = re.search(pattern, text, re.DOTALL)
    governing_law = match.group(1).strip() if match else ""
    return governing_law if governing_law else "Missing"
    
def extract_start_date(text):
    pattern = r"This Agreement will begin on (\w+ \d{1,2}, \d{4})"
    match = re.search(pattern, text)
    start_date = match.group(1).strip() if match else ""
    return start_date if start_date else "Missing"


def extract_end_date(text):
    pattern = r"will continue until (\w+ \d{1,2}, \d{4})"
    match = re.search(pattern, text)
    end_date = match.group(1).strip() if match else ""
    return end_date if end_date else "Missing"

def extract_contract_date(text):
    pattern = r"entered into on (\w+ \d{1,2}, \d{4})"
    match = re.search(pattern, text)
    contract_date = match.group(1).strip() if match else ""
    return contract_date if contract_date else "Missing"

# Define the main function

def extract_contract_data(file_path):
    # Read the contract
    contract_text = read_contract_file(file_path)

    # Initialize contract data dictionary
    contract_data = {}

    # Apply extraction functions and store results in contract_data
    contract_data['Service Provider'] = extract_service_provider(contract_text)
    contract_data['Provider Address'] = extract_provider_address(contract_text)
    contract_data['Provider Email'] = extract_provider_email(contract_text)
    contract_data['Client Name'] = extract_client_name(contract_text)
    contract_data['Client Address'] = extract_client_address(contract_text)
    contract_data['Client Email'] = extract_client_email(contract_text)
    contract_data['Service Description'] = extract_service_description(contract_text)
    contract_data['Payment Amount'] = extract_payment_amount(contract_text)
    contract_data['Payment Terms'] = extract_payment_terms(contract_text)
    contract_data['Termination Conditions'] = extract_termination_conditions(contract_text)
    contract_data['Governing Law'] = extract_governing_law(contract_text)
    contract_data['Start Date'] = extract_start_date(contract_text)
    contract_data['End Date'] = extract_end_date(contract_text)
    contract_data['Contract Date'] = extract_contract_date(contract_text)

    # Return both contract_data and contract_text
    return contract_data, contract_text
