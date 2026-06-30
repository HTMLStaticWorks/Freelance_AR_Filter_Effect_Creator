import glob
import re

desktop_pattern = re.compile(
    r'<button id="rtl-toggle-desktop" class="text-muted hover:text-strong font-bold uppercase tracking-wider text-xs focus:outline-none transition-colors px-2"[^>]*>[\s\S]*?RTL[\s\S]*?</button>'
)

desktop_replacement = '''<button id="rtl-toggle-desktop" class="flex items-center justify-center bg-surface border border-divider hover:border-primary/50 text-muted hover:text-main focus:outline-none px-4 py-1.5 rounded-full transition-all group shadow-sm" title="Toggle RTL">
                        <span class="text-[10px] uppercase font-bold tracking-wider text-strong opacity-80 group-hover:opacity-100">RTL</span>
                    </button>'''

mobile_pattern = re.compile(
    r'<button id="rtl-toggle-mobile" class="text-muted hover:text-strong font-bold uppercase tracking-wider text-xs focus:outline-none p-2 transition-colors flex-1 text-center border border-divider rounded-md"[^>]*>[\s\S]*?RTL[\s\S]*?</button>'
)

mobile_replacement = '''<button id="rtl-toggle-mobile" class="text-muted hover:text-main focus:outline-none p-2 border border-divider rounded-md flex-1 flex justify-center items-center transition-colors">
                        <span class="text-xs font-bold uppercase tracking-wider text-strong">RTL</span>
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
