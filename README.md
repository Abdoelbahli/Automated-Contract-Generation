# Automated-Contract-Generation



```markdown
# Automated Contract Management

A Python project that automates contract data extraction, validation, and generation using templates. This project includes the following functionalities:
1. Extraction of key data points from contract files (e.g., provider/client info, contract dates).
2. Validation of extracted data to check for completeness, date issues, and expiring contracts.
3. Automated generation of contract documents from a template and a list of sample data.

## Project Structure

```
Automated-Contract-Management
│
├── contract_loader.py               # File for extracting contract information
├── validation_checks.py             # Validation checks for contract data
├── Contract_template.docx           # Contract template file
├── Generate_test_samples            # Folder for test sample generation
│   ├── contract_generation.py       # Script for generating contract samples
│   └── contract_data.py             # Sample data for contract generation
└── generated_contracts              # Folder to store generated contracts (leave empty, will be filled by script)
```

## Requirements

- Python 3.7+
- Required Python packages:
  ```bash
  pip install python-docx docxtpl spacy python-dateutil
  ```
- Download spaCy language model:
  ```bash
  python -m spacy download en_core_web_sm
  ```

## Usage

### 1. Extract Contract Data

Use `contract_loader.py` to extract data from an existing DOCX contract file. This script includes functions to extract details like the service provider, client info, and contract dates.

### 2. Validate Contract Data

Use `validation_checks.py` to validate extracted data. This module identifies missing fields, checks date validity, and flags contracts that are expiring soon.

### 3. Generate Sample Contracts

To generate sample contracts:
1. Populate `contract_data.py` with sample data.
2. Run `contract_generation.py` to create DOCX files based on `Contract_template.docx` for each sample in `contract_data.py`.

### Sample Usage

```python
# Extract and validate contract data
from contract_loader import extract_contract_data
from validation_checks import validate_contract_data

file_path = "path_to_your_contract.docx"
contract_data, contract_text = extract_contract_data(file_path)
validation_issues = validate_contract_data(contract_data)

print("Extracted Data:", contract_data)
print("Validation Issues:", validation_issues)
```

### Folder and File Descriptions

- **contract_loader.py**: Extracts details from DOCX files, such as service provider, client name, and contract dates.
- **validation_checks.py**: Validates extracted contract data, identifying missing or invalid information and flagging expiring contracts.
- **Generate_test_samples/**: Folder containing:
  - `contract_generation.py`: Generates sample contracts using a template.
  - `contract_data.py`: Contains sample data dictionaries for generating contracts.
- **Contract_template.docx**: DOCX file template for contract generation.
- **generated_contracts/**: Folder where generated contracts are saved.

## License

See the `LICENSE` file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue to discuss the changes first.
