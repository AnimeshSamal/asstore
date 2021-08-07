from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models.product import Product
from .models.customer import Customer
from .models.mens import Mens
from django.contrib.auth.hashers import check_password, make_password
from django.views import View



def index(request):
    print(' you are :', request.session.get('email'))
    return render(request , 'index/index.html')

def product(request):

    print('comming here')
    prds = Product.get_all_product()
    return render(request , 'product/product.html', {'products': prds})

def signup(request):
    if request.method == 'GET':
       return render(request , 'index/signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        phone = postData.get('phone')
        address = postData.get('address')
        password = postData.get('password')
        city = postData.get('city')
        state = postData.get('state')
        pin = postData.get('pin')
        print(first_name , last_name , email , phone , address , password , city , state , pin)
        customer = Customer(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone = phone,
            address = address,
            password = password,
            city = city,
            state = state,
            pin = pin
        )
        customer.register()
        return HttpResponse('sIGN UP SUCCESULLY')


class login (View):
   def get(self , request):
       return render(request, 'index/login.html')

   def post(self, request):
       email = request.POST.get('email')
       password = request.POST.get('password')
       customer = Customer.get_customer_by_email(email)
       error_message = None
       if customer:
           print('password : ' + customer.password)
           print('email : ' + customer.email)
           passwordEncode = make_password(customer.password)
           flag = check_password(password, passwordEncode)
           if flag:
               request.session['customer_id'] = customer.id
               request.session['email'] = customer.email
               return redirect('product/')
           else:
               error_message = ('Email and password invalid...')
       else:

           error_message = ('Email and password invalid..')

       print(email, password)

       return render(request, 'index/login.html', {'error': error_message})


def contact(request):
    return render( request ,'index/contact.html')


class mens(View):
    def post(self,request):
        product = request.POST.get('productmen')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart['productmen'] = 1
        request.session['cart'] = cart

    def get(self , request):

         prds = Mens.get_all_product()
         return render(request , 'product/mens.html' , {'productmen' : prds})



def account(request):
      return render( request , 'index/account.html')


def details(request,  slug):
       details = Mens.objects.get(slug=slug)
       context = {
           "details": details
       }
       return render( request , 'product/details.html', context=context )



def orders(request):
      return render(request, 'product/orders.html')


class cart(View):
    def get(self , request):
        print(request.session.get('cart'))
        return render(request , 'product/cart.html')