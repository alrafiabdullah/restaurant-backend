# Restaurant Backend

##

### Endpoints

> POST - http://127.0.0.1:8000/api/v1/register

> POST - http://127.0.0.1:8000/api/v1/login

> POST - http://127.0.0.1:8000/api/v1/checkout

> POST - http://127.0.0.1:8000/api/v1/token

> POST - http://127.0.0.1:8000/api/v1/token/refresh

> POST - http://127.0.0.1:8000/api/v1/token/verify

> GET - http://127.0.0.1:8000/api/v1/food

> GET - http://127.0.0.1:8000/api/v1/coupon

> GET - http://127.0.0.1:8000/api/v1/checkout/user

> GET - http://127.0.0.1:8000/api/v1/customer

> GET - http://127.0.0.1:8000/api/v1/category

### Requirements

1. Go to the root directory of the program with CMD/your preferred terminal.
2. Create and activate a virtual environment.
3. Run `pip install -r requirements.txt`.
4. Run `python manage.py runserver`.
5. For local network deployment `python manage.py runserver 0.0.0.0:{port_number}`.

### Functionalities

- Retrieve existing user
- Registers new user
- Login existing user
- Detailed menu list
- Discount coupon verification
- Online checkout
- User checkouts
- Verify user is customer
- Category list
- JWT token retrieve
- JWT token refresh
- JWT token verify

##

#### **Retrieve existing user - GET**

1. Parameter
   - id (int)
2. Authenticate the request with a Bearer token
3. Serializes data in the following format:
   "user": {
   "id": int,
   "last_login": datetime,
   "is_superuser": boolean,
   "username": string,
   "first_name": string,
   "last_name": string,
   "email": string,
   "is_staff": boolean,
   "is_active": boolean,
   "date_joined": datetime,
   "groups": JSONArray,
   "user_permissions": JSONArray
   }
4. Returns the information as JSON.

##

#### **Registers new user - POST**

1. Parameters
   - username(string, unique)
   - email(string, unique)
   - password
   - confirm_password
2. Serializes data in the following format:
   "user": {
   "id": int,
   "last_login": datetime,
   "is_superuser": boolean,
   "username": string,
   "first_name": string,
   "last_name": string,
   "email": string,
   "is_staff": boolean,
   "is_active": boolean,
   "date_joined": datetime,
   "groups": JSONArray,
   "user_permissions": JSONArray
   }
3. Returns the information as JSON.

##

#### **Login existing user - POST**

1. Parameters
   - username(string)
   - password
2. Serializes data in the following format:
   "user": {
   "id": int,
   "last_login": datetime,
   "is_superuser": boolean,
   "username": string,
   "first_name": string,
   "last_name": string,
   "email": string,
   "is_staff": boolean,
   "is_active": boolean,
   "date_joined": datetime,
   "groups": JSONArray,
   "user_permissions": JSONArray
   }
3. Returns the information as JSON.

##

#### **Detailed menu list - GET**

1. Serializes data in the following format:
   "int": {
   "name": string,
   "image": string,
   "price(BDT)": int,
   "preparation_time(minutes)": int,
   "category": string
   }
2. Returns the information as JSON.

##

#### **Discount coupon verification - GET**

1. Parameter
   - name(string)
2. Authenticate the request with a Bearer token
3. Serializes data in the following format:
   {
   "name": string,
   "percentage": int,
   "duration(days)": int,
   "status": boolean,
   "created_at": datetime
   }
4. Returns the information as JSON.

##

#### **Online checkout - POST**

1. Parameters
   - user_id(int)
   - items([int])
   - total(int)
   - address(string)
2. Authenticate the request with a Bearer token
3. Serializes data in the following format:
   {
   "order": string
   }
4. Returns the information as JSON.

##

#### **User checkouts - GET**

1. Parameter
   - user_id(int)
2. Authenticate the request with a Bearer token
3. Serializes data in the following format:
   "string": {
   "number": string,
   "total": int,
   "items": [JSONArray],
   "address": string,
   "ordered_at": datetime
   }
4. Returns the information as JSON.

##

#### **Verify user is customer - GET**

1. Parameter
   - user_id(int)
2. Authenticate the request with a Bearer token
3. Serializes data in the following format:
   {
   "customer": boolean
   }
4. Returns the information as JSON.

#### **Category list - GET**

1. Serializes data in the following format:
   "int": {
   "id": int,
   "name": string
   }
2. Returns the information as JSON.

##

#### **JWT token retrieve - POST**

1. Parameters
   - username(string)
   - password
2. Serializes data in the following format:
   {
   "refresh": string,
   "access": string
   }
3. Returns the information as JSON.

##

#### **JWT token refresh - POST**

1. Parameter
   - refresh(string)
2. Serializes data in the following format:
   {
   "access": string
   }
3. Returns the information as JSON.

##

#### **JWT token verify - POST**

1. Parameter
   - token(string)
2. Serializes data in the following format:
   {}
3. Returns the information as JSON.

##

### Contributions

- Please create pull request on the development branch
