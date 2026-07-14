#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Générateur du site multipage JA IMAGE."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- images ---
IMG = {
    'hero':            'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=1800&q=80&auto=format&fit=crop',
    'audience':        'https://images.unsplash.com/photo-1601506521937-0121a7fc2a6b?w=1200&q=80&auto=format&fit=crop',
    'camera_hand':     'https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?w=1000&q=80&auto=format&fit=crop',
    'clapper_gear':    'https://images.unsplash.com/photo-1594908900066-3f47337549d8?w=1000&q=80&auto=format&fit=crop',
    'vintage_cam':     'https://images.unsplash.com/photo-1517697471339-4aa32003c11a?w=1000&q=80&auto=format&fit=crop',
    'popcorn_theatre': 'https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=1000&q=80&auto=format&fit=crop',
    'portrait_1':      'https://images.unsplash.com/photo-1571847140471-1d7766e825ea?w=800&q=80&auto=format&fit=crop',
    'set_filming':     'https://images.unsplash.com/photo-1517457373958-b7bdd4587205?w=1000&q=80&auto=format&fit=crop',
    'group_people':    'https://images.unsplash.com/photo-1524712245354-2c4e5e7121c0?w=1000&q=80&auto=format&fit=crop',
    'portrait_3':      'https://images.unsplash.com/photo-1596727147705-61a532a659bd?w=800&q=80&auto=format&fit=crop',
    'clapper_2':       'https://images.unsplash.com/photo-1554941829-202a0b2403b8?w=1000&q=80&auto=format&fit=crop',
    'film_reel':       'https://images.unsplash.com/photo-1533106418989-88406c7cc8ca?w=1000&q=80&auto=format&fit=crop',
    'workshop_laptop': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=1000&q=80&auto=format&fit=crop',
    'group_smile':     'https://images.unsplash.com/photo-1531058020387-3be344556be6?w=1000&q=80&auto=format&fit=crop',
    'portrait_woman1': 'https://images.unsplash.com/photo-1594751543129-6701ad444259?w=800&q=80&auto=format&fit=crop',
    'group_meeting':   'https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=1000&q=80&auto=format&fit=crop',
    'portrait_man1':   'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=800&q=80&auto=format&fit=crop',
    'presenting':      'https://images.unsplash.com/photo-1560184611-ff3e53f00e8f?w=1000&q=80&auto=format&fit=crop',
    'crowd_event':     'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=1000&q=80&auto=format&fit=crop',
    'portrait_man2':   'https://images.unsplash.com/photo-1551038247-3d9af20df552?w=800&q=80&auto=format&fit=crop',
    'group_laptop':    'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1000&q=80&auto=format&fit=crop',
    'portrait_woman2': 'https://images.unsplash.com/photo-1543269865-cbf427effbad?w=800&q=80&auto=format&fit=crop',
}

FORM_EMAIL = "contact@jaimage.ml"  # placeholder — à remplacer par la vraie adresse

# Nav complète (utilisée pour le pied de page / sitemap)
NAV = [
    ("index.html", "Accueil"),
    ("association.html", "Association"),
    ("programmes.html", "Programmes"),
    ("formation.html", "Formation"),
    ("ressources.html", "Ressources"),
    ("concours.html", "Ciné Court School"),
    ("actualites.html", "Actualités"),
    ("galerie.html", "Galerie"),
    ("partenaires.html", "Partenaires"),
    ("contact.html", "Contact"),
]

# Nav resserrée affichée dans l'en-tête (les pages secondaires restent
# accessibles depuis le pied de page et les liens contextuels)
NAV_TOP = [
    ("index.html", "Accueil"),
    ("association.html", "Association"),
    ("programmes.html", "Programmes"),
    ("concours.html", "Ciné Court School"),
    ("actualites.html", "Actualités"),
    ("galerie.html", "Galerie"),
]

# Rattache une page secondaire à son onglet parent pour l'état actif
ACTIVE_PARENT = {
    "formation.html": "programmes.html",
    "ressources.html": "programmes.html",
    "partenaires.html": "association.html",
}

# ------------------------------------------------------------- fragments ---

def head(title, desc):
    return f"""<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — JA IMAGE</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Bebas+Neue&family=Work+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>"""


def header(active):
    effective = ACTIVE_PARENT.get(active, active)
    links = []
    for href, label in NAV_TOP:
        classes = []
        if href == effective:
            classes.append("active")
        if href == "concours.html":
            classes.append("flagship")
        cls = f' class="{" ".join(classes)}"' if classes else ''
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    links_html = "\n        ".join(links)
    return f"""<header class="site-header">
  <div class="container">
    <a href="index.html" class="brand">
      <img src="assets/logo.png" alt="JA IMAGE">
      <span>ja <em>image</em></span>
    </a>
    <nav class="nav-list">
        {links_html}
        <a href="contact.html" class="nav-cta">Nous rejoindre</a>
    </nav>
    <button class="nav-toggle" aria-label="Menu">☰</button>
  </div>
</header>"""


def footer():
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/logo.png" alt="JA IMAGE">
        <p>Association pour la promotion du cinéma africain et international, et l'accompagnement des cinéastes autodidactes. Basée à Bamako, Mali.</p>
      </div>
      <div>
        <h4>Association</h4>
        <a href="association.html">Qui sommes-nous</a>
        <a href="partenaires.html">Partenaires</a>
        <a href="actualites.html">Actualités</a>
        <a href="galerie.html">Galerie</a>
      </div>
      <div>
        <h4>Autodidactes</h4>
        <a href="programmes.html">Programmes</a>
        <a href="formation.html">Formation</a>
        <a href="ressources.html">Espace autodidactes</a>
        <a href="concours.html">Ciné Court School</a>
      </div>
      <div>
        <h4>Contact</h4>
        <a href="#">Hamdalaye, Bamako, Mali</a>
        <a href="tel:+22300000000">+223 00 00 00 00</a>
        <a href="mailto:{FORM_EMAIL}">{FORM_EMAIL}</a>
        <a href="#">Facebook · Instagram</a>
      </div>
    </div>
    <div class="bogolan-band" style="margin-bottom:24px;"></div>
    <div class="footer-bottom">
      <span>© <span class="year"></span> JA IMAGE — Bamako, Mali</span>
      <span>Contenu provisoire — site en construction</span>
    </div>
  </div>
</footer>"""


INTRO = """<div class="intro">
  <div class="intro__beam"></div>
  <div class="intro__grain"></div>
  <div class="intro__content">
    <div class="intro__stage">
      <div class="intro__flash"></div>
      <img class="piece piece--black" src="assets/fig_black.png" alt="">
      <img class="piece piece--red" src="assets/fig_red.png" alt="">
      <img class="piece piece--yellow" src="assets/fig_yellow.png" alt="">
      <img class="piece piece--purple" src="assets/fig_purple.png" alt="JA IMAGE">
    </div>
    <div class="intro__tagline">Cinéma malien &amp; africain · Bamako</div>
    <div class="intro__bar"></div>
  </div>
  <button class="intro__skip">Passer ›</button>
</div>"""


def page(filename, title, desc, body, with_intro=False):
    intro_html = INTRO if with_intro else ""
    html = f"""<!DOCTYPE html>
<html lang="fr">
{head(title, desc)}
<body>
{intro_html}
{header(filename)}
{body}
{footer()}
<script src="js/main.js"></script>
</body>
</html>"""
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("écrit:", filename)


def pagehero(eyebrow, title_html, lead):
    return f"""<section class="pagehero">
  <div class="container">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title_html}</h1>
    <p>{lead}</p>
  </div>
</section>"""

# ================================================================ ACCUEIL ==

def build_index():
    body = f"""
<section class="hero">
  <div class="hero__bg" style="--img:url('{IMG['hero']}')"></div>
  <div class="hero__figs"><img src="assets/logo.png" alt=""></div>
  <div class="container hero__inner">
    <p class="eyebrow">Association JA IMAGE — Cinéma malien &amp; africain, Bamako</p>
    <h1>L'ÉCRAN COMME <em>ÉCOLE</em></h1>
    <p class="lead">Des griots d'hier aux courts-métrages d'aujourd'hui : JA IMAGE fait vivre le cinéma malien et africain à Bamako, et accompagne les cinéastes autodidactes qui apprennent à cadrer, raconter et monter par eux-mêmes.</p>
    <div class="btn-row">
      <a href="programmes.html" class="btn btn--primary">Découvrir nos programmes</a>
      <a href="contact.html" class="btn btn--outline">Rejoindre l'association</a>
    </div>
  </div>
</section>

<section class="reveal">
  <div class="container two-col">
    <div>
      <p class="eyebrow">Notre conviction</p>
      <p class="manifesto">On n'a pas besoin d'une école de cinéma pour raconter une histoire. On a besoin d'un <span class="accent">écran</span>, d'une caméra, et d'une salle qui y croit.</p>
    </div>
    <div>
      <p>JA IMAGE réunit un public curieux et des cinéastes en apprentissage autour d'une même idée : le cinéma se transmet aussi par la pratique, la projection et la rencontre — pas seulement par les bancs d'une école.</p>
      <div class="stats" style="margin-top:32px;">
        <div class="stat"><b>120+</b><span>Autodidactes accompagnés</span></div>
        <div class="stat"><b>40</b><span>Projections organisées</span></div>
        <div class="stat"><b>15</b><span>Ateliers &amp; résidences</span></div>
        <div class="stat"><b>8</b><span>Pays représentés à l'écran</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section--dark reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Ce que nous faisons</p>
      <h2>Trois manières de faire vivre le cinéma</h2>
      <p>Chaque action de l'association nourrit la suivante : montrer des films, ouvrir des fenêtres sur le monde, et donner aux autodidactes les moyens d'en tourner à leur tour.</p>
    </div>
    <div class="grid grid--3">
      <div class="card"><span class="num">01</span><h3>Cinéma malien &amp; africain</h3><p>Ciné-clubs, projections en plein air et rencontres avec des cinéastes pour donner à voir les films qui racontent le Mali et le continent.</p></div>
      <div class="card"><span class="num">02</span><h3>Fenêtre sur les cinémas du monde</h3><p>Une place aussi pour les cinémas étrangers, pour nourrir les regards et créer des ponts entre les cultures.</p></div>
      <div class="card"><span class="num">03</span><h3>Accompagnement des autodidactes</h3><p>Formations, mentorat et prêt de matériel pour celles et ceux qui apprennent à filmer sans passer par une école.</p></div>
    </div>
  </div>
</section>

<section class="reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Prochainement</p>
      <h2>Au programme</h2>
    </div>
    <div class="grid grid--3">
      <div>
        <div class="imgcard"><img src="{IMG['set_filming']}" alt="Tournage"><div class="imgcard__label"><span class="tag">Ciné-club</span><h3>Séance mensuelle de courts-métrages africains</h3></div></div>
      </div>
      <div>
        <div class="imgcard"><img src="{IMG['workshop_laptop']}" alt="Atelier montage"><div class="imgcard__label"><span class="tag">Atelier</span><h3>Initiation au montage pour débutants</h3></div></div>
      </div>
      <div>
        <a href="concours.html"><div class="imgcard"><img src="{IMG['group_smile']}" alt="Ciné Court School"><div class="imgcard__label"><span class="tag">Concours annuel</span><h3>Ciné Court School — le concours des élèves cinéastes</h3></div></div></a>
      </div>
    </div>
    <p style="margin-top:32px;"><a href="programmes.html" class="btn btn--outline">Voir tous les programmes</a></p>
  </div>
</section>

<section class="section--dark reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">À la une</p>
      <h2>Actualités</h2>
    </div>
    <div class="grid grid--3">
      <div class="card"><span class="num">12 juil. 2026</span><h3>Un nouveau ciné-club mensuel à Bamako</h3><p>JA IMAGE lance une séance récurrente dédiée aux courts-métrages africains, ouverte à tous les publics.</p></div>
      <div class="card"><span class="num">28 juin 2026</span><h3>Cinq courts-métrages africains à voir cette année</h3><p>Notre sélection de films marquants portés par une nouvelle génération de cinéastes.</p></div>
      <div class="card"><span class="num">15 juin 2026</span><h3>Retour sur notre atelier montage de printemps</h3><p>Douze autodidactes ont terminé leur premier montage encadré en trois semaines.</p></div>
    </div>
    <p style="margin-top:32px;"><a href="actualites.html" class="btn btn--outline">Toutes les actualités</a></p>
  </div>
</section>

<section class="reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Ils nous soutiennent</p>
      <h2>Partenaires</h2>
    </div>
    <div class="partners-grid">
      <div class="partner-card">Partenaire institutionnel</div>
      <div class="partner-card">Partenaire média</div>
      <div class="partner-card">Partenaire culturel</div>
      <div class="partner-card">Votre structure ?</div>
    </div>
  </div>
</section>

<section class="cta-band reveal">
  <div class="container">
    <h2>Vous voulez apprendre, projeter ou soutenir ?</h2>
    <p style="max-width:50ch;margin:0 auto 28px;opacity:.9;">Rejoignez une association qui croit que le cinéma se pratique autant qu'il se regarde.</p>
    <a href="contact.html" class="btn btn--primary">Nous rejoindre</a>
  </div>
</section>
"""
    page("index.html", "Accueil", "JA IMAGE, association de promotion du cinéma africain et international, et d'accompagnement des cinéastes autodidactes à Bamako.", body, with_intro=True)

# ============================================================ ASSOCIATION ==

def build_association():
    body = f"""
{pagehero("Générique", "QUI SOMMES-<em>NOUS</em>", "JA IMAGE est une association basée à Bamako, née de la conviction que le cinéma se transmet aussi hors des écoles.")}

<section class="reveal">
  <div class="container two-col">
    <img src="{IMG['group_meeting']}" alt="Rencontre de l'équipe JA IMAGE">
    <div>
      <p class="eyebrow">Notre histoire</p>
      <h2 style="font-size:34px;">Une salle, une caméra, une communauté</h2>
      <p>JA IMAGE est née à Bamako de la rencontre entre passionnés de cinéma et jeunes cinéastes autodidactes, convaincus que la caméra peut s'apprendre autrement qu'à l'école. Depuis, l'association organise des projections, anime des ateliers et accompagne celles et ceux qui apprennent à raconter des histoires par l'image.</p>
      <p>Ce qui nous rassemble : la conviction qu'un regard curieux et une caméra suffisent pour commencer — dans la lignée d'un pays où l'on raconte des histoires depuis bien avant l'invention de la caméra.</p>
      <p class="credit-line">Le Mali a donné au cinéma africain des cinéastes majeurs, comme Souleymane Cissé — et un rendez-vous continental, le FESPACO à Ouagadougou, qui continue d'inspirer notre travail au quotidien.</p>
    </div>
  </div>
</section>

<section class="section--dark reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Notre mission</p>
      <h2>Trois engagements</h2>
    </div>
    <div class="grid grid--3">
      <div class="card"><span class="num">01</span><h3>Promouvoir</h3><p>Faire connaître le cinéma africain et les cinémas du monde auprès du public malien, à travers des projections accessibles.</p></div>
      <div class="card"><span class="num">02</span><h3>Accompagner</h3><p>Offrir aux autodidactes un cadre d'apprentissage concret, en dehors des circuits de formation classiques.</p></div>
      <div class="card"><span class="num">03</span><h3>Relier</h3><p>Créer des espaces de rencontre entre cinéastes, publics, institutions et partenaires.</p></div>
    </div>
  </div>
</section>

<section class="reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Ce qui nous guide</p>
      <h2>Nos valeurs</h2>
    </div>
    <div class="grid grid--4">
      <div class="card"><h3 style="font-size:19px;">Accessibilité</h3><p>Le cinéma et son apprentissage doivent rester ouverts à tous, quels que soient les moyens de départ.</p></div>
      <div class="card"><h3 style="font-size:19px;">Créativité</h3><p>Chaque parcours d'autodidacte est différent — nous nous adaptons plutôt que d'imposer un moule.</p></div>
      <div class="card"><h3 style="font-size:19px;">Transmission</h3><p>Ceux qui savent partagent avec ceux qui apprennent, dans les deux sens.</p></div>
      <div class="card"><h3 style="font-size:19px;">Solidarité panafricaine</h3><p>Le cinéma africain se regarde et se soutient au-delà des frontières.</p></div>
    </div>
  </div>
</section>

<section class="section--tinted reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">L'équipe</p>
      <h2>Celles et ceux qui font JA IMAGE</h2>
      <p>Une petite équipe, portée par des bénévoles et des cinéastes engagés. <em>(Contenu provisoire à personnaliser.)</em></p>
    </div>
    <div class="grid grid--4">
      <div class="member"><div class="photo"><img src="{IMG['portrait_woman1']}" alt="Portrait"></div><h3>Aïssata Diarra</h3><p class="role">Présidente</p></div>
      <div class="member"><div class="photo"><img src="{IMG['portrait_man1']}" alt="Portrait"></div><h3>Moussa Traoré</h3><p class="role">Coordinateur des programmes</p></div>
      <div class="member"><div class="photo"><img src="{IMG['portrait_woman2']}" alt="Portrait"></div><h3>Fatoumata Coulibaly</h3><p class="role">Responsable formation</p></div>
      <div class="member"><div class="photo"><img src="{IMG['portrait_man2']}" alt="Portrait"></div><h3>Ibrahim Keïta</h3><p class="role">Chargé de communication</p></div>
    </div>
  </div>
</section>

<section class="cta-band reveal">
  <div class="container">
    <h2>Envie de nous rejoindre ?</h2>
    <a href="contact.html" class="btn btn--primary" style="margin-top:10px;">Nous contacter</a>
  </div>
</section>
"""
    page("association.html", "Association", "Qui sommes-nous : histoire, mission, valeurs et équipe de l'association JA IMAGE à Bamako.", body)

# ============================================================= PROGRAMMES ==

def build_programmes():
    body = f"""
{pagehero("Au programme", "NOS <em>PROGRAMMES</em>", "Trois façons de participer à la vie de JA IMAGE, du simple spectateur au cinéaste en formation.")}

<section class="reveal">
  <div class="container">
    <div class="grid grid--3">
      <div>
        <div class="imgcard"><img src="{IMG['set_filming']}" alt="Ciné-clubs"><div class="imgcard__label"><span class="tag">Diffusion</span><h3>Ciné-clubs &amp; projections</h3></div></div>
        <p style="margin-top:14px;color:var(--gris-fonce);">Des séances régulières, en salle ou en plein air, pour découvrir le cinéma africain et international et en discuter ensemble.</p>
      </div>
      <div>
        <div class="imgcard"><img src="{IMG['group_smile']}" alt="Résidences et ateliers"><div class="imgcard__label"><span class="tag">Rencontre</span><h3>Résidences &amp; ateliers</h3></div></div>
        <p style="margin-top:14px;color:var(--gris-fonce);">Des temps courts et intensifs pour écrire, tourner ou monter, encadrés par des cinéastes expérimentés.</p>
      </div>
      <div>
        <div class="imgcard"><img src="{IMG['workshop_laptop']}" alt="Suivi individualisé"><div class="imgcard__label"><span class="tag">Accompagnement</span><h3>Suivi individualisé des autodidactes</h3></div></div>
        <p style="margin-top:14px;color:var(--gris-fonce);">Un mentorat personnalisé pour les autodidactes qui veulent aller plus loin sur un projet précis.</p>
      </div>
    </div>
  </div>
</section>

<section class="section--dark reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Le parcours</p>
      <h2>Comment ça marche</h2>
    </div>
    <div class="steps">
      <div class="step"><span class="n">01</span><div><h3>Découverte</h3><p>Vous nous contactez ou participez à une séance découverte pour comprendre les formats proposés.</p></div></div>
      <div class="step"><span class="n">02</span><div><h3>Inscription</h3><p>Vous rejoignez le programme qui correspond à votre niveau, via l'espace autodidactes.</p></div></div>
      <div class="step"><span class="n">03</span><div><h3>Accompagnement</h3><p>Ateliers, mentorat et prêt de matériel tout au long du parcours.</p></div></div>
      <div class="step"><span class="n">04</span><div><h3>Restitution</h3><p>Vos projets sont présentés lors d'une projection publique ou d'un ciné-club.</p></div></div>
    </div>
  </div>
</section>

<section class="cta-band reveal">
  <div class="container">
    <h2>Je m'inscris à un programme</h2>
    <a href="ressources.html" class="btn btn--primary" style="margin-top:10px;">Voir l'espace autodidactes</a>
  </div>
</section>
"""
    page("programmes.html", "Programmes", "Ciné-clubs, résidences, ateliers et accompagnement individualisé proposés par JA IMAGE.", body)

# ============================================================== FORMATION ==

def build_formation():
    body = f"""
{pagehero("Coulisses", "FORMATION", "Un parcours pensé pour celles et ceux qui apprennent le cinéma seuls, à leur rythme, avec un accompagnement quand il le faut.")}

<section class="reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Le programme</p>
      <h2>Trois modules</h2>
    </div>
    <div class="grid grid--3">
      <div class="card"><span class="num">01</span><h3>Écriture &amp; scénario</h3><p>Construire une histoire, structurer un court-métrage, écrire un pitch qui donne envie de tourner.</p></div>
      <div class="card"><span class="num">02</span><h3>Prise de vue &amp; lumière</h3><p>Cadrage, mouvement de caméra, lumière naturelle et matériel léger — filmer avec ce qu'on a.</p></div>
      <div class="card"><span class="num">03</span><h3>Montage &amp; post-production</h3><p>Monter avec des outils accessibles, travailler le son, s'initier à l'étalonnage simple.</p></div>
    </div>
  </div>
</section>

<section class="section--dark reveal">
  <div class="container two-col">
    <img src="{IMG['vintage_cam']}" alt="Matériel de formation">
    <div>
      <p class="eyebrow">Format des sessions</p>
      <h2 style="font-size:32px;">Petits groupes, mentors, projet concret</h2>
      <p>Chaque module se déroule en petit groupe, avec un mentor cinéaste et un projet réel à réaliser d'ici la fin de la session.</p>
      <ul style="display:flex;flex-direction:column;gap:10px;margin-top:18px;">
        <li>— Séances hebdomadaires, en soirée ou le week-end</li>
        <li>— Groupes de 8 à 12 personnes</li>
        <li>— Mentorat par des cinéastes confirmés</li>
        <li>— Un projet concret à la clé, présenté en ciné-club</li>
      </ul>
    </div>
  </div>
</section>

<section class="reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Calendrier</p>
      <h2>Prochaines sessions</h2>
      <p><em>Dates provisoires — à confirmer.</em></p>
    </div>
    <div class="steps">
      <div class="step"><span class="n">SEPT</span><div><h3>Écriture &amp; scénario</h3><p>À partir du 4 septembre 2026 — places limitées.</p></div></div>
      <div class="step"><span class="n">OCT</span><div><h3>Prise de vue &amp; lumière</h3><p>À partir du 2 octobre 2026.</p></div></div>
      <div class="step"><span class="n">NOV</span><div><h3>Montage &amp; post-production</h3><p>À partir du 6 novembre 2026.</p></div></div>
    </div>
  </div>
</section>

<section class="cta-band reveal">
  <div class="container">
    <h2>Réserver ma place</h2>
    <a href="ressources.html" class="btn btn--primary" style="margin-top:10px;">Faire ma demande</a>
  </div>
</section>
"""
    page("formation.html", "Formation", "Le programme de formation de JA IMAGE pour cinéastes autodidactes : écriture, prise de vue, montage.", body)

# ============================================================= RESSOURCES ==

def build_ressources():
    body = f"""
{pagehero("Boîte à outils", "ESPACE <em>AUTODIDACTES</em>", "Guides, tutoriels, matériel et accompagnement pour apprendre à filmer par vous-même.")}

<section class="reveal">
  <div class="container">
    <div class="grid grid--4">
      <div class="card"><span class="num">GUIDE</span><h3>Bases du cadrage</h3><p>Un guide pas-à-pas pour composer ses plans avec peu de moyens.</p></div>
      <div class="card"><span class="num">VIDÉO</span><h3>Tutoriels de montage</h3><p>Des tutoriels courts sur les logiciels de montage accessibles et gratuits.</p></div>
      <div class="card"><span class="num">PRÊT</span><h3>Matériel à emprunter</h3><p>Caméras, micros et éclairages disponibles pour les membres actifs.</p></div>
      <div class="card"><span class="num">LECTURE</span><h3>Bibliothèque de scénarios</h3><p>Des scénarios de courts-métrages africains à consulter sur place.</p></div>
    </div>
  </div>
</section>

<section class="section--dark reveal">
  <div class="container two-col">
    <div>
      <p class="eyebrow">Rejoindre l'espace autodidactes</p>
      <h2 style="font-size:32px;">Dites-nous où vous en êtes</h2>
      <p>Que vous débutiez avec votre téléphone ou que vous ayez déjà tourné un premier court-métrage, l'accompagnement s'adapte à votre niveau.</p>
      <img src="{IMG['clapper_gear']}" alt="Matériel de tournage" style="border-radius:2px;margin-top:24px;">
    </div>
    <form class="form-panel" action="https://formsubmit.co/{FORM_EMAIL}" method="POST">
      <input type="hidden" name="_subject" value="Nouvelle inscription — Espace autodidactes JA IMAGE">
      <input type="text" name="_honey" style="display:none">
      <input type="hidden" name="_captcha" value="false">
      <div class="field"><label for="nom">Nom complet</label><input id="nom" name="Nom" type="text" required></div>
      <div class="form-row">
        <div class="field"><label for="email">Email</label><input id="email" name="Email" type="email" required></div>
        <div class="field"><label for="tel">Téléphone</label><input id="tel" name="Téléphone" type="tel"></div>
      </div>
      <div class="field">
        <label for="niveau">Niveau</label>
        <select id="niveau" name="Niveau">
          <option>Débutant</option>
          <option>Intermédiaire</option>
          <option>Avancé</option>
        </select>
      </div>
      <div class="field"><label for="motiv">Ce que vous voulez apprendre</label><textarea id="motiv" name="Message"></textarea></div>
      <button type="submit" class="btn btn--primary" style="width:100%;justify-content:center;">Envoyer ma demande</button>
    </form>
  </div>
</section>
"""
    page("ressources.html", "Espace autodidactes", "Ressources, matériel et inscription pour les cinéastes autodidactes accompagnés par JA IMAGE.", body)

# ============================================================= ACTUALITES ==

def build_actualites():
    articles = [
        (IMG['camera_hand'], "12 juillet 2026", "Un nouveau ciné-club mensuel à Bamako",
         "JA IMAGE lance une séance récurrente dédiée aux courts-métrages africains, ouverte à tous les publics, avec un temps d'échange après chaque projection."),
        (IMG['clapper_2'], "28 juin 2026", "Cinq courts-métrages africains à voir cette année",
         "Notre sélection de films marquants portés par une nouvelle génération de cinéastes du continent."),
        (IMG['workshop_laptop'], "15 juin 2026", "Retour sur notre atelier montage de printemps",
         "Douze autodidactes ont terminé leur premier montage encadré en trois semaines, avec restitution publique."),
        (IMG['crowd_event'], "2 juin 2026", "JA IMAGE partenaire d'un festival régional",
         "L'association s'associe à un festival de cinéma régional pour présenter les projets de ses autodidactes."),
        (IMG['group_smile'], "20 mai 2026", "Trois autodidactes présentent leur premier court-métrage",
         "Un aboutissement pour trois membres accompagnés depuis un an, dont les films seront projetés en ciné-club."),
    ]
    items = "\n".join(f"""
    <div class="article">
      <img src="{img}" alt="{title}">
      <div>
        <span class="date">{date}</span>
        <h3>{title}</h3>
        <p>{excerpt}</p>
        <a href="#" class="btn btn--outline" style="padding:9px 18px;font-size:13px;">Lire la suite</a>
      </div>
    </div>""" for img, date, title, excerpt in articles)

    body = f"""
{pagehero("À la une", "ACTUALITÉS", "Les nouvelles de l'association : projections, ateliers, partenariats et parcours d'autodidactes.")}

<section class="reveal">
  <div class="container">
    {items}
  </div>
</section>
"""
    page("actualites.html", "Actualités", "Actualités de l'association JA IMAGE : projections, ateliers, partenariats et réussites d'autodidactes.", body)

# ================================================================ GALERIE ==

def build_galerie():
    items = [
        (IMG['hero'], "Projections", "Séance en salle"),
        (IMG['audience'], "Projections", "Public en séance"),
        (IMG['popcorn_theatre'], "Projections", "Avant la séance"),
        (IMG['set_filming'], "Tournages", "En plein tournage"),
        (IMG['clapper_gear'], "Tournages", "Prêts pour la première prise"),
        (IMG['film_reel'], "Tournages", "Retour à la pellicule"),
        (IMG['workshop_laptop'], "Ateliers", "Atelier montage"),
        (IMG['group_laptop'], "Ateliers", "Travail en groupe"),
        (IMG['crowd_event'], "Événements", "Rencontre publique"),
    ]
    cards = "\n".join(f"""
      <div class="imgcard"><img src="{img}" alt="{title}"><div class="imgcard__label"><span class="tag">{tag}</span><h3>{title}</h3></div></div>""" for img, tag, title in items)

    body = f"""
{pagehero("Salle comble", "GALERIE", "Projections, tournages, ateliers : quelques images de la vie de JA IMAGE.")}

<section class="reveal">
  <div class="container">
    <div class="tag-row">
      <span class="tag">Projections</span><span class="tag">Ateliers</span><span class="tag">Tournages</span><span class="tag">Événements</span>
    </div>
    <div class="grid grid--3">
      {cards}
    </div>
  </div>
</section>
"""
    page("galerie.html", "Galerie", "Galerie photos de JA IMAGE : projections, tournages, ateliers et événements.", body)

# ============================================================= PARTENAIRES ==

def build_partenaires():
    body = f"""
{pagehero("Alliés", "PARTENAIRES &amp; <em>SOUTIENS</em>", "JA IMAGE avance grâce à des partenaires institutionnels, culturels, techniques et financiers.")}

<section class="reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Nos partenaires</p>
      <h2>Ils rendent nos programmes possibles</h2>
      <p><em>Emplacements provisoires — logos à intégrer.</em></p>
    </div>
    <div class="partners-grid">
      <div class="partner-card">Partenaire institutionnel</div>
      <div class="partner-card">Partenaire média</div>
      <div class="partner-card">Partenaire technique</div>
      <div class="partner-card">Partenaire culturel</div>
      <div class="partner-card">Partenaire financier</div>
      <div class="partner-card">Votre structure ?</div>
    </div>
  </div>
</section>

<section class="section--dark reveal">
  <div class="container two-col">
    <div>
      <p class="eyebrow">Devenir partenaire</p>
      <h2 style="font-size:32px;">Soutenir le cinéma qui se pratique</h2>
      <p>Prêt de salle, mécénat de matériel, soutien financier ou visibilité média : chaque forme de partenariat aide directement les autodidactes accompagnés par JA IMAGE.</p>
      <a href="contact.html" class="btn btn--primary" style="margin-top:12px;">Nous contacter</a>
    </div>
    <img src="{IMG['crowd_event']}" alt="Événement JA IMAGE">
  </div>
</section>
"""
    page("partenaires.html", "Partenaires", "Devenez partenaire de JA IMAGE : soutien institutionnel, culturel, technique ou financier.", body)

# ================================================================ CONTACT ==

def build_contact():
    body = f"""
{pagehero("Prise de contact", "CONTACT", "Une question, un projet, une envie de rejoindre l'association ? Écrivez-nous.")}

<section class="reveal">
  <div class="container two-col">
    <div>
      <p class="eyebrow">Nos coordonnées</p>
      <h2 style="font-size:32px;">Venez nous voir</h2>
      <p style="color:var(--gris-fonce);">Adresse : Hamdalaye, Bamako, Mali <em>(à préciser)</em><br>
      Téléphone : +223 00 00 00 00 <em>(à préciser)</em><br>
      Email : {FORM_EMAIL}<br>
      Réseaux : Facebook · Instagram</p>
      <img src="{IMG['group_laptop']}" alt="Équipe JA IMAGE" style="border-radius:2px;margin-top:24px;">
    </div>
    <form class="form-panel" action="https://formsubmit.co/{FORM_EMAIL}" method="POST">
      <input type="hidden" name="_subject" value="Nouveau message — Site JA IMAGE">
      <input type="text" name="_honey" style="display:none">
      <input type="hidden" name="_captcha" value="false">
      <div class="field"><label for="c-nom">Nom</label><input id="c-nom" name="Nom" type="text" required></div>
      <div class="field"><label for="c-email">Email</label><input id="c-email" name="Email" type="email" required></div>
      <div class="field">
        <label for="c-sujet">Sujet</label>
        <select id="c-sujet" name="Sujet">
          <option>Adhésion</option>
          <option>Programme autodidactes</option>
          <option>Partenariat</option>
          <option>Presse</option>
          <option>Autre</option>
        </select>
      </div>
      <div class="field"><label for="c-msg">Message</label><textarea id="c-msg" name="Message" required></textarea></div>
      <button type="submit" class="btn btn--primary" style="width:100%;justify-content:center;">Envoyer le message</button>
    </form>
  </div>
</section>
"""
    page("contact.html", "Contact", "Contactez l'association JA IMAGE à Bamako : adhésion, programmes, partenariats.", body)

# ========================================================== CINÉ COURT SCHOOL ==

def build_concours():
    body = f"""
<section class="pagehero">
  <div class="container">
    <p class="eyebrow">Concours annuel</p>
    <h1>CINÉ COURT <em>SCHOOL</em></h1>
    <p>Le concours annuel de courts-métrages de JA IMAGE, ouvert aux élèves maliens qui veulent raconter une histoire à l'image — du collège au lycée.</p>
    <div class="btn-row" style="margin-top:26px;">
      <a href="#inscription" class="btn btn--primary">Inscrire mon établissement</a>
      <a href="#reglement" class="btn btn--outline">Voir le règlement</a>
    </div>
  </div>
  <div class="bogolan-band" style="position:absolute;left:0;right:0;bottom:0;"></div>
</section>

<section class="reveal">
  <div class="container two-col">
    <img src="{IMG['set_filming']}" alt="Tournage d'élèves">
    <div>
      <p class="eyebrow">Le concours</p>
      <h2 style="font-size:32px;">Filmer dès l'école, avec ce qu'on a sous la main</h2>
      <p>Ciné Court School invite des équipes d'élèves, encadrées par un enseignant ou un mentor JA IMAGE, à écrire, tourner et monter un court-métrage sur un thème imposé chaque année. Téléphone, caméscope ou caméra empruntée : le matériel disponible suffit pour se lancer.</p>
      <p>Chaque édition se termine par une projection publique et une remise de prix, à Bamako.</p>
    </div>
  </div>
</section>

<section class="section--dark reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Qui peut participer</p>
      <h2>Catégories &amp; prix</h2>
    </div>
    <div class="grid grid--4">
      <div class="card"><span class="num">Collège</span><h3>Catégorie Collège</h3><p>Équipes encadrées, film de 3 minutes maximum.</p></div>
      <div class="card"><span class="num">Lycée</span><h3>Catégorie Lycée</h3><p>Équipes encadrées, film de 8 minutes maximum.</p></div>
      <div class="card"><span class="num">Jury</span><h3>Prix du jury</h3><p>Décerné par des professionnels du cinéma malien.</p></div>
      <div class="card"><span class="num">Public</span><h3>Prix du public</h3><p>Voté lors de la projection finale à Bamako.</p></div>
    </div>
  </div>
</section>

<section class="reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Calendrier de l'édition</p>
      <h2>Comment participer</h2>
      <p><em>Dates provisoires — à confirmer pour l'édition 2026-2027.</em></p>
    </div>
    <div class="steps">
      <div class="step"><span class="n">01</span><div><h3>Inscriptions ouvertes</h3><p>À partir de septembre 2026, via le formulaire ci-dessous — un établissement ou un enseignant référent par équipe.</p></div></div>
      <div class="step"><span class="n">02</span><div><h3>Ateliers de préparation</h3><p>Sessions courtes sur l'écriture et le tournage, animées par JA IMAGE, pour les équipes inscrites.</p></div></div>
      <div class="step"><span class="n">03</span><div><h3>Tournage</h3><p>Chaque équipe tourne son court-métrage sur le thème imposé de l'édition.</p></div></div>
      <div class="step"><span class="n">04</span><div><h3>Dépôt des films</h3><p>Envoi du montage final avant la date limite de l'édition.</p></div></div>
      <div class="step"><span class="n">05</span><div><h3>Projection &amp; cérémonie</h3><p>Projection publique à Bamako et remise des prix devant le jury et les familles.</p></div></div>
    </div>
  </div>
</section>

<section class="section--dark reveal" id="reglement">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">À respecter</p>
      <h2>Règlement, en bref</h2>
    </div>
    <ul class="rule-list">
      <li><b>Durée</b><span>3 minutes maximum en catégorie Collège, 8 minutes en catégorie Lycée.</span></li>
      <li><b>Encadrement</b><span>Chaque équipe est suivie par un enseignant de son établissement ou un mentor JA IMAGE.</span></li>
      <li><b>Matériel</b><span>Téléphone, caméscope ou caméra empruntée sont acceptés — le fond prime sur la forme.</span></li>
      <li><b>Thème</b><span>Un thème commun est imposé à toutes les équipes chaque année.</span></li>
      <li><b>Langue</b><span>Films en français ou en langue nationale, sous-titrés en français.</span></li>
    </ul>
    <p style="margin-top:24px;"><a href="#" class="btn btn--outline">Télécharger le règlement complet (PDF)</a></p>
  </div>
</section>

<section class="reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Éditions précédentes</p>
      <h2>Ce que les élèves ont déjà tourné</h2>
    </div>
    <div class="grid grid--3">
      <div class="imgcard"><img src="{IMG['group_smile']}" alt="Édition précédente"><div class="imgcard__label"><span class="tag">Édition 2025</span><h3>Remise des prix</h3></div></div>
      <div class="imgcard"><img src="{IMG['workshop_laptop']}" alt="Édition précédente"><div class="imgcard__label"><span class="tag">Édition 2025</span><h3>Atelier de préparation</h3></div></div>
      <div class="imgcard"><img src="{IMG['crowd_event']}" alt="Édition précédente"><div class="imgcard__label"><span class="tag">Édition 2025</span><h3>Projection publique</h3></div></div>
    </div>
  </div>
</section>

<section class="section--dark reveal" id="inscription">
  <div class="container two-col">
    <div>
      <p class="eyebrow">Inscription</p>
      <h2 style="font-size:32px;">Inscrire une équipe ou un établissement</h2>
      <p>Enseignants, encadrants ou élèves majeurs : dites-nous qui vous êtes, nous revenons vers vous avec le calendrier détaillé et le thème de l'édition.</p>
    </div>
    <form class="form-panel" action="https://formsubmit.co/{FORM_EMAIL}" method="POST">
      <input type="hidden" name="_subject" value="Nouvelle inscription — Ciné Court School">
      <input type="text" name="_honey" style="display:none">
      <input type="hidden" name="_captcha" value="false">
      <div class="form-row">
        <div class="field"><label for="cc-nom">Nom de l'équipe / élève</label><input id="cc-nom" name="Nom" type="text" required></div>
        <div class="field"><label for="cc-etab">Établissement</label><input id="cc-etab" name="Établissement" type="text" required></div>
      </div>
      <div class="form-row">
        <div class="field"><label for="cc-ville">Ville</label><input id="cc-ville" name="Ville" type="text"></div>
        <div class="field">
          <label for="cc-cat">Catégorie</label>
          <select id="cc-cat" name="Catégorie">
            <option>Collège</option>
            <option>Lycée</option>
          </select>
        </div>
      </div>
      <div class="field"><label for="cc-email">Email de l'encadrant</label><input id="cc-email" name="Email" type="email" required></div>
      <div class="field"><label for="cc-msg">Message</label><textarea id="cc-msg" name="Message"></textarea></div>
      <button type="submit" class="btn btn--primary" style="width:100%;justify-content:center;">Envoyer l'inscription</button>
    </form>
  </div>
</section>
"""
    page("concours.html", "Ciné Court School", "Ciné Court School, le concours annuel de courts-métrages pour élèves organisé par JA IMAGE à Bamako.", body)

# =============================================================== RUN ALL ==

if __name__ == "__main__":
    build_index()
    build_association()
    build_programmes()
    build_formation()
    build_ressources()
    build_concours()
    build_actualites()
    build_galerie()
    build_partenaires()
    build_contact()
    print("\nSite généré avec succès.")
