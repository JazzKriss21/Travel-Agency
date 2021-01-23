# Travel Agency 
It is a Django Rest Framework based website targetted at tourists. 
It is concentrated at Service Oriented Architecture. Hence, as many as 4 RESTful APIs have been exposed and 7 APIs have been consumed.

## Features for users

- Search Flight Details
- Search Hotel Details
- Rent Travel Products
- Crowdfunding Travel Expenses
- Find a Travel Partner
- Weather
- Stripe for Secure Payments
- Github and Google Authentication

## Mock Server Application (Django)
A Django based Mock Application to show the implementation, working, and permissions of the exposed APIs.

#### To Run the Mock Application
Go to the 'app' directory and run:
```bash
python manage.py runserver 8000
```
Open another shell and go to 'mock' directory and run:
```bash
python manage.py runserver 4000
```
To see the mock application, go to localhost:4000 on your web browser.
