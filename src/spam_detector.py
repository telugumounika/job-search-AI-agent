"""Spam Detector - Identifies suspicious job postings"""

import logging
import re
from typing import Dict
from config.company_database import SPAM_INDICATORS, VERIFIED_DOMAINS

logger = logging.getLogger(__name__)

class SpamDetector:
    """Detects spam and suspicious job postings"""
    
    def __init__(self):
        self.spam_indicators = SPAM_INDICATORS
        self.verified_domains = VERIFIED_DOMAINS
        
    def analyze(self, job: Dict) -> float:
        """Analyze job posting and return spam score (0-1)"""
        score = 0.0
        
        # Check for spam indicators in description
        score += self._check_spam_indicators(job.get('description', ''))
        
        # Check for spam indicators in title
        score += self._check_spam_indicators(job.get('title', '')) * 0.5
        
        # Check company verification
        score += self._check_company_verification(job.get('company', ''))
        
        # Check URL validity
        score += self._check_url_validity(job.get('url', ''))
        
        # Check salary suspicion
        score += self._check_salary_suspicion(job.get('salary', ''))
        
        # Check job type suspicion
        score += self._check_job_type(job.get('job_type', ''))
        
        # Normalize score to 0-1
        return min(score / 5.0, 1.0)
        
    def _check_spam_indicators(self, text: str) -> float:
        """Check for known spam indicators in text"""
        score = 0.0
        text_lower = text.lower()
        
        for indicator in self.spam_indicators:
            if indicator in text_lower:
                score += 0.2
                
        return min(score, 1.0)
        
    def _check_company_verification(self, company_name: str) -> float:
        """Check if company is verified"""
        # Extract domain from company info
        # If company is known and verified, return low score
        # Otherwise return higher score
        
        verified_companies = [
            'google', 'microsoft', 'amazon', 'apple', 'meta',
            'tcs', 'infosys', 'wipro', 'accenture',
            'linkedin', 'github', 'ibm', 'oracle'
        ]
        
        if company_name.lower() in verified_companies:
            return 0.0
        return 0.1
        
    def _check_url_validity(self, url: str) -> float:
        """Check if URL looks suspicious"""
        if not url:
            return 0.3
            
        # Check for suspicious URL patterns
        suspicious_patterns = [
            r'bit\.ly',
            r'tinyurl',
            r'short\.link',
            r'job-money',
            r'earn-now',
            r'work-from-home',
        ]
        
        for pattern in suspicious_patterns:
            if re.search(pattern, url, re.IGNORECASE):
                return 0.4
                
        # Check for HTTPS
        if 'https://' not in url:
            return 0.2
            
        return 0.0
        
    def _check_salary_suspicion(self, salary: str) -> float:
        """Check if salary seems suspicious"""
        if not salary:
            return 0.1
            
        salary_lower = salary.lower()
        
        # Check for extremely high salaries
        if any(keyword in salary_lower for keyword in ['unlimited', 'negotiable', 'crore']):
            return 0.2
            
        return 0.0
        
    def _check_job_type(self, job_type: str) -> float:
        """Check job type for suspicion"""
        suspicious_types = ['work from home', 'part time', 'freelance', 'temporary']
        
        if not job_type:
            return 0.0
            
        for suspicious_type in suspicious_types:
            if suspicious_type.lower() in job_type.lower():
                return 0.1
                
        return 0.0
        
    def get_spam_reasons(self, job: Dict) -> list:
        """Get detailed reasons why a job might be spam"""
        reasons = []
        
        # Check spam indicators
        for indicator in self.spam_indicators:
            if indicator.lower() in job.get('description', '').lower():
                reasons.append(f"Spam indicator detected: '{indicator}'")
                
        # Check company
        if not self._is_verified_company(job.get('company', '')):
            reasons.append("Company not in verified database")
            
        # Check URL
        if not job.get('url'):
            reasons.append("No job URL provided")
        elif 'https://' not in job.get('url', ''):
            reasons.append("URL is not HTTPS")
            
        return reasons
        
    def _is_verified_company(self, company: str) -> bool:
        """Check if company is verified"""
        verified_companies = [
            'google', 'microsoft', 'amazon', 'apple', 'meta',
            'tcs', 'infosys', 'wipro', 'accenture',
        ]
        return company.lower() in verified_companies
