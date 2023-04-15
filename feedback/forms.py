from django import forms
from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):

    """
    A form for users to give feedback to the developer
    """
    
    class Meta:
        model = Feedback
        fields = (
            'name',
            'email',
            'game_choice',
            'message',
        )
