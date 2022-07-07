from django.db import models


class Scores(models.Model):
    code = models.CharField(unique=True, max_length=255, null=False)
    home_team = models.CharField( max_length=250, null=False)
    home_goals = models.CharField(max_length=3, null=False)
    away_goals = models.CharField(max_length=3, null=False)
    away_team = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.code
