from celery.schedules import crontab
from celery.task import periodic_task
from django.utils import timezone
from .models import  Asset

@periodic_task(run_every=crontab(minute='*/1'))
def delete_old_foos():
    # Query all the foos in our database
    assets = Asset.objects.all()

    # Iterate through them
    for asset in assets:

        # If the expiration date is bigger than now delete it
        if asset.Expiry_date < timezone.now():
            asset.delete()
            # log deletion
    return "completed deleting foos at {}".format(timezone.now())

