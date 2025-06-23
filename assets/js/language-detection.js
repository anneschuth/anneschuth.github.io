// Language detection and homepage redirection
(function() {
  'use strict';

  // Only run on homepage
  if (window.location.pathname !== '/' && window.location.pathname !== '/index.html') {
    return;
  }

  // Check if we're coming from an English post
  const referrer = document.referrer;
  const isFromEnglishPost = referrer && referrer.includes('/toch-een-architect-en.html');

  // Check localStorage for language preference
  const savedLang = localStorage.getItem('preferred-language');

  // Check URL parameters
  const urlParams = new URLSearchParams(window.location.search);
  const langParam = urlParams.get('lang');

  // Determine if we should show English content
  const shouldShowEnglish = langParam === 'en' || savedLang === 'en' || isFromEnglishPost;

  if (shouldShowEnglish && window.location.pathname === '/') {
    // Redirect to English homepage
    window.location.href = '/en/';
  }

  // Save language preference
  const currentLang = window.location.pathname.startsWith('/en/') ? 'en' : 'nl';
  localStorage.setItem('preferred-language', currentLang);
})();
