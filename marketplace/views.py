from django.shortcuts import render, get_object_or_404, redirect
from .models import TrekkingGear, TravelPackage, Category  # हाम्रो मोडल ल्याएको


def home(request):
    categories = Category.objects.all()
    category_id = request.GET.get("category")

    # १. सर्च बक्समा लेखेको कुरा (q) तान्ने
    search_query = request.GET.get("q")

    gears = TrekkingGear.objects.filter(is_available=True)

    if category_id:
        gears = gears.filter(category_id=category_id)

    # २. यदि मान्छेले सर्च गरेको छ भने, त्यो शब्द मिल्ने सामान मात्र फिल्टर गर्ने
    if search_query:
        gears = gears.filter(name__icontains=search_query)

    context = {
        "gears": gears,
        "packages": TravelPackage.objects.all(),
        "categories": categories,
    }
    return render(request, "home.html", context)


# 👇 यो नयाँ लोजिक थप्ने (Detail Page को लागि) 👇
def gear_detail(request, id):
    # Database बाट त्यो ID भएको सामान मात्र तान्ने (भेटिएन भने 404 Error देखाउने)
    gear = get_object_or_404(TrekkingGear, id=id)

    # त्यसलाई 'gear_detail.html' भन्ने नयाँ पेजमा पठाउने
    return render(request, "gear_detail.html", {"gear": gear})

    # 👇 यो नयाँ लोजिक थप्ने (package Detail Page को लागि) 👇


def package_detail(request, id):
    # Database बाट ID अनुसार एउटा मात्र Package तान्ने
    package = get_object_or_404(TravelPackage, id=id)

    # yeslai pane package_detail.html vanne page ma pathaune
    return render(request, "package_detail.html", {"package": package})


def explore_packages(request):
    # सर्च बक्समा लेखेको कुरा तान्ने
    search_query = request.GET.get("q")

    # सुरुमा सबै प्याकेज तान्ने
    packages = TravelPackage.objects.all()

    # यदि सर्च गरेको छ भने प्याकेज मात्र खोज्ने
    if search_query:
        packages = packages.filter(title__icontains=search_query)

    context = {
        "packages": packages,
    }
    # यसले 'packages.html' भन्ने नयाँ पेज खोल्छ
    return render(request, "packages.html", context)


def add_to_cart(request, gear_id):
    # गियर भेट्ने
    gear = get_object_or_404(TrekkingGear, id=gear_id)

    # सेसनमा 'cart' भन्ने लिस्ट तान्ने, छैन भने खाली लिस्ट बनाउने
    cart = request.session.get("cart", [])

    # त्यो गियरको ID लाई कार्टमा थप्ने
    cart.append(gear.id)

    # अपडेट भएको लिस्टलाई फेरि सेसनमा सेभ गर्ने
    request.session["cart"] = cart

    # अनि युजरलाई कार्ट पेजमा लैजाने
    return redirect("cart_view")


def cart_view(request):
    cart_ids = request.session.get("cart", [])
    # कार्टमा भएको ID अनुसार गियरहरु तान्ने
    cart_items = TrekkingGear.objects.filter(id__in=cart_ids)

    return render(request, "cart.html", {"cart_items": cart_items})
