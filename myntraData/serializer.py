from rest_framework import serializers
from myntraData.models import *


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carousel
        fields="__all__"

class SizeFitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeFit
        fields = ["id","title"]

class MaterialCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialCare
        fields = ["id",'title',"product_detail"]

class ProductDetailSerializer(serializers.ModelSerializer):
    sizefit = SizeFitSerializer(many=True,required=False)
    materialcare = MaterialCareSerializer(many=True,required=False)
    class Meta:
        model = ProductDetail
        fields = "__all__"
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id","product","image","alt"]
  
class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ["id","product","size"]
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id',"user","product","img","message","date"]
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id","product","rating"]
        
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)
    size = ProductSizeSerializer(many=True, required=False)
    productDetails = ProductDetailSerializer(many=True, required=False)
    comments = CommentSerializer(many=True, required=False)
    ratings = RatingSerializer(many=True, required=False)
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images',[])
        sizes_data = validated_data.pop('size',[])
        product_details_data = validated_data.pop('productDetails',[])
        comments = validated_data.pop("comments",[])
        ratings = validated_data.pop("ratings",[])
        
        product = super().create(validated_data)

        for image_data in images_data:
            ProductImage.objects.create( **image_data, product=product)

        for size_data in sizes_data:
            ProductSize.objects.create( **size_data, product=product)

        for product_detail_data in product_details_data:
            size_fits_data = product_detail_data.pop('sizefit',[])
            material_care_data = product_detail_data.pop('materialcare',[])

            product_detail = ProductDetail.objects.create( **product_detail_data, product=product)

            for size_fit_data in size_fits_data:
                SizeFit.objects.create(**size_fit_data ,product_detail=product_detail )

            for material_care_data in material_care_data:
                MaterialCare.objects.create( **material_care_data, product_detail=product_detail)
        for comment in comments:
            Comment.objects.create(**comment, product=product)
        
        for rating in ratings:
            Rating.objects.create(**rating, product=product)
        
        return product


    

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAddress
        fields="__all__"

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model=WishLists
        fields="__all__"
    
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItems
        fields="__all__"
        
class ProductIdSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductId
        fields="__all__"
        
class BoughtProductSerializer(serializers.ModelSerializer):
    productIds = ProductIdSerializer(required=False, many=True)
    class Meta:
        model=BoughtProduct
        fields="__all__"
        
    def create(self, validated_data):
        productIds = validated_data.pop("productIds")
        bought_product = BoughtProduct.objects.create(**validated_data)
        
        for productId in productIds:
            ProductId.objects.create(bought_product=bought_product, **productId)
        
        return bought_product

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInfo
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    useraddress = UserAddressSerializer(many=True, required=False)
    wishlist = WishListSerializer(many=True, required=False)
    cartItem = CartItemSerializer(many=True, required=False)
    boughtproduct = BoughtProductSerializer(many=True, required=False)
    user_info = UserInfoSerializer(many=True, required=False)
    class Meta:
        model= User
        fields = "__all__"
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = "__all__"
        
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text']
        
class BrandCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandCategory
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = "__all__"
        
    def create(self,validated_data):
        choices = validated_data.pop("choices",[])
        question = Question.objects.create(**validated_data)
        for choice in choices:
            Choice.objects.create(**choice, question=question)
        return question