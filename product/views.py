from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.serializers import CategoryListSerializers, ProductListSerializers, ReviewListSerializers
from product.models import Category, Product, Review

# Create your views here.

@api_view(['GET'])
def category_list_api_view(request):
    # 1 Step: Get data from DB
    category = Category.objects.all()

    # 2 Step: Serialize data to dict
    data = CategoryListSerializers(category, many=True).data

    # 3 Step: Return dict as JSON
    return Response(data=data)

@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error_message': 'Category not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = CategoryListSerializers(category).data
    return Response(data=data)


@api_view(['GET'])
def product_list_api_view(request):
    # 1 Step: Get data from DB
    product = Product.objects.all()

    # 2 Step: Serialize data to dict
    data = ProductListSerializers(product, many=True).data

    # 3 Step: Return dict as JSON
    return Response(data=data)

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error_message': 'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ProductListSerializers(product).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    # 1 Step: Get data from DB
    review = Review.objects.all()

    # 2 Step: Serialize data to dict
    data = ReviewListSerializers(review, many=True).data

    # 3 Step: Return dict as JSON
    return Response(data=data)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error_message': 'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewListSerializers(review).data
    return Response(data=data)
