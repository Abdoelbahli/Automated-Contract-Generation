# contract_data.py
from datetime import datetime

contract_data_list = [
    {
        "contract_date": datetime.strptime("2024-11-01", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "XYZ Consulting Services",
        "provider_address": "123 Main St, Cityville, Country",
        "provider_email": "contact@xyzconsulting.com",
        "client_name": "Alice Johnson",
        "client_address": "789 Oak St, Suburbia, Country",
        "client_email": "alice.j@example.com",
        "service_description": "IT consulting to streamline workflow automation.",
        "payment_amount": "$7500",
        "payment_terms": "50% upfront, 50% upon completion",
        "start_date": "November 15, 2024",
        "end_date": "November 15, 2025",
        "termination_conditions": "30-day written notice required by either party.",
        "governing_law": "State of California, USA"
    },
    {
        "contract_date": datetime.strptime("2024-11-03", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "ABC Financial Advisors",
        "provider_address": "456 Maple Ave, Metropolis, Country",
        "provider_email": "info@abcfinance.com",
        "client_name": "Bob Smith",
        "client_address": "101 Pine Rd, Townsville, Country",
        "client_email": "bob.smith@example.com",
        "service_description": "Financial advisory and portfolio management.",
        "payment_amount": "$10000",
        "payment_terms": "Monthly payments of $2000",
        "start_date": "November 20, 2024",
        "end_date": "November 20, 2025",
        "termination_conditions": "15-day written notice required by either party.",
        "governing_law": "Province of Ontario, Canada"
    },
    {
        "contract_date": datetime.strptime("2024-11-05", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "LMN Marketing Solutions",
        "provider_address": "789 Willow Blvd, Industrial Park, Country",
        "provider_email": "contact@lmnmarketing.com",
        "client_name": "Carol Williams",
        "client_address": "567 Birch St, Uptown, Country",
        "client_email": "carol.w@example.com",
        "service_description": "Digital marketing and social media management.",
        "payment_amount": "$5000",
        "payment_terms": "Full payment due after three months",
        "start_date": "November 22, 2024",
        "end_date": "February 22, 2025",
        "termination_conditions": "Termination upon non-payment of fees.",
        "governing_law": "State of Texas, USA"
    },
    # Perfect data
    {
        "contract_date": datetime.strptime("2024-11-01", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "XYZ Consulting Services",
        "provider_address": "123 Main St, Cityville, Country",
        "provider_email": "contact@xyzconsulting.com",
        "client_name": "Alice Johnson",
        "client_address": "789 Oak St, Suburbia, Country",
        "client_email": "alice.j@example.com",
        "service_description": "IT consulting to streamline workflow automation.",
        "payment_amount": "$7500",
        "payment_terms": "50% upfront, 50% upon completion",
        "start_date": "November 15, 2024",
        "end_date": "November 15, 2025",
        "termination_conditions": "30-day written notice required by either party.",
        "governing_law": "State of California, USA"
    },
    # Incomplete data (missing email and address)
    {
        "contract_date": datetime.strptime("2024-11-03", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "ABC Financial Advisors",
        "provider_address": "456 Maple Ave, Metropolis, Country",
        "provider_email": "",
        "client_name": "Bob Smith",
        "client_address": "",
        "client_email": "bob.smith@example.com",
        "service_description": "Financial advisory and portfolio management.",
        "payment_amount": "$10000",
        "payment_terms": "Monthly payments of $2000",
        "start_date": "November 20, 2024",
        "end_date": "November 20, 2025",
        "termination_conditions": "15-day written notice required by either party.",
        "governing_law": "Province of Ontario, Canada"
    },
    # Expired contract
    {
        "contract_date": datetime.strptime("2023-11-01", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "Global Tech Solutions",
        "provider_address": "321 Sunset Blvd, Rivertown, Country",
        "provider_email": "contact@globaltech.com",
        "client_name": "Diana Green",
        "client_address": "22 Elm St, Lakeside, Country",
        "client_email": "diana.green@example.com",
        "service_description": "Cloud infrastructure management and support.",
        "payment_amount": "$20000",
        "payment_terms": "50% upfront, 50% upon project completion",
        "start_date": "January 10, 2022",
        "end_date": "January 10, 2023",
        "termination_conditions": "Either party may terminate with 30 days' written notice.",
        "governing_law": "New York, USA"
    },
    # Expiring soon contract (less than 30 days)
    {
        "contract_date": datetime.strptime("2024-10-01", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "Elite Design Services",
        "provider_address": "555 River Rd, Downtown, Country",
        "provider_email": "info@elitedesign.com",
        "client_name": "John Doe",
        "client_address": "101 Maple St, Downtown, Country",
        "client_email": "john.doe@example.com",
        "service_description": "Website design and SEO optimization services.",
        "payment_amount": "$3500",
        "payment_terms": "One-time payment upon completion",
        "start_date": "November 1, 2024",
        "end_date": "November 28, 2024",
        "termination_conditions": "Either party may terminate with written notice.",
        "governing_law": "State of California, USA"
    },
    # End date before start date (invalid contract)
    {
        "contract_date": datetime.strptime("2024-11-10", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "Acme Corp.",
        "provider_address": "999 Acme Blvd, Industrial Park, Country",
        "provider_email": "contact@acmecorp.com",
        "client_name": "Sarah Lee",
        "client_address": "123 Oak St, Citytown, Country",
        "client_email": "sarah.lee@example.com",
        "service_description": "Enterprise software development and support.",
        "payment_amount": "$15000",
        "payment_terms": "25% upfront, 75% upon completion",
        "start_date": "December 15, 2024",
        "end_date": "December 1, 2024",  # Invalid: end date before start date
        "termination_conditions": "30 days' written notice by either party.",
        "governing_law": "Texas, USA"
    },
    # Missing governing law
    {
        "contract_date": datetime.strptime("2024-11-07", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "PQR Digital Marketing",
        "provider_address": "800 Digital St, Tech City, Country",
        "provider_email": "contact@pqrdigital.com",
        "client_name": "Tom Harris",
        "client_address": "250 Main Rd, Cityville, Country",
        "client_email": "tom.harris@example.com",
        "service_description": "Social media marketing and content creation.",
        "payment_amount": "$4000",
        "payment_terms": "50% upfront, 50% upon campaign launch",
        "start_date": "December 1, 2024",
        "end_date": "December 1, 2025",
        "termination_conditions": "Termination possible for breach of contract.",
        "governing_law": ""  # Missing governing law
    },
    # Perfect contract data
    {
        "contract_date": datetime.strptime("2024-09-01", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "Tech Innovations Ltd.",
        "provider_address": "123 Tech Avenue, Silicon Valley, Country",
        "provider_email": "support@techinnovations.com",
        "client_name": "Samuel Parker",
        "client_address": "456 Sunset Blvd, Metro City, Country",
        "client_email": "samuel.parker@example.com",
        "service_description": "Software development and system integration.",
        "payment_amount": "$25000",
        "payment_terms": "50% upfront, 50% upon successful integration",
        "start_date": "October 1, 2024",
        "end_date": "October 1, 2026",
        "termination_conditions": "Either party may terminate with 30 days' notice.",
        "governing_law": "State of California, USA"
    },
    # Contract with missing payment terms
    {
        "contract_date": datetime.strptime("2024-09-15", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "Visionary Technologies",
        "provider_address": "789 Tech Park, Innovate City, Country",
        "provider_email": "contact@visionarytech.com",
        "client_name": "Emily Carter",
        "client_address": "101 Park St, Downtown, Country",
        "client_email": "emily.carter@example.com",
        "service_description": "Custom AI solutions for data analysis.",
        "payment_amount": "$45000",
        "payment_terms": "",
        "start_date": "November 15, 2024",
        "end_date": "November 15, 2026",
        "termination_conditions": "Termination upon mutual agreement.",
        "governing_law": "Ontario, Canada"
    },
    # Expiring contract (less than 30 days)
    {
        "contract_date": datetime.strptime("2024-10-15", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "GreenTech Solutions",
        "provider_address": "400 Green St, Eco City, Country",
        "provider_email": "contact@greentechsolutions.com",
        "client_name": "Laura Briggs",
        "client_address": "310 Oak Blvd, Forest Hill, Country",
        "client_email": "laura.briggs@example.com",
        "service_description": "Sustainability consulting and green energy solutions.",
        "payment_amount": "$12000",
        "payment_terms": "Monthly installments of $2000",
        "start_date": "November 1, 2024",
        "end_date": "November 28, 2024",
        "termination_conditions": "Termination with 14 days' notice if deliverables are not met.",
        "governing_law": "State of New York, USA"
    },
    # Expired contract
    {
        "contract_date": datetime.strptime("2023-09-01", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "Cloud Computing Co.",
        "provider_address": "123 Cloud Rd, Tech City, Country",
        "provider_email": "info@cloudcomputingco.com",
        "client_name": "Michael Roberts",
        "client_address": "505 Maple St, Uptown, Country",
        "client_email": "michael.roberts@example.com",
        "service_description": "Cloud infrastructure setup and management.",
        "payment_amount": "$30000",
        "payment_terms": "50% upfront, 50% upon completion of setup",
        "start_date": "March 1, 2023",
        "end_date": "March 1, 2024",
        "termination_conditions": "Either party can terminate with 30 days' written notice.",
        "governing_law": "Illinois, USA"
    },
    # Invalid contract with end date before start date
    {
        "contract_date": datetime.strptime("2024-09-20", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "NextGen Innovations",
        "provider_address": "800 NextGen Blvd, Silicon Valley, Country",
        "provider_email": "nextgen@nextgeninnovations.com",
        "client_name": "Sarah Johnson",
        "client_address": "12 Broadway St, Hightown, Country",
        "client_email": "sarah.johnson@example.com",
        "service_description": "Product innovation and technology consulting.",
        "payment_amount": "$50000",
        "payment_terms": "Payment upon project milestones completion",
        "start_date": "October 15, 2024",
        "end_date": "October 10, 2024",  # Invalid: end date before start date
        "termination_conditions": "Termination by mutual agreement with 15 days' notice.",
        "governing_law": "California, USA"
    },
    # Missing service provider name
    {
        "contract_date": datetime.strptime("2024-09-25", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "",
        "provider_address": "789 Enterprise Blvd, Silicon Valley, Country",
        "provider_email": "contact@enterprise.com",
        "client_name": "Linda Mitchell",
        "client_address": "98 River Rd, Countrytown, Country",
        "client_email": "linda.mitchell@example.com",
        "service_description": "Big data analytics and machine learning services.",
        "payment_amount": "$25000",
        "payment_terms": "50% upfront, 50% upon delivery",
        "start_date": "November 5, 2024",
        "end_date": "November 5, 2026",
        "termination_conditions": "Either party can terminate with 30 days' notice.",
        "governing_law": "Florida, USA"
    },
    # Expiring soon contract with only start date and no end date
    {
        "contract_date": datetime.strptime("2024-10-10", "%Y-%m-%d").strftime("%B %d, %Y"),
        "service_provider": "Skyline Technologies",
        "provider_address": "400 Sky Rd, Tech Park, Country",
        "provider_email": "contact@skylinetechnologies.com",
        "client_name": "Richard Taylor",
        "client_address": "250 Lakeview Dr, Downtown, Country",
        "client_email": "richard.taylor@example.com",
        "service_description": "Data analysis and machine learning model development.",
        "payment_amount": "$18000",
        "payment_terms": "Full payment upon completion",
        "start_date": "November 20, 2024",
        "end_date": "",  # Missing end date
        "termination_conditions": "Termination upon failure to meet key performance metrics.",
        "governing_law": "Washington, USA"
    }

]
