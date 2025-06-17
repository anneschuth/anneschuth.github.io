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
    // Create theme toggle button if it doesn't exist
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

    // Create search toggle button if it doesn't exist
    let searchToggle = document.querySelector('.search-toggle');
    if (!searchToggle) {
      searchToggle = document.createElement('button');
      searchToggle.className = 'search-toggle';
      searchToggle.setAttribute('aria-label', 'Open search');
      searchToggle.setAttribute('title', 'Search (press /)');
      searchToggle.textContent = '🔍';

      // Add click handler to open search overlay
      searchToggle.addEventListener('click', () => {
        showSearchOverlay();
      });

      document.body.appendChild(searchToggle);
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

  // Search overlay functionality
  function showSearchOverlay() {
    // Create overlay if it doesn't exist
    let overlay = document.getElementById('search-overlay');
    if (!overlay) {
      overlay = createSearchOverlay();
    }

    overlay.style.display = 'flex';
    document.body.style.overflow = 'hidden';

    // Focus the search input
    const searchInput = overlay.querySelector('.search-input');
    if (searchInput) {
      setTimeout(() => searchInput.focus(), 100);
    }
  }

  function hideSearchOverlay() {
    const overlay = document.getElementById('search-overlay');
    if (overlay) {
      overlay.style.display = 'none';
      document.body.style.overflow = '';
    }
  }

  function createSearchOverlay() {
    const overlay = document.createElement('div');
    overlay.id = 'search-overlay';
    overlay.className = 'search-overlay';

    overlay.innerHTML = `
      <div class="search-overlay-backdrop"></div>
      <div class="search-overlay-content">
        <div class="search-overlay-header">
          <h2>Search</h2>
          <button class="search-close" aria-label="Close search">&times;</button>
        </div>
        <div id="search-container" class="search-container">
          <form id="search-form" class="search-form">
            <div class="search-input-wrapper">
              <input
                type="text"
                id="search-input"
                class="search-input"
                placeholder="Search posts, publications, and talks..."
                autocomplete="off"
              >
              <span class="search-shortcut">ESC to close</span>
            </div>
          </form>

          <div id="search-status" class="search-status"></div>

          <div id="search-results" class="search-results" style="display: none;">
            <!-- Results will be populated by JavaScript -->
          </div>
        </div>

        <div class="search-help-mini">
          <p><strong>Tips:</strong> Use quotes for exact phrases, field:term for specific searches</p>
        </div>
      </div>
    `;

    // Add event listeners
    const closeButton = overlay.querySelector('.search-close');
    const backdrop = overlay.querySelector('.search-overlay-backdrop');

    closeButton.addEventListener('click', hideSearchOverlay);
    backdrop.addEventListener('click', hideSearchOverlay);

    // Handle escape key
    overlay.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        hideSearchOverlay();
      }
    });

    document.body.appendChild(overlay);
    return overlay;
  }

  // Make search overlay accessible globally
  window.showSearchOverlay = showSearchOverlay;
  window.hideSearchOverlay = hideSearchOverlay;

  // Expose theme toggle for external use
  window.ThemeToggle = Theme;
})();
