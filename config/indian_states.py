INDIAN_STATES = {
    'andhra_pradesh': {
        'name': 'Andhra Pradesh',
        'code': 'AP',
        'major_cities': ['Hyderabad', 'Visakhapatnam', 'Vijayawada', 'Guntur'],
        'tech_hubs': ['Hyderabad']
    },
    'arunachal_pradesh': {
        'name': 'Arunachal Pradesh',
        'code': 'AR',
        'major_cities': ['Itanagar', 'Naharlagun'],
        'tech_hubs': []
    },
    'assam': {
        'name': 'Assam',
        'code': 'AS',
        'major_cities': ['Guwahati', 'Dibrugarh'],
        'tech_hubs': ['Guwahati']
    },
    'bihar': {
        'name': 'Bihar',
        'code': 'BR',
        'major_cities': ['Patna', 'Gaya', 'Darbhanga'],
        'tech_hubs': ['Patna']
    },
    'chhattisgarh': {
        'name': 'Chhattisgarh',
        'code': 'CG',
        'major_cities': ['Raipur', 'Bhilai', 'Durg'],
        'tech_hubs': ['Raipur']
    },
    'delhi': {
        'name': 'Delhi',
        'code': 'DL',
        'major_cities': ['New Delhi', 'Delhi', 'Gurugram', 'Noida'],
        'tech_hubs': ['New Delhi', 'Gurugram', 'Noida']
    },
    'goa': {
        'name': 'Goa',
        'code': 'GA',
        'major_cities': ['Panaji', 'Margao'],
        'tech_hubs': []
    },
    'gujarat': {
        'name': 'Gujarat',
        'code': 'GJ',
        'major_cities': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot'],
        'tech_hubs': ['Ahmedabad']
    },
    'haryana': {
        'name': 'Haryana',
        'code': 'HR',
        'major_cities': ['Gurugram', 'Faridabad', 'Hisar'],
        'tech_hubs': ['Gurugram']
    },
    'himachal_pradesh': {
        'name': 'Himachal Pradesh',
        'code': 'HP',
        'major_cities': ['Shimla', 'Solan'],
        'tech_hubs': []
    },
    'jharkhand': {
        'name': 'Jharkhand',
        'code': 'JH',
        'major_cities': ['Ranchi', 'Jamshedpur', 'Dhanbad'],
        'tech_hubs': ['Ranchi']
    },
    'karnataka': {
        'name': 'Karnataka',
        'code': 'KA',
        'major_cities': ['Bangalore', 'Mangalore', 'Belgaum', 'Mysore'],
        'tech_hubs': ['Bangalore']
    },
    'kerala': {
        'name': 'Kerala',
        'code': 'KL',
        'major_cities': ['Kochi', 'Thiruvananthapuram', 'Kozhikode'],
        'tech_hubs': ['Kochi']
    },
    'madhya_pradesh': {
        'name': 'Madhya Pradesh',
        'code': 'MP',
        'major_cities': ['Indore', 'Bhopal', 'Gwalior'],
        'tech_hubs': ['Indore']
    },
    'maharashtra': {
        'name': 'Maharashtra',
        'code': 'MH',
        'major_cities': ['Mumbai', 'Pune', 'Nagpur', 'Nashik'],
        'tech_hubs': ['Mumbai', 'Pune']
    },
    'manipur': {
        'name': 'Manipur',
        'code': 'MN',
        'major_cities': ['Imphal'],
        'tech_hubs': []
    },
    'meghalaya': {
        'name': 'Meghalaya',
        'code': 'ML',
        'major_cities': ['Shillong'],
        'tech_hubs': []
    },
    'mizoram': {
        'name': 'Mizoram',
        'code': 'MZ',
        'major_cities': ['Aizawl'],
        'tech_hubs': []
    },
    'nagaland': {
        'name': 'Nagaland',
        'code': 'NL',
        'major_cities': ['Kohima', 'Dimapur'],
        'tech_hubs': []
    },
    'odisha': {
        'name': 'Odisha',
        'code': 'OD',
        'major_cities': ['Bhubaneswar', 'Cuttack'],
        'tech_hubs': ['Bhubaneswar']
    },
    'punjab': {
        'name': 'Punjab',
        'code': 'PB',
        'major_cities': ['Chandigarh', 'Ludhiana', 'Amritsar'],
        'tech_hubs': ['Chandigarh']
    },
    'rajasthan': {
        'name': 'Rajasthan',
        'code': 'RJ',
        'major_cities': ['Jaipur', 'Udaipur', 'Jodhpur'],
        'tech_hubs': ['Jaipur']
    },
    'sikkim': {
        'name': 'Sikkim',
        'code': 'SK',
        'major_cities': ['Gangtok'],
        'tech_hubs': []
    },
    'tamil_nadu': {
        'name': 'Tamil Nadu',
        'code': 'TN',
        'major_cities': ['Chennai', 'Coimbatore', 'Salem', 'Madurai'],
        'tech_hubs': ['Chennai']
    },
    'telangana': {
        'name': 'Telangana',
        'code': 'TG',
        'major_cities': ['Hyderabad', 'Secunderabad'],
        'tech_hubs': ['Hyderabad']
    },
    'tripura': {
        'name': 'Tripura',
        'code': 'TR',
        'major_cities': ['Agartala'],
        'tech_hubs': []
    },
    'uttar_pradesh': {
        'name': 'Uttar Pradesh',
        'code': 'UP',
        'major_cities': ['Noida', 'Greater Noida', 'Lucknow', 'Kanpur'],
        'tech_hubs': ['Noida']
    },
    'uttarakhand': {
        'name': 'Uttarakhand',
        'code': 'UT',
        'major_cities': ['Dehradun'],
        'tech_hubs': []
    },
    'west_bengal': {
        'name': 'West Bengal',
        'code': 'WB',
        'major_cities': ['Kolkata', 'Darjeeling'],
        'tech_hubs': ['Kolkata']
    }
}

def get_state_by_name(state_name):
    """Get state information by name"""
    for key, value in INDIAN_STATES.items():
        if value['name'].lower() == state_name.lower():
            return value
    return None

def get_all_states():
    """Get all states"""
    return [value['name'] for value in INDIAN_STATES.values()]

def get_tech_hubs():
    """Get all tech hubs in India"""
    hubs = set()
    for state in INDIAN_STATES.values():
        hubs.update(state['tech_hubs'])
    return sorted(list(hubs))
