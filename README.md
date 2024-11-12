# Automated Contract Management

A Python-based application for automating contract management tasks, such as data extraction, validation, and document generation using templates. This app allows users to upload contract files, validate essential information, generate new contracts, and view analytics.

## Features
1. Extracts key data points (provider/client info, contract dates) from uploaded DOCX contract files.
2. Validates extracted data for completeness, date accuracy, and contract status (e.g., active, expiring).
3. Generates new contracts using a template with sample data.
4. Provides analytics on uploaded contract data, such as contract count, average duration, and expiration trends.

## Project Structure
```markdown
Automated-Contract-Management
│
├── app.py                         # Main Streamlit app file for the contract management UI
├── contract_loader.py             # Extracts contract information from DOCX files
├── validation_checks.py           # Validates contract data for completeness and accuracy
├── Contract_template.docx         # Template file for generating new contracts
├── Generate_test_samples          # Folder for test sample generation
│   ├── contract_generation.py     # Script for generating contract samples
│   └── contract_data.py           # Sample data for contract generation
└── generated_contracts            # Folder to store generated contracts (initially empty)
```

## Requirements

### Prerequisites
- **Python** (3.7+)
- **Dependencies**: Install required packages by running the following command:
  ```bash
  pip install -r requirements.txt
  ```
  Ensure you have the required language model for spaCy:
  ```bash
  python -m spacy download en_core_web_sm
  ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abdoelbahli/Automated-Contract-Generation
   cd Automated-Contract-Management
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

### Running the App

1. **Start the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

2. **App Features**:
   - **Upload Contracts**: Upload DOCX files for extraction and validation.
   - **View Extracted Data**: See extracted fields (provider/client info, dates, etc.).
   - **Validate Contracts**: Check for missing information, date issues, or expiring contracts.
   - **Analytics**: View contract statistics (e.g., number of active, expiring, expired contracts).

3. **Generating Sample Contracts** (for testing purposes):
   - Populate `contract_data.py` with sample data.
   - Run `contract_generation.py` to create DOCX files based on `Contract_template.docx`.
   ```bash
   python Generate_test_samples/contract_generation.py
   ```
   - Generated contracts will be saved in the `generated_contracts` folder.

### Example Usage

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

## Demo
follow the setup steps above and launch the app locally.

## License

See the `LICENSE` file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For questions or issues, feel free to contact me 


