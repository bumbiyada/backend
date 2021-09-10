from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .process import process, process_2


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(process_2, 'interval', minutes=1)
    #process()
    scheduler.start(paused=True)
