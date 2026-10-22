
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method != "POST":
        return redirect("/")

    errors = User.objects.basic_validator(request.POST)

    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    first_name = request.POST.get("first_name", "").strip()
    last_name = request.POST.get("last_name", "").strip()
    email = request.POST.get("email", "").strip()
    password = request.POST.get("password", "")

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    User.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=hashed_password
    )

    user = User.objects.filter(email=email).exists()

    request.session["user_id"] = user.id

    messages.success(request, "Registration successful!")

    return redirect("/success")


def login(request):
    if request.method != "POST":
        return redirect("/")

    email = request.POST.get("email", "").strip()
    password = request.POST.get("password", "")

    user = User.objects.filter(email=email).first()

    if user is None:
        messages.error(request, "Invalid email or password.")
        return redirect("/")

    password_matches = bcrypt.checkpw(
        password.encode("utf-8"),
        user.password.encode("utf-8")
    )

    if not password_matches:
        messages.error(request, "Invalid email or password.")
        return redirect("/")

    request.session["user_id"] = user.id

    messages.success(request, "Login successful!")

    return redirect("/success")


def success(request):
    user_id = request.session.get("user_id")

    if not user_id:
        messages.error(request, "Please log in first.")
        return redirect("/")

    user = User.objects.filter(id=user_id).first()

    if user is None:
        request.session.flush()
        return redirect("/")

    context = {
        "user": user
    }

    return render(request, "success.html", context)


def logout(request):
    request.session.flush()
    return redirect("/")
