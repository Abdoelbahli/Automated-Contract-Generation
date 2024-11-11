# validation_checks.py
import spacy
from datetime import datetime, timedelta
from dateutil import parser

nlp = spacy.load("en_core_web_sm")

def validate_contract_data(contract_data):
    """
    Validates key contract fields and categorizes issues into missing data,
    date problems, and expiring soon.
    """
    issues = {
        "Missing Information": [],
        "Date Problems": [],
        "Expiring Soon": []
    }

    # Check for missing fields
    for field, value in contract_data.items():
        if value == "Missing":
            issues["Missing Information"].append(f"{field.replace('_', ' ').title()} is missing.")

    # Validate date fields and categorize issues
    validate_date_fields(contract_data, issues)

    # Remove any categories that don't have issues
    issues = {k: v for k, v in issues.items() if v}

    if not issues:
        return {"Complete and Valid": ["Contract is complete and valid."]}

    return issues


def validate_date_fields(contract_data, issues):
    """
    Checks for date-related issues including missing dates, invalid formats,
    expiration status, and date inconsistencies.
    """
    contract_date = contract_data.get("Contract Date")
    start_date = contract_data.get("Start Date")
    end_date = contract_data.get("End Date")

    # Validate format and existence
    contract_date_valid = validate_date(contract_date)
    start_date_valid = validate_date(start_date)
    end_date_valid = validate_date(end_date)

    if not contract_date_valid:
        issues["Date Problems"].append("Contract date has an invalid format.")
    if not start_date_valid:
        issues["Date Problems"].append("Start date has an invalid format.")
    if not end_date_valid:
        issues["Date Problems"].append("End date has an invalid format.")

    # Convert dates to datetime objects for comparison
    contract_date = parser.parse(contract_date) if contract_date_valid else None
    start_date = parser.parse(start_date) if start_date_valid else None
    end_date = parser.parse(end_date) if end_date_valid else None

    # Check date logical consistency
    if start_date and end_date and start_date > end_date:
        issues["Date Problems"].append("Start date is after the end date.")

    # Flag contracts expiring within 30 days
    if end_date:
        if end_date <= datetime.now():
            issues["Expiring Soon"].append("Contract has expired.")
        elif end_date <= datetime.now() + timedelta(days=30):
            issues["Expiring Soon"].append("Contract is expiring within 30 days.")

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
