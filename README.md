# #ticketing_system
# #this Django app allow usr to create tickests, update it and search it

# #before running this app, please run following commands to setup tables in your database(sqllite):
python manage.py makemigrations
python manage.py migrate --run-syncdb

# #run this application using following command:
python manage.py runserver 8003

# #now you can view tickets in URL:
http://127.0.0.1:8003/ticket/

# #you can search tickets by category by selecting a category

# #you can add new tickets by clicking Add New.

# #you can edit ticket details by clicking on the title of ticket and it will redirect to edit page.
