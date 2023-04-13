from django.db import models

# Create your models here.


class Feedback(models.Model):
    """ 
    Feedback model for users to send feedback to the developer 
  
    Attributes:
        name: Name of the user giving a feedback
        email: email address of the sender
        game_choice: the game for which the sending is giving feedback
        message: the feedback message
    """
   
    GAME_TYPES = (
        ('chat', 'chat'),
        ('quiz', 'quiz')
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    game_choice = models.CharField(max_length=100, null=False, blank=False, choices=GAME_TYPES)
    message = models.CharField(max_length=350, null=False, blank=False)

    def __str__(self):
        return str(self.name)
