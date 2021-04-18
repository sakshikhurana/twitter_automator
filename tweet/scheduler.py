from .tweet_handler import tweet_scheduler
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    print("HI")
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        tweet_scheduler, 'interval', minutes=1)
    scheduler.start()
