__author__ = 'jay'

import datetime

from django.db import models

from acu import constants as acuCon

class ACUBaseModel(models.Model):

    class Meta:
        abstract = True
        app_label = 'acu'

class Player(ACUBaseModel):

    user = models.OneToOneField('auth.User')
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    gender = models.CharField(max_length=16,choices=acuCon.GENDER_CHOICES,default=acuCon.GENDER_MALE)
    age = models.IntegerField(default=18)
    teams = models.ManyToManyField('acu.Team', blank=True, null=True)

    def __unicode__(self):
        """Gets string representation of the model instance"""
        return "Player:%s - %s %s" % (self.id,self.first_name,self.last_name)

    class Meta:
        app_label = 'acu'
        verbose_name = "Player"
        verbose_name_plural = "Players"

class Team(ACUBaseModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)

    def __unicode__(self):
        """Gets string representation of the model instance"""
        return "Team:%s - %s" % (self.id,self.name)

    class Meta:
        app_label = 'acu'
        verbose_name = "Team"
        verbose_name_plural = "Teams"

class Event(ACUBaseModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    start_date = models.DateField(default=datetime.datetime.today())
    end_date = models.DateField(default=datetime.datetime.today())

    def __unicode__(self):
        """Gets string representation of the model instance"""
        return "Event:%s - %s" % (self.id,self.name)

    class Meta:
        app_label = 'acu'
        verbose_name = "Event"
        verbose_name_plural = "Events"

class Game(ACUBaseModel):

    game_date = models.DateField(default=datetime.datetime.today())
    event = models.ForeignKey('acu.Event')
    game_type = models.CharField(max_length=64, choices=acuCon.GAME_TYPE_CHOICES, default=acuCon.GAME_TYPE_REGULAR)
    home_team = models.ForeignKey('acu.Team', related_name='home_game_set')
    away_team = models.ForeignKey('acu.Team', related_name='away_game_set')

    def __unicode__(self):
        """Gets string representation of the model instance"""
        return "Game:%s - %s:%s" % (self.id,self.event.name,self.game_date)

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
        return "Stat:%s - %s %s Game:%s" % (self.id,self.player.first_name,self.player.last_name,self.game)

    class Meta:
        app_label = 'acu'
        verbose_name = "Stat"
        verbose_name_plural = "Stats"
        unique_together = ("player", "game")