<img src="https://media.tenor.com/mGgWY8RkgYMAAAAC/hello-world.gif" width="100%" style="border-radius: 5px;" />

# Django Email Notification Project 🚀

## Maqsad
Foydalanuvchi xabarlari qo'shilganda avtomatik email yuborish va Celery yordamida cron joblarni ishlatish.

## Ishga Tushirish
1. Virtual muhitni yarating va faollashtiring:
    ```
    python -m venv venv
    source venv/bin/activate
    ```
2. Kutubxonalarni o'rnating:
    ```
    pip install -r requirements.txt
    ```
3. Migratsiya bajaring:
    ```
    python manage.py migrate
    ```
4. Serverni ishga tushiring:
    ```
    python manage.py runserver
    ```
5. Celery va Redis-ni ishga tushiring:
    ```
    redis-server
    celery -A email_notification_project worker --loglevel=info
    celery -A email_notification_project beat --loglevel=info
    ```
   Menda Redis ishga tushmadi.

## Qo‘shimcha
- Admin panel: `http://127.0.0.1:8000/admin/`
- Email backend: Konsolda chiqariladi.
