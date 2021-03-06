from django.conf.urls import url
import sys
sys.path.append('../')
from Bangazon_api.views import register_view
from Bangazon_api.views import login_view
from Bangazon_api.views import payment_type_view
from Bangazon_api.views import product_view
from Bangazon_api.views import product_type_view
from Bangazon_api.views import product_list_view
from Bangazon_api.views.product_detail_view import ProductDetailView
from Bangazon_api.views.add_to_order_view import *
from Bangazon_api.views import order_detail_view
from Bangazon_api.views import home_page_view

app_name = 'Bangazon_api'
urlpatterns = [
    url(r'^$', home_page_view.context_data, name='home_page'),
    url(r'^register/', register_view.Register.as_view(), name='register'),
    url(r'^login/', login_view.Login.as_view(), name='login'),
    url(r'^logout/', login_view.logout_user, name="logout"),
    url(r'^payment_type_create/', payment_type_view.PaymentTypeView.as_view(), name="payment_type_create"),
    url(r'^product/',product_view.Create_product.as_view(), name='product' ),
    url(r'^product_detail/(?P<pk>[0-9]+)/$',ProductDetailView.as_view(), name='product_detail' ),
    url(r'^product_type/', product_type_view.Create_product_type.as_view(), name='product_type'),
    url(r'^add_to_order/', add_to_order, name='add_to_order'),
    url(r'^product_type_list/', product_type_view.product_type, name='product_type_list'),
    url(r'^order_detail/$', order_detail_view.OrderDetail.as_view(), name = 'order_detail'),
    url(r'^product_list/(?P<pk>[0-9]+)/$', product_list_view.ProductListView.as_view(), name='product_list'),
    url(r'^home_page/', home_page_view.context_data, name='home_page'),



]


