from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from django.views import View
from capp.models import Contact
from capp.forms import ContactForm,UpdateContactForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.
class Home(TemplateView):
    template_name = 'index.html'
class ContactView(CreateView):
    template_name='add_contact.html'
    form_class=ContactForm
    model=Contact
    success_url=reverse_lazy("home_view")
    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.success(self.request,"todo created successfully")
        return super().form_valid(form)
class ListContact(View):
    def get(self,request):
        contacts=Contact.objects.all()
        return render(request,'view_contact.html',{'contacts':contacts})
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        con=Contact.objects.get(id=id)
        con.delete()
        return redirect("home_view")
class TodoUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        con=Contact.objects.get(id=id)
        form=UpdateContactForm(instance=con)
        return render(request,'update.html',{'con':con,'form':form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        con=Contact.objects.get(id=id)
        fname=request.POST.get("contact_name")   
        email=request.POST.get("contact_email")   
        phone=request.POST.get("contact_phone")   
        con.contact_name=fname
        con.contact_email=email
        con.contact_phone=phone
        con.save()
        return redirect('view') 


        
        

