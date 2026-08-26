from celery import shared_task


@shared_task
def test_task():
    return "Nexora Celery is working!"