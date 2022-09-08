from django.contrib.auth.models import AnonymousUser
from django.utils import timezone

from myauth.models import MyUser
from django.contrib.auth.middleware import AuthenticationMiddleware


class LastSeen:
    def __init__(self, get_request):
        self.get_request = get_request

    def __call__(self, request):
        if request.user.is_authenticated:
            # import pdb; pdb.set_trace()
            user = MyUser.objects.get(username=request.user.username)
            user.last_seen = timezone.now()
            user.save()
            global last_seen
            last_seen = user.last_seen
        request = self.get_request(request)

        return request
