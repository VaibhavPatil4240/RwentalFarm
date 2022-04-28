from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("owner/products/<int:myid>", views.productOwnView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path("owner/",views.ownerDashBoard,name="ownerDash"),
    path("owner/addproduct/", views.add_prod, name="Add prod"),
    path("owner/rentproduct/", views.rent_summary, name="Rent summary"),
    path("updateproducts/<int:myid>", views.update_prod, name="Productupd"),

]
