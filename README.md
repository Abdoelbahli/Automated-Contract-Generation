# Automated Contract Management

A Python project that automates contract data extraction, validation, generation, and analysis using templates. This project includes the following functionalities:

1. **Extraction of key data points** from contract files (e.g., provider/client info, contract dates).
2. **Validation of extracted data** to check for completeness, date issues, and expiring contracts.
3. **Automated generation of contract documents** from a template and a list of sample data.
4. **Data analysis and visualization** of contract statuses, trends, and summaries through a Streamlit application.

## Project Structure

```markdown
Automated-Contract-Management
│
├── app.py                          # Main Streamlit application for contract management
├── contract_loader.py               # File for extracting contract information
├── validation_checks.py             # Validation checks for contract data
├── Contract_template.docx           # Contract template file
├── Generate_test_samples            # Folder for test sample generation
│   ├── contract_generation.py       # Script for generating contract samples
│   └── contract_data.py             # Sample data for contract generation
├── generated_contracts              # Folder to store generated contracts (leave empty, will be filled by script)
└── requirements.txt                 # Dependencies for the project
```

## Requirements

- **Python 3.7+**
- Install required packages:
  ```bash
  pip install -r requirements.txt
  ```
- **spaCy Language Model**:
  ```bash
  python -m spacy download en_core_web_sm
  ```

## Usage

### 1. Streamlit Application (`app.py`)

The main entry point of this project is `app.py`, a Streamlit application for managing contract data and visualizing insights. This app provides an easy-to-use interface for:

- **Uploading Contracts**: Upload DOCX contract files for automated extraction and validation.
- **Viewing Contract Data**: Display extracted contract information.
- **Running Validations**: Check for missing fields, date issues, and flag expiring contracts.
- **Visualizing Contract Trends**: Analyze contracts by status (e.g., active, expiring, expired), average contract length, renewal rates, and more.

To start the Streamlit app:

```bash
streamlit run app.py
```

### 4. Generate Sample Contracts (Optional)

To generate sample contracts for testing:
1. Populate `contract_data.py` with sample data.
2. Run `contract_generation.py` to create DOCX files based on `Contract_template.docx` for each sample in `contract_data.py`.

```python
python Generate_test_samples/contract_generation.py
```

### Folder and File Descriptions

- **app.py**: The main Streamlit application for contract management, analysis, and visualization.
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
