#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Générateur du site multipage JA IMAGE."""
import os

import time
OUT = os.path.dirname(os.path.abspath(__file__))
ASSET_V = str(int(time.time()))  # invalide le cache navigateur/CDN à chaque régénération

# ---------------------------------------------------------------- images ---
# Photos réelles des formations JA IMAGE / Ciné Court School (fournies par l'association)
IMG = {
    'group_library':      'assets/photos/group_library.jpg',
    'classroom_camop':     'assets/photos/classroom_camop.jpg',
    'camera_training':     'assets/photos/camera_training.jpg',
    'desks_snacks':        'assets/photos/desks_snacks.jpg',
    'adults_table':        'assets/photos/adults_table.jpg',
    'landscape':           'assets/photos/landscape.jpg',
    'portrait_boubou':     'assets/photos/portrait_boubou.jpg',
    'classroom_wide1':     'assets/photos/classroom_wide1.jpg',
    'classroom_flipchart': 'assets/photos/classroom_flipchart.jpg',
    'classroom_banner':    'assets/photos/classroom_banner.jpg',
    'classroom_boubou2':   'assets/photos/classroom_boubou2.jpg',
    'certificate_ceremony':'assets/photos/certificate_ceremony.jpg',
    'boubou_gesture2':     'assets/photos/boubou_gesture2.jpg',
    'adults_table2':       'assets/photos/adults_table2.jpg',
    'outdoor_filming':     'assets/photos/outdoor_filming.jpg',
    'students_qa':         'assets/photos/students_qa.jpg',
    'speaker_mic':         'assets/photos/speaker_mic.jpg',
    'camera_artwall':      'assets/photos/camera_artwall.jpg',
    'camera_mentorship':   'assets/photos/camera_mentorship.jpg',
    'hilltop_camera':      'assets/photos/hilltop_camera.jpg',
}
LOGO_CCS = 'assets/photos/logo_ccs.png'

# Informations réelles — extraites du document de présentation de l'association
ORG = {
    "nom_legal": "Association Culturelle JA",
    "nom_marque": "JA IMAGE",
    "devise": "Former, créer, inspirer",
    "slogan": "Cultivons les talents, partageons les histoires",
    "fondation": "2020",
    "adresse": "Lafiabougou, Rue 352, Porte 432 — Commune IV, Bamako, Mali",
    "telephone": "+223 74 60 91 09",
    "telephone_href": "+22374609109",
}

FORM_EMAIL = "contactdja.image@gmail.com"  # confirmé par Zaide — adresse réelle de l'association

# Nav complète (utilisée pour le pied de page / sitemap)
NAV = [
    ("index.html", "Accueil"),
    ("association.html", "Association"),
    ("festival.html", "Festival Cinéastes Autodidactes"),
    ("concours.html", "Ciné Court School"),
    ("programmes.html", "Programmes"),
    ("formation.html", "Formation"),
    ("ressources.html", "Ressources"),
    ("initiatives.html", "Nos initiatives"),
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
    ("festival.html", "Festival"),
    ("concours.html", "Ciné Court School"),
    ("actualites.html", "Actualités"),
]

# Rattache une page secondaire à son onglet parent pour l'état actif
ACTIVE_PARENT = {
    "formation.html": "programmes.html",
    "ressources.html": "programmes.html",
    "initiatives.html": "programmes.html",
    "partenaires.html": "association.html",
    "galerie.html": "actualites.html",
}

# ------------------------------------------------------------- fragments ---

def reel_svg(extra_class=""):
    cls = f"reel reel--spin {extra_class}".strip()
    return f"""<svg class="{cls}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="46" fill="var(--noir-salle-2)" stroke="var(--or-projecteur)" stroke-width="3.5"/>
  <circle cx="50" cy="50" r="13" fill="var(--noir-salle)" stroke="var(--or-projecteur)" stroke-width="3.5"/>
  <circle cx="50" cy="50" r="4" fill="var(--or-projecteur)"/>
  <circle cx="50" cy="19" r="9" fill="var(--noir-salle)" stroke="var(--or-projecteur)" stroke-width="3.5"/>
  <circle cx="76.8" cy="34.5" r="9" fill="var(--noir-salle)" stroke="var(--or-projecteur)" stroke-width="3.5"/>
  <circle cx="76.8" cy="65.5" r="9" fill="var(--noir-salle)" stroke="var(--or-projecteur)" stroke-width="3.5"/>
  <circle cx="50" cy="81" r="9" fill="var(--noir-salle)" stroke="var(--or-projecteur)" stroke-width="3.5"/>
  <circle cx="23.2" cy="65.5" r="9" fill="var(--noir-salle)" stroke="var(--or-projecteur)" stroke-width="3.5"/>
  <circle cx="23.2" cy="34.5" r="9" fill="var(--noir-salle)" stroke="var(--or-projecteur)" stroke-width="3.5"/>
</svg>"""


def hero_reel(photo_keys):
    """Bobine avec un ruban de pellicule (vraies photos) qui s'en échappe en éventail.
    Toujours dans le flux de la hero — ne dépend d'aucune largeur d'écran."""
    import math
    n = len(photo_keys)
    r_start, r_end = 80, 258
    a_start, a_end = 190, 253
    size_start, size_end = 56, 90
    frames = []
    for i, key in enumerate(photo_keys):
        t = i / (n - 1)
        r = r_start + (r_end - r_start) * t
        a = math.radians(a_start + (a_end - a_start) * t)
        x = r * math.cos(a)
        y = r * math.sin(a)
        size = size_start + (size_end - size_start) * t
        rot = math.degrees(a) + 90
        frames.append(
            f'<div class="hero-reel__frame" style="'
            f'--x:{x:.1f}px; --y:{y:.1f}px; --rot:{rot:.1f}deg; --size:{size:.0f}px; --i:{i};">'
            f'<img src="{IMG[key]}" alt=""></div>'
        )
    return f"""<div class="hero-reel">
  <div class="hero-reel__frames">{"".join(frames)}</div>
  <div class="hero-reel__hub">{reel_svg()}</div>
</div>"""


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
<link rel="stylesheet" href="css/style.css?v={ASSET_V}">
</head>"""


def header(active):
    effective = ACTIVE_PARENT.get(active, active)
    links = []
    for href, label in NAV_TOP:
        classes = []
        if href == effective:
            classes.append("active")
        if href in ("concours.html", "festival.html"):
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
        <p>{ORG['nom_legal']} — {ORG['nom_marque']}, fondée en {ORG['fondation']}. Promotion du cinéma, de la culture et de la jeunesse au Mali ; formation et professionnalisation des cinéastes autodidactes.</p>
        <p style="font-style:italic;opacity:.75;margin-top:10px;">« {ORG['devise']} »<br>{ORG['slogan']}</p>
      </div>
      <div>
        <h4>Association</h4>
        <a href="association.html">Qui sommes-nous</a>
        <a href="festival.html">Festival Cinéastes Autodidactes</a>
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
        <a href="initiatives.html">Nos initiatives</a>
      </div>
      <div>
        <h4>Contact</h4>
        <a href="contact.html">{ORG['adresse']}</a>
        <a href="tel:{ORG['telephone_href']}">{ORG['telephone']}</a>
        <a href="mailto:{FORM_EMAIL}">{FORM_EMAIL}</a>
        <a href="#">Facebook · Instagram</a>
      </div>
    </div>
    <div class="bogolan-band" style="margin-bottom:24px;"></div>
    <div class="footer-bottom">
      <span>© <span class="year"></span> {ORG['nom_legal']} ({ORG['nom_marque']}) — Bamako, Mali</span>
      <span>Contenu provisoire — site en construction</span>
    </div>
  </div>
</footer>"""


INTRO = f"""<div class="intro">
  <div class="intro__flicker"></div>
  <div class="intro__beam"></div>
  <div class="intro__grain"></div>
  <div class="intro__content">
    <div class="intro__reel-row">
      {reel_svg()}
      <div class="intro__stage">
        <div class="intro__flash"></div>
        <img class="piece piece--black" src="assets/fig_black.png" alt="">
        <img class="piece piece--red" src="assets/fig_red.png" alt="">
        <img class="piece piece--yellow" src="assets/fig_yellow.png" alt="">
        <img class="piece piece--purple" src="assets/fig_purple.png" alt="JA IMAGE">
      </div>
      {reel_svg()}
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
<script src="js/main.js?v={ASSET_V}"></script>
</body>
</html>"""
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("écrit:", filename)


def pagehero(eyebrow, title_html, lead):
    return f"""<section class="pagehero">
  <div class="mesh-bg"><span></span><span></span><span></span></div>
  <div class="container">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title_html}</h1>
    <p>{lead}</p>
  </div>
</section>"""

# ================================================================ ACCUEIL ==

def build_index():
    strip_photos = ['camera_training','classroom_camop','outdoor_filming','hilltop_camera',
                     'students_qa','camera_mentorship','classroom_wide1','speaker_mic']
    strip_frames = "".join(f'<div class="reel-strip__frame"><img src="{IMG[k]}" alt=""></div>' for k in strip_photos * 2)
    reel_strip = f"""<div class="reel-strip">
  {reel_svg()}
  <div class="reel-strip__window"><div class="reel-strip__track">{strip_frames}</div></div>
</div>"""
    body = f"""
{reel_strip}
<section class="hero">
  <div class="hero__bg" style="background:linear-gradient(180deg, rgba(12,12,16,.35) 0%, rgba(12,12,16,.55) 55%, #0c0c10 100%), url('{IMG['group_library']}') center/cover no-repeat;"></div>
  <div class="mesh-bg"><span></span><span></span><span></span></div>
  {hero_reel(['camera_training','classroom_camop','outdoor_filming','students_qa','hilltop_camera'])}
  <div class="container hero__inner">
    <p class="eyebrow">Association JA IMAGE — Cinéma malien &amp; africain, Bamako</p>
    <h1><span class="word" style="animation-delay:.5s">L'ÉCRAN</span> <span class="word" style="animation-delay:.62s">COMME</span> <span class="word" style="animation-delay:.74s"><em>ÉCOLE</em></span></h1>
    <p class="lead">Des griots d'hier aux courts-métrages d'aujourd'hui : JA IMAGE fait vivre le cinéma malien et africain à Bamako, et accompagne les cinéastes autodidactes qui apprennent à cadrer, raconter et monter par eux-mêmes.</p>
    <div class="btn-row">
      <a href="programmes.html" class="btn btn--primary">Découvrir nos programmes</a>
      <a href="contact.html" class="btn btn--outline">Rejoindre l'association</a>
    </div>
  </div>
</section>

<div class="marquee">
  <div class="marquee__track">
    {"".join(f"<span>{t} <b style='opacity:.45'>✶</b></span>" for t in ["Cinéma malien &amp; africain","Ciné Court School","Autodidactes","Bamako, Mali"]*2)}
  </div>
</div>

<section class="reveal">
  <div class="container two-col">
    <div>
      <p class="eyebrow">Notre conviction</p>
      <p class="manifesto">On n'a pas besoin d'une école de cinéma pour raconter une histoire. On a besoin d'un <span class="accent">écran</span>, d'une caméra, et d'une salle qui y croit.</p>
    </div>
    <div>
      <p>JA IMAGE réunit un public curieux et des cinéastes en apprentissage autour d'une même idée : le cinéma se transmet aussi par la pratique, la projection et la rencontre — pas seulement par les bancs d'une école.</p>
      <p style="font-family:var(--label);letter-spacing:.08em;text-transform:uppercase;font-size:14px;color:var(--rouge-rideau);margin-top:18px;">« {ORG['devise']} » — {ORG['slogan']}</p>
      <div class="stats" style="margin-top:32px;">
        <div class="stat"><b data-count="120" data-suffix="+">0</b><span>Autodidactes accompagnés</span></div>
        <div class="stat"><b data-count="40">0</b><span>Projections organisées</span></div>
        <div class="stat"><b data-count="15">0</b><span>Ateliers &amp; résidences</span></div>
        <div class="stat"><b data-count="8">0</b><span>Pays représentés à l'écran</span></div>
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
        <div class="imgcard"><img src="{IMG['camera_training']}" alt="Tournage"><div class="imgcard__label"><span class="tag">Ciné-club</span><h3>Séance mensuelle de courts-métrages africains</h3></div></div>
      </div>
      <div>
        <a href="festival.html"><div class="imgcard"><img src="{IMG['certificate_ceremony']}" alt="Festival Cinéastes Autodidactes"><div class="imgcard__label"><span class="tag">Festival annuel</span><h3>Festival Cinéastes Autodidactes</h3></div></div></a>
      </div>
      <div>
        <a href="concours.html"><div class="imgcard"><img src="{IMG['classroom_banner']}" alt="Ciné Court School"><div class="imgcard__label"><span class="tag">Concours annuel</span><h3>Ciné Court School — le concours des élèves cinéastes</h3></div></div></a>
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
  <div class="mesh-bg"><span></span><span></span><span></span></div>
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
{pagehero("Générique", "QUI SOMMES-<em>NOUS</em>", f"{ORG['nom_legal']} — {ORG['nom_marque']} — est une association basée à Bamako, fondée en {ORG['fondation']}, née de la conviction que le cinéma se transmet aussi hors des écoles.")}

<section class="reveal">
  <div class="container two-col">
    <img src="{IMG['adults_table']}" alt="Réunion de l'équipe JA IMAGE">
    <div>
      <p class="eyebrow">Fondation &amp; mission</p>
      <h2 style="font-size:34px;">Une salle, une caméra, une communauté</h2>
      <p>Créée en {ORG['fondation']}, {ORG['nom_legal']} œuvre pour la promotion du cinéma, de la culture et de la jeunesse au Mali. Elle soutient la formation et la professionnalisation des cinéastes autodidactes à travers des programmes de formation, de production et de diffusion.</p>
      <p>Ce qui nous rassemble : la conviction qu'un regard curieux et une caméra suffisent pour commencer — dans la lignée d'un pays où l'on raconte des histoires depuis bien avant l'invention de la caméra.</p>
      <p class="credit-line">Le Mali a donné au cinéma africain des cinéastes majeurs, comme Souleymane Cissé — et un rendez-vous continental, le FESPACO à Ouagadougou, qui continue d'inspirer notre travail au quotidien.</p>
      <p style="margin-top:22px;font-family:var(--display);font-size:22px;text-transform:none;color:var(--rouge-rideau);">« {ORG['devise']} »</p>
      <p style="font-family:var(--label);letter-spacing:.08em;text-transform:uppercase;font-size:14px;color:var(--gris-fonce);">{ORG['slogan']}</p>
    </div>
  </div>
</section>

<section class="section--dark reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Nos objectifs</p>
      <h2>Trois engagements</h2>
    </div>
    <div class="grid grid--3">
      <div class="card"><span class="num">01</span><h3>Formation</h3><p>Offrir des formations de qualité couvrant tous les aspects de la réalisation cinématographique.</p></div>
      <div class="card"><span class="num">02</span><h3>Promotion</h3><p>Organiser un festival annuel dédié aux cinéastes autodidactes — le Festival Cinéastes Autodidactes.</p></div>
      <div class="card"><span class="num">03</span><h3>Soutien</h3><p>Fournir un appui technique, logistique et financier à la production de films indépendants.</p></div>
    </div>
  </div>
</section>

<section class="reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Sur le terrain</p>
      <h2>Actions concrètes</h2>
    </div>
    <div class="grid grid--4">
      <div class="card"><h3 style="font-size:18px;">Formations intensives</h3><p>Organisées dans plusieurs régions du Mali, pas seulement à Bamako.</p></div>
      <div class="card"><h3 style="font-size:18px;">Banque d'images &amp; répertoire de tournage</h3><p>Deux outils en préparation pour les cinéastes et les productions au Mali.</p></div>
      <div class="card"><h3 style="font-size:18px;">Soutien à la production</h3><p>Accompagnement de films indépendants portés par des autodidactes.</p></div>
      <div class="card"><h3 style="font-size:18px;">Événements culturels</h3><p>Projections publiques et événements ouverts à tous, à Bamako.</p></div>
    </div>
  </div>
</section>

<section class="section--tinted reveal">
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

<section class="reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Sur le terrain</p>
      <h2>Celles et ceux qui font JA IMAGE</h2>
      <p>Une équipe de formateurs, bénévoles et mentors, en action lors de nos ateliers et séances Ciné Court School.</p>
    </div>
    <div class="grid grid--4">
      <div class="member"><div class="photo"><img src="{IMG['portrait_boubou']}" alt="Formateur JA IMAGE en atelier"></div><h3>Formation</h3><p class="role">Encadrement des ateliers</p></div>
      <div class="member"><div class="photo"><img src="{IMG['classroom_camop']}" alt="Prise de vue en atelier"></div><h3>Prise de vue</h3><p class="role">Accompagnement technique</p></div>
      <div class="member"><div class="photo"><img src="{IMG['adults_table']}" alt="Réunion de l'équipe"></div><h3>Coordination</h3><p class="role">Pilotage des programmes</p></div>
      <div class="member"><div class="photo"><img src="{IMG['classroom_flipchart']}" alt="Atelier pédagogique"></div><h3>Pédagogie</h3><p class="role">Suivi des autodidactes</p></div>
    </div>
  </div>
</section>

<section class="cta-band reveal">
  <div class="mesh-bg"><span></span><span></span><span></span></div>
  <div class="container">
    <h2>Envie de nous rejoindre ?</h2>
    <a href="contact.html" class="btn btn--primary" style="margin-top:10px;">Nous contacter</a>
  </div>
</section>
"""
    page("association.html", "Association", f"{ORG['nom_legal']} ({ORG['nom_marque']}) : histoire, mission, objectifs et équipe de l'association, fondée en {ORG['fondation']} à Bamako.", body)

# ============================================================= PROGRAMMES ==

def build_programmes():
    body = f"""
{pagehero("Nos programmes", "NOS <em>PROGRAMMES</em>", "Quatre façons de participer à la vie de JA IMAGE, du simple spectateur au cinéaste en production.")}

<section class="reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Vue d'ensemble</p>
      <h2>Formation, production, écriture, financement</h2>
    </div>
    <div class="grid grid--4">
      <div class="card"><span class="num">01</span><h3>La formation</h3><p>Un programme complet pour développer les compétences techniques et artistiques : scénario, réalisation, montage, son — pour débutants et niveaux avancés.</p><p style="margin-top:14px;"><a href="formation.html" class="btn btn--outline" style="padding:9px 16px;font-size:13px;">Voir la formation</a></p></div>
      <div class="card"><span class="num">02</span><h3>La production</h3><p>Transformer les idées en réalisations cinématographiques de qualité, de la conception à la postproduction, avec les technologies et les talents locaux.</p><p style="margin-top:14px;"><a href="contact.html" class="btn btn--outline" style="padding:9px 16px;font-size:13px;">En discuter</a></p></div>
      <div class="card"><span class="num">03</span><h3>Résidence d'écriture</h3><p>Un espace calme et propice à la création scénaristique, avec mentorat, ateliers, consultations individuelles et rencontres avec des professionnels.</p><p style="margin-top:14px;"><a href="contact.html" class="btn btn--outline" style="padding:9px 16px;font-size:13px;">Candidater</a></p></div>
      <div class="card"><span class="num">04</span><h3>Fonds de création</h3><p>Un soutien financier à l'écriture, à la production et à la postproduction des cinéastes autodidactes — cinéma, documentaire, court métrage, fiction.</p><p style="margin-top:14px;"><a href="contact.html" class="btn btn--outline" style="padding:9px 16px;font-size:13px;">Déposer un dossier</a></p></div>
    </div>
  </div>
</section>

<section class="section--tinted reveal">
  <div class="container">
    <div class="grid grid--3">
      <div>
        <div class="imgcard"><img src="{IMG['hilltop_camera']}" alt="Ciné-clubs"><div class="imgcard__label"><span class="tag">Diffusion</span><h3>Ciné-clubs &amp; projections</h3></div></div>
        <p style="margin-top:14px;color:var(--gris-fonce);">Des séances régulières, en salle ou en plein air, pour découvrir le cinéma africain et international et en discuter ensemble.</p>
      </div>
      <div>
        <div class="imgcard"><img src="{IMG['classroom_banner']}" alt="Résidences et ateliers"><div class="imgcard__label"><span class="tag">Rencontre</span><h3>Résidences &amp; ateliers</h3></div></div>
        <p style="margin-top:14px;color:var(--gris-fonce);">Des temps courts et intensifs pour écrire, tourner ou monter, encadrés par des cinéastes expérimentés.</p>
      </div>
      <div>
        <div class="imgcard"><img src="{IMG['classroom_flipchart']}" alt="Suivi individualisé"><div class="imgcard__label"><span class="tag">Accompagnement</span><h3>Suivi individualisé des autodidactes</h3></div></div>
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

<section class="reveal">
  <div class="container" style="text-align:center;">
    <p class="eyebrow" style="justify-content:center;">Et bientôt</p>
    <h2 style="font-size:28px;">Répertoire de tournage, guide des cinéastes, banque d'images</h2>
    <p style="max-width:56ch;margin:0 auto 24px;color:var(--gris-fonce);">Trois outils en préparation pour toute la communauté du cinéma malien.</p>
    <a href="initiatives.html" class="btn btn--outline">Découvrir nos initiatives</a>
  </div>
</section>

<section class="cta-band reveal">
  <div class="mesh-bg"><span></span><span></span><span></span></div>
  <div class="container">
    <h2>Je m'inscris à un programme</h2>
    <a href="ressources.html" class="btn btn--primary" style="margin-top:10px;">Voir l'espace autodidactes</a>
  </div>
</section>
"""
    page("programmes.html", "Programmes", "Formation, production, résidence d'écriture et fonds de création proposés par JA IMAGE aux cinéastes autodidactes.", body)

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
    <img src="{IMG['camera_mentorship']}" alt="Mentorat caméra">
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
  <div class="container two-col">
    <div>
      <p class="eyebrow">À la clé</p>
      <h2 style="font-size:32px;">Une attestation de fin de formation</h2>
      <p>Chaque module se termine par une remise d'attestation, lors d'une petite cérémonie avec les autres autodidactes de la session. De quoi valoriser le chemin parcouru — et le montrer.</p>
    </div>
    <img src="{IMG['certificate_ceremony']}" alt="Remise d'attestation">
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
  <div class="mesh-bg"><span></span><span></span><span></span></div>
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
      <img src="{IMG['classroom_banner']}" alt="Matériel de tournage" style="border-radius:2px;margin-top:24px;">
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
        (IMG['certificate_ceremony'], "14 juillet 2026", "Remise d'attestations pour nos autodidactes",
         "Une nouvelle session de formation s'est conclue par une cérémonie de remise d'attestations, entre autodidactes et formateurs."),
        (IMG['classroom_camop'], "12 juillet 2026", "Un nouveau ciné-club mensuel à Bamako",
         "JA IMAGE lance une séance récurrente dédiée aux courts-métrages africains, ouverte à tous les publics, avec un temps d'échange après chaque projection."),
        (IMG['classroom_boubou2'], "28 juin 2026", "Cinq courts-métrages africains à voir cette année",
         "Notre sélection de films marquants portés par une nouvelle génération de cinéastes du continent."),
        (IMG['classroom_flipchart'], "15 juin 2026", "Retour sur notre atelier montage de printemps",
         "Douze autodidactes ont terminé leur premier montage encadré en trois semaines, avec restitution publique."),
        (IMG['adults_table'], "2 juin 2026", "JA IMAGE partenaire d'un festival régional",
         "L'association s'associe à un festival de cinéma régional pour présenter les projets de ses autodidactes."),
        (IMG['group_library'], "20 mai 2026", "Trois autodidactes présentent leur premier court-métrage",
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
        (IMG['hilltop_camera'], "Tournages", "Prise de vue en hauteur, Bamako"),
        (IMG['certificate_ceremony'], "Événements", "Remise d'attestations"),
        (IMG['group_library'], "Événements", "Promo Ciné Court School"),
        (IMG['outdoor_filming'], "Tournages", "Tournage en extérieur"),
        (IMG['students_qa'], "Ateliers", "Question de la salle"),
        (IMG['camera_mentorship'], "Ateliers", "Mentorat caméra"),
        (IMG['classroom_camop'], "Ateliers", "Prise en main caméra"),
        (IMG['camera_training'], "Tournages", "En plein exercice pratique"),
        (IMG['classroom_flipchart'], "Ateliers", "Atelier pédagogique"),
        (IMG['camera_artwall'], "Tournages", "Interview en intérieur"),
        (IMG['speaker_mic'], "Événements", "Prise de parole"),
        (IMG['classroom_wide1'], "Ateliers", "Séance de formation"),
        (IMG['classroom_banner'], "Ateliers", "Présentation JA IMAGE"),
        (IMG['adults_table2'], "Événements", "Réunion de l'équipe"),
        (IMG['desks_snacks'], "Ateliers", "Pause pendant la session"),
    ]
    cards = "\n".join(f"""
      <div class="imgcard"><img src="{img}" alt="{title}"><div class="imgcard__label"><span class="tag">{tag}</span><h3>{title}</h3></div></div>""" for img, tag, title in items)

    body = f"""
{pagehero("Salle comble", "GALERIE", "Projections, tournages, ateliers : quelques images de la vie de JA IMAGE.")}

<section class="reveal">
  <div class="container">
    <div class="tag-row">
      <span class="tag">Ateliers</span><span class="tag">Tournages</span><span class="tag">Événements</span>
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
    <img src="{IMG['adults_table']}" alt="Réunion JA IMAGE">
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
      <p style="color:var(--gris-fonce);">Adresse : {ORG['adresse']}<br>
      Téléphone : {ORG['telephone']}<br>
      Email : {FORM_EMAIL}<br>
      Réseaux : Facebook · Instagram</p>
      <p style="margin-top:16px;font-style:italic;color:var(--gris-fonce);">« {ORG['devise']} » — {ORG['slogan']}</p>
      <img src="{IMG['landscape']}" alt="Bamako, Mali" style="border-radius:2px;margin-top:24px;">
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

# ==================================================== FESTIVAL AUTODIDACTES ==

def build_festival():
    body = f"""
{pagehero("Événement annuel", "FESTIVAL CINÉASTES <em>AUTODIDACTES</em>", f"Organisé par {ORG['nom_legal']}, le festival met en lumière les talents émergents du cinéma malien — une vitrine pour les œuvres des cinéastes autodidactes et un espace d'échange avec les professionnels.")}

<section class="reveal">
  <div class="container two-col">
    <img src="{IMG['certificate_ceremony']}" alt="Cérémonie du festival">
    <div>
      <p class="eyebrow">Présentation</p>
      <h2 style="font-size:32px;">La vitrine du cinéma autodidacte malien</h2>
      <p>Le Festival Cinéastes Autodidactes est un événement annuel qui met en lumière les talents émergents du cinéma malien. Il constitue une vitrine pour les œuvres réalisées par des cinéastes autodidactes et un espace d'échange entre professionnels et passionnés.</p>
      <p style="font-family:var(--display);font-size:20px;text-transform:none;color:var(--rouge-rideau);">« {ORG['devise']} »</p>
    </div>
  </div>
</section>

<section class="section--dark reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Objectifs</p>
      <h2>Ce que porte le festival</h2>
    </div>
    <div class="grid grid--3">
      <div class="card"><span class="num">01</span><h3>Valoriser</h3><p>La créativité des cinéastes autodidactes, sur scène et à l'écran.</p></div>
      <div class="card"><span class="num">02</span><h3>Promouvoir</h3><p>La diversité culturelle et artistique du Mali auprès du public et des professionnels.</p></div>
      <div class="card"><span class="num">03</span><h3>Encourager</h3><p>La professionnalisation du secteur cinématographique malien.</p></div>
    </div>
  </div>
</section>

<section class="reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Programmation</p>
      <h2>Au fil du festival</h2>
    </div>
    <div class="grid grid--4">
      <div class="card"><h3 style="font-size:18px;">Projections</h3><p>Courts et longs métrages de cinéastes autodidactes.</p></div>
      <div class="card"><h3 style="font-size:18px;">Masterclass</h3><p>Ateliers de formation animés par des professionnels.</p></div>
      <div class="card"><h3 style="font-size:18px;">Rencontres</h3><p>Panels et échanges entre cinéastes, publics et institutions.</p></div>
      <div class="card"><h3 style="font-size:18px;">Cérémonie</h3><p>Remise des prix devant le public et le jury.</p></div>
    </div>
  </div>
</section>

<section class="section--tinted reveal">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Compétition</p>
      <h2>Les films en compétition</h2>
      <p>Évalués par un jury composé de professionnels du cinéma.</p>
    </div>
    <div class="grid grid--4">
      <div class="card"><span class="num">Prix</span><h3>Meilleure réalisation</h3><p>Récompense la mise en scène d'ensemble du film.</p></div>
      <div class="card"><span class="num">Prix</span><h3>Meilleur scénario</h3><p>Récompense l'écriture et la construction du récit.</p></div>
      <div class="card"><span class="num">Prix</span><h3>Meilleure image</h3><p>Récompense la direction photo et le cadrage.</p></div>
      <div class="card"><span class="num">Prix</span><h3>Prix du public</h3><p>Voté par les spectateurs lors des projections.</p></div>
    </div>
  </div>
</section>

<section class="reveal">
  <div class="container">
    <div class="grid grid--3">
      <div class="imgcard"><img src="{IMG['outdoor_filming']}" alt="Tournage autodidacte"><div class="imgcard__label"><span class="tag">Coulisses</span><h3>Sur le tournage</h3></div></div>
      <div class="imgcard"><img src="{IMG['speaker_mic']}" alt="Rencontre professionnelle"><div class="imgcard__label"><span class="tag">Rencontre</span><h3>Échange avec un cinéaste</h3></div></div>
      <div class="imgcard"><img src="{IMG['group_library']}" alt="Public du festival"><div class="imgcard__label"><span class="tag">Public</span><h3>Salle comble</h3></div></div>
    </div>
  </div>
</section>

<section class="section--dark reveal" id="soumettre">
  <div class="container two-col">
    <div>
      <p class="eyebrow">Participer</p>
      <h2 style="font-size:32px;">Soumettre un film</h2>
      <p>Cinéaste autodidacte malien, vous avez un court ou un long métrage à présenter ? Dites-nous-en plus, nous revenons vers vous avec les modalités et les dates de la prochaine édition.</p>
    </div>
    <form class="form-panel" action="https://formsubmit.co/{FORM_EMAIL}" method="POST">
      <input type="hidden" name="_subject" value="Soumission de film — Festival Cinéastes Autodidactes">
      <input type="text" name="_honey" style="display:none">
      <input type="hidden" name="_captcha" value="false">
      <div class="form-row">
        <div class="field"><label for="f-nom">Nom du réalisateur</label><input id="f-nom" name="Nom" type="text" required></div>
        <div class="field"><label for="f-titre">Titre du film</label><input id="f-titre" name="Titre" type="text" required></div>
      </div>
      <div class="field"><label for="f-email">Email</label><input id="f-email" name="Email" type="email" required></div>
      <div class="field"><label for="f-msg">Présentation du film</label><textarea id="f-msg" name="Message"></textarea></div>
      <button type="submit" class="btn btn--primary" style="width:100%;justify-content:center;">Envoyer ma soumission</button>
    </form>
  </div>
</section>
"""
    page("festival.html", "Festival Cinéastes Autodidactes", f"Le Festival Cinéastes Autodidactes, événement annuel de {ORG['nom_legal']} (JA IMAGE), vitrine du cinéma autodidacte malien à Bamako.", body)

# ======================================================== NOS INITIATIVES ==

def build_initiatives():
    body = f"""
{pagehero("En préparation", "NOS <em>INITIATIVES</em>", "Trois outils que JA IMAGE construit pour toute la communauté du cinéma malien — cinéastes, techniciens, productions.")}

<section class="reveal">
  <div class="container">
    <div class="grid grid--3">
      <div class="card">
        <span class="num">Bientôt</span>
        <h3>Répertoire de cité de tournage</h3>
        <p>Une base de données complète des lieux de tournage au Mali : paysages naturels, urbains et historiques. Recherche par région, type de décor ou mot-clé, avec photos HD et conditions d'accès pour chaque fiche.</p>
        <p style="margin-top:14px;color:var(--gris-fonce);"><em>Vous avez un lieu à proposer ?</em> <a href="contact.html">Contactez-nous</a>.</p>
      </div>
      <div class="card">
        <span class="num">Bientôt</span>
        <h3>Guide des cinéastes du Mali</h3>
        <p>Un répertoire des réalisateurs, scénaristes, acteurs et techniciens du Mali — un espace de visibilité et de mise en réseau qui facilite les partenariats artistiques et techniques.</p>
        <p style="margin-top:14px;color:var(--gris-fonce);"><em>Vous êtes cinéaste ?</em> <a href="contact.html">Soumettez votre profil</a>.</p>
      </div>
      <div class="card">
        <span class="num">Bientôt</span>
        <h3>Banque d'images</h3>
        <p>Une collection d'images authentiques illustrant la culture, les paysages et la vie quotidienne au Mali, produites par des photographes locaux. Une partie des revenus soutient directement les artistes maliens.</p>
        <p style="margin-top:14px;color:var(--gris-fonce);"><em>Photographe malien ?</em> <a href="contact.html">Rejoignez le projet</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section--dark reveal">
  <div class="container two-col">
    <div>
      <p class="eyebrow">Pourquoi ces outils</p>
      <h2 style="font-size:32px;">Une infrastructure pour le cinéma malien</h2>
      <p>Au-delà de la formation et du festival, {ORG['nom_legal']} construit les outils qui manquent au secteur : savoir où tourner, savoir qui appeler, et pouvoir montrer le Mali en images justes.</p>
    </div>
    <img src="{IMG['landscape']}" alt="Paysage malien">
  </div>
</section>

<section class="cta-band reveal">
  <div class="mesh-bg"><span></span><span></span><span></span></div>
  <div class="container">
    <h2>Une idée, un lieu, un profil à proposer ?</h2>
    <a href="contact.html" class="btn btn--primary" style="margin-top:10px;">Nous écrire</a>
  </div>
</section>
"""
    page("initiatives.html", "Nos initiatives", "Répertoire de tournage, guide des cinéastes et banque d'images : les initiatives à venir de JA IMAGE.", body)

# ========================================================== CINÉ COURT SCHOOL ==

def build_concours():
    body = f"""
<section class="pagehero">
  <div class="container" style="display:flex;gap:36px;align-items:flex-end;flex-wrap:wrap;">
    <div class="ccs-badge"><img src="{LOGO_CCS}" alt="Logo Ciné Court School"></div>
    <div style="flex:1;min-width:260px;">
      <p class="eyebrow">Concours annuel</p>
      <h1>CINÉ COURT <em>SCHOOL</em></h1>
      <p>Le concours annuel de courts-métrages de JA IMAGE, ouvert aux élèves maliens qui veulent raconter une histoire à l'image — du collège au lycée.</p>
      <div class="btn-row" style="margin-top:26px;">
        <a href="#inscription" class="btn btn--primary">Inscrire mon établissement</a>
        <a href="#reglement" class="btn btn--outline">Voir le règlement</a>
      </div>
    </div>
  </div>
  <div class="bogolan-band" style="position:absolute;left:0;right:0;bottom:0;"></div>
</section>

<section class="reveal">
  <div class="container two-col">
    <img src="{IMG['group_library']}" alt="Élèves Ciné Court School">
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
      <div class="imgcard"><img src="{IMG['classroom_wide1']}" alt="Édition précédente"><div class="imgcard__label"><span class="tag">Édition 2025</span><h3>Séance de formation</h3></div></div>
      <div class="imgcard"><img src="{IMG['classroom_flipchart']}" alt="Édition précédente"><div class="imgcard__label"><span class="tag">Édition 2025</span><h3>Atelier de préparation</h3></div></div>
      <div class="imgcard"><img src="{IMG['desks_snacks']}" alt="Édition précédente"><div class="imgcard__label"><span class="tag">Édition 2025</span><h3>Entre deux séances</h3></div></div>
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
    build_festival()
    build_programmes()
    build_formation()
    build_ressources()
    build_initiatives()
    build_concours()
    build_actualites()
    build_galerie()
    build_partenaires()
    build_contact()
    print("\nSite généré avec succès.")
