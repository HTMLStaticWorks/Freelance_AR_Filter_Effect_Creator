import glob

favicon_svg = '''<svg fill="none" viewBox="0 0 24 24" stroke="#8b5cf6" stroke-width="2" xmlns="http://www.w3.org/2000/svg">
  <path stroke-linecap="round" stroke-linejoin="round" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
</svg>'''

with open('images/favicon.svg', 'w', encoding='utf-8') as f:
    f.write(favicon_svg)

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<link rel="icon"' not in content:
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if '</title>' in line:
                lines.insert(i + 1, '    <link rel="icon" type="image/svg+xml" href="images/favicon.svg">')
                break
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
