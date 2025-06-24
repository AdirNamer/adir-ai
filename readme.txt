📦 פרויקט ADIR AI - גרסה מלאה:
- בוט טלגרם
- דשבורד גרפי
- ניהול פקודות מרחוק

להפעלה:
1. הוסף משתנה TELEGRAM_TOKEN ב-Render
2. העלה את כל הקבצים ל-GitHub
3. ב-Render:
   Build command: pip install -r requirements.txt
   Start command: gunicorn main:app
4. הגדר Webhook בטלגרם:
   https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=https://YOUR_RENDER_URL/webhook