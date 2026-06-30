// Initialize Theme and RTL from localStorage immediately
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'light') {
    document.body.classList.add('light-theme');
}
const savedRTL = localStorage.getItem('rtl');
if (savedRTL === 'rtl') {
    document.documentElement.dir = 'rtl';
}

document.addEventListener('DOMContentLoaded', () => {
    // Initialize AOS (Animate On Scroll)
    AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: true,
        mirror: false,
        offset: 50
    });

    // Mobile Menu Toggle
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
            
            // Hamburger Icon Animation
            const icons = mobileMenuButton.querySelectorAll('svg');
            icons.forEach(icon => icon.classList.toggle('hidden'));
        });
    }

    // Theme Toggle Logic
    const themeDesktop = document.getElementById('theme-toggle-desktop');
    const themeMobile = document.getElementById('theme-toggle-mobile');
    
    function updateThemeIcons(isLight) {
        document.querySelectorAll('#theme-icon-sun').forEach(icon => {
            isLight ? icon.classList.remove('hidden') : icon.classList.add('hidden');
        });
        document.querySelectorAll('#theme-icon-moon').forEach(icon => {
            isLight ? icon.classList.add('hidden') : icon.classList.remove('hidden');
        });
    }

    function toggleTheme() {
        const isLight = document.body.classList.toggle('light-theme');
        localStorage.setItem('theme', isLight ? 'light' : 'dark');
        updateThemeIcons(isLight);
    }

    if (themeDesktop) themeDesktop.addEventListener('click', toggleTheme);
    if (themeMobile) themeMobile.addEventListener('click', toggleTheme);
    
    // Set initial icon state
    if (savedTheme === 'light') {
        updateThemeIcons(true);
    }

    // RTL Toggle Logic
    const rtlDesktop = document.getElementById('rtl-toggle-desktop');
    const rtlMobile = document.getElementById('rtl-toggle-mobile');
    
    function toggleRTL() {
        const isRTL = document.documentElement.dir === 'rtl';
        document.documentElement.dir = isRTL ? 'ltr' : 'rtl';
        localStorage.setItem('rtl', document.documentElement.dir);
    }
    
    if (rtlDesktop) rtlDesktop.addEventListener('click', toggleRTL);
    if (rtlMobile) rtlMobile.addEventListener('click', toggleRTL);

    // Scroll to Top Button
    const scrollTopBtn = document.createElement('button');
    scrollTopBtn.id = 'scroll-to-top';
    scrollTopBtn.innerHTML = `
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    `;
    scrollTopBtn.className = 'fixed bottom-6 right-6 md:bottom-10 md:right-10 z-50 glass text-primary p-3 rounded-full shadow-lg opacity-0 pointer-events-none transition-all duration-300 hover:-translate-y-1 focus:outline-none flex items-center justify-center translate-y-10';
    document.body.appendChild(scrollTopBtn);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 400) {
            scrollTopBtn.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-10');
            scrollTopBtn.classList.add('opacity-100', 'pointer-events-auto', 'translate-y-0');
        } else {
            scrollTopBtn.classList.add('opacity-0', 'pointer-events-none', 'translate-y-10');
            scrollTopBtn.classList.remove('opacity-100', 'pointer-events-auto', 'translate-y-0');
        }
    });

    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});
