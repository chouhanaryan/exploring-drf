# exploring-drf

This is a project exploring the Django-Rest-Framework with Djoser.

Through the project, I created Function-based views, Class-based views, Class-based views for Serialized Models, Generic views for Serialized Models and Viewsets. In the final code, everything except the Viewsets is commented out. Relevant URLs and code can be uncommented to explore different functionality as well.

## Installation

First, clone the repository and create a virtual environment. Install all dependencies and start the server.

```bash
git clone https://github.com/chouhanaryan/exploring-drf.git
cd .\exploring-drf\
pipenv shell
pipenv install
cd .\drf\
python manage.py runserver
```

## Usage

- **Root**

```GET``` ```/```

_Response_ - URLs of main API structure

- **Login**

```POST``` ```/auth/token/login/```

_Response_ - Returns authorization token

_Body_ - Password, Email

- **Logout** _(Authentication Required)_

```POST``` ```/auth/token/logout/```

_Response_ - None

- **Users** _(Authentication Required)_

```GET``` ```/auth/users/```

_Response_ - Detailed list of all users

- **Users** _(Authentication Required)_

```POST``` ```/auth/users/```

_Response_ - Register a new user

_Body_ - Username, First name, Last name, Email, Password, Re password

- **Person** _(Authentication Required)_

```GET | POST | PUT | DELETE``` ```/person/```

_Response_ - Detailed list of all people registered

_Body_ - Name, Email, DOB, Age, ID (as and when required)

- **Person (ID)** _(Authentication Required)_

```GET``` ```/person/<id>```

_Response_ - Details of specific person by ID

- **House** _(Authentication Required)_

```GET | POST | PUT | DELETE``` ```/house/```

_Response_ - Detailed list of all houses registered

_Body_ - Loc, Owner (URL), pin (unique), ID (as and when required)

- **House (ID)** _(Authentication Required)_

```GET``` ```/house/<id>```

_Response_ - Details of specific house by ID

## Notes

To explore the API, use Postman or any other API development platforms.

**Administrator login credentials**: 

_email_: ```admin@admin.com```

_password_: ```admin```

**User login credentials**: 

_email_: ```test1@admin.com``` / ```test2@admin.com```

_password_: ```Aryan123```

Login using any of these by sending the appropriate request to the API, and you shall receive an authorization token. Now, include this token as a header (_format_: ```Authorization: Token <token>```) to send requests that require authorization.

The administrator credentials can also be used to manually add people, houses, users and generate tokens via the Django admin panel.

Documentation for additional functionality can be accessed at the [Djoser docs](https://djoser.readthedocs.io/en/latest/).
