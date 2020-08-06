# GFC_Test
 Django App Blog


## Run the project
To run the project you have to be in the testDatadict directory.

Open a terminal and run the following command, it create a SQLITE database (you can open and manage it with DB Browser link : https://sqlitebrowser.org/).

 ```bash
 python .\manage.py migrate 
```

You can create  super admin to get the acces to the admin dashboard with the following command :
 
 ```bash
 python .\manage.py createsuperuser  
```

Dashboard address : http://127.0.0.1:8000/admin ( localhoast )

You can manage everythings on it.

To run the project:
 ```bash
 python .\manage.py runserver
```

If you remove somethings in classes you have to run the 2 following commands:

 ```bash
 python .\manage.py makemigration
 python .\manage.py migrate 
```
## Use the project

To use the project you have to create a user you have 2 options here :
 - register by the super admin command (it work with the both logins)
 - register by the normal way to get a simple user
 
The filter for the date in the home page shall be used like that :

 month/day/year
 
 
