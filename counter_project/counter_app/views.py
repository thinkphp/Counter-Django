from django.shortcuts import render, redirect

# Initialize the counter
counter = 0

def index(request):
    global counter
    return render(request, 'counter_app/index.html', {'counter': counter})

def increase(request):
    global counter
    counter += 1
    return redirect('index')

def decrease(request):
    global counter
    counter -= 1
    return redirect('index')

