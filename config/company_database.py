# Major Indian and MNC Companies Database
COMPANIES = {
    # Tech Giants
    'tcs': {'name': 'Tata Consultancy Services', 'type': 'MNC', 'hq': 'Hyderabad'},
    'infosys': {'name': 'Infosys', 'type': 'MNC', 'hq': 'Bangalore'},
    'wipro': {'name': 'Wipro', 'type': 'MNC', 'hq': 'Bangalore'},
    'cognizant': {'name': 'Cognizant', 'type': 'MNC', 'hq': 'Pune'},
    'accenture': {'name': 'Accenture', 'type': 'MNC', 'hq': 'Bangalore'},
    'deloitte': {'name': 'Deloitte', 'type': 'MNC', 'hq': 'Bangalore'},
    'ibm': {'name': 'IBM', 'type': 'MNC', 'hq': 'Bangalore'},
    'microsoft': {'name': 'Microsoft', 'type': 'MNC', 'hq': 'Bangalore'},
    'google': {'name': 'Google', 'type': 'MNC', 'hq': 'Bangalore'},
    'amazon': {'name': 'Amazon', 'type': 'MNC', 'hq': 'Bangalore'},
    'apple': {'name': 'Apple', 'type': 'MNC', 'hq': 'Bangalore'},
    'meta': {'name': 'Meta', 'type': 'MNC', 'hq': 'Pune'},
    'cisco': {'name': 'Cisco', 'type': 'MNC', 'hq': 'Bangalore'},
    'oracle': {'name': 'Oracle', 'type': 'MNC', 'hq': 'Bangalore'},
    'salesforce': {'name': 'Salesforce', 'type': 'MNC', 'hq': 'Hyderabad'},
    
    # Indian IT Companies
    'hcl': {'name': 'HCL Technologies', 'type': 'Indian', 'hq': 'Noida'},
    'mindtree': {'name': 'Mindtree', 'type': 'Indian', 'hq': 'Bangalore'},
    'tech_mahindra': {'name': 'Tech Mahindra', 'type': 'Indian', 'hq': 'Pune'},
    'mphasis': {'name': 'Mphasis', 'type': 'Indian', 'hq': 'Bangalore'},
    'everestech': {'name': 'Everestech', 'type': 'Indian', 'hq': 'Bangalore'},
    
    # E-commerce & Startups
    'flipkart': {'name': 'Flipkart', 'type': 'Startup', 'hq': 'Bangalore'},
    'swiggy': {'name': 'Swiggy', 'type': 'Startup', 'hq': 'Bangalore'},
    'oyo': {'name': 'OYO', 'type': 'Startup', 'hq': 'Gurugram'},
    'byju': {'name': 'BYJU\'S', 'type': 'Startup', 'hq': 'Bangalore'},
    'razorpay': {'name': 'Razorpay', 'type': 'Startup', 'hq': 'Bangalore'},
    'delhivery': {'name': 'Delhivery', 'type': 'Startup', 'hq': 'Gurugram'},
    'zomato': {'name': 'Zomato', 'type': 'Startup', 'hq': 'Gurugram'},
    'unacademy': {'name': 'Unacademy', 'type': 'Startup', 'hq': 'Bangalore'},
    'paytm': {'name': 'Paytm', 'type': 'Startup', 'hq': 'Gurugram'},
    'ola': {'name': 'Ola', 'type': 'Startup', 'hq': 'Bangalore'},
    'udaan': {'name': 'Udaan', 'type': 'Startup', 'hq': 'Bangalore'},
    'cred': {'name': 'CRED', 'type': 'Startup', 'hq': 'Bangalore'},
    'nykaa': {'name': 'Nykaa', 'type': 'Startup', 'hq': 'Mumbai'},
    'dream11': {'name': 'Dream11', 'type': 'Startup', 'hq': 'Mumbai'},
    'moj': {'name': 'Moj', 'type': 'Startup', 'hq': 'Bangalore'},
}

SPAM_INDICATORS = [
    'work from home guaranteed',
    'earn money instantly',
    'no experience needed',
    'guaranteed income',
    'work part time',
    'easy money',
    'money back guarantee',
    'risk free',
    'limited time offer',
    'act now',
    'too good to be true',
]

VERIFIED_DOMAINS = {
    'google.com',
    'microsoft.com',
    'amazon.com',
    'apple.com',
    'meta.com',
    'ibm.com',
    'oracle.com',
    'cisco.com',
    'salesforce.com',
    'tcs.com',
    'infosys.com',
    'wipro.com',
    'cognizant.com',
    'accenture.com',
    'hcltech.com',
    'flipkart.com',
    'amazon.in',
    'linkedin.com',
    'naukri.com',
    'indeed.com',
}

def get_company_info(company_name):
    """Get company information"""
    key = company_name.lower().replace(' ', '_')
    return COMPANIES.get(key, None)

def get_all_companies():
    """Get all companies"""
    return COMPANIES

def is_verified_domain(domain):
    """Check if domain is verified"""
    return domain in VERIFIED_DOMAINS
