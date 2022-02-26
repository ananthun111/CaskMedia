from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = [
    path("termsandconditions",TemplateView.as_view(template_name="termsandconditions.html"),name="termsandconditions"),
    path("PrivacyPolicy",TemplateView.as_view(template_name="Privacy Policy.html"),name="privacypolicy"),
    ]