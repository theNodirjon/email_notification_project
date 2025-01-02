# Django Email Notification Project

## Maqsad
Foydalanuvchi xabarlari yaratilganda avtomatik email yuborish.

## Loyihaning Tuzilishi
- **Model:** UserNotification
- **Signal:** Yangi model instansi qo'shilganda avtomatik email yuborish.
- **Email Backend:** Konsolda email aks ettirish.

## Ishga Tushirish
1. Virtual muhit yarating:
   ```bash
   python -m venv venv
   source venv/bin/activate


## ✅ **Qo'shimcha Topshiriq (Cron Job / Celery)**

**Celery yordamida kundalik xat yuborish**:  

1. Celery va Redis o'rnating:  
   ```bash
   pip install celery redis