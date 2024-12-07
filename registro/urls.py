from django.urls import path, include

urlspatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", SignupView.as_view(), name="signup"),
]