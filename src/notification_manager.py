"""Notification Manager - Handles job alerts and subscriptions"""

import logging
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List
from config.settings import NOTIFICATION_DB

logger = logging.getLogger(__name__)

class NotificationManager:
    """Manages job notifications and subscriptions"""
    
    def __init__(self):
        self.db_path = Path(NOTIFICATION_DB)
        self.subscriptions = self._load_subscriptions()
        self.notifications = self._load_notifications()
        
    def add_subscription(self, subscription: Dict) -> bool:
        """Add a new subscription"""
        try:
            if 'id' not in subscription:
                subscription['id'] = f"sub_{len(self.subscriptions)}_{datetime.now().timestamp()}"
                
            self.subscriptions.append(subscription)
            self._save_subscriptions()
            logger.info(f"Added subscription: {subscription['id']}")
            return True
        except Exception as e:
            logger.error(f"Error adding subscription: {str(e)}")
            return False
            
    def add_notification(self, job: Dict, subscription_id: str) -> bool:
        """Add a job notification"""
        try:
            notification = {
                'id': f"notif_{len(self.notifications)}_{datetime.now().timestamp()}",
                'subscription_id': subscription_id,
                'job': job,
                'created_at': datetime.now().isoformat(),
                'read': False
            }
            
            self.notifications.append(notification)
            self._save_notifications()
            logger.info(f"Added notification: {notification['id']}")
            return True
        except Exception as e:
            logger.error(f"Error adding notification: {str(e)}")
            return False
            
    def get_unread_notifications(self, subscription_id: str) -> List[Dict]:
        """Get unread notifications for a subscription"""
        return [
            n for n in self.notifications
            if n['subscription_id'] == subscription_id and not n['read']
        ]
        
    def mark_as_read(self, notification_id: str) -> bool:
        """Mark notification as read"""
        try:
            for notification in self.notifications:
                if notification['id'] == notification_id:
                    notification['read'] = True
                    self._save_notifications()
                    return True
            return False
        except Exception as e:
            logger.error(f"Error marking notification as read: {str(e)}")
            return False
            
    def get_subscriptions(self) -> List[Dict]:
        """Get all subscriptions"""
        return self.subscriptions
        
    def _load_subscriptions(self) -> List[Dict]:
        """Load subscriptions from database"""
        try:
            if self.db_path.exists():
                with open(self.db_path, 'r') as f:
                    data = json.load(f)
                    return data.get('subscriptions', [])
        except Exception as e:
            logger.error(f"Error loading subscriptions: {str(e)}")
        return []
        
    def _save_subscriptions(self):
        """Save subscriptions to database"""
        try:
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            data = {'subscriptions': self.subscriptions, 'notifications': self.notifications}
            with open(self.db_path, 'w') as f:
                json.dump(data, f, indent=2, default=str)
        except Exception as e:
            logger.error(f"Error saving subscriptions: {str(e)}")
            
    def _load_notifications(self) -> List[Dict]:
        """Load notifications from database"""
        try:
            if self.db_path.exists():
                with open(self.db_path, 'r') as f:
                    data = json.load(f)
                    return data.get('notifications', [])
        except Exception as e:
            logger.error(f"Error loading notifications: {str(e)}")
        return []
        
    def _save_notifications(self):
        """Save notifications to database"""
        try:
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            data = {'subscriptions': self.subscriptions, 'notifications': self.notifications}
            with open(self.db_path, 'w') as f:
                json.dump(data, f, indent=2, default=str)
        except Exception as e:
            logger.error(f"Error saving notifications: {str(e)}")
