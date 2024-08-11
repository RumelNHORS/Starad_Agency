from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactMessageForm
from .models import About, Service, RecentWork



class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactMessageForm()
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {
                'form': ContactMessageForm(),  # Clear the form after submission
                'success_message': 'Your message has been sent successfully!',
                'about': About.objects.first(),
                'services': Service.objects.all(),
                'works': RecentWork.objects.all(),
            })
        else:
            return render(request, self.template_name, {
                'form': form,
                'about': About.objects.first(),
                'services': Service.objects.all(),
                'works': RecentWork.objects.all(),
            })

