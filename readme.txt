Little Lemon Restaurant API

Make sure you have MySQL installed on your PC and create a database named LittleLemon. You should set the database configuration in the settings.py file as follows:

DATABASES = {   
    'default': {   
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'LittleLemon',   
        'USER': 'root',   
        'PASSWORD': 'laptop',   
        'HOST': '127.0.0.1',   
        'PORT': '3307',   
        'OPTIONS': {   
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"   
        }   
    }   
}

---

Accessing the Admin Panel
1. Open the admin panel at:
   http://127.0.0.1:8000/admin/

2. Admin credentials:
   - Username: admin
   - Password: password

---

Available Endpoints

1. Menu
- List all menu items:
  GET /restaurant/menu/
- Retrieve a specific menu item:
  GET /restaurant/menu/<id>/
- Create a new menu item:
  POST /restaurant/menu/
- Update an existing menu item:
  PUT /restaurant/menu/<id>/
- Delete a menu item:
  DELETE /restaurant/menu/<id>/

2. Table Booking
- List all bookings:
  GET /restaurant/booking/tables/
- Retrieve a specific booking:
  GET /restaurant/booking/tables/<id>/
- Create a new booking:
  POST /restaurant/booking/tables/
- Update an existing booking:
  PUT /restaurant/booking/tables/<id>/
- Delete a booking:
  DELETE /restaurant/booking/tables/<id>/

3. User Authentication
These endpoints manage user registration and authentication using Djoser:

- Login:
  POST /auth/login/
  Required Data:
  {
      "username": "<your_username>",
      "password": "<your_password>"
  }

- Logout:
  POST /auth/logout/

- Register a new user:
  POST /auth/users/
  Required Data:
  {
      "username": "<your_username>",
      "password": "<your_password>",
      "email": "<your_email>"
  }

- Retrieve authentication token:
  POST /auth/token/login/

- Remove authentication token:
  POST /auth/token/logout/

---

Running Unit Tests
To execute the unit tests, run:
python manage.py test

---

Testing the API
You can test the above endpoints using Postman or Insomnia.
