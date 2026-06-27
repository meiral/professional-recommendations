import re
import json
from collections import Counter

def update_data():
    # פתיחת קובץ הוואטסאפ בקידוד UTF-8
    try:
        with open('_chat.txt', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("קובץ _chat.txt לא נמצא!")
        return

    # זיהוי מספרי טלפון ישראליים
    phone_pattern = r'05\d-?\d{7}'
    phones = re.findall(phone_pattern, content)
    counts = Counter(phones)

    # יצירת רשימת תוצאות
    results = []
    for phone, count in counts.items():
        if count >= 1: # הצג את כולם, גם אם הומלצו פעם אחת
            results.append({
                "name": "בעל מקצוע",
                "phone": phone.replace('-', ''),
                "recs": count
            })

    # מיון לפי כמות המלצות (מהגבוה לנמוך)
    results.sort(key=lambda x: x['recs'], reverse=True)

    # שמירה ל-JSON בפורמט UTF-8
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("קובץ data.json עודכן בהצלחה!")

if __name__ == "__main__":
    update_data()
