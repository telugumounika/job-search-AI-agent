"""Job Aggregator - Fetches jobs from multiple sources"""

import logging
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict
import requests
from config.settings import JOBS_DATABASE, JOB_CACHE_DURATION

logger = logging.getLogger(__name__)

class JobAggregator:
    """Aggregates job postings from multiple sources"""
    
    def __init__(self):
        self.db_path = Path(JOBS_DATABASE)
        self.cache_time = JOB_CACHE_DURATION
        self.last_update = None
        self.jobs_cache = []
        
    def aggregate_jobs(self) -> List[Dict]:
        """Aggregate jobs from all sources"""
        try:
            # Check if cache is still valid
            if self._is_cache_valid():
                logger.info("Using cached jobs")
                return self.jobs_cache
                
            jobs = []
            
            # Fetch from different sources
            logger.info("Aggregating jobs from multiple sources...")
            
            jobs.extend(self._fetch_linkedin_jobs())
            jobs.extend(self._fetch_indeed_jobs())
            jobs.extend(self._fetch_naukri_jobs())
            jobs.extend(self._fetch_angellist_jobs())
            jobs.extend(self._fetch_company_career_pages())
            
            # Remove duplicates
            jobs = self._remove_duplicates(jobs)
            
            # Update cache
            self.jobs_cache = jobs
            self.last_update = datetime.now()
            
            # Save to database
            self._save_to_db(jobs)
            
            logger.info(f"Aggregated {len(jobs)} jobs")
            return jobs
            
        except Exception as e:
            logger.error(f"Error aggregating jobs: {str(e)}")
            # Try to load from database if aggregation fails
            return self._load_from_db()
            
    def _is_cache_valid(self) -> bool:
        """Check if cache is still valid"""
        if self.last_update is None:
            return False
        return (datetime.now() - self.last_update).seconds < self.cache_time
        
    def _fetch_linkedin_jobs(self) -> List[Dict]:
        """Fetch jobs from LinkedIn"""
        try:
            logger.info("Fetching from LinkedIn...")
            # LinkedIn scraper would be implemented here
            # For now, returning mock data
            return self._get_mock_linkedin_jobs()
        except Exception as e:
            logger.error(f"Error fetching LinkedIn jobs: {str(e)}")
            return []
            
    def _fetch_indeed_jobs(self) -> List[Dict]:
        """Fetch jobs from Indeed"""
        try:
            logger.info("Fetching from Indeed...")
            return self._get_mock_indeed_jobs()
        except Exception as e:
            logger.error(f"Error fetching Indeed jobs: {str(e)}")
            return []
            
    def _fetch_naukri_jobs(self) -> List[Dict]:
        """Fetch jobs from Naukri"""
        try:
            logger.info("Fetching from Naukri...")
            return self._get_mock_naukri_jobs()
        except Exception as e:
            logger.error(f"Error fetching Naukri jobs: {str(e)}")
            return []
            
    def _fetch_angellist_jobs(self) -> List[Dict]:
        """Fetch jobs from AngelList (startups)"""
        try:
            logger.info("Fetching from AngelList...")
            return self._get_mock_angellist_jobs()
        except Exception as e:
            logger.error(f"Error fetching AngelList jobs: {str(e)}")
            return []
            
    def _fetch_company_career_pages(self) -> List[Dict]:
        """Fetch jobs from company career pages"""
        try:
            logger.info("Fetching from company career pages...")
            return self._get_mock_company_jobs()
        except Exception as e:
            logger.error(f"Error fetching company jobs: {str(e)}")
            return []
            
    def _remove_duplicates(self, jobs: List[Dict]) -> List[Dict]:
        """Remove duplicate job postings"""
        seen = set()
        unique_jobs = []
        
        for job in jobs:
            key = (job.get('title'), job.get('company'), job.get('location'))
            if key not in seen:
                seen.add(key)
                unique_jobs.append(job)
                
        return unique_jobs
        
    def _save_to_db(self, jobs: List[Dict]):
        """Save jobs to database"""
        try:
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.db_path, 'w') as f:
                json.dump(jobs, f, indent=2, default=str)
            logger.info(f"Saved {len(jobs)} jobs to database")
        except Exception as e:
            logger.error(f"Error saving to database: {str(e)}")
            
    def _load_from_db(self) -> List[Dict]:
        """Load jobs from database"""
        try:
            if self.db_path.exists():
                with open(self.db_path, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Error loading from database: {str(e)}")
        return []
        
    # Mock data methods for demonstration
    def _get_mock_linkedin_jobs(self) -> List[Dict]:
        """Get mock LinkedIn jobs"""
        return [
            {
                'id': 'linkedin_1',
                'company': 'Google',
                'title': 'Software Engineer',
                'location': 'Bangalore, Karnataka',
                'state': 'Karnataka',
                'salary': '₹10,00,000 - ₹20,00,000',
                'experience': '2-4 years',
                'job_type': 'Full-time',
                'description': 'We are looking for experienced software engineers to join our team.',
                'posted_date': datetime.now().isoformat(),
                'url': 'https://linkedin.com/jobs/...',
                'source': 'LinkedIn'
            },
            {
                'id': 'linkedin_2',
                'company': 'Microsoft',
                'title': 'Cloud Solutions Architect',
                'location': 'Hyderabad, Telangana',
                'state': 'Telangana',
                'salary': '₹15,00,000 - ₹25,00,000',
                'experience': '5-7 years',
                'job_type': 'Full-time',
                'description': 'Design and implement cloud solutions for enterprise clients.',
                'posted_date': datetime.now().isoformat(),
                'url': 'https://linkedin.com/jobs/...',
                'source': 'LinkedIn'
            }
        ]
        
    def _get_mock_indeed_jobs(self) -> List[Dict]:
        """Get mock Indeed jobs"""
        return [
            {
                'id': 'indeed_1',
                'company': 'Amazon',
                'title': 'Data Scientist',
                'location': 'Bangalore, Karnataka',
                'state': 'Karnataka',
                'salary': '₹12,00,000 - ₹18,00,000',
                'experience': '3-5 years',
                'job_type': 'Full-time',
                'description': 'Analyze large datasets and build ML models.',
                'posted_date': datetime.now().isoformat(),
                'url': 'https://indeed.com/jobs/...',
                'source': 'Indeed'
            }
        ]
        
    def _get_mock_naukri_jobs(self) -> List[Dict]:
        """Get mock Naukri jobs"""
        return [
            {
                'id': 'naukri_1',
                'company': 'TCS',
                'title': 'Senior Software Developer',
                'location': 'Pune, Maharashtra',
                'state': 'Maharashtra',
                'salary': '₹8,00,000 - ₹12,00,000',
                'experience': '4-6 years',
                'job_type': 'Full-time',
                'description': 'Lead development of enterprise applications.',
                'posted_date': datetime.now().isoformat(),
                'url': 'https://naukri.com/jobs/...',
                'source': 'Naukri'
            }
        ]
        
    def _get_mock_angellist_jobs(self) -> List[Dict]:
        """Get mock AngelList jobs"""
        return [
            {
                'id': 'angellist_1',
                'company': 'Razorpay',
                'title': 'Backend Engineer',
                'location': 'Bangalore, Karnataka',
                'state': 'Karnataka',
                'salary': '₹10,00,000 - ₹16,00,000',
                'experience': '2-4 years',
                'job_type': 'Full-time',
                'description': 'Build scalable backend systems for fintech.',
                'posted_date': datetime.now().isoformat(),
                'url': 'https://angellist.com/jobs/...',
                'source': 'AngelList'
            }
        ]
        
    def _get_mock_company_jobs(self) -> List[Dict]:
        """Get mock company career page jobs"""
        return [
            {
                'id': 'company_1',
                'company': 'Infosys',
                'title': 'IT Consultant',
                'location': 'Chennai, Tamil Nadu',
                'state': 'Tamil Nadu',
                'salary': '₹6,00,000 - ₹10,00,000',
                'experience': '1-3 years',
                'job_type': 'Full-time',
                'description': 'Provide IT consulting services to clients.',
                'posted_date': datetime.now().isoformat(),
                'url': 'https://infosys.com/careers/...',
                'source': 'Infosys'
            }
        ]
