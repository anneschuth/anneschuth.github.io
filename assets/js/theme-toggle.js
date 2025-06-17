// Dark mode toggle functionality
(function() {
  'use strict';

  // Constants
  const THEME_KEY = 'theme-preference';
  const DARK_THEME = 'dark';
  const LIGHT_THEME = 'light';

  // Theme management
  const Theme = {
    // Get stored theme preference or detect system preference
    getPreference() {
      const stored = localStorage.getItem(THEME_KEY);
      if (stored) return stored;

      // Check system preference
      return window.matchMedia('(prefers-color-scheme: dark)').matches
        ? DARK_THEME
        : LIGHT_THEME;
    },

    // Set theme preference
    setPreference(theme) {
      localStorage.setItem(THEME_KEY, theme);
      this.apply(theme);
    },

    // Apply theme to document
    apply(theme) {
      document.documentElement.setAttribute('data-theme', theme);
      this.updateToggleIcon(theme);
    },

    // Toggle between themes
    toggle() {
      const current = this.getPreference();
      const next = current === DARK_THEME ? LIGHT_THEME : DARK_THEME;
      this.setPreference(next);

      // Add rotation animation
      const toggle = document.querySelector('.theme-toggle');
      if (toggle) {
        toggle.classList.add('rotating');
        setTimeout(() => toggle.classList.remove('rotating'), 300);
      }
    },

    // Update toggle button icon
    updateToggleIcon(theme) {
      const icon = document.querySelector('.theme-toggle .icon');
      if (icon) {
        icon.textContent = theme === DARK_THEME ? '☀️' : '🌙';
        icon.setAttribute('aria-label',
          theme === DARK_THEME ? 'Switch to light mode' : 'Switch to dark mode'
        );
      }
    },

    // Initialize theme
    init() {
      // Apply initial theme before page renders
      this.apply(this.getPreference());

      // Listen for system theme changes
      window.matchMedia('(prefers-color-scheme: dark)')
        .addEventListener('change', (e) => {
          // Only auto-switch if user hasn't set a preference
          if (!localStorage.getItem(THEME_KEY)) {
            this.apply(e.matches ? DARK_THEME : LIGHT_THEME);
          }
        });
    }
  };

  // Initialize theme immediately (before DOM loads)
  Theme.init();

  // Setup toggle button when DOM is ready
  document.addEventListener('DOMContentLoaded', function() {
    // Create toggle button if it doesn't exist
    let toggle = document.querySelector('.theme-toggle');
    if (!toggle) {
      toggle = document.createElement('button');
      toggle.className = 'theme-toggle';
      toggle.setAttribute('aria-label', 'Toggle dark mode');
      toggle.setAttribute('title', 'Toggle dark mode');

      const icon = document.createElement('span');
      icon.className = 'icon';
      icon.setAttribute('aria-hidden', 'true');

      toggle.appendChild(icon);
      document.body.appendChild(toggle);
    }

    // Update icon based on current theme
    Theme.updateToggleIcon(Theme.getPreference());

    // Add click event listener
    toggle.addEventListener('click', () => Theme.toggle());

    // Keyboard accessibility
    toggle.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        Theme.toggle();
      }
    });
  });

  // Expose theme toggle for external use
  window.ThemeToggle = Theme;
})();
