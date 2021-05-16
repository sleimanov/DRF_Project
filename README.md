# Kolesa  
### About project
Wheels is a clone of the Kazakhstan website Kolesa.kz
The service allows people to easily sell/buy any submitted cars quickly and conveniently
You can view all the ads, and filter the results by the necessary criteria, such as, year of manufacture, car brand, etc.


# Features
* Registering a new user
* Login / Logout
* Ability to add new car brands
* Adding car body options
* Adding models of a specific brand
* The user can view all the ads
* Filtering ads by selected criteria
* Changes to the entered data
* Ability to add publications to your Favorites

# UML diagram
![](https://github.com/sleimanov/DRF_Project/blob/main/UML%20diagram.png)

# Used technologies
When developing the service, the Django backend framework was chosen
This is a very popular and multifunctional tool for quickly building large and small systems

# Virtual Env
Create local virtual env with ```virtualenv venv```

Then install all project requirements with ```pip freeze -r requirements.txt```

# Build and Run
For applying current migrations run ```python manage.py migrate```

Then run application with ```python manage.py runserver```
