import datetime
import celery


@celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=5))
def myTask():
    pass
