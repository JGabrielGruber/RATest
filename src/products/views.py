from django.http        import HttpResponse, HttpResponseRedirect
from django.shortcuts   import render, get_object_or_404, redirect
from django.contrib     import messages

from .forms             import ProductForm
from .models            import Product

# Create your views here.

def products_list(request):
    query_set = Product.objects.all()
    context = {
        "title": "List",
        "object_list": query_set,
    }
    return render(request, 'product_list.html', context)

def products_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Succesfuly Created!!")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Succesfuly Created!!")
    context = {
        "form": form
    }
    return render(request, 'product_form.html', context)

def products_detail(request, id=None):
    instance    = get_object_or_404(Product, id=id)
    context     = {
        "title": instance.name,
        "object": instance,
    }
    return render(request, 'product_detail.html', context)

def products_update(request, id=None):
    instance    = get_object_or_404(Product, id=id)
    form        = ProductForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Succesfuly Updated!!")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Succesfuly Updated!!")
    context     = {
        "title" : instance.name,
        "object": instance,
        "form"  : form
    }

    return render(request, 'product_form.html', context)

def products_delete(request, id=None):
    instance    = get_object_or_404(Product, id=id)
    instance.delete()
    messages.success(request, "Succesfuly Deleted!!")
    return redirect("products:list")
