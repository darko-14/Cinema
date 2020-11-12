from django.shortcuts import render, redirect
from App1.models import Post
from django.contrib import messages
from .models import Ticket
from django.views.generic import View
from django.core.mail import send_mail
import stripe 
from Try1 import settings

stripe.api_key = ''


class BookingView(View):
   model = Ticket
   template_name = 'booking/booking.html'
    
   def get(self, request, *args, **qwargs):
      
      pass
   def post(self, request, *args, **kwargs):
      title = request.POST.get('title')
      price = request.POST.get('price')
      date = request.POST.get('date')
      # x = Ticket.objects.values_list('seats', flat=True)
      # y = Ticket.objects.values_list('movie', flat=True)
      # z = Ticket.objects.values_list('date', flat=True)
      all = list(Ticket.objects.values('movie', 'date', 'seats'))
      
      q = [item for item in all if item["movie"] == title and item["date"] == date]
      f = [x['seats']for x in q]
      w = [x['seats'][:2]for x in q]
      e = [x['seats'][2:]for x in q]

     

      # li = [x for x in all]
      # x = li[0]
      # y = li[1]
      # z = li[2] 



      context = {
         'title':title, 
         'price':price, 
         'date':date,
         'w':w,
         'e':e,
         # 'z':z,
         # 'all':all,
         'f':f,
         # 'q':q,
      }
      return render(request,'booking/booking.html', context)



class BuyView(View):
   model = Post
   template_name = 'booking/buy.html'
    
   def get(self, request, *args, **qwargs):
      pass

   def post(self, request, *args, **kwargs):
      title = request.POST.get('title')
      price = request.POST.get('price')
      date = request.POST.get('date')
      seats = request.POST.get('seats')
      num = request.POST.get('num')
      total = request.POST.get('total')
      email = request.POST.get('email')
      name = request.POST.get('name')

      

      context = {
         'title':title, 
         'price':price, 
         'date':date,
         'seats':seats,
         'num': num,
         'total':total,
         'email':email,
         'name':name,
      }
      return render(request,'booking/buy.html', context)
  


class ConfirmView(View):
   model = Ticket
   template_name = 'booking/confirm.html'
    
   def get(self, request, *args, **qwargs):
      pass


   def post(self, request, *args, **kwargs):
      title = request.POST.get('title')
      price = request.POST.get('price')
      date = request.POST.get('date')
      seats = request.POST.get('seats')
      num = request.POST.get('num')
      total = int(request.POST.get('total'))
      email = request.POST.get('email')
      name = request.POST.get('name')


      print(request.POST)
      

      try:
         customer = stripe.Customer.create(
            email = request.POST['email'],
            name = request.POST['name'],
            source = request.POST['stripeToken']
         )
         stripe.Charge.create(
            customer=customer,
            amount=total*100,
            currency='mkd',
            description=name,
         )
         Ticket.objects.all()
         x = Ticket(movie=title,date=date, price=price, seats=seats, num=num, total=total, email=email, name=name)
         x.save()
         messages.warning(
            self.request, "Вашето плаќање беше успешно, Ви благодариме.")

         subject = 'Ticket Reservation Payment'
         msg = 'Hi, your ticket reservation was successfull.'
         send_mail(
            subject,
            msg,
            settings.EMAIL_HOST_USER,
            [email],
            )

      except Exception as e:
         # send an email to ourselves
         messages.warning(
            self.request, "Вашето плаќање беше неуспешно, обидете се повторно.")
         # return redirect('/')

      context = {
         'title':title, 
         'price':price, 
         'date':date,
         'seats':seats,
         'num': num,
         'total':total,
         'email':email,
         'name':name,
      }

     

      return render(request,'booking/confirm.html', context)   


