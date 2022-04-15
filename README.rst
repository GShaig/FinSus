=====
FinSus
=====

FinSus is Financial Sustainability App built in Python by Shaig Gafarli.

Nowadays, people change their jobs and positions very often and usually take several months long brakes before they jump in to their next opportunity. Financial Sustainability App (FinSus) will take your savings and daily expenses as input, save into the database and calculate how many days you would survive in these conditions.

Quick start
-----------

1. Add "finsus" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'finsus',
    ]

2. Include the finsus URLconf in your project urls.py like this::

    path('finsus/', include('finsus.urls')),

3. Run ``python manage.py migrate`` to create the finsus models.

4. Start the development server and visit http://127.0.0.1:8000/finsus/ to answer questions and see your result!

FinSus App was deployed to Heroku.
Please visit: https://finsus.herokuapp.com/
