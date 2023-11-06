from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from digi_save_vsla_api.models import Users

class PhoneCodeBackend(ModelBackend):
    def authenticate(self, request, phone=None, code=None, **kwargs):
        try:
            user = Users.objects.get(phone=phone, unique_code=code)
            return user
        except Users.DoesNotExist:
            return None