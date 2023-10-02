from django.shortcuts import render
from .forms import QuestionForm
from .utils import classify_question

# Calma que ainda tá simples. O feito é melhor que perfeito.
# Sem Overengineering

def get_question(request):
    # if this is a POST request we need to process the form data
    question = None
    difficulty = None

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            question = form.cleaned_data['question']
            difficulty = classify_question(question=question)

    form = QuestionForm()

    return render(request, "neural_network/base.html", {"form": form, "question":question, "difficulty":difficulty})
