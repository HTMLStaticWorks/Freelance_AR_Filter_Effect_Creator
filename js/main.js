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
});
