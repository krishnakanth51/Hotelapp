"""from django.shortcuts import render
from .models import application,Signup
from .forms import Signup
from django.http import HttpResponse"""

"""from django.shortcuts import render,redirect
from .forms import signupform,loginform,checkinform
from .models import signup,Rent,Booking
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.



def reg(request):
        if request.method=="POST":
                form=registration(request.POST)
                if form.is_valid():
                        Platinum=models.CharField(max_length=44)
                        suit=models.CharField(max_length=52)
                        gold=models.CharField(max_length=60)
                        Ordinary=models.CharField(max_length=55)

                        data =Customer(Platinum=Platinum,
                        suit=suit,
                        gold=gold'
                        Ordinary=Ordinary
                        data.save()
                return render(request,'forms.html',{'form':form})
        else:
                form=registration()
        return render(request,'forms.html',{'form':form})

       



def signup (request):
        if request.method=="POST":
                form=signup(request.POST)
                if form.is_valid():
                        Customer_name=request.POST.get('Customer_name','')
                        username=request.POST.get('username','')
                        password=request.POST.get('password','')
                        data=signup.objects.filter(Customer_name=Customer_name,username=username,
                        password=password)

                        if data:
                              return HttpResponse("ok")
                        else:
                                return HttpResponse("No")
            
                return render(request,'signup.html',{'form':form})
        else:
                form=signup() 
        return render(request,'signup.html',{'form':form})   





def login (request):
        if request.method=="POST":
                form=login(request.POST)
                if form.is_valid():
                        username=request.POST.get('username','')
                        password=request.POST.get('password','')
                        data=login.objects.filter(username=username,
                        password=password)

                       # if data:
                        #      return HttpResponse("ok")
                        #else:
                         #       return HttpResponse("No")
            
                #return render(request,'login.html',{'form':form})
        #else:
                form=login() 
        return render(request,'login.html',{'form':form})


"""from django.shortcuts import render,redirect
from .forms import signupform,loginform,checkinform
from .models import signup,Rent,Booking
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.
def signup(request):
    form = signupform()
    if request.method =='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form=form.save()
            return render(request,'signup.html',{'form':form})
        return render(request,'signup.html',{'form':form})
    return render(request,'signup.html',{'form':form})


def login(request):
    form = loginform()
    if request.method == 'POST':
        form= loginform(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            m = signupmodel.objects.filter(username=username,password=password)
            if not m:
                # return HttpResponse('try again')
                return render(request,'login.html')
            else:
                # return redirect(request,checkin)
                return redirect(checkin)
        else:
            return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':form})


def checkin(request):
    if request.method =='POST':
        form=checkinform(request.POST)
        if form.is_valid():
            checkin = request.POST.get('checkin')
            checkout = request.POST.get('checkout')
            user=Rent.objects.filter(checkin=checkin,checkout=checkout)
            form.save()
            
        return redirect(receipt)
    else:
        
        form=checkinform
        return render(request,'checkin.html',{'form':form})


def receipt(request):
    form = signupform()
    if request.method =='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form=form.save()
            return render(request,'receipt.html',{'form':form})
        return render(request,'receipt.html',{'form':form})
    return render(request,'receipt.html',{'form':form})
    return render(request,'receipt.html')


def search(request):
    if request.method == 'POST':
            
            form = checkinform(request.POST)
            if form.is_valid():
                                  
                booking= request.POST['']
                booking = Booking.objects.filter(Book_name__contains=book) #to find book from database
                return render(request,'drop.html',{'bookname':bookname})
            else:
                form = checkinform()          
                return render(request,'search.html',{'form':form})

    else:     
           form = checkinform()          
           return render(request,'search.html',{'form':form})"""        



from django.shortcuts import render,redirect
from .forms import signupform,loginform,checkinform,NonForm
from .models import signupmodel,Check,Non
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.
def signup(request):
    form = signupform()
    if request.method =='POST':
        form = signupform(request.POST)
        if form.is_valid():
            global ty
            ty=form.cleaned_data['category']
            form.save(commit=True)
        return redirect('/login')
    return render(request,'signup.html',{'form':form})

def pre(request):
    return render(request,'pre.html')
def non(request):
    return render(request,'non.html')

def checkin(request):
    form = checkinform()
    if request.method == 'POST':
        form = checkinform(request.POST)
        if form.is_valid():
            c=request.POST.get('checkin')
            co=request.POST.get('checkout')
            ro=request.POST.get('room')
            # ci = request.POST.get('id')
            # bi = request.POST.get('id')
            form.save()
        return render(request,'prereceipt.html',{'c':c,'co':co,'ro':ro,})#'ci':ci}) #,'ci':ci,'bi':bi})
    return render(request,'checkin.html',{'form':form})

def Nonfunc(request):
    form=NonForm()
    if request.method=='POST':
        form=NonForm(request.POST)
        if form.is_valid():
            ci=form.cleaned_data['checkin']
            print(ci)
            form.save()
        return render(request,'nonreceipt.html')
    return render(request,'non.html',{'form':form})




































"""def search(request):
        if request.method == 'POST':

                form = searchform(request.POST)
                if form.is_valid():

                        book = request.POST['Book_name']
                        bookname = bookdata.objects.filter(Book_name__contains=book) #to find book from database
                        return render(request,'drop.html',
        {'bookname':bookname})
                else:
                    form = searchform() 
                return render(request,'search.html',
        {'form':form})

                
        else: 
            form = searchform() 
        return render(request,'search.html',
        {'form':form})"""
