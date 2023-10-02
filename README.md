# Drunk Ninja
Simple tienda de licor contruida con `Django` python framework.

</br>
</br>

## Recursos
- [Django Framework](https://www.djangoproject.com/)
- [Django Store - YuriiDorosh](https://github.com/YuriiDorosh/django-store)
- [Hot Food - shyam999](https://github.com/shyam999/Hot-Food)
- [Django Ecommerce- shyam999](https://github.com/shyam999/Django-ecommerce)
- [Profiles And Groups In Django](https://www.scaler.com/topics/django/profiles-and-groups-in-django/)
- [Django Permissions](https://testdriven.io/blog/django-permissions/)

</br>
</br>

## Testea Webpay (Test Mode)
La clave para el rut y visa es la misma

```
Credit Cart (Visa): 4051885600446623
Ex. Date: Any Valid Date
Rut: 11.111.111-1
Password: 123
```

</br>
</br>

## Instalacion
1. Clone the Repo
```
git clone https://github.com/MaximilianoMO95/DrunkNinja
```

</br>

2. Install Dependencies
```
pip install django
pip install python-dotenv
pip install Pillow
pip install djangorestframework
pip install requests
pip install django-recaptcha
```

</br>

3. Set your `.env` file (you can use open ssh to generate a key)
```
SECRET_KEY='django-insecure-uo3kkl61h0w5eh$2%n*5ndv4(i)=t3^6q+biiz9-s2&3zt3esm'
```

</br>

4. Migrate The Database
```
python manage.py makemigrations
python manage.py migrate
```

</br>

5. Start The Server
```
python manage.py runserver
```

</br>
</br>

## Usar Oracle (Opcional)
1. Install oracle driver
```
pip install cx-Oracle
```

</br>

2. Set your `.env` file (after that start oracle db)
```
ORACLE_DB_NAME='drunkNinja'
ORACLE_USER='ninja'
ORACLE_PASSWORD='Insecure007'
ORACLE_HOST='localhost'
ORACLE_PORT='1521'
```

</br>

3. Migrate The Database
```
python manage.py makemigrations
python manage.py migrate --database oracle_db
```

</br>

4. Start The Server
```
python manage.py runserver
```
