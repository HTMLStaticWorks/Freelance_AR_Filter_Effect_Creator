import glob

target = '''                    <button id="theme-toggle-desktop" class="flex items-center gap-2 bg-surface border border-divider hover:border-primary/50 text-muted hover:text-main focus:outline-none px-3 py-1.5 rounded-full transition-all group shadow-sm">
                        <svg id="theme-icon-moon" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                        <svg id="theme-icon-sun" class="w-4 h-4 hidden" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                        <span class="text-[10px] uppercase font-bold tracking-wider text-strong opacity-80 group-hover:opacity-100">Theme</span>
                    </button>
                    <button id="rtl-toggle-desktop" class="flex items-center justify-center bg-surface border border-divider hover:border-primary/50 text-muted hover:text-main focus:outline-none px-4 py-1.5 rounded-full transition-all group shadow-sm" title="Toggle RTL">
                        <span class="text-[10px] uppercase font-bold tracking-wider text-strong opacity-80 group-hover:opacity-100">RTL</span>
                    </button>'''

replacement = '''                    <div class="flex items-center gap-3">
                        <button id="theme-toggle-desktop" class="flex items-center gap-2 bg-surface border border-divider hover:border-primary/50 text-muted hover:text-main focus:outline-none px-3 py-1.5 rounded-full transition-all group shadow-sm">
                            <svg id="theme-icon-moon" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                            <svg id="theme-icon-sun" class="w-4 h-4 hidden" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                            <span class="text-[10px] uppercase font-bold tracking-wider text-strong opacity-80 group-hover:opacity-100">Theme</span>
                        </button>
                        <button id="rtl-toggle-desktop" class="flex items-center justify-center bg-surface border border-divider hover:border-primary/50 text-muted hover:text-main focus:outline-none px-4 py-1.5 rounded-full transition-all group shadow-sm" title="Toggle RTL">
                            <span class="text-[10px] uppercase font-bold tracking-wider text-strong opacity-80 group-hover:opacity-100">RTL</span>
                        </button>
                    </div>'''

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target in content:
        content = content.replace(target, replacement)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
