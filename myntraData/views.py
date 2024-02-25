from myntraData.models import *
from django.http import HttpResponse, JsonResponse
from myntraData.serializer import *
from myntraData.otp_utils import generate_otp, send_otp_via_sms
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django.core.cache import cache

@api_view(['GET'])
def send_otp(request,phone_number):
    if request.method == "GET":
        if phone_number:
            otp = generate_otp()
            # send_otp_via_sms(phone_number, otp)
            cache.set(otp, {'otp': otp, "phone_number":phone_number}, timeout=300)   
            return HttpResponse(otp)
        else:
            return HttpResponse("please enter the number correctly")

@api_view(['GET'])
def verify_otp(request, got_otp):
    if request.method == "GET":
        data = cache.get(got_otp)
        phone_number = data['phone_number']
        otp = data["otp"]
        print(phone_number, otp)
        if got_otp == got_otp:
            user, created = User.objects.get_or_create(phone_number=phone_number)
            return JsonResponse({'user_id': user.id, 'phone_number': phone_number}, status=200)
        else:
            return HttpResponse({'status': 'error', 'message': 'Invalid OTP'}, status=301)

@api_view(['GET']) 
def get_carousel(request):
    carousel_data = Carousel.objects.all()
    serializer = CarouselSerializer(carousel_data, many=True)
    return Response(serializer.data)
    
@api_view(["GET", "POST"])
def user_address(request):
    if(request.method == "GET"):
        user_address_data = UserAddress.objects.all()
        serializer = UserAddressSerializer(user_address_data, many=True)
        return Response(serializer.data)
    elif(request.method == "POST"):
        print("address", request.data)
        serializer = UserAddressSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"address saved successfully"}, status=201)
        else:
            return Response(serializer.errors, status=400)

@api_view(['GET'])
def users_userAddress(request, user_id):
    user_address_data = UserAddress.objects.filter(user=user_id)
    serializer = UserAddressSerializer(user_address_data, many=True)
    return Response(serializer.data)

@api_view(["GET",'PUT', "DELETE"])
def update_user_address(request,id):
    try:
        user_address_item = UserAddress.objects.get(id=id)
    except UserAddress.DoesNotExist:
        return Response({"error": "User address not found"}, status=404)
    if request.method == "PUT":
        print("data", request.data)
        serializers = UserAddressSerializer(user_address_item, data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=200)
        return Response(serializers.errors, status=400)
    elif request.method == "DELETE":
        user_address_item.delete()
        return Response({"message":"item removed successfully"}, status=201)
    
        
            
@api_view(['GET',"POST"])      
def wishlist(request):
    if request.method == "GET":
        wishlist_data = WishLists.objects.all()
        serializer = WishListSerializer(wishlist_data, many=True)
        return Response(serializer.data, status=201)
    elif request.method == "POST":
        serializer = WishListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Product added succesfully"}, status=201)
        return Response(serializer.errors)
 
@api_view(['GET'])
def user_wishlist(request,user_id):
    wishlist_data = WishLists.objects.filter(user=user_id)
    serializer = WishListSerializer(wishlist_data, many=True)
    return Response(serializer.data, status=201)
    
@api_view(['DELETE'])    
def update_wishlist(request,id):
    wishlist_item = WishLists.objects.filter(product_id=id).first()
    if wishlist_item:
        wishlist_item.delete()
        return Response({"message":"item removed successfully"}, status=201)
    else:
        return Response({"Error":"No such item in the wish list"}, status=400)

@api_view(['GET', "POST"])
def cart(request):
    if request.method == "GET":
        cart_data = CartItems.objects.all()
        serializer = CartItemSerializer(cart_data, many=True)
        return Response(serializer.data, status=201)
    elif request.method == "POST":
        print("data", request.data)
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Item Added successfully"},status=201)
        else:
            return Response(serializer.errors,status=400)
    
@api_view(["GET"])
def bag(request,user_id):
    cart_data = CartItems.objects.filter(user=user_id)
    serializer = CartItemSerializer(cart_data, many=True)
    return Response(serializer.data, status=201)

@api_view(["PUT","DELETE"])
def update_cart(request,id):
    cart_item = CartItems.objects.filter(product_id=id).first()
    if cart_item:
        cart_item.delete()
        return Response({"message":"item removed successfully"}, status=201)

@api_view(['GET',"POST"])
def comment(request):
    if request.method == "GET":
        comment = Comment.objects.all()
        serializers = CommentSerializer(comment, many=True)
        return Response(serializers.data, status=201)
    elif request.method == "POST":
        print("comment response", request.data)
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"comment added successfully"}, status=201)
        return Response(serializers.errors, status=400)
    
@api_view(["PUT"])
def update_comment(request,id):
    comment = Comment.objects.filter(id=id).first()
    if request.method == "PUT":
        serializers = CommentSerializer(comment, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        else:
            return Response(serializers.error, status=201)
        
    
    
@api_view(['GET',"POST"])
def rating(request):
    if request.method == "GET":
        rating = Rating.objects.all()
        serializers = RatingSerializer(rating, many=True)
        return Response(serializers.data, status=201)
    elif request.method == "POST":
        print(request.data)
        serializers = RatingSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message":"rating added successfully"}, status=201)
        return Response(serializers.errors, status=400)

@api_view(["GET", "POST"])
def category(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data, status=200)
    elif request.method == "POST":
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=200)
        return Response({"message":"comment is invalid"}, status=400)

@api_view(["GET", "POST"])
def category(request):
    if request.method == "GET":
        category = Search.objects.all()
        serializers = SearchSerializer(category, many=True)
        return Response(serializers.data, status=200)
    elif request.method == "POST":
        serializers = SearchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=200)
        return Response({"message":"comment is invalid"}, status=400) 

@api_view(["GET", "POST"])
def brand_category(request):
    if request.method == "GET":
        category = BrandCategory.objects.all()
        serializers = BrandCategorySerializer(category, many=True)
        return Response(serializers.data, status=200)
    elif request.method == "POST":
        serializers = BrandCategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=200)
        return Response({"message":"comment is invalid"}, status=400) 
    
@api_view(["GET"])
def bought_product(request,user_id):
    product = BoughtProduct.objects.filter(user=user_id)
    if product:
        serializers = BoughtProductSerializer(product, many=True)
        return Response(serializers.data, status=200)
    else:
        return Response("No products found for the user", status=404)
    
@api_view(["POST"])
def post_bought_product(request):
    print("request.data", request.data)
    serializer = BoughtProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)  
    return Response(serializer.errors, status=400) 
  
@api_view(["GET","POST"])   
def add_user_info(request, user_id):
    user = User.objects.filter(id=user_id)
    if user:
        if request.method == 'POST':
            print("user", request.data)
            serializers = UserSerializer(user, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=200)
            else:
                return Response(serializers.errors, status=301)
        elif request.method == "GET":
            serializers = UserSerializer(user, many=True)
            return Response(serializers.data, status=200)
    else:
        return Response({"message":"user not found"}, status=301)
  
@api_view(["POST"])
def user_info(request):
    print("userInfo", request.data)
    serializers = UserInfoSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({"message":"information added successfullly"}, status=200)
    else:
        return Response(serializers.errors, status=301)
    
@api_view(['GET', "PUT"])
def access_user_info(request, user_id):
    user = UserInfo.objects.get(user=user_id)
    if request.method == "GET":
        user_data = UserInfo.objects.filter(user=user_id)
        serializers = UserInfoSerializer(user_data, many=True)
        return Response(serializers.data, status=201)
    elif request.method == "PUT":
        print("user", request.data)
        serializers = UserInfoSerializer(user, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.errors, status=200)
        
          
       
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data = request.data)
        if serializers.is_valid():
            self.perform_create(serializers)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
