from django.shortcuts import render
import requests

# Create your views here.
def homepage_view(request):
    
    context = {}

    #creating new user
    newuser = {
        "email": "mockuser2@gmail.com",
        "name": "mock user2",
        "password": "jaswanth"
        }
    response = requests.post('http://127.0.0.1:8000/account/api/profile_api/', data=newuser)
    post_new_user = response.json()
    context['post_new_user'] = post_new_user


    #creating duplicate user
    duplicateuser = {
        "email": "mockuser2@gmail.com",
        "name": "mock user2",
        "password": "jaswanth"
        }
    response = requests.post('http://127.0.0.1:8000/account/api/profile_api/', data=duplicateuser)
    post_duplicate_user = response.json()
    context['post_duplicate_user'] = post_duplicate_user


    #logging user in to get token
    login = {
        "username": "mockuser2@gmail.com",
        "password": "jaswanth"
        }
    response = requests.post('http://127.0.0.1:8000/account/api/login/', data=login)
    login_token = response.json()
    context['login_token'] = login_token


    #edit user without token authentication
    edituser = {
        "email": "edited@gmail.com",
        "name": "edited name",
        "password": "jaswanth"
        }
    id = context['post_new_user']['id']
    response = requests.put(f'http://127.0.0.1:8000/account/api/profile_api/{id}/', data=edituser)
    edit_without_token = response.json()
    context['edit_without_token'] = edit_without_token


    #edit current token user
    edituser = {
        "email": "edited@gmail.com",
        "name": "edited name",
        "password": "jaswanth"
        }
    token = context['login_token']['token']
    idd = context['post_new_user']['id']
    headers={'Authorization': f'Token {token}'}
    response = requests.put(f'http://localhost:8000/account/api/profile_api/{idd}/', data=edituser, headers=headers )
    edit = response.json()
    context['edit'] = edit



    #edit different user profile
    edit_different_user = {
        "email": "edited@gmail.com",
        "name": "edited name",
        "password": "jaswanth"
        }
    token = context['login_token']['token']
    headers={'Authorization': f'Token {token}'}
    response = requests.put(f'http://localhost:8000/account/api/profile_api/2/', data=edit_different_user, headers=headers)
    edit_different_user = response.json()
    context['edit_different_user'] = edit_different_user


    #delete user without token authentication
    a=context['post_new_user']
    a = a['id']
    response = requests.delete(f'http://127.0.0.1:8000/account/api/profile_api/{a}')
    delete_without_token = response.json()
    context['delete_without_token'] = delete_without_token


    #delete current token user
    a = context['login_token']['token']
    b = context['post_new_user']['id']
    headers={'Authorization': f'Token {a}'}
    response = requests.delete(f'http://localhost:8000/account/api/profile_api/{b}', headers={'Authorization': 'Token {}'.format(a)})
    # delete = {}
    context['delete'] = {'status':response.status_code}


    #delete different user profile
    a = context['login_token']['token']
    headers={'Authorization': f'Token {a}'}
    response = requests.delete(f'http://localhost:8000/account/api/profile_api/1', headers=headers)
    delete_different_user = response.json()
    context['delete_different_user'] = delete_different_user

    print(context)
    return render(request, "apimock/home.html", context=context)



def shop_view(request):
    context = {}

    #list of endpoints
    response = requests.get('http://127.0.0.1:8000/shop/api/')
    endpoints = response.json()
    context['endpoints'] = endpoints


    #carts, addresses, orders associated with current logged in user
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.get(f'http://localhost:8000/shop/api/account', headers=headers)
    current_user = response.json()
    context['current_user'] = current_user
    
    
    #all products
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.get(f'http://localhost:8000/shop/api/products', headers=headers)
    products = response.json()
    context['products'] = products

    #add new product as staff user
    new_product = {"product_name": "Mock Product",
        "category": 5,
        "status": "ABC",
        "our_price": "10000.00",
        "original_price": "12345.00",
        "image_url": "a",
        "origianl_url": "mock",
        "html": "mock",
        "options": "mock"}
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.post(f'http://localhost:8000/shop/api/products/', data=new_product, headers=headers)
    add_new_product = response.json()
    context['add_new_product'] = add_new_product
    

    # add product without permission
    new_product = {"product_name": "Mock Product",
        "category": 5,
        "status": "ABC",
        "our_price": "10000.00",
        "original_price": "12345.00",
        "image_url": "a",
        "origianl_url": "mock",
        "html": "mock",
        "options": "mock"}
    headers={'Authorization': 'Token 5fb00f809f3b218b3354372d64edfbae164ba087'}
    response = requests.post(f'http://localhost:8000/shop/api/products/', data=new_product, headers=headers)
    add_without_permission = response.json()
    context['add_without_permission'] = add_without_permission
    

    # delete product
    url = context['add_new_product']['url']
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.delete(f'{url}', headers=headers)
    context['delete'] = {'status':response.status_code}
    
    # carts of current user
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.get(f'http://localhost:8000/shop/api/cart', headers=headers)
    cart = response.json()
    context['cart'] = cart
    

    # addresses of current user
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.get(f'http://localhost:8000/shop/api/addresses', headers=headers)
    address = response.json()
    context['address'] = address
    

    # orders placed by current user
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.get(f'http://localhost:8000/shop/api/orders', headers=headers)
    orders = response.json()
    context['orders'] = orders

    
    print(context)
    return render(request, "apimock/shop.html", context=context)


def travelpartner_view(request):
    context = {}

    # list of travel partner registrations
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.get(f'http://localhost:8000/travelpartner/api/travelpartner', headers=headers)
    listAll = response.json()
    context['listAll'] = listAll


    # register yourself
    new_registration = {
        "user": '1',
        "name": "mockuser",
        "start_date": '2020-12-22',
        "end_date": '2020-12-22',
        "destination": "mock",
        "description": "mock",
        "phone": "123"
        }
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.post(f'http://localhost:8000/travelpartner/api/travelpartner/', data=new_registration, headers=headers)
    newReg = response.json()
    context['newReg'] = newReg


    # edit info
    edit = {
        'name' : 'edited name',
        'destination' : 'edited destination',
        'description' : 'edited description'
    }
    url = context['newReg']['url']
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.patch(f'{url}', data=edit, headers=headers)
    edit = response.json()
    context['edit'] = edit


    # edit different person's info
    edit = {
        'name' : 'edited name',
        'destination' : 'edited destination',
        'description' : 'edited description'
    }
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.patch("http://127.0.0.1:8000/travelpartner/api/travelpartner/5/", data=edit, headers=headers)
    edit_different_person = response.json()
    context['edit_different_person'] = edit_different_person



    # delete new registration
    url = context['newReg']['url']
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.delete(f'{url}', headers=headers)
    context['delete'] = {'status':response.status_code}



    # delete different registration
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.delete(f'http://127.0.0.1:8000/travelpartner/api/travelpartner/5/', headers=headers)
    context['delete_different'] = response.json()

    print(context)
    return render(request, "apimock/travelpartner.html", context=context)


def crowdfund_view(request):
    context = {}

    # list of travel partner registrations
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.get(f'http://localhost:8000/crowdfund/api/fund', headers=headers)
    listAll = response.json()
    context['listAll'] = listAll


    # register yourself
    new_registration = {
        "user": '1',
        "title": "mock",
        "description": "mock",
        "date_goal": '2021-12-22',
        "amount_goal": "2000"
        }
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.post(f'http://localhost:8000/crowdfund/api/fund/', data=new_registration, headers=headers)
    newReg = response.json()
    context['newReg'] = newReg


    # edit info
    edit = {
        'title' : 'edited title',
        'description' : 'edited description'
    }
    idd = context['newReg']['id']
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.patch(f'http://localhost:8000/crowdfund/api/fund/{idd}/', data=edit, headers=headers)
    edit = response.json()
    context['edit'] = edit


    # edit different person's info
    edit = {
        'name' : 'edited name',
        'destination' : 'edited destination',
        'description' : 'edited description'
    }
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.patch("http://localhost:8000/crowdfund/api/fund/1/", data=edit, headers=headers)
    edit_different_person = response.json()
    context['edit_different_person'] = edit_different_person



    # delete new registration
    idd = context['newReg']['id']
    headers={'Authorization': 'Token 6f3a6f7564ab2524e595572875d2241b62d44804'}
    response = requests.delete(f'http://localhost:8000/crowdfund/api/fund/{idd}/', headers=headers)
    context['delete'] = response.status_code

    print(context)
    return render(request, "apimock/crowdfund.html", context=context)