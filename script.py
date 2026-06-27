import re, json, os
from collections import Counter

def update():
    file_name = '_chat.txt'
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()

    # חיפוש גמיש יותר: מחפש כל רצף של 10 ספרות שמתחיל ב-05
    # זה יתפוס גם אם יש רווחים או מקפים משונים
    phones = re.findall(r'05\d[\s\-]?\d{3}[\s\-]?\d{4}', content)

    # ניקוי המספרים מרווחים ומקפים כדי שיהיה אחיד
    clean_phones = [re.sub(r'[\s\-]', '', p) for p in phones]

    print(f"Found {len(clean_phones)} numbers: {clean_phones}")

    counts = Counter(clean_phones)
    results = [{"phone": p, "recs": c} for p, c in counts.items()]

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("data.json created successfully.")

if __name__ == "__main__":
    update()
