# validation_checks.py
from datetime import datetime, timedelta
from dateutil import parser

def check_completeness(contract_text):
    """Simple validation without spaCy"""
    required_fields = [
        "client_name",
        "project_name",
        "start_date",
        "end_date",
        "contract_value",
        "payment_terms",
        "scope_of_work"
    ]
    
    missing = []
    for field in required_fields:
        if field not in contract_text.lower():
            missing.append(field)
    
    return missing

def validate_contract_data(contracts):
    """Validate contract data"""
    issues = {}
    
    # Handle multiple contracts
    if not isinstance(contracts, list):
        contracts = [contracts]
    
    for contract in contracts:
        # Extract data from tuple
        client_name, project_name, start_date, end_date, contract_value, payment_terms, scope_of_work = contract
        
        # Check for missing or empty fields
        required_fields = {
            "client_name": client_name,
            "project_name": project_name,
            "start_date": start_date,
            "end_date": end_date,
            "contract_value": contract_value,
            "payment_terms": payment_terms,
            "scope_of_work": scope_of_work
        }
        
        missing_fields = []
        for field, value in required_fields.items():
            if not value:
                missing_fields.append(field)
        
        if missing_fields:
            issues["Missing Fields"] = [f"Missing {field}" for field in missing_fields]
        
        # Validate dates
        try:
            start_date = parser.parse(str(start_date))
            end_date = parser.parse(str(end_date))
            
            if start_date > end_date:
                issues["Date Problems"] = ["End date must be after start date"]
            
            # Check if contract is expiring soon (within 30 days)
            if end_date - datetime.now() <= timedelta(days=30):
                issues["Expiring Soon"] = ["Contract expires within 30 days"]
                
        except (ValueError, TypeError):
            issues["Date Problems"] = ["Invalid date format"]
    
    return issues
