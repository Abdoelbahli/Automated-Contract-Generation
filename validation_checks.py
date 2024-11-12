# validation_checks.py
import spacy
from datetime import datetime, timedelta
from dateutil import parser

nlp = spacy.load("en_core_web_sm")

def validate_contract_data(contract_data):
    """Validate contract data"""
    issues = {}
    
    # Ensure we have a tuple with the right number of elements
    expected_fields = 7
    if len(contract_data) != expected_fields:
        issues["Missing Fields"] = [f"Contract data is incomplete. Expected {expected_fields} fields, got {len(contract_data)}"]
        return issues
    
    # Unpack tuple values only if we have the right number of elements
    try:
        client_name, project_name, start_date, end_date, contract_value, payment_terms, scope_of_work = contract_data
        
        # Rest of your validation logic remains the same
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
            
    except Exception as e:
        issues["Error"] = [f"Error validating contract: {str(e)}"]
    
    return issues

def validate_date(date_str):
    """
    Validates whether the provided date string is in a proper date format.
    """
    try:
        parser.parse(date_str)
        return True
    except (ValueError, TypeError):
        return False

def check_completeness(text):
    """
    Uses spaCy to analyze the text for entities to assess 
    whether key details are included.
    """
    doc = nlp(text)
    expected_entities = {"DATE", "PERSON", "ORG", "GPE"}
    found_entities = {ent.label_ for ent in doc.ents}

    # Check if required entities are present
    missing_entities = expected_entities - found_entities
    return list(missing_entities)
