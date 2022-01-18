from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view to return the bag page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a specified product to the users shopping bag """

    product = Product.objects.get(pk = item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})


    bag[item_id] = 1

    request.session['bag'] = bag
    messages.success(request, f'Added: {product.name}')

    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """ remove a specified product to the users shopping bag """

    try:
        bag = request.session.get('bag', {})
        
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)