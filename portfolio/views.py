from typing import List
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View, TemplateView, DetailView
from .models import Project
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

class HomeView(ListView):
    template_name = 'portfolio/home.html'
    queryset = Project.objects.filter(starred=True)
    context_object_name = 'projects'
    
class ProjectListView(ListView):
    template_name = 'portfolio/project_list.html'
    queryset = Project.objects.all()
    context_object_name = 'projects'
    
    
class ProjectDetailView(DetailView):
    model = Project
    template_name='portfolio/project_detail.html'
    context_object_name = 'project'
    
    def get_object(self):
        url_name = self.kwargs.get("url_name")
        return get_object_or_404(Project,url_name=url_name)

class ResumeTemplateView(TemplateView):
    template_name = 'portfolio/resume.html'
    
    
class ContactView(View):
    form_class = ContactForm
    template_name = 'portfolio/contact.html'
    

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] =  ContactForm()
    #     return context
    
    def post(self, request, *args, **kwargs):
        #Send email
        form = self.form_class(request.POST)
        if form.is_valid():
            #Send email here
            email = form.cleaned_data.get("email")
            subject= form.cleaned_data.get("subject")
            text= form.cleaned_data.get("text")
            text += "\n Sent by: " + email
            
            send_mail(subject, text, "andrew.benson.testmail@gmail.com", ["andrew.benson.testmail@gmail.com"],fail_silently=False)
            print(email +" : " + subject)
        
        
        messages.info(self.request, f'Email has been sent')
        return redirect('portfolio-contact')