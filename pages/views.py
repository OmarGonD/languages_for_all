from django.views.generic import TemplateView, FormView
from .forms import ContactForm



class HomePageView(TemplateView):
    template_name = 'pages/index.html'



# class RegistrationPageView(TemplateView):
#     template_name = "pages/register.html"


class ContactFormView(FormView):
    template_name = "pages/contact-us.html"
    form_class = ContactForm
    success_url = '.'

    def form_valid(self, form):
        # process the data in form.cleaned_data
        ...
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = self.get_form()
        return context


# class HomePageView(FormView):
#     template_name = 'pages/home.html'
#     form_class = CountryForm
#     success_url = '.'
#
#     def get_context_data(self, **kwargs):
#         context = super(HomePageView, self).get_context_data(**kwargs)
#         #context["country_form"] = "this is a new context var"
#         return context
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         #form.send_email()
#         #print "form is valid"
#         return super(HomePageView, self).form_valid(form)
#



# class HomePageView(TemplateView):
#     template_name = "pages/home.html"

class CoursesListView(TemplateView):
    template_name = "pages/course-list.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class KidsPageView(TemplateView):
    template_name = "pages/kids.html"

class AdultsPageView(TemplateView):
    template_name = "pages/adults.html"

class CorporatePageView(TemplateView):
    template_name = "pages/corporate.html"

class ProfessionalsPageView(TemplateView):
    template_name = "pages/professionals.html"

class IndividuosPageView(TemplateView):
    template_name = "pages/individuals.html"



class ContactPageView(TemplateView):
    template_name = "pages/contact.html"




