# [EVENTS-APP](https://events-app-uhp8.onrender.com)


## This is a EVENTS-APP site project built with  **Django** that includes a publicly accessible personal site and events creation by registered users.
> Actively supported by [ @SoftUni ](https://softuni.bg/"). Many thanks on [@Doncho Minkov ](https://github.com/donchominkov) for your help.

<br>

## This is a site `Home page`
![home_page]()

<br />

## This is a `Register` page
![signup]()


<br />

## This is a `Profile page`
![profile_details]()

<br />

## This is a `Profile edit` page
![profile_edit]()

<br />

## This is a `Add EVENT` page if user is registered
![add_event]()

<br />

## This is a `EVEN DETAIL` page for personal events created by users
![user_content]()

<br />

## This is a `EVEN DETAIL` page for public events
![public_content]()

## How to use it
<br />

> **Install the package** via `PIP` 

```bash
$ Use the pip install -r requirements.txt command 
// OR
$ pip install git+https://github.com/ivanmarinoff/Events-app.git
```

<br />

> Use command `venv\Scripts\activate` in to terminal to create `venv` file of your Django project directory!

<br />

> **Start the app**
>:

```bash
$ # Set up the SQLite database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

Access the `admin` section in the browser: `http://127.0.0.1:8000/`
<br />
