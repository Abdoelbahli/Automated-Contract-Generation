import streamlit as st
from docxtpl import DocxTemplate
from datetime import datetime
import os
import zipfile
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
from contract_loader import extract_contract_data
from validation_checks import check_completeness, validate_contract_data
from pathlib import Path

# Define the template path
TEMPLATE_PATH = Path(__file__).parent / "templates" / "contract_template.docx"

# Function to load and process contract data
def load_contract_data(files):
    contract_data_list = []

    for file in files:
        contract_data, _ = extract_contract_data(file)
        contract_data_list.append(contract_data)

    df = pd.DataFrame(contract_data_list)

    # Ensure date columns are in datetime format
    df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
    df['End Date'] = pd.to_datetime(df['End Date'], errors='coerce')
    df['Contract Date'] = pd.to_datetime(df['Contract Date'], errors='coerce')

    # Calculate contract length in days
    df['Contract Length'] = (df['End Date'] - df['Start Date']).dt.days

    return df

# Sidebar with three options
st.sidebar.title("Options")
option = st.sidebar.radio("Select an option:", ("Generate Contract", "Check Contract", "Contract Insights"))

if option == "Generate Contract":
    st.title("Contract Generator")
    st.write("Fill in the contract details below:")

    contract_date = st.date_input("Contract Date").strftime("%B %d, %Y")
    service_provider = st.text_input("Service Provider")
    provider_address = st.text_input("Provider Address")
    provider_email = st.text_input("Provider Email")
    client_name = st.text_input("Client Name")
    client_address = st.text_input("Client Address")
    client_email = st.text_input("Client Email")
    service_description = st.text_area("Service Description")
    payment_amount = st.text_input("Payment Amount")
    payment_terms = st.text_area("Payment Terms")
    start_date = st.date_input("Start Date").strftime("%B %d, %Y")
    end_date = st.date_input("End Date").strftime("%B %d, %Y")
    termination_conditions = st.text_area("Termination Conditions")
    governing_law = st.text_input("Governing Law")

    if st.button("Generate Contract"):
        contract_data = {
            "contract_date": contract_date,
            "service_provider": service_provider,
            "provider_address": provider_address,
            "provider_email": provider_email,
            "client_name": client_name,
            "client_address": client_address,
            "client_email": client_email,
            "service_description": service_description,
            "payment_amount": payment_amount,
            "payment_terms": payment_terms,
            "start_date": start_date,
            "end_date": end_date,
            "termination_conditions": termination_conditions,
            "governing_law": governing_law
        }

        # When using the template
        template = load_contract_template()
        if template is None:
            st.stop()

        template.render(contract_data)
        output_filename = f"generated_contract_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
        template.save(output_filename)
        st.success(f"Contract generated and saved as {output_filename}")

        # Button to download the generated contract
        with open(output_filename, "rb") as file:
            st.download_button(
                label="Download Contract",
                data=file,
                file_name=output_filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

# Contract Checker
elif option == "Check Contract":
    st.title("Contract Checker App")
    st.write("Upload a single contract file, select multiple contract files, or upload a zip folder containing contracts.")

    # File uploader for single or multiple contract files or a zip folder
    uploaded_files = st.file_uploader("Upload contract file(s) or a zip folder containing contracts:", type=["docx", "zip"], accept_multiple_files=True)

    # Button to start checking contracts
    if st.button("Check Contracts"):
        contract_results = []

        if uploaded_files:
            for uploaded_file in uploaded_files:
                if uploaded_file.type == "application/zip":
                    st.write("Checking contracts in the uploaded zip folder...")

                    # Extract zip file contents
                    with zipfile.ZipFile(BytesIO(uploaded_file.getbuffer()), 'r') as zip_ref:
                        zip_ref.extractall("temp_contracts")

                    # Process each contract file in the extracted folder
                    for file_name in os.listdir("temp_contracts"):
                        if file_name.endswith(".docx"):
                            file_path = os.path.join("temp_contracts", file_name)

                            # Load contract data and text
                            contract_data, contract_text = extract_contract_data(file_path)

                            # Check completeness and validation issues
                            missing_entities = check_completeness(contract_text)
                            validation_issues = validate_contract_data(contract_data)

                            # Compile issues
                            issues = {"Missing Information": [], "Date Problems": [], "Expiring Soon": []}
                            if missing_entities:
                                friendly_messages = {
                                    "DATE": "The contract is missing a date.",
                                    "GPE": "The contract is missing a location (e.g., country, state, city).",
                                    "PERSON": "The contract is missing a person or party involved.",
                                    "ORG": "The contract is missing an organization name."
                                }
                                for entity in missing_entities:
                                    issues["Missing Information"].append(friendly_messages.get(entity, f"The contract is missing: {entity}"))

                            if validation_issues and validation_issues != {"Complete and Valid": ["Contract is complete and valid."]}:
                                for category, issue_list in validation_issues.items():
                                    issues[category].extend(issue_list)

                            # Remove any categories that don't have issues
                            issues = {k: v for k, v in issues.items() if v}

                            # Store results with flag for issues
                            has_issues = bool(issues)
                            contract_results.append({
                                "file_name": file_name,
                                "issues": issues,
                                "has_issues": has_issues
                            })
                else:
                    # Handle the uploaded contract file
                    st.write(f"Checking the uploaded contract file: {uploaded_file.name}")

                    # Save the uploaded file
                    file_path = os.path.join("temp_contracts", uploaded_file.name)
                    os.makedirs("temp_contracts", exist_ok=True)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    # Process the uploaded file
                    contract_data, contract_text = extract_contract_data(file_path)

                    # Check completeness and validation issues
                    missing_entities = check_completeness(contract_text)
                    validation_issues = validate_contract_data(contract_data)

                    # Compile issues
                    issues = {"Missing Information": [], "Date Problems": [], "Expiring Soon": []}
                    if missing_entities:
                        friendly_messages = {
                            "DATE": "The contract is missing a date.",
                            "GPE": "The contract is missing a location (e.g., country, state, city).",
                            "PERSON": "The contract is missing a person or party involved.",
                            "ORG": "The contract is missing an organization name."
                        }
                        for entity in missing_entities:
                            issues["Missing Information"].append(friendly_messages.get(entity, f"The contract is missing: {entity}"))

                    if validation_issues and validation_issues != {"Complete and Valid": ["Contract is complete and valid."]}:
                        for category, issue_list in validation_issues.items():
                            issues[category].extend(issue_list)

                    # Remove any categories that don't have issues
                    issues = {k: v for k, v in issues.items() if v}

                    # Store results with flag for issues
                    has_issues = bool(issues)
                    contract_results.append({
                        "file_name": uploaded_file.name,
                        "issues": issues,
                        "has_issues": has_issues
                    })

            # Sort contracts with issues first
            contract_results.sort(key=lambda x: x["has_issues"], reverse=True)

            # Display results
            for result in contract_results:
                file_display = f"**{result['file_name']}**"
                if result["has_issues"]:
                    st.write(file_display, ":red[Issue found!]")
                    for category, issue_list in result["issues"].items():
                        st.markdown(f"### {category}")
                        for issue in issue_list:
                            st.markdown(f"- {issue}")
                else:
                    st.write(file_display, ":green[All checks passed!]")
                    st.markdown("### Contract is complete and valid.")
                st.markdown("---")  # Add horizontal line between results
        else:
            st.error("Please upload a contract file, multiple contract files, or a zip folder containing contracts.")

# Contract Insights
elif option == "Contract Insights":
    st.title("Contract Insights Dashboard")
    st.write("Upload your contract files to generate insightful statistics and visualizations.")

    uploaded_files = st.file_uploader("Upload contract file(s) or a zip folder containing contracts:", type=["docx", "zip"], accept_multiple_files=True)

    if st.button("Generate Insights"):
        if uploaded_files:
            contract_data_list = []

            for uploaded_file in uploaded_files:
                if uploaded_file.type == "application/zip":
                    st.write("Extracting and processing contracts from the uploaded zip folder...")

                    with zipfile.ZipFile(BytesIO(uploaded_file.getbuffer()), 'r') as zip_ref:
                        zip_ref.extractall("temp_contracts")
                    for file_name in os.listdir("temp_contracts"):
                        if file_name.endswith(".docx"):
                            file_path = os.path.join("temp_contracts", file_name)
                            contract_data, _ = extract_contract_data(file_path)
                            contract_data["File Name"] = file_name
                            contract_data_list.append(contract_data)
                else:
                    st.write(f"Processing the uploaded contract file: {uploaded_file.name}")
                    file_path = os.path.join("temp_contracts", uploaded_file.name)
                    os.makedirs("temp_contracts", exist_ok=True)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    contract_data, _ = extract_contract_data(file_path)
                    contract_data["File Name"] = uploaded_file.name
                    contract_data_list.append(contract_data)

            df = pd.DataFrame(contract_data_list)
            df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
            df['End Date'] = pd.to_datetime(df['End Date'], errors='coerce')
            df['Contract Date'] = pd.to_datetime(df['Contract Date'], errors='coerce')
            today = datetime.today()
            df['Contract Length'] = (df['End Date'] - df['Start Date']).dt.days
            df['Status'] = df['End Date'].apply(lambda x: 'Expired' if x < today else ('Expiring Soon' if x <= today + pd.DateOffset(days=30) else 'Active'))

            contracts_with_issues = df[(df[['Start Date', 'End Date', 'Service Provider', 'Client Name']].isnull().any(axis=1))]
            good_contracts = df[df['Status'] == 'Active']
            expiring_contracts = df[df['Status'] == 'Expiring Soon']

            st.write("### Statistics")
            st.write(f"Total Contracts: {len(df)}")
            st.write(f"Active Contracts: {len(good_contracts)}")
            st.write(f"Expiring Contracts: {len(expiring_contracts)}")
            st.write(f"Contracts with Issues: {len(contracts_with_issues)}")
            st.write(f"Average Contract Length: {df['Contract Length'].mean():.2f} days")

            st.write("### Visualizations")

            # Number of contracts by status
            fig, ax = plt.subplots()
            status_counts = df['Status'].value_counts()
            ax.bar(status_counts.index, status_counts.values)
            ax.set_title("Number of Contracts by Status")
            ax.set_xlabel("Status")
            ax.set_ylabel("Count")
            st.pyplot(fig)

            fig, ax = plt.subplots()
            ax.hist(df['Contract Length'], bins=20, color='skyblue', edgecolor='black')
            ax.set_title("Distribution of Contract Length")
            ax.set_xlabel("Contract Length (days)")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)

            # Contracts overview pie chart with legend
            fig, ax = plt.subplots()
            issue_counts = [len(good_contracts), len(expiring_contracts), len(contracts_with_issues)]
            labels = ['Active Contracts', 'Expiring Soon', 'Contracts with Issues']
            colors = ['#66c2a5', '#fc8d62', '#8da0cb']
            wedges, texts, autotexts = ax.pie(issue_counts, labels=labels, autopct='%1.1f%%', colors=colors)
            ax.legend(wedges, labels, title="Contract Status", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
            ax.set_title("Contracts Overview")
            st.pyplot(fig)
        else:
            st.error("Please upload a contract file, multiple contract files, or a zip folder containing contracts.")

# When using the template
def load_contract_template():
    try:
        if not TEMPLATE_PATH.exists():
            st.error(f"Template file not found at: {TEMPLATE_PATH}")
            return None
        return DocxTemplate(str(TEMPLATE_PATH))
    except Exception as e:
        st.error(f"Error loading template: {str(e)}")
        return None

def generate_contract(contract_data):
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
