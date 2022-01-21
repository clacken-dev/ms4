from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Review
from orders.models import Testimonial

from .forms import ReviewForm
# Create your views here.


def all_products(request):
    """ A view to show all products """
    testimonies = Testimonial.objects.all()

    products = Product.objects.all()

    context = {
        'products': products,
        'testimonies': testimonies,
    }

    return render(request, 'products/products2.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    # Pass the review form to the template
    form = ReviewForm()
    # get all reviews for this product
    reviews = Review.objects.filter(product=product)
    
    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
        
    }

    return render(request, 'products/product_detail2.html', context)


@login_required
def add_review(request, product_id):
    """Add a review to a specific product on the product details page"""

    if request.method == "POST":
        # Get the product currently displayed
        product = get_object_or_404(Product, pk=product_id)
        # create a form to review product
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.workout = workout
            review.user = request.user
            review.save()
            messages.success(request, "Review submitted successfully!")
            return redirect(
                reverse("product_detail", kwargs={"product_id": product_id})
            )

    # If not a POST request then display the form to enter review
    else:
        form = ReviewForm()

    # Render the template depending on the context
    return render(
        request, "products/add_review.html", {"form": form, "product_id": product_id}
    )