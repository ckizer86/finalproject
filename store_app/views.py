from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponse
from django.views.generic import FormView
from django.urls import reverse
from django.conf import settings # new
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new
import stripe

# payments/views.py

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)

def SuccessView(request):
    return render(request, "success.html")


def CancelledView(request):
    return render(request, "cancelled.html")

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'T-shirt',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '2000',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

# new
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

# Create your views here.
def index(request):
    
    return render(request, "index.html")

def login_page(request):

    return render(request, "login.html")

def login(request):
    
    return redirect('/login')

def register_page(request):

    return render(request, "register.html")

def register(request):

    return redirect('/register')

def category(request, id):

    return render(request, "category.html")

def product(request, id):

    return render(request, "product.html")

def addcart(request):

    return redirect('/cart')

def cart(request):

    return render(request, "cart.html")

def likeditems(request):

    return render(request, "like.html")

def dashboard(request):

    return render(request, "dashboard.html")

def accountinfo(request):

    return render(request, "accountinfo.html")

def accountupdate(request):

    return redirect('/account')

def recentorders(request):

    return render(request, "recentorders.html")

def vieworder(request, id):

    return render(request, "vieworder.html")

def admindash(request):

    return render(request, "admindashboard.html")

def adminneworders(request):

    return render(request, "adminneworders.html")

def adminpastorders(request):

    return render(request, "adminpastorders.html")

def adminvieworder(request, id):

    return render(request, "adminvieworder.html")

def updatetracking(request):

    return redirect('/admin')

def products(request):

    return render(request, "products.html")

def addprod(request):

    return render(request, "addproduct.html")

def addingprod(request):

    return redirect('/admin')

def storeinfo(request):

    return render(request, "store.html")

def editstore(request):

    return redirect('/admin/store')