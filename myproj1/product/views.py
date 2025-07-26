from django.shortcuts import render, redirect
from product.forms import Addproduct
from product.models import Product
from django.contrib.auth.decorators import permission_required

# Create your views here.
@permission_required('product.view_product', raise_exception=True)
def list_product(request):
    all_products = Product.objects.all()
    return render(request, 'product/list.html', context={'products':all_products})

@permission_required('product.add_product', raise_exception=True)
def add_product(request):
    if request.method == 'POST':
        form = Addproduct(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('product_list')
    else:
        form = Addproduct()

    return render(request, 'product/add.html', context={'form':form})

@permission_required('product.view_product', raise_exception=True)
def detail_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product/detail.html', context= {'product':product})

@permission_required('product.delete_product', raise_exception=True)
def delete_product(request, id):
    if request.method == 'POST':
        product = Product.objects.filter(id=id)
        if product.exists():
            product.delete()
        
        return redirect('product_list')

    return render(request, 'product/delete.html')

@permission_required('product.change_product', raise_exception=True)
def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = Addproduct(request.POST, instance=product)
        form.save()
        return redirect('product_list')
    else:
        form = Addproduct(instance=product)

    return render(request, 'product/add.html', context={'form':form})