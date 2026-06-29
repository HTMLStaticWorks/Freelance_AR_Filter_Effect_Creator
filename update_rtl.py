import glob
import re

desktop_pattern = re.compile(
    r'<button id="rtl-toggle-desktop"[^>]*>[\s\S]*?<span[^>]*>RTL</span>[\s\S]*?</button>'
)

desktop_replacement = '''<button id="rtl-toggle-desktop" class="text-muted hover:text-strong font-bold uppercase tracking-wider text-xs focus:outline-none transition-colors px-2" title="Toggle RTL">
                        RTL
                    </button>'''

mobile_pattern = re.compile(
    r'<button id="rtl-toggle-mobile"[^>]*>[\s\S]*?<span[^>]*>RTL</span>[\s\S]*?</button>'
)

mobile_replacement = '''<button id="rtl-toggle-mobile" class="text-muted hover:text-strong font-bold uppercase tracking-wider text-xs focus:outline-none p-2 transition-colors flex-1 text-center border border-divider rounded-md">
                        RTL
                    </button>'''

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = desktop_pattern.sub(desktop_replacement, content)
    new_content = mobile_pattern.sub(mobile_replacement, new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {filepath}')
