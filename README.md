# Room Rate Management API

This project is a Room Management API built with Django and Django Rest Framework (DRF). It manages room rates, overridden rates, and discounts, and provides an endpoint to calculate the lowest room rates for specific dates.

## Features

- **Room Rates Management**: Create, update, delete, and list room rates.
- **Overridden Rates Management**: Create, update, delete, and list overridden rates for specific dates.
- **Discounts Management**: Create, update, delete, and list discounts.
- **Lowest Rates Calculation**: Calculate the lowest room rate for specific dates considering overridden rates and discounts.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- PostgreSQL

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/Room-management-api.git
    cd Room-management-api
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database:**

    Create a database named `room_rate_management` in PostgreSQL and update the database configuration in `settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'room_rate_management',
            'USER': 'yourusername',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. **Apply the migrations:**

    ```sh
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

8. **Access the admin panel:**

    Open your web browser and go to `http://127.0.0.1:8000/admin/`. Use the superuser credentials to log in.

### API Documentation

The project uses Swagger for API documentation. You can access it at:

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **Redoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

### Usage

#### Room Rates Management

- **Create Room Rate**: POST `/api/roomrates/`
- **Update Room Rate**: PUT `/api/roomrates/{id}/`
- **Delete Room Rate**: DELETE `/api/roomrates/{id}/`
- **List Room Rates**: GET `/api/roomrates/`

#### Overridden Rates Management

- **Create Overridden Rate**: POST `/api/overriddenroomrates/`
- **Update Overridden Rate**: PUT `/api/overriddenroomrates/{id}/`
- **Delete Overridden Rate**: DELETE `/api/overriddenroomrates/{id}/`
- **List Overridden Rates**: GET `/api/overriddenroomrates/`

#### Discounts Management

- **Create Discount**: POST `/api/discounts/`
- **Update Discount**: PUT `/api/discounts/{id}/`
- **Delete Discount**: DELETE `/api/discounts/{id}/`
- **List Discounts**: GET `/api/discounts/`

#### Lowest Rates Calculation

- **Get Lowest Rates**: GET `/api/lowest-rates/{room_name}/{start_date}/{end_date}/`
  - Example: `/api/lowest-rates/Deluxe%20Suite/2024-07-01/2024-07-10/`


## Acknowledgments

- Django and Django Rest Framework documentation
- Swagger and drf-yasg documentation

