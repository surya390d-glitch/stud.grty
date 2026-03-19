import codecs
import re

path = r'c:\Users\Surya\Desktop\stud.gravity\stud.grty\index.html'
with codecs.open(path, 'r', 'utf-8') as f:
    html = f.read()

new_css = """        :root {
            --bg: #000000;
            --surf: #09090b;
            --card: #121214;
            --card2: #18181b;
            --b1: #27272a;
            --b2: #3f3f46;
            --blue: #d4af37;
            --teal: #facc15;
            --gold: #f59e0b;
            --green: #10b981;
            --red: #ef4444;
            --pink: #ec4899;
            --purp: #8b5cf6;
            --ora: #f97316;
            --txt: #f1f5f9;
            --tm: #94a3b8;
            --r: 10px;
            --rm: 16px;
            --rl: 22px;
            --t: .25s cubic-bezier(.4, 0, .2, 1);
        }"""
html = re.sub(r':root\s*\{[^}]+\}', new_css, html, 1)

img_pattern = r'<img\s+class="logo-img"\s+src="data:image/[^"]+"\s+alt="[^"]+">'
new_img = '<img class="logo-img" src="logo.jpg" alt="Sudharsan Engineering College Logo">'
html = re.sub(img_pattern, new_img, html)

html = html.replace('<div class="logo-name">SUDHARSAN GROUP</div>', '<div class="logo-name">SUDHARSAN</div>')
html = html.replace('<div class="logo-sub">of Institutions</div>', '<div class="logo-sub">Engineering College</div>')

# Note: Sometimes there is <br> or newline in the html
html = re.sub(r'CSE\s*&bull;\s*ECE\s*&bull;\s*EEE\s*&bull;\s*MECH\s*&bull;\s*CIVIL\s*&bull;\s*AI&ML\s*&bull;\s*AI&DS',
              'CSE &bull; ECE &bull; EEE &bull; MECH &bull; CIVIL &bull; AI&ML &bull; AI&DS &bull; IT &bull; CYBERSECURITY', html)

with codecs.open(path, 'w', 'utf-8') as f:
    f.write(html)
print('Done!')
