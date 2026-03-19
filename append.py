import codecs
import re

path = r'c:\Users\Surya\Desktop\stud.gravity\stud.grty\index.html'
with codecs.open(path, 'r', 'utf-8') as f:
    html = f.read()

# 1. Add department cards
cards_insertion = """                    <div class="dept-card" style="--dc:#10b981" onclick="goTo('sec-aids')">
                        <div class="di" style="background:rgba(16,185,129,0.1)">📊</div>
                        <div class="dn" style="color:#10b981">AI&amp;DS</div>
                        <div class="df">AI &amp; Data Science</div>
                        <div class="dc-cta" style="color:#10b981">View Roadmap →</div>
                    </div>"""

new_cards = cards_insertion + """
                    <div class="dept-card" style="--dc:#0ea5e9" onclick="goTo('sec-it')">
                        <div class="di" style="background:rgba(14,165,233,0.1)">🌐</div>
                        <div class="dn" style="color:#0ea5e9">IT</div>
                        <div class="df">Information Technology</div>
                        <div class="dc-cta" style="color:#0ea5e9">View Roadmap →</div>
                    </div>
                    <div class="dept-card" style="--dc:#8b5cf6" onclick="goTo('sec-cyber')">
                        <div class="di" style="background:rgba(139,92,246,0.1)">🛡️</div>
                        <div class="dn" style="color:#8b5cf6">CYBER</div>
                        <div class="df">Cybersecurity</div>
                        <div class="dc-cta" style="color:#8b5cf6">View Roadmap →</div>
                    </div>"""

html = html.replace(cards_insertion, new_cards)


# 2. Duplicate the page-sec-cse block for IT and Cyber
parts = html.split('<!-- PAGE: sec-ece -->')
before_ece = parts[0]
page_cse_match = re.search(r'(<!-- PAGE: sec-cse -->.*?)(?=<!-- PAGE: sec-ece -->|$)', html, re.DOTALL)
if page_cse_match:
    page_cse = page_cse_match.group(1)
    
    # IT Portal
    page_it = page_cse.replace('<!-- PAGE: sec-cse -->', '<!-- PAGE: sec-it -->')
    page_it = page_it.replace('id="page-sec-cse"', 'id="page-sec-it"')
    page_it = page_it.replace('>CSE<', '>IT<')
    page_it = page_it.replace('💻 CSE', '🌐 IT')
    page_it = page_it.replace('Computer Science & Engineering', 'Information Technology')
    page_it = page_it.replace('sec-cse-', 'sec-it-')
    
    # CYBER Portal
    page_cyber = page_cse.replace('<!-- PAGE: sec-cse -->', '<!-- PAGE: sec-cyber -->')
    page_cyber = page_cyber.replace('id="page-sec-cse"', 'id="page-sec-cyber"')
    page_cyber = page_cyber.replace('>CSE<', '>CYBER<')
    page_cyber = page_cyber.replace('💻 CSE', '🛡️ CYBER')
    page_cyber = page_cyber.replace('Computer Science & Engineering', 'Cybersecurity')
    page_cyber = page_cyber.replace('sec-cse-', 'sec-cyber-')
    
    # Insert before arts&science portal
    # Wait, they should go after sec-aids
    arts_split = html.split('<!-- ARTS & SCIENCE PORTAL -->')
    new_html = arts_split[0] + page_it + '\n    ' + page_cyber + '\n    <!-- ARTS & SCIENCE PORTAL -->' + arts_split[1]
    
    with codecs.open(path, 'w', 'utf-8') as f:
        f.write(new_html)
    print("Added IT and CYBER portals!")
else:
    print("Could not find sec-cse page block.")
