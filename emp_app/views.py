from django.shortcuts import render,redirect
from .models import Kitchen,Bedroom,Hall,Handles,Doors,Bedroom_handles,Bedroom_doors,Hall_handles,Hall_doors,Checkout


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):	
	if request.method == 'GET':
		return render(request, 'accounts/login.html')
	elif request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect('/home')
		else:
			context = {'error': 'Invalid username/password'}
			return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/login')

def validate_user(username, password1, password2):
	status = True
	message = ''
	user_existence = User.objects.filter(username=username).exists()
	if user_existence:
		status = False
		message = 'Username already exists'
	if password1 != password2:
		status = False
		message = 'Passwords not matching'
	return status, message


def register_view(request):
	if request.method == 'GET':
		return render(request, 'accounts/register.html')
	elif  request.method == 'POST':
		username = request.POST.get('username')
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		email= request.POST.get('email')
		password1= request.POST.get('password1')
		password2= request.POST.get('password2')
		status, message = validate_user(username, password1, password2)
		if status:
			user = User.objects.create_user(username, email=email, password=password1)
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			login(request, user)
			return redirect('/home')
		else:
			context = {'error': message}
			return render(request, 'accounts/register.html', context)


@login_required(login_url='/login')
def home_view(request):
	return render(request,'home.html')

def kitchendetails_view(request):
	kitchen_cost =Kitchen.objects.all()
	if request.method == "GET":
		context ={
		'kitchen_cost':kitchen_cost
		}
		return render(request,'k_details.html',context)
	elif request.method == "POST":
		for k in kitchen_cost:			
			k.length = request.POST.get('kit_length')
			k.width = request.POST.get('kit_width')
			k.cost = request.POST.get('kit_cost')
			k.save()
		return redirect('/k_details')


def bedroomdetails_view(request):
	wardrobe_cost =Bedroom.objects.all()
	if request.method == "GET":
		context ={
		'wardrobe_cost':wardrobe_cost
		}
		return render(request,'b_details.html',context)
	elif request.method == "POST":
		for w in wardrobe_cost:
			w.length = request.POST.get('bed_length')
			w.width = request.POST.get('bed_width')
			w.cost = request.POST.get('bed_cost')
			w.save()
		return redirect('/b_details')

def halldetails_view(request):
	hall_cost =Hall.objects.all()
	if request.method == "GET":
		context ={
		'hall_cost':hall_cost
		}
		return render(request,'h_details.html',context)
	elif request.method == "POST":
		for h in hall_cost:
			h.length = request.POST.get('hall_length')
			h.width = request.POST.get('hall_width')
			h.cost = request.POST.get('hall_cost')
			h.save()
		return redirect('/h_details')


def edit_door_system(request,id):
    door_instance =Doors.objects.get(id=id)
    if request.method == 'GET':
        context = {'door_instance': door_instance}
        return render(request, 'edit_door_system.html', context)
    elif request.method == 'POST':
        door_instance.quantity = request.POST.get('dquantity')
        door_instance.totalprice = request.POST.get('dtotal')
        door_instance.save()
        return redirect('/doors')


####################################################

def compute_final_cost():
	kitchen_obj = Kitchen.objects.first()
	k_value = kitchen_obj.total_price
	wardrobe_obj =Bedroom.objects.first()
	b_value = wardrobe_obj.total_price
	hall_obj =Hall.objects.first()
	h_value = hall_obj.total_price

	total_value = k_value + b_value + h_value
	return total_value

###################################################

def cart_view(request):
	handles = Handles.objects.all()
	doors =Doors.objects.all()
	kitchen_obj = Kitchen.objects.all()
	wardrobe_obj =Bedroom.objects.all()
	hall_obj =Hall.objects.all()
	bedroom_handles = Bedroom_handles.objects.all()
	hall_handles = Hall_handles.objects.all()
	value =compute_final_cost()
	context ={
		'handles':handles,
		'doors':doors,
		'kitchen_obj':kitchen_obj,
		'wardrobe_obj':wardrobe_obj,
		'hall_obj':hall_obj,
		'bedroom_handles':bedroom_handles,
		'hall_handles':hall_handles,
		'value':value
	}
	return render(request,'cart.html', context)


def handle_view(request):
	handles = Handles.objects.all()
	bedroom_handles = Bedroom_handles.objects.all()
	hall_handles = Hall_handles.objects.all()
	context = {
		'handles': handles,
		'bedroom_handles':bedroom_handles,
		'hall_handles':hall_handles
	}
	return render(request,'handles.html',context)


def edit_system(request,id):
    handles_system = Handles.objects.get(id=id)   
    if request.method == 'GET':
        context = {
            'handles_system': handles_system,
        	}
        return render(request, 'edit_system.html', context)
    elif request.method == 'POST':
        handles_system.quantity = request.POST.get('handle_quantity')
        handles_system.totalprice = request.POST.get('handle_total')
        handles_system.save()
        return redirect('/handles')

def edit_bedroom_handle(request,id):
    bedroom_handles = Bedroom_handles.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'bedroom_handles':bedroom_handles
        }
        return render(request, 'edit_bedroom_handle.html', context)
    elif request.method == 'POST':
        bedroom_handles.quantity = request.POST.get('b_handle_quantity')
        bedroom_handles.totalprice = request.POST.get('b_handle_total')
        bedroom_handles.save()
        return redirect('/handles')

def edit_hall_handle(request,id):
    hall_handles = Hall_handles.objects.get(id=id)
    if request.method == 'GET':
        context = {
        'hall_handles':hall_handles
        }
        return render(request, 'edit_hall_handles.html', context)
    elif request.method == 'POST':
        hall_handles.quantity = request.POST.get('h_hall_quantity')
        hall_handles.totalprice = request.POST.get('h_hall_total')
        hall_handles.save()
        return redirect('/handles')
#########################################################################################
def doors_view():
	pass
	
def edit_bedroom_doors():
	pass

def edit_hall_doores():
	pass

###########################################################################################
def checkout_view(request):
	check =Checkout.objects.all()
	kitchen_obj = Kitchen.objects.all()
	wardrobe_obj =Bedroom.objects.all()
	hall_obj =Hall.objects.all()
	if request.method == "GET":
		context ={
		'check':check,
		'kitchen_obj':kitchen_obj,
		'wardrobe_obj':wardrobe_obj,
		'hall_obj':hall_obj

		}
		return render(request,'checkout.html',context)
	elif request.method == "POST":
		for c in check:
			c.fullname=request.POST.get('firstname')
			c.email=request.POST.get('email')
			c.address=request.POST.get('address')
			c.state=request.POST.get('state')
			c.city=request.POST.get('city')
			c.zipp=request.POST.get('zip')
			c.nameoncard=request.POST.get('cardname')
			c.cardnumber=request.POST.get('cardnumber')
			c.expyear=request.POST.get('expyear')
			c.expmonth=request.POST.get('expmonth')
			c.cvv=request.POST.get('cvv')
			c.save()
		return redirect('/checkout')

