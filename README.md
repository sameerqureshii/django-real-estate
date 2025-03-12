# Django Real Estate CRUD Application

## Introduction
This is a simple Django CRUD (Create, Read, Update, Delete) application for managing real estate properties. The project allows users to add, view, update, and delete property listings.

## Features
- Add new property listings
- View all properties
- Update property details
- Delete property listings

## Installation
### Prerequisites
- Python (>=3.8)
- Django (>=4.0)
- SQLite database

### Steps
1. Clone the repository:
   ```sh
   git clone http://github.com/sameerqureshii/django-real-estate/.git
   cd real_estate
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure database settings in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': 'real_estate',
           'USER': 'admin@example.com',
           'PASSWORD': 'estate123',
           'HOST': 'localhost',
           'PORT': '8000',
       }
   }
   ```
5. Run migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```sh
   python manage.py runserver
   ```
8. Access the application at `http://127.0.0.1:8000/`

## Usage
- Navigate to the admin panel (`/admin`) to manage properties.
- Visit the `/properties/` endpoint to view all property listings.
- Use forms to add, edit, or delete properties.

## Models
The application includes a `Property` model with the following fields:
- `title`: CharField
- `description`: TextField
- `price`: DecimalField
- `location`: CharField
- `image`: ImageField

## API Endpoints (Optional)
| Method | Endpoint       | Description |
|--------|---------------|-------------|
| GET    | /properties/  | List all properties |
| POST   | /properties/add/ | Add a new property |
| GET    | /properties/<id>/ | View property details |
| PUT    | /properties/edit/<id>/ | Update property details |
| DELETE | /properties/delete/<id>/ | Delete property |

## Contributing
Feel free to fork this repository, submit issues, and contribute improvements.

## License
This project is open-source and available under the MIT License.
