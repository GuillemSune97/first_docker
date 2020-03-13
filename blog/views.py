from django.shortcuts import render
from .models import Customer, Car
from .forms import CustomerForm, CarForm
from django.shortcuts import redirect, get_object_or_404

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'blog/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    customer_cars = Car.objects.filter(customer=pk)
    return render(
      request,
      'blog/customer_detail.html',
      {
        'customer': customer,
        'cars': customer_cars,
      }
    )

def customer_new(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'blog/customer_new.html', {'form': form})

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'blog/customer_new.html', {'form': form})

def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request, 'blog/car_detail.html', {'car': car})

def car_new(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'blog/car_new.html', {'form': form})
