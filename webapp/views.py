from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import ProductForm, CategoryForm
from webapp.models import Product, Category


# Create your views here.
def products_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'products.html', context=context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })


def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product', pk=product.id)
    else:
        form = ProductForm()
    return render(request, 'form.html', {
        'form': form,
        'title': 'New product',
    })


def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product', pk=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'form.html', {
        'form': form,
        'title': 'Edit product',
    })


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products')


def categories_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context=context)


def category_add_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'form.html', {
        'form': form,
        'title': 'New category',
    })
