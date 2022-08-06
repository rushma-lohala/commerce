from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .models import FIELD_CHOICE



# Create your views here.
def index(request):
    categories=Category.objects.all()
    product=Product.objects.all()
    context={'categories':categories,'product':product}
    return render(request,'index.html')


def product_insert(request):
    categories=Category.objects.all()
    products=Product.objects.all()
    
    if request.method=='POST':
        product_name=request.POST["name"]
        product_price=request.POST["price"]
        product_type=request.POST["product_type"]
        is_active=request.POST.get("is_active")
        if is_active == 'on':
            is_active= True
        else:
            is_active= False
        
        errors={}
        try:
            """
                Checking if the category exists in database or not
            """
            product_category=Category.objects.get(id =request.POST.get('category'))
        except Category.DoesNotExist as e:
            errors["product_category"]=f"Category Does Not Exist {e}"
        # if is_active == 'on':
        #     is_active= True
        # else:
        #     is_active= False
        if  len(product_name)<=0 or len(product_name)>200 or len(product_name)<3 : 
            # errors.append({
            #     "name":"name is required which characters is less than 200"
            # })
            errors["name"]="name is required which characters is greater than 3 and less than 200"
            # name_error=messages.info(request,' ')
        
      


        if type(product_price)!=float and len(product_price)<=0.00:
            # price_error=messages.errors(request,'price is required')
            # errors.append({
            #     'price': "price is must be required"
            # })
            errors["price"]="price must be required"

        if not (product_type, product_type) in FIELD_CHOICE:
            errors["type"]="this is not is not valid product type"

        # if product_category!=categories:
        #     errors["category"]="this is not is not valid category"
        

        if len(errors)>0:
            return render(request,'product/product.html',context={"errors":errors,'categories':categories,'product_choices':FIELD_CHOICE})
    
        else:
            post=Product(name=product_name,price=product_price,product_type=product_type,is_active=is_active,category=product_category)
            post.save()

            messages.success(request,'sucessfully send!')
            return redirect('product-list')
        # else:
        #     messages.info(request,'all fields are required')
        #     return redirect('/products/insert/')  
      
    context={'categories':categories,'products':products,"product_choices":FIELD_CHOICE}
    return render(request,'product/product.html',context)

     
def category_insert(request):
    if request.method=='POST':
        category_name=request.POST["name"]   
        post=Category(name=category_name)
        post.save()
         
    return render(request,'product/category.html')

def product_list(request):
    products=Product.objects.all() 
    context={'products':products}

    return render(request,"product/product_list.html",context)
   
"""
        queries:
            - get() -> single value return , 
                        if not fount returns DoesNotExist exception
            - all() -> returns all the tuples in database

            - filter() -> returns the values that match the patameter
     """     

def product_detail(request,slug):
    product=Product.objects.get(slug=slug)
    return render(request,"product/product_detail.html",context={"product":product})
    
     

    
