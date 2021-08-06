
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from core.forms import ContactForm
from django.contrib import messages


class ErrorView(TemplateView):
    template_name = 'core/error-404.html'




class IndexView(TemplateView):
    template_name = 'core/index.html'




class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'core/contact.html'
    success_url = '/'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, 'Thank you for request! We will get in touch with you soon!')
        return result

