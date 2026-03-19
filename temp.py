import re
with open(r'c:\Users\Surya\Desktop\stud.gravity\stud.grty\index.html', encoding='utf-8') as f:
    text = f.read()
pages = re.findall(r'<div id="page-([^"]+)"\s*class="page.*">(.*?)</div>\s*<!-- PAGE:', text, re.DOTALL)
for p, content in pages:
    print(f"{p}: {len(content)} characters")
