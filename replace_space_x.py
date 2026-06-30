import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace positive space-x-8 with gap-8
    new_content = re.sub(r'(?<!-)space-x-8', 'gap-8', content)
    
    # Replace positive space-x-4 with gap-4
    new_content = re.sub(r'(?<!-)space-x-4', 'gap-4', new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {filepath}')
