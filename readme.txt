This is a simple Django API web app for a resturant it has the following APIs:


resturant/booking (list bookings)

resturant/booking/create (create new booking)

resturant/menu/<int:pk> (view or delete a specific menuitem)

resturant/menu/items (list all menu items)

To run the project open the folder in VS Code (after installing python, django and making a virtural environment)  and edit the Database settings
in the settings.py of the project folder to match your database and then run: 
Python manage.py makemigrations
Python manage.py migrate
Python manage.py runserver 

