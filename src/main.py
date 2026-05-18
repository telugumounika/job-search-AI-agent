#!/usr/bin/env python3
"""
Main entry point for Job Search AI Agent
"""

import sys
import logging
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.align import Align

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from aggregator import JobAggregator
from state_filter import StateFilter
from spam_detector import SpamDetector
from notification_manager import NotificationManager

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
console = Console()

class JobSearchAgent:
    def __init__(self):
        self.aggregator = JobAggregator()
        self.state_filter = StateFilter()
        self.spam_detector = SpamDetector()
        self.notification_manager = NotificationManager()
        self.jobs = []
        self.selected_state = None
        
    def display_welcome(self):
        """Display welcome screen"""
        welcome_text = """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║         🚀 JOB SEARCH AI AGENT - INDIA 🚀                ║
║                                                            ║
║    Intelligent Job Search & Analysis Platform              ║
║    Search Jobs by State • Detect Spam • Get Alerts        ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """
        console.print(Panel(welcome_text, style="bold blue"))
        
    def select_state(self):
        """Interactive state selection"""
        states = self.state_filter.get_all_states()
        console.print("\n[bold cyan]Available States:[/bold cyan]")
        
        for idx, state in enumerate(states, 1):
            console.print(f"{idx}. {state}")
            
        while True:
            try:
                choice = Prompt.ask("\nSelect state (enter number or name)")
                
                # Try to parse as number
                if choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(states):
                        self.selected_state = states[idx]
                        break
                else:
                    # Try to match by name
                    matching_states = [s for s in states if choice.lower() in s.lower()]
                    if matching_states:
                        self.selected_state = matching_states[0]
                        break
                        
                console.print("[bold red]Invalid selection. Please try again.[/bold red]")
            except KeyboardInterrupt:
                console.print("\n[yellow]Operation cancelled[/yellow]")
                sys.exit(0)
                
    def fetch_jobs(self):
        """Fetch jobs for selected state"""
        console.print(f"\n[bold cyan]Fetching jobs for {self.selected_state}...[/bold cyan]")
        
        # Get all jobs
        all_jobs = self.aggregator.aggregate_jobs()
        
        # Filter by state
        self.jobs = self.state_filter.filter_by_state(all_jobs, self.selected_state)
        
        # Detect spam
        for job in self.jobs:
            spam_score = self.spam_detector.analyze(job)
            job['spam_score'] = spam_score
            job['is_spam'] = spam_score > 0.7
            
        console.print(f"[green]✓ Found {len(self.jobs)} jobs[/green]")
        
    def display_jobs(self):
        """Display jobs in a formatted table"""
        if not self.jobs:
            console.print("[yellow]No jobs found for this state[/yellow]")
            return
            
        # Separate spam and legitimate jobs
        legitimate_jobs = [j for j in self.jobs if not j.get('is_spam', False)]
        spam_jobs = [j for j in self.jobs if j.get('is_spam', False)]
        
        # Display legitimate jobs
        if legitimate_jobs:
            console.print("\n[bold green]✓ Legitimate Job Postings[/bold green]\n")
            table = Table(title=f"Jobs in {self.selected_state}")
            table.add_column("Company", style="cyan")
            table.add_column("Role", style="magenta")
            table.add_column("Location", style="green")
            table.add_column("Experience", style="yellow")
            table.add_column("Salary", style="blue")
            
            for idx, job in enumerate(legitimate_jobs, 1):
                table.add_row(
                    job.get('company', 'N/A'),
                    job.get('title', 'N/A'),
                    job.get('location', 'N/A'),
                    job.get('experience', 'N/A'),
                    job.get('salary', 'N/A')
                )
                
            console.print(table)
            
        # Display spam jobs with warning
        if spam_jobs:
            console.print("\n[bold red]⚠️  SPAM/SUSPICIOUS JOB POSTINGS[/bold red]\n")
            for idx, job in enumerate(spam_jobs, 1):
                console.print(
                    f"[red]⚠️  [{idx}] {job.get('company', 'Unknown')} - "
                    f"{job.get('title', 'N/A')} "
                    f"(Spam Score: {job.get('spam_score', 0):.2f})[/red]"
                )
                
    def display_companies(self):
        """Display unique companies hiring in selected state"""
        if not self.jobs:
            console.print("[yellow]No jobs found[/yellow]")
            return
            
        companies = {}
        for job in self.jobs:
            if not job.get('is_spam', False):
                company = job.get('company', 'Unknown')
                if company not in companies:
                    companies[company] = []
                companies[company].append(job.get('title', 'N/A'))
                
        console.print(f"\n[bold cyan]Companies Hiring in {self.selected_state}:[/bold cyan]\n")
        
        for idx, (company, roles) in enumerate(companies.items(), 1):
            console.print(f"[bold green]{idx}. {company}[/bold green]")
            for role in set(roles):
                console.print(f"   • {role}")
            console.print()
            
    def view_job_details(self):
        """View details of a specific job"""
        if not self.jobs:
            return
            
        legitimate_jobs = [j for j in self.jobs if not j.get('is_spam', False)]
        
        if not legitimate_jobs:
            console.print("[yellow]No legitimate jobs to view[/yellow]")
            return
            
        console.print("\n[bold cyan]Available Jobs:[/bold cyan]")
        for idx, job in enumerate(legitimate_jobs, 1):
            console.print(
                f"{idx}. {job.get('company')} - {job.get('title')} "
                f"({job.get('location')})"
            )
            
        try:
            choice = int(Prompt.ask("Select job number to view details")) - 1
            if 0 <= choice < len(legitimate_jobs):
                job = legitimate_jobs[choice]
                self._display_job_panel(job)
        except (ValueError, IndexError):
            console.print("[red]Invalid selection[/red]")
            
    def _display_job_panel(self, job):
        """Display job details in a panel"""
        details = f"""
[bold]Company:[/bold] {job.get('company', 'N/A')}
[bold]Title:[/bold] {job.get('title', 'N/A')}
[bold]Location:[/bold] {job.get('location', 'N/A')}
[bold]Experience:[/bold] {job.get('experience', 'N/A')}
[bold]Salary:[/bold] {job.get('salary', 'N/A')}
[bold]Job Type:[/bold] {job.get('job_type', 'N/A')}
[bold]Posted Date:[/bold] {job.get('posted_date', 'N/A')}
[bold]Description:[/bold]
{job.get('description', 'N/A')}
[bold]Link:[/bold] {job.get('url', 'N/A')}
        """
        console.print(Panel(details, title="Job Details", expand=False))
        
    def subscribe_to_notifications(self):
        """Subscribe to job notifications"""
        email = Prompt.ask("Enter your email for notifications")
        frequency = Prompt.ask(
            "Notification frequency (daily/weekly/real-time)",
            default="daily"
        )
        
        subscription = {
            'email': email,
            'state': self.selected_state,
            'frequency': frequency,
            'created_at': datetime.now().isoformat()
        }
        
        self.notification_manager.add_subscription(subscription)
        console.print(f"\n[green]✓ Subscribed to job notifications for {self.selected_state}[/green]")
        
    def show_main_menu(self):
        """Display main menu and get user choice"""
        console.print("\n[bold cyan]Main Menu[/bold cyan]")
        console.print("1. View all jobs")
        console.print("2. View companies hiring")
        console.print("3. View job details")
        console.print("4. Subscribe to notifications")
        console.print("5. Change state")
        console.print("6. Exit")
        
        choice = Prompt.ask("\nSelect option")
        return choice
        
    def run(self):
        """Main application loop"""
        self.display_welcome()
        
        # Select state
        self.select_state()
        console.print(f"\n[bold green]✓ Selected: {self.selected_state}[/bold green]")
        
        # Fetch jobs
        self.fetch_jobs()
        
        # Main menu loop
        while True:
            choice = self.show_main_menu()
            
            if choice == '1':
                self.display_jobs()
            elif choice == '2':
                self.display_companies()
            elif choice == '3':
                self.view_job_details()
            elif choice == '4':
                self.subscribe_to_notifications()
            elif choice == '5':
                self.select_state()
                console.print(f"\n[bold green]✓ Changed to: {self.selected_state}[/bold green]")
                self.fetch_jobs()
            elif choice == '6':
                console.print("\n[bold green]Thank you for using Job Search AI Agent![/bold green]")
                sys.exit(0)
            else:
                console.print("[red]Invalid option[/red]")

if __name__ == '__main__':
    try:
        agent = JobSearchAgent()
        agent.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]Application terminated by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Application error: {str(e)}", exc_info=True)
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)
