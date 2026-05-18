"""State Filter - Filters jobs by Indian state"""

import logging
from typing import List, Dict
from config.indian_states import get_all_states, get_state_by_name

logger = logging.getLogger(__name__)

class StateFilter:
    """Filters job postings by Indian state"""
    
    def __init__(self):
        self.states = get_all_states()
        
    def filter_by_state(self, jobs: List[Dict], state_name: str) -> List[Dict]:
        """Filter jobs by state name"""
        state_info = get_state_by_name(state_name)
        if not state_info:
            logger.warning(f"State not found: {state_name}")
            return []
            
        major_cities = state_info['major_cities']
        filtered_jobs = []
        
        for job in jobs:
            if self._matches_state(job, state_name, major_cities):
                filtered_jobs.append(job)
                
        logger.info(f"Filtered {len(filtered_jobs)} jobs for {state_name}")
        return filtered_jobs
        
    def _matches_state(self, job: Dict, state_name: str, cities: List[str]) -> bool:
        """Check if job matches the state"""
        location = job.get('location', '').lower()
        state_lower = state_name.lower()
        
        # Check by state name
        if state_lower in location:
            return True
            
        # Check by major cities
        for city in cities:
            if city.lower() in location:
                return True
                
        # Check by state code
        state_info = get_state_by_name(state_name)
        if state_info and state_info['code'].lower() in location:
            return True
            
        return False
        
    def get_all_states(self) -> List[str]:
        """Get all available states"""
        return self.states
        
    def get_companies_by_state(self, jobs: List[Dict], state_name: str) -> Dict[str, List[str]]:
        """Get unique companies and their roles in a state"""
        filtered_jobs = self.filter_by_state(jobs, state_name)
        
        companies = {}
        for job in filtered_jobs:
            company = job.get('company', 'Unknown')
            role = job.get('title', 'N/A')
            
            if company not in companies:
                companies[company] = []
            if role not in companies[company]:
                companies[company].append(role)
                
        return companies
