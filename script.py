import re, json, os
from collections import Counter

def update():
    # הדפסה שתראה לנו בלוג מה הסקריפט באמת רואה
    print(f"Current directory: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}")

    file_name = '_chat.txt'
    if not os.path.exists(file_name):
        print(f"ERROR: {file_name} not found!")
        return

    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()

    phones = re.findall(r'05\d-?\d{7}', content)
    counts = Counter(phones)
    results = [{"phone": p, "recs": c} for p, c in counts.items()]

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("data.json created successfully.")

if __name__ == "__main__":
    update()
