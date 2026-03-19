import re

with open(r'c:\Users\Surya\Desktop\stud.gravity\stud.grty\index.html', encoding='utf-8') as f:
    text = f.read()

def get_page(id):
    pattern = f'<div id="{id}" class="page">(.*?)</div>\\s*<!--'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        print(f"--- {id} --- (Length: {len(match.group(1))})")
        print(match.group(1)[:500])
    else:
        print(f"NOT FOUND: {id}")

get_page('page-arts')
get_page('page-poly')
get_page('page-sec')
