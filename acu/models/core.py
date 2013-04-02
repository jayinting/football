__author__ = 'jay'

import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from acu import constants as acuCon

class ACUBaseModel(models.Model):

    class Meta:
        abstract = True
        app_label = 'acu'

class Contact(ACUBaseModel):

    user = models.OneToOneField('auth.User')
    type = models.CharField(max_length=64, choices= acuCon.CONTACT_TYPE_CHOICES, default=acuCon.CONTACT_TYPE_PLAYER)

    def __unicode__(self):
        """Gets string representation of the model instance"""
        return "%s %s" % (self.user.first_name,self.user.last_name)

    def is_admin(self):
        return True if self.type == acuCon.CONTACT_TYPE_ADMIN else False

    class Meta:
        app_label = 'acu'
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

def create_contact(sender, instance, created, **kwargs):
    if created:
        profile, created = Contact.objects.get_or_create(user=instance)

post_save.connect(create_contact, sender=User)
User.contact = property(lambda u: u.get_profile())

class Player(ACUBaseModel):

    contact = models.ForeignKey('acu.Contact')
    event = models.ForeignKey('acu.Event')
    team = models.ForeignKey('acu.Team')

    def __unicode__(self):
        """Gets string representation of the model instance"""
        return "%s - %s" % (self.team.name,self.contact)

    class Meta:
        app_label = 'acu'
        verbose_name = "Player"
        verbose_name_plural = "Players"
        unique_together = ("contact", "team")

class Team(ACUBaseModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    event = models.ForeignKey('acu.Event')
    description = models.TextField(max_length=2048, blank=True, null=True)

    def __unicode__(self):
        """Gets string representation of the model instance"""
        return "%s" % (self.name)

    class Meta:
        app_label = 'acu'
        verbose_name = "Team"
        verbose_name_plural = "Teams"

class Venue(ACUBaseModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=2048, blank=True, null=True)
    featured_image = models.ImageField(upload_to='images/venues/featured/%Y/%m/%d', blank=True, null=True)

    def __unicode__(self):
        """Gets string representation of the model instance"""
        return "%s" % (self.name)

    class Meta:
        app_label = 'acu'
        verbose_name = "Venue"
        verbose_name_plural = "Venues"

class Event(ACUBaseModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=64, choices=acuCon.EVENT_TYPE_CHOICES, default=acuCon.EVENT_TYPE_REGULAR)
    description = models.TextField(max_length=2048, blank=True, null=True)
    start_date = models.DateField(default=datetime.datetime.today())
    end_date = models.DateField(default=datetime.datetime.today())

    def __unicode__(self):
        """Gets string representation of the model instance"""
        return "%s" % (self.name)

    class Meta:
        app_label = 'acu'
        verbose_name = "Event"
        verbose_name_plural = "Events"

class Game(ACUBaseModel):

    event = models.ForeignKey('acu.Event')
    description = models.TextField(max_length=2048, blank=True, null=True)
    game_date = models.DateField(default=datetime.datetime.today())
    home_team = models.ForeignKey('acu.Team', related_name='home_game_set')
    away_team = models.ForeignKey('acu.Team', related_name='away_game_set')
    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        """Gets string representation of the model instance"""
        return "%s - %s" % (self.event.name,self.game_date)

    class Meta:
        app_label = 'acu'
        verbose_name = "Game"
        verbose_name_plural = "Games"

class Stat(ACUBaseModel):

    player = models.ForeignKey('acu.Player')
    game = models.ForeignKey('acu.Game')
    goals = models.IntegerField(default=0)

    def __unicode__(self):
        """Gets string representation of the model instance"""
        return "Stat(%s):%s - %s" % (self.id,self.player,self.game)

    class Meta:
        app_label = 'acu'
        verbose_name = "Stat"
        verbose_name_plural = "Stats"
        unique_together = ("player", "game")