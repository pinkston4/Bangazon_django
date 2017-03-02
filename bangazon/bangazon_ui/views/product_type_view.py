from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


def product_type(request):
    """
        This method is to list product type in the product_type_list page
        Author: Julia Kim-Chung
    """
    context = {}
    product_type_list = product_type_model.ProductType.objects.all()[:10]
    for product_type in product_type_list:
        product_list = product_model.Product.objects.filter(product_type = product_type.pk).order_by("-created")
        context.update({product_type: product_list})
    return render(request, 'bangazon_ui/product_type_list.html', {"context":context})


class Create_product_type(TemplateView):
    """
        This class is called to go to create_product_type.html template to create product type with the post method
        once created it redirects to the product_type_list page
    """

    template_name = 'bangazon_ui/create_product_type.html'

    def post(self, request):
        data = request.POST
        ProductType.objects.create(
            label=data['label'])

        return HttpResponseRedirect(redirect_to='/product_type_list')



