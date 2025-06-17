// Site search functionality using Lunr.js
(function() {
  'use strict';

  let searchData = [];
  let searchIndex;
  let searchResults = [];

  // Initialize search when DOM is ready
  document.addEventListener('DOMContentLoaded', function() {
    loadSearchData();
    bindSearchEvents();
  });

  // Load search data and create Lunr index
  function loadSearchData() {
    fetch('/search.json')
      .then(response => response.json())
      .then(data => {
        searchData = data;
        createSearchIndex();
      })
      .catch(error => console.error('Error loading search data:', error));
  }

  // Create Lunr search index
  function createSearchIndex() {
    searchIndex = lunr(function() {
      this.field('title', { boost: 10 });
      this.field('content');
      this.field('authors');
      this.field('venue');
      this.field('tags', { boost: 5 });
      this.field('excerpt', { boost: 3 });
      this.ref('url');

      searchData.forEach(doc => {
        this.add(doc);
      });
    });
  }

  // Bind search events - now works with dynamically created overlays
  function bindSearchEvents() {
    // Create debounced search function
    const debouncedSearch = debounce(performSearch, 300);

    // Use event delegation for dynamic content
    document.addEventListener('input', function(e) {
      if (e.target && e.target.id === 'search-input') {
        debouncedSearch();
      }
    });

    // Handle search form submission
    document.addEventListener('submit', function(e) {
      if (e.target && e.target.id === 'search-form') {
        e.preventDefault();
        performSearch();
      }
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
      // Open search with '/' key
      if (e.key === '/' && !isInputFocused()) {
        e.preventDefault();
        if (window.showSearchOverlay) {
          window.showSearchOverlay();
        }
      }
      // Close search with Escape
      if (e.key === 'Escape') {
        if (window.hideSearchOverlay) {
          window.hideSearchOverlay();
        }
      }
    });
  }

  // Perform search
  function performSearch() {
    const searchInput = document.getElementById('search-input');
    if (!searchInput) return;

    const query = searchInput.value.trim();

    if (query.length < 2) {
      hideSearchResults();
      return;
    }

    if (!searchIndex) return;

    try {
      // Try multiple search strategies for better results
      let results = [];

      // 1. Exact phrase search
      try {
        results = searchIndex.search(`"${query}"`);
      } catch (e) {}

      // 2. If no exact results, try wildcard search for partial matches
      if (results.length === 0) {
        const wildcardQuery = query.split(' ').map(term => `${term}*`).join(' ');
        try {
          results = searchIndex.search(wildcardQuery);
        } catch (e) {}
      }

      // 3. If still no results, try fuzzy search
      if (results.length === 0) {
        const fuzzyQuery = query.split(' ').map(term => `${term}~1`).join(' ');
        try {
          results = searchIndex.search(fuzzyQuery);
        } catch (e) {}
      }

      // 4. Fall back to basic search
      if (results.length === 0) {
        try {
          results = searchIndex.search(query);
        } catch (e) {}
      }

      displaySearchResults(results, query);
    } catch (error) {
      console.error('Search error:', error);
    }
  }

  // Display search results
  function displaySearchResults(results, query) {
    const searchResults = document.getElementById('search-results');
    const searchStatus = document.getElementById('search-status');

    if (!searchResults) return;

    if (results.length === 0) {
      searchResults.innerHTML = '<div class="search-no-results">No results found</div>';
      if (searchStatus) searchStatus.textContent = 'No results found';
    } else {
      const html = results.slice(0, 10).map(result => {
        const item = searchData.find(d => d.url === result.ref);
        if (!item) return '';

        const typeIcon = getTypeIcon(item.type);
        const metadata = getItemMetadata(item);
        const highlightedExcerpt = highlightSearchTerms(item.excerpt, query);
        const matchInfo = getMatchInfo(item, query);

        return `
          <div class="search-result">
            <div class="search-result-header">
              <span class="search-result-type">${typeIcon} ${item.type}</span>
              ${metadata}
            </div>
            <h3 class="search-result-title">
              <a href="${item.url}">${highlightSearchTerms(item.title, query)}</a>
            </h3>
            ${matchInfo}
            <p class="search-result-excerpt">${highlightedExcerpt}</p>
          </div>
        `;
      }).join('');

      searchResults.innerHTML = html;
      if (searchStatus) {
        searchStatus.textContent = `${results.length} result${results.length !== 1 ? 's' : ''} found`;
      }
    }

    showSearchResults();
  }

  // Get type icon
  function getTypeIcon(type) {
    const icons = {
      'post': '📝',
      'publication': '📄',
      'talk': '🎤'
    };
    return icons[type] || '📄';
  }

  // Get item metadata
  function getItemMetadata(item) {
    switch(item.type) {
      case 'post':
        return item.date ? `<span class="search-meta">${formatDate(item.date)}</span>` : '';
      case 'publication':
        const year = item.year ? item.year : '';
        const venue = item.venue ? ` • ${item.venue}` : '';
        return year || venue ? `<span class="search-meta">${year}${venue}</span>` : '';
      case 'talk':
        return item.date ? `<span class="search-meta">${formatDate(item.date)}</span>` : '';
      default:
        return '';
    }
  }

  // Get match information showing which fields matched
  function getMatchInfo(item, query) {
    if (item.type === 'publication' && item.authors) {
      return `<div class="search-match-info">${highlightSearchTerms(item.authors, query)}</div>`;
    }

    return '';
  }

  // Highlight search terms
  function highlightSearchTerms(text, query) {
    if (!text || !query) return text;

    const terms = query.toLowerCase().split(/\s+/);
    let highlightedText = text;

    terms.forEach(term => {
      if (term.length > 1) {
        const regex = new RegExp(`(${escapeRegex(term)})`, 'gi');
        highlightedText = highlightedText.replace(regex, '<mark>$1</mark>');
      }
    });

    return highlightedText;
  }

  // Utility functions
  function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }

  function isInputFocused() {
    const activeElement = document.activeElement;
    return activeElement && (
      activeElement.tagName === 'INPUT' ||
      activeElement.tagName === 'TEXTAREA' ||
      activeElement.contentEditable === 'true'
    );
  }

  function showSearchContainer() {
    const container = document.getElementById('search-container');
    if (container) {
      container.classList.add('search-active');
    }
  }

  function showSearchResults() {
    const results = document.getElementById('search-results');
    if (results) {
      results.style.display = 'block';
    }
    showSearchContainer();
  }

  function hideSearchResults() {
    const results = document.getElementById('search-results');
    const container = document.getElementById('search-container');

    if (results) results.style.display = 'none';
    if (container) container.classList.remove('search-active');
  }

  function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  }

  function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }
})();
