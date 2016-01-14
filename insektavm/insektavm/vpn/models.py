from django.db import models

from insektavm.base.models import UserToken


class AssignedIPAddress(models.Model):
    user_token = models.OneToOneField(UserToken)
    ip_address = models.GenericIPAddressField(protocol='ipv4')

    def __str__(self):
        return '{} -> {}'.format(self.user_token, self.ip_address)
