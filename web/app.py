"""Flask Web Application for Job Search AI Agent"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import logging
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from aggregator import JobAggregator
from state_filter import StateFilter
from spam_detector import SpamDetector
from notification_manager import NotificationManager
from config.indian_states import get_all_states

# Setup Flask
app = Flask(__name__)
CORS(app)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize services
aggregator = JobAggregator()
state_filter = StateFilter()
spam_detector = SpamDetector()
notification_manager = NotificationManager()

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/api/states')
def get_states():
    """Get all Indian states"""
    try:
        states = get_all_states()
        return jsonify({'success': True, 'states': states})
    except Exception as e:
        logger.error(f"Error fetching states: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/jobs')
def get_jobs():
    """Get jobs for selected state"""
    try:
        state = request.args.get('state')
        if not state:
            return jsonify({'success': False, 'error': 'State parameter required'}), 400
            
        # Get all jobs
        all_jobs = aggregator.aggregate_jobs()
        
        # Filter by state
        jobs = state_filter.filter_by_state(all_jobs, state)
        
        # Analyze for spam
        for job in jobs:
            spam_score = spam_detector.analyze(job)
            job['spam_score'] = spam_score
            job['is_spam'] = spam_score > 0.7
            
        return jsonify({
            'success': True,
            'state': state,
            'total_jobs': len(jobs),
            'legitimate_jobs': len([j for j in jobs if not j.get('is_spam')]),
            'spam_jobs': len([j for j in jobs if j.get('is_spam')]),
            'jobs': jobs
        })
    except Exception as e:
        logger.error(f"Error fetching jobs: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/companies')
def get_companies():
    """Get companies hiring in a state"""
    try:
        state = request.args.get('state')
        if not state:
            return jsonify({'success': False, 'error': 'State parameter required'}), 400
            
        # Get all jobs
        all_jobs = aggregator.aggregate_jobs()
        
        # Get companies by state
        companies = state_filter.get_companies_by_state(all_jobs, state)
        
        return jsonify({
            'success': True,
            'state': state,
            'companies': companies
        })
    except Exception as e:
        logger.error(f"Error fetching companies: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    """Subscribe to job notifications"""
    try:
        data = request.json
        
        subscription = {
            'email': data.get('email'),
            'state': data.get('state'),
            'frequency': data.get('frequency', 'daily')
        }
        
        if notification_manager.add_subscription(subscription):
            return jsonify({'success': True, 'message': 'Subscribed successfully'})
        else:
            return jsonify({'success': False, 'error': 'Failed to subscribe'}), 500
    except Exception as e:
        logger.error(f"Error subscribing: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/job/<job_id>')
def get_job_details(job_id):
    """Get detailed information about a job"""
    try:
        all_jobs = aggregator.aggregate_jobs()
        
        for job in all_jobs:
            if job.get('id') == job_id:
                # Analyze for spam
                spam_score = spam_detector.analyze(job)
                job['spam_score'] = spam_score
                job['spam_reasons'] = spam_detector.get_spam_reasons(job)
                
                return jsonify({'success': True, 'job': job})
                
        return jsonify({'success': False, 'error': 'Job not found'}), 404
    except Exception as e:
        logger.error(f"Error fetching job details: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'success': False, 'error': 'Internal server error'}), 500

if __name__ == '__main__':
    logger.info("Starting Job Search AI Agent Web Server")
    app.run(debug=True, host='0.0.0.0', port=5000)
