import glob

header_target = '<a href="index.html" class="text-2xl font-bold font-display text-gradient">AR Vision</a>'
header_replace = '''<a href="index.html" class="flex items-center gap-2 text-2xl font-bold font-display text-gradient">
                        <svg class="w-8 h-8 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
                        </svg>
                        AR Vision
                    </a>'''

footer_target = '<div class="text-2xl font-bold font-display text-gradient mb-4 md:mb-0">AR Vision</div>'
footer_replace = '''<div class="flex items-center gap-2 text-2xl font-bold font-display text-gradient mb-4 md:mb-0">
                <svg class="w-8 h-8 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
                </svg>
                AR Vision
            </div>'''

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(header_target, header_replace)
    content = content.replace(footer_target, footer_replace)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
