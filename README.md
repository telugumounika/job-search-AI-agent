# Job Search AI Agent

An intelligent AI-powered job search tool that aggregates job postings from multiple sources across India, analyzes them, and provides smart filtering by location with spam detection.

## Features

✅ **Multi-Source Job Aggregation**
- Indian Companies (Startups & MNCs)
- LinkedIn Jobs
- Indeed
- Naukri
- AngelList (Startups)
- Custom company career pages

✅ **State-Based Filtering**
- Filter jobs by Indian states (Andhra Pradesh, Karnataka, Tamil Nadu, etc.)
- View all companies hiring in your preferred location
- See job roles and descriptions

✅ **Spam Detection**
- AI-powered verification of job postings
- Automatic flagging of suspicious postings
- Company legitimacy checking

✅ **Job Notifications**
- Real-time job notifications
- Store notification history
- Email alerts for new postings
- Customizable notification preferences

✅ **User-Friendly Interface**
- Interactive CLI and Web Dashboard
- Easy state selection
- Direct job links
- Company details and hiring trends

## Project Structure

```
job-search-AI-agent/
├── README.md
├── requirements.txt
├── .env.example
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── indian_states.py
│   └── company_database.py
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── aggregator.py
│   ├── spam_detector.py
│   ├── notification_manager.py
│   ├── state_filter.py
│   └── database/
│       ├── __init__.py
│       ├── db_manager.py
│       └── models.py
├── scrapers/
│   ├── __init__.py
│   ├── base_scraper.py
│   ├── linkedin_scraper.py
│   ├── indeed_scraper.py
│   ├── naukri_scraper.py
│   ├── angellist_scraper.py
│   └── company_scraper.py
├── web/
│   ├── __init__.py
│   ├── app.py
│   ├── routes.py
│   └── templates/
│       ├── index.html
│       ├── jobs.html
│       ├── notifications.html
│       └── base.html
├── tests/
│   ├── __init__.py
│   ├── test_aggregator.py
│   ├── test_spam_detector.py
│   └── test_state_filter.py
└── data/
    ├── jobs_database.json
    ├── notifications.json
    └── spam_list.json
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/telugumounika/job-search-AI-agent.git
cd job-search-AI-agent
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Setup environment variables
```bash
cp .env.example .env
# Edit .env with your API keys
```

## Usage

### CLI Mode
```bash
python src/main.py
```

This will launch an interactive menu:
1. Select your preferred state
2. View all hiring companies
3. Browse job postings
4. Check notifications
5. View spam flagged jobs

### Web Dashboard
```bash
python web/app.py
```

Access at `http://localhost:5000`

## Environment Variables

Create a `.env` file:
```
LINKEDIN_EMAIL=your_email@gmail.com
LINKEDIN_PASSWORD=your_password
INDEED_API_KEY=your_api_key
NAUKRI_API_KEY=your_api_key
ANGELLIST_API_KEY=your_api_key
DB_PATH=data/jobs_database.json
NOTIFICATION_EMAIL=your_email@gmail.com
```

## API Reference

### Aggregator
Gathers jobs from multiple sources

### Spam Detector
Verifies job authenticity using ML models

### State Filter
Filters jobs by Indian states

### Notification Manager
Handles job alerts and notifications

## Supported Indian States
- Andhra Pradesh
- Arunachal Pradesh
- Assam
- Bihar
- Chhattisgarh
- Delhi
- Goa
- Gujarat
- Haryana
- Himachal Pradesh
- Jharkhand
- Karnataka
- Kerala
- Madhya Pradesh
- Maharashtra
- Manipur
- Meghalaya
- Mizoram
- Nagaland
- Odisha
- Punjab
- Rajasthan
- Sikkim
- Tamil Nadu
- Telangana
- Tripura
- Uttar Pradesh
- Uttarakhand
- West Bengal

## Contributing
Contributions welcome! Please create a pull request with your improvements.

## License
MIT License

## Support
For issues or questions, create an issue in the GitHub repository.
