# **Carsoko App Clone** - *Backend*

## Description

- This project aims to clone the [Carsoko](https://www.carsoko.co.ke/) App. The project is built using Django and the Django Rest Framework.

- It is a simple CRUD API that allows users view the different cars available. However, only the admin can add, update and delete cars but this can be changed in the permissions section of the admin site.

- The Database Schema is as shown below:

    <iframe width="560" height="315" src='https://dbdiagram.io/embed/6493d57702bd1c4a5ee1430a'> </iframe>

- All app permissions, including creating new users, are handled by the admin on the admin site.

---

## Setup/Installation Instructions

1. Clone the repository

2. Install the project requirements using the command below:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file and add the following configurations:

    ```bash
    SECRET_KEY='<your_secret_key>'
    DEBUG=True
    ```

4. Run the migrations using the following commands:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser account using the command below: (follow the prompts)

    ```bash
    python manage.py createsuperuser
    ```

6. Run the server using the command below:

    ```bash
    python manage.py runserver
    ```

7. Open the browser and navigate to [`localhost:8000/admin`](localhost:8000/admin) to access the admin site (login with your superuser credentials) and [`localhost:8000/apis/`](localhost:8000/apis/) to access the API endpoints on the browsable API.

8. On the admin site, you can add new cars, features and images. You can also assign permissions to users as group or individual permissions.

9. On the browsable API, you can view the cars, features and images. You can also add new cars, features and images.
