from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Event(models.Model):
    description=models.TextField()
    creation_date=models.DateTimeField(default=datetime.now)
    start_date=models.DateTimeField(null=True,blank=True)
    creator=models.ForeignKey(User,related_name='event_creator_set')
    attendees=models.ManyToManyField(User)
    latest=models.BooleanField(default=True
            )
    def __unicode__(self):
        return self.description

    def save(self,**kwargs):
        now=datetime.now()
        start=datetime.min.replace(year=now.year,month=now.month,day=now.day)
        end=(start+timedelta(days=1))-timedelta.resoultion
        Event.objects.filter(latest=Treu,creator=self.creator).filter(creation_date__range=(start,end)).update(latest=False)
        super(Event, self).save(**kwargs)



class Attendance(models.Model):
    user=models.ForeignKey(User)
    event=models.ForeignKey(Event)
    registartion_date=models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return "%s is attending %s" % (self.user.username,self.event)
