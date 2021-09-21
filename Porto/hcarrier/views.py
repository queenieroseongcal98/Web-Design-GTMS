from django.shortcuts import render, HttpResponse
from hcarrier.models import Transactions, Payment, Feedback


# Create your views here.
def homecarrier(request):
    #return HttpResponse("This is my homepage(/)")
    context = {'name': 'Mars','course': 'Django'}
    return render(request, 'hcarrier/homecarrier.htm', context)


def transactions(request):
    if request.method=="POST": 
        if request.POST.get('address'):
            address = request.POST['address']
            date = request.POST['date']
            transactions = Transactions(address=address, date=date)
            transactions.save()
            return render(request, 'hcarrier/transactions.htm')

        if request.POST.get('confirmation'):
            confirmation = request.POST['confirmation']
            payment = Payment(confirmation=confirmation)
            payment.save()
        return render(request, 'hcarrier/transactions.htm')
    else:

    #return HttpResponse("This is my transactions page(/transactions)")
        return render(request, 'hcarrier/transactions.htm') 


def feedback(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        feedback = Feedback(name=name, email=email, phone=phone, desc=desc)
        feedback.save()
        print("the data has been written to the db")
        
    #return HttpResponse("This is my myaccount page(/myaccount)")
    return render(request, 'hcarrier/feedback.htm')

