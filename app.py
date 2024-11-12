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
            # Load template
            template = DocxTemplate(str(TEMPLATE_PATH))
            
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

elif option == "Contract Validation":
    st.header("Contract Validation")
    st.write("Upload your contract file(s) for validation.")

    uploaded_files = st.file_uploader("Upload contract file(s) or a zip folder containing contracts:", 
                                    type=["docx", "zip"], 
                                    accept_multiple_files=True)

    if uploaded_files:
        contract_results = []
        
        for uploaded_file in uploaded_files:
            # Your existing validation logic here
            contract_data = {}  # Replace with your actual contract data extraction
            validation_issues = validate_contract_data(contract_data)
            
            # Store results
            has_issues = bool(validation_issues) and validation_issues != {"Complete and Valid": ["Contract is complete and valid."]}
            contract_results.append({
                "file_name": uploaded_file.name,
                "issues": validation_issues,
                "has_issues": has_issues
            })

        # Sort and display results
        contract_results.sort(key=lambda x: x["has_issues"], reverse=True)
        
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
            st.markdown("---")
    else:
        st.error("Please upload a contract file, multiple contract files, or a zip folder containing contracts.")

elif option == "Contract Insights":
    st.header("Contract Insights Dashboard")
    st.write("Upload your contract files to generate insightful statistics and visualizations.")
    
    # Your existing insights code here
