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
      setTimeout(function () { intro.remove(); }, 900);
    };
    if (alreadySeen) {
      intro.remove();
    } else {
      document.body.style.overflow = 'hidden';
      var skipBtn = intro.querySelector('.intro__skip');
      if (skipBtn) skipBtn.addEventListener('click', closeIntro);
      setTimeout(closeIntro, 3100);
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

  /* ---- Révélation au scroll ---- */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---- Année dans le pied de page ---- */
  document.querySelectorAll('.year').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

});
