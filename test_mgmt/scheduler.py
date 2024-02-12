from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from requirements.views import get_alm_requirements


def start():
    scheduler = BackgroundScheduler()
    trigger = CronTrigger(year="*", month="*", day="*", hour="23", minute="59", second="00")
    scheduler.add_job(get_alm_requirements, trigger, name="Update ALM Requirement")
    scheduler.start()