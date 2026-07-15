// JA IMAGE — comportements partagés
document.addEventListener('DOMContentLoaded', function () {

  /* ---- Intro cinématique (une fois par session, page d'accueil) ---- */
  var intro = document.querySelector('.intro');
  if (intro) {
    var alreadySeen = sessionStorage.getItem('ja_intro_seen');
    var closeIntro = function () {
      intro.classList.add('hide');
      sessionStorage.setItem('ja_intro_seen', '1');
      document.body.style.overflow = '';
      setTimeout(function () { if (intro.parentNode) intro.remove(); }, 900);
    };
    if (alreadySeen) {
      intro.remove();
    } else {
      document.body.style.overflow = 'hidden';
      var skipBtn = intro.querySelector('.intro__skip');
      if (skipBtn) skipBtn.addEventListener('click', closeIntro);
      setTimeout(closeIntro, 6400);
    }
  }

  /* ---- Menu mobile ---- */
  var toggle = document.querySelector('.nav-toggle');
  var navList = document.querySelector('.nav-list');
  if (toggle && navList) {
    toggle.addEventListener('click', function () {
      navList.classList.toggle('open');
      toggle.textContent = navList.classList.contains('open') ? '✕' : '☰';
    });
    navList.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        navList.classList.remove('open');
        toggle.textContent = '☰';
      });
    });
  }

  /* ---- En-tête qui se resserre au scroll ---- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 60) header.classList.add('scrolled');
      else header.classList.remove('scrolled');
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---- Révélation au scroll (fiable : seuil bas + filet de sécurité) ---- */
  var revealEls = Array.prototype.slice.call(document.querySelectorAll('.reveal'));

  // Étage les cartes d'une même grille pour un effet de cascade
  document.querySelectorAll('.grid').forEach(function (grid) {
    Array.prototype.forEach.call(grid.children, function (child, i) {
      child.style.transitionDelay = Math.min(i * 90, 360) + 'ms';
    });
  });

  function showEl(el) { el.classList.add('in'); }

  if (revealEls.length) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            showEl(entry.target);
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.01, rootMargin: '0px 0px -2% 0px' });
      revealEls.forEach(function (el) { io.observe(el); });

      // filet de sécurité : si un élément est déjà dans la fenêtre au chargement
      // (ou si l'observer tarde), on le révèle sans attendre
      revealEls.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight && r.bottom > 0) showEl(el);
      });
    } else {
      revealEls.forEach(showEl);
    }
    // filet de sécurité final : personne ne doit rester invisible
    setTimeout(function () { revealEls.forEach(showEl); }, 2500);
  }

  /* ---- Compteurs animés ---- */
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    var animateCount = function (el) {
      var target = parseInt(el.getAttribute('data-count'), 10) || 0;
      var suffix = el.getAttribute('data-suffix') || '';
      var start = null;
      var duration = 1400;
      function step(ts) {
        if (!start) start = ts;
        var progress = Math.min((ts - start) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(eased * target) + suffix;
        if (progress < 1) requestAnimationFrame(step);
        else el.textContent = target + suffix;
      }
      requestAnimationFrame(step);
    };
    if ('IntersectionObserver' in window) {
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animateCount(entry.target);
            cio.unobserve(entry.target);
          }
        });
      }, { threshold: 0.4 });
      counters.forEach(function (el) { cio.observe(el); });
    } else {
      counters.forEach(animateCount);
    }
  }

  /* ---- Bobine verticale : tourne et avance avec le scroll de la page ---- */
  var reelStrip = document.querySelector('.reel-strip');
  if (reelStrip) {
    var reelIcon = reelStrip.querySelector('.reel');
    var track = reelStrip.querySelector('.reel-strip__track');
    var ticking = false;
    var updateReel = function () {
      var doc = document.documentElement;
      var scrollTop = window.scrollY || doc.scrollTop;
      var maxScroll = (doc.scrollHeight - window.innerHeight) || 1;
      var fraction = Math.min(Math.max(scrollTop / maxScroll, 0), 1);
      if (reelIcon) reelIcon.style.transform = 'rotate(' + (fraction * 1080) + 'deg)';
      if (track) track.style.transform = 'translateY(' + (-fraction * 50) + '%)';
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { requestAnimationFrame(updateReel); ticking = true; }
    }, { passive: true });
    window.addEventListener('resize', updateReel);
    updateReel();
  }

  /* ---- Année dans le pied de page ---- */
  document.querySelectorAll('.year').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

});
