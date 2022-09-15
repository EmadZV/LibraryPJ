# from celery.utils.log import get_task_logger
# from django.core.mail import send_mail

from boook1.celery import app
# from myauth.models import MyUser
# from mycontent.models import Book

# logger = get_task_logger(__name__)


@app.task
def daily_message():
    # MyUser.objects.create(name='very_test', desc='very_test')
    # users = MyUser.objects.all()
    # book = Book.objects.get(id=1)
    # for user in users:
    #     subject = f"Dear {user.username}we recommend you to read " \
    #               f"{book.title}"
    #     message = f"Read {book.title} at {book.get_absolute_url()}"
    #     send_mail(subject, message, 'admin@myblog.com',
    #               user.email)
    print('hell')
    return 1

# celery -A core beat
# celery -A core worker -l info
