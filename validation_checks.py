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
    
    # Unpack tuple values
    try:
        client_name, project_name, start_date, end_date, contract_value, payment_terms, scope_of_work = contract_data
        
        # Check for missing or empty fields
        if not all([client_name, project_name, start_date, end_date, contract_value, payment_terms, scope_of_work]):
            issues["Missing Fields"] = []
            if not client_name:
                issues["Missing Fields"].append("Missing client name")
            if not project_name:
                issues["Missing Fields"].append("Missing project name")
            if not start_date:
                issues["Missing Fields"].append("Missing start date")
            if not end_date:
                issues["Missing Fields"].append("Missing end date")
            if not contract_value:
                issues["Missing Fields"].append("Missing contract value")
            if not payment_terms:
                issues["Missing Fields"].append("Missing payment terms")
            if not scope_of_work:
                issues["Missing Fields"].append("Missing scope of work")
        
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
            
        if not issues:
            issues["Complete and Valid"] = ["Contract is complete and valid."]
            
    except (ValueError, TypeError) as e:
        issues["Error"] = [f"Invalid contract data format: {str(e)}"]
    
    return issues
