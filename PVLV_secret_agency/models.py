from django.db import models


class Guild(models.Model):
    platform = models.CharField(max_length=50)
    guild_id = models.IntegerField()
    channel_id = models.IntegerField()


class Target(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # editors = models.ManyToManyField()
    # viewers = models.ManyToManyField()
    monitorable = models.BooleanField(default=True)
    sending_points = models.ManyToManyField(to=Guild)
    name = models.CharField(max_length=50)
    age = models.IntegerField()


class TargetMonitoringPlatform(models.Model):
    """
    Creation point where begin a monitoring of a new person.
    """
    target = models.ForeignKey(to=Target, on_delete=models.CASCADE)
    monitoring = models.BooleanField(default=True)
    platform = models.CharField(max_length=50)
    last_seen = models.DateTimeField()
    data_to_collect = models.IntegerField()


class TargetPersonalData(models.Model):
    target = models.ForeignKey(to=Target, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    note = models.TextField()



