import re, json, os

def update():
    file_path = '_chat.txt'
    if not os.path.exists(file_path):
        print("Error: _chat.txt not found!")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # חיפוש טלפונים
    phones = re.findall(r'05\d[\s\-]?\d{3}[\s\-]?\d{4}', content)
    # יצירת קובץ JSON פשוט
    data = [{"phone": p, "recs": 1} for p in phones]

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"DEBUG: Successfully wrote {len(data)} items to data.json")
    print(f"DEBUG: File exists: {os.path.exists('data.json')}")

if __name__ == "__main__":
    update()
