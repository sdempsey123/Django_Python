from django.shortcuts import render, redirect
from django.contrib import messages



# Create your views here.

def index(request):
        return render(request, 'aircontrol.html')

def about(request):
        return render(request, "about.html")

def services(request):
        return render(request, "services.html")

def contact(request):
        return render(request, "contact.html")

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/aircontrol')

def logout(request):
    request.session.clear()
    return redirect('/')

def show(request, show_id):
    # query for one show with show_id
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'aircontrol.html', context)

def wall(request):
    if not 'user_id' in request.session:
        return redirect("/")
    

    context ={
        "user": User.objects.get(id=request.session['user_id']),
        "wall_messages": Wall_Message.objects.all()
    }
    return render(request, "wall.html", context)

def post_message(request):
    if request.method == "POST":
        errors = Wall_Message.objects.message_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        Wall_Message.objects.create(message=profanity.censor(request.POST['message']), poster=User.objects.get(id=request.session['user_id']))
    return redirect("/wall")

def post_comment(request, wall_message_id):
    if request.method == "POST":
        errors = Comment.objects.comment_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Comment.objects.create(
                comment = profanity.censor(request.POST['comment']),
                poster = User.objects.get(id=request.session['user_id']),
                wall_message = Wall_Message.objects.get(id=wall_message_id)
            )

    return redirect("/wall")

def delete_message(request, wall_message_id):
    if request.method == "POST":
        wall_message = Wall_Message.objects.get(id=wall_message_id)
        wall_message.delete()

    return redirect("/wall")

def delete_comment(request, comment_id):
    print(request.session)
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        if comment.poster.id == request.session['user_id']:
            comment.delete()

    return redirect("/wall")

def profile(request, profile_id):
    context = {
        "user": User.objects.get(id=profile_id)
    }

    return render(request, "profile.html", context)


    profanity.load_censor_words()

    text = "You p1ec3 of sHit."
    censored_text = profanity.censor(text, "*")
    print(censored_text)
    # You **** of ****.
