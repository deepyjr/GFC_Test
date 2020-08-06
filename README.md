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

If you remove somethings on a Class you have to run the 2 following commands:

 ```bash
 python .\manage.py makemigration
 python .\manage.py migrate 
```
