"""
URL configuration for trek_trail_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from marketplace import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    # for gear detail
    path("gear/<int:id>?", views.gear_detail, name="gear_detail"),
    # for package detail
    path("package/<int:id>/", views.package_detail, name="package_detail"),
    # for explore packages
    path("packages/", views.explore_packages, name="explore_packages"),
    path("add-to-cart/<int:gear_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart_view, name="cart_view"),
]

# यो तलको लाइनले फोटोलाई वेबसाइटमा देखाउन मद्दत गर्छ
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
