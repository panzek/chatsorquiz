from django.shortcuts import render, redirect
from .forms import FeedbackForm


def feedback(request):

    """ A view to render feedback form in template """
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('home')
    
    form = FeedbackForm()

    template = 'feedback/feedback.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
