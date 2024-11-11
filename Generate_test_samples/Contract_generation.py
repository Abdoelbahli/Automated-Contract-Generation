from docxtpl import DocxTemplate
from contract_data import contract_data_list  # Import the list of dictionaries

# Load the contract template
template_path = "Contract_template.docx"
template = DocxTemplate(template_path)

# Loop through each dictionary and generate a contract with an indexed filename
for index, contract_data in enumerate(contract_data_list):
    template.render(contract_data)
    output_filename = f"C:/Users/PAVILION/Desktop/Automated Contract Generation/generated_contracts/generated_contract_{index+1}.docx"  # Unique filename for each contract
    template.save(output_filename)
    print(f"Contract generated and saved as {output_filename}")
