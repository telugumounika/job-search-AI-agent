import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Base Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / 'data'
LOGS_DIR = BASE_DIR / 'logs'

# Create directories if they don't exist
DATABASE_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# API Keys
LINKEDIN_EMAIL = os.getenv('LINKEDIN_EMAIL')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')
INDEED_API_KEY = os.getenv('INDEED_API_KEY')
NAUKRI_API_KEY = os.getenv('NAUKRI_API_KEY')
ANGELLIST_API_KEY = os.getenv('ANGELLIST_API_KEY')

# Database Paths
JOBS_DATABASE = os.getenv('DB_PATH', str(DATABASE_DIR / 'jobs_database.json'))
NOTIFICATION_DB = os.getenv('NOTIFICATION_DB', str(DATABASE_DIR / 'notifications.json'))
SPAM_LIST_DB = os.getenv('SPAM_LIST_DB', str(DATABASE_DIR / 'spam_list.json'))

# Email Configuration
NOTIFICATION_EMAIL = os.getenv('NOTIFICATION_EMAIL')
NOTIFICATION_EMAIL_PASSWORD = os.getenv('NOTIFICATION_EMAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))

# Application Settings
DEBUG = os.getenv('DEBUG', 'False') == 'True'
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Scraping Configuration
REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', 10))
RETRY_ATTEMPTS = int(os.getenv('RETRY_ATTEMPTS', 3))
RETRY_DELAY = int(os.getenv('RETRY_DELAY', 5))

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', str(LOGS_DIR / 'app.log'))

# Job Aggregation Settings
JOB_CACHE_DURATION = 3600  # 1 hour
MAX_JOBS_PER_SOURCE = 500
SPAM_THRESHOLD = 0.7  # Confidence threshold for spam detection

# User Preferences
DEFAULT_STATE = 'Karnataka'
DEFAULT_NOTIFICATION_FREQUENCY = 'daily'  # daily, weekly, real-time
