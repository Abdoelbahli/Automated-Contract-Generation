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

def validate_contract_data(contract_data):
    """Validate contract data"""
    issues = {}
    
    # Convert tuple to dictionary if needed
    if isinstance(contract_data, tuple):
        contract_dict = {
            "client_name": contract_data[0] if len(contract_data) > 0 else "",
            "project_name": contract_data[1] if len(contract_data) > 1 else "",
            "start_date": contract_data[2] if len(contract_data) > 2 else "",
            "end_date": contract_data[3] if len(contract_data) > 3 else "",
            "contract_value": contract_data[4] if len(contract_data) > 4 else "",
            "payment_terms": contract_data[5] if len(contract_data) > 5 else "",
            "scope_of_work": contract_data[6] if len(contract_data) > 6 else ""
        }
    else:
        contract_dict = contract_data
    
    # Check for missing or empty fields
    required_fields = [
        "client_name",
        "project_name",
        "start_date",
        "end_date",
        "contract_value",
        "payment_terms",
        "scope_of_work"
    ]
    
    missing_fields = []
    for field in required_fields:
        if field not in contract_dict or not contract_dict[field]:
            missing_fields.append(field)
    
    if missing_fields:
        issues["Missing Fields"] = [f"Missing {field}" for field in missing_fields]
    
    # Validate dates
    try:
        start_date = parser.parse(str(contract_dict.get("start_date", "")))
        end_date = parser.parse(str(contract_dict.get("end_date", "")))
        
        if start_date > end_date:
            issues["Date Problems"] = ["End date must be after start date"]
        
        # Check if contract is expiring soon (within 30 days)
        if end_date - datetime.now() <= timedelta(days=30):
            issues["Expiring Soon"] = ["Contract expires within 30 days"]
            
    except (ValueError, TypeError):
        issues["Date Problems"] = ["Invalid date format"]
    
    # If no issues found
    if not issues:
        issues["Complete and Valid"] = ["Contract is complete and valid."]
    
    return issues
