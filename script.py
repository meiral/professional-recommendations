import re, json
from collections import Counter

def update():
    with open('_chat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    phones = re.findall(r'05\d-?\d{7}', content)
    counts = Counter(phones)
    results = [{"phone": p, "recs": c} for p, c in counts.items() if c >= 2]
    results.sort(key=lambda x: x['recs'], reverse=True)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    update()