from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Card

# Create your views here.

def index(request):
    # This view is responsible for rendering the homepage of the trivia app.
    
    # If there are no records in the Card table (when the app is first set up),
    # populate the table with data from a text file.
    if Card.objects.count() == 0:
        # Open the questions.txt file that contains questions, answers, and hints
        with open('trivia/static/trivia/questions.txt', 'r') as file:
            for line in file:
                # Split each line into question, answer, and hint (separated by commas)
                x = line.split(',')
                # Create a new Card object and save it to the database
                obj = Card(question=x[0], answer=x[1], hint=x[2])
                obj.save()
    
    # Fetch the first Card object from the database to display as the first question
    card = Card.objects.first()
    # Pass the card object to the template as context
    params = {'card': card}
    
    # Render the index.html template, passing the card details to the front-end
    return render(request, 'trivia/index.html', params)

def eval(request):
    # This view handles the evaluation of the user's answer.
    
    # Check if the request method is POST (meaning the form was submitted)
    if request.method == 'POST':
        # Get the answer the user submitted, and remove any leading/trailing spaces
        answerText = request.POST.get('answerText').strip()
        # Get the current card ID from the hidden form field
        currentId = request.POST.get('currentId')
        
        # Retrieve the corresponding Card object from the database using the cardId
        card = Card.objects.get(cardId=currentId)
        
        # Compare the user's answer with the correct answer (both stripped of extra spaces)
        if card.answer.strip() == answerText:
            # If the answer is correct, fetch the next question by incrementing the cardId
            updateId = int(currentId) + 1
            updateCard = Card.objects.get(cardId=updateId)
            
            # Prepare the next question, hint, and ID to send back to the front-end
            nextQuestion = updateCard.question
            nextHint = updateCard.hint
            
            # Return a JSON response indicating the answer was correct, and provide the next question
            return JsonResponse({
                'correct': True,
                'nextQuestion': nextQuestion,
                'nextId': updateId,
                'nextHint': nextHint
            })
        else:
            # If the answer is incorrect, return a JSON response indicating failure
            return JsonResponse({
                'correct': False
            })
