import re, json
from collections import Counter

def update():
    with open('_chat.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    all_data = []
    # מילון לספירת מילים שמופיעות ליד טלפונים כדי לזהות מקצועות
    potential_professions = Counter()

    # שלב 1: איסוף נתונים וזיהוי מילים "מקצועיות"
    for line in lines:
        phone_match = re.search(r'05\d[\s\-]?\d{3}[\s\-]?\d{4}', line)
        if phone_match:
            phone = phone_match.group().replace('-', '').replace(' ', '')
            # ניקוי השורה ממספר הטלפון כדי לחלץ את המקצוע והשם
            clean_line = re.sub(r'05\d[\s\-]?\d{3}[\s\-]?\d{4}', '', line)
            words = [w for w in clean_line.split() if len(w) > 2 and w not in ['ממליץ', 'על', 'הוא', 'מספר', 'טלפון', 'בעל']]
            
            # מניחים שהמילה הראשונה היא שם והשאר פוטנציאל למקצוע
            name = words[0] if words else "לא ידוע"
            prof_candidates = words[1:]
            
            for prof in prof_candidates:
                potential_professions[prof] += 1
            
            all_data.append({"name": name, "phone": phone, "prof_candidates": prof_candidates})

    # שלב 2: סינון המקצועות המובילים (אלו שמופיעים הכי הרבה)
    top_professions = [word for word, count in potential_professions.most_common(20)]

    # שלב 3: בניית ה-JSON הסופי
    final_results = []
    phone_recs = Counter([e['phone'] for e in all_data])

    for entry in all_data:
        # בודק איזה מהמועמדים הוא המקצוע הכי סביר
        found_prof = next((p for p in entry['prof_candidates'] if p in top_professions), "לא מוגדר")
        
        # מוודא שלא נוסיף כפילויות
        if not any(f['phone'] == entry['phone'] for f in final_results):
            final_results.append({
                "name": entry['name'],
                "profession": found_prof,
                "phone": entry['phone'],
                "recommendations": phone_recs[entry['phone']]
            })
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(final_results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    update()
