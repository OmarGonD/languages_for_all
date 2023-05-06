from django.urls import path, re_path
from django.urls import path, include

from .views import HomePageView, AboutPageView, CorporatePageView, AdultsPageView, KidsPageView, ProfessionalsPageView, CoursesListView, ContactFormView
import accounts.views



urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("courses-list/", CoursesListView.as_view(), name="courses_list"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("kids/", KidsPageView.as_view(), name="kids"),
    path("adults/", AdultsPageView.as_view(), name="adults"),
    path("professionals/", ProfessionalsPageView.as_view(), name="professionals"),
    path("corporative/", CorporatePageView.as_view(), name="corporate"),
    path("contactanos/", ContactFormView.as_view(), name="contact-form")
]
