#!/usr/bin/env python3
"""Generate two static CVs from content.json. Python standard library only."""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "content.json").read_text(encoding="utf-8"))


def e(value):
    return escape(value, quote=True)


def heading(key, labels):
    return f'<h2 id="{key}-heading">{e(labels[key])}</h2>'


def entry(item, badge=''):
    bullets = "".join(f"<li>{line}</li>" for line in item.get("bullets", []))
    tags = "".join(f"<li>{e(tag)}</li>" for tag in item.get("tags", []))
    links = "".join(f'<a href="{e(link["url"])}">{e(link["label"]) } <span aria-hidden="true">↗</span></a>' for link in item.get("links", []))
    results = "".join(f'<div><strong>{e(result["value"])}</strong><span>{e(result["label"])}</span></div>' for result in item.get("results", []))
    return f'''<article class="entry">
      <div class="entry-heading"><h3>{f'<span class="entry-badge" aria-hidden="true">{badge}</span>' if badge else ''}<span>{e(item['title'])}</span></h3><p class="date">{e(item['date'])}</p></div>
      <p class="entry-subtitle">{e(item['subtitle'])}</p>
      <p class="entry-summary">{item['summary']}</p>
      {f'<div class="project-results">{results}</div>' if results else ''}
      {f'<ul class="entry-bullets">{bullets}</ul>' if bullets else ''}
      {f'<ul class="tags" aria-label="Technologies">{tags}</ul>' if tags else ''}
      {f'<div class="entry-links">{links}</div>' if links else ''}
    </article>'''


def icon(name):
    paths = {
        "mail": '<rect x="2" y="2" width="20" height="20" rx="4"/><rect x="6" y="7" width="12" height="10" rx="1" fill="white"/><path d="m6 8 6 5 6-5" fill="none" stroke="currentColor" stroke-width="1.5"/>',
        "phone": '<rect x="2" y="2" width="20" height="20" rx="4"/><path d="m8 5 3 4-2 2a12 12 0 0 0 4 4l2-2 4 3-1 3C11 20 4 13 5 6z" fill="white"/>',
        "web": '<path d="M12 1a11 11 0 0 0-3.48 21.44c.55.1.75-.24.75-.53v-2.05c-3.06.66-3.71-1.3-3.71-1.3-.5-1.27-1.22-1.61-1.22-1.61-1-.68.08-.67.08-.67 1.1.08 1.68 1.13 1.68 1.13.98 1.68 2.57 1.19 3.2.91.1-.71.39-1.19.7-1.46-2.45-.28-5.03-1.22-5.03-5.44 0-1.2.43-2.18 1.13-2.94-.11-.28-.49-1.4.11-2.91 0 0 .92-.29 3.02 1.13a10.5 10.5 0 0 1 5.5 0c2.1-1.42 3.02-1.13 3.02-1.13.6 1.51.22 2.63.11 2.91.7.76 1.13 1.74 1.13 2.94 0 4.23-2.58 5.16-5.04 5.44.4.34.75 1.01.75 2.04v3.05c0 .29.2.64.76.53A11 11 0 0 0 12 1z"/>',
        "pin": '<path fill-rule="evenodd" d="M12 1a8 8 0 0 0-8 8c0 5.4 8 14 8 14s8-8.6 8-14a8 8 0 0 0-8-8m0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6"/>'
    }
    return f'<svg class="contact-icon" viewBox="0 0 24 24" aria-hidden="true">{paths[name]}</svg>'


def page(lang, content):
    labels = content["sections"]
    badges = {'experience': ['🏢', '🎓'], 'projects': ['🧠', '🛡️', '🎮', '📊', '🛍️'], 'research': ['🔎', '💬', '🧩']}
    assert all(len(content[key]) == len(badges[key]) for key in badges)
    blocks = "".join(f'<section class="section" id="{key}" aria-labelledby="{key}-heading">{heading(key, labels)}{"".join(entry(item, badge) for item, badge in zip(content[key], badges[key]))}</section>' for key in ("experience", "projects", "research"))
    pubs = []
    for item in content["publications"]:
        title = f'<a href="{e(item["url"])}">{e(item["title"])}</a>' if item.get("url") else e(item["title"])
        pubs.append(f'<li class="publication"><h3>{title}</h3><p>{item["authors"]}</p><p class="publication-venue">{e(item["venue"])} <span class="status">{e(item["status"])}</span></p></li>')
    schools = "".join(f'<article class="school"><h3>{e(item["title"])}</h3><p>{e(item["degree"])}</p><p class="date">{e(item["date"])}</p>{"".join(f"<p>{detail}</p>" for detail in item["details"])}</article>' for item in content["education"])
    skills = "".join(f'<div class="skill"><h3>{e(item["title"])}</h3><p>{e(item["text"])}</p></div>' for item in content["skills"])
    interests = "".join(f'<li>{e(item)}</li>' for item in content["interests"])
    nav = "".join(f'<a href="#{key}">{e(labels[key])}</a>' for key in ("experience", "projects", "research", "publications"))
    ko_current = ' aria-current="page"' if lang == "ko" else ''
    en_current = ' aria-current="page"' if lang == "en" else ''
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{e(content['description'])}">
  <meta name="theme-color" content="#477560">
  <title>{e(content['title'])}</title>
  <link rel="alternate" hreflang="ko" href="./index.html">
  <link rel="alternate" hreflang="en" href="./en.html">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%23477560'/%3E%3Ctext x='32' y='44' text-anchor='middle' font-family='Arial' font-size='38' fill='white'%3ES%3C/text%3E%3C/svg%3E">
  <link rel="preload" href="./PretendardVariable.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="./styles.css?v=5">
  <script src="./print.js" defer></script>
</head>
<body id="top">
  <a class="skip-link" href="#main-content">{e(content['skip'])}</a>
  <div class="resume">
    <header class="header">
      <div class="identity">
        <nav class="language-switch" aria-label="Language / 언어">
          <a href="./index.html" lang="ko" hreflang="ko"{ko_current}><span aria-hidden="true">🇰🇷</span> KOR<span class="sr-only"> · 한국어</span></a>
          <a href="./en.html" lang="en" hreflang="en"{en_current}><span aria-hidden="true">🇺🇸</span> ENG<span class="sr-only"> · English</span></a>
        </nav>
        <h1>{e(content['name'])}</h1>
        <p class="alternate-name">{e(content['alternateName'])}</p>
        <p class="role">{e(content['role'])}</p>
      </div>
      <address aria-label="{e(content['contactLabel'])}">
        <a href="mailto:seungminshin00@gmail.com">{icon('mail')}<span>seungminshin00@gmail.com</span></a>
        <a href="tel:+821045220340">{icon('phone')}<span>+82 10 4522 0340</span></a>
        <a href="https://github.com/seummin">{icon('web')}<span>github.com/seummin</span></a>
        <span class="location">{icon('pin')}<span>{e(content['location'])}</span></span>
      </address>
    </header>
    <div class="intro">
      <img class="portrait" src="./portrait.png" alt="{'신승민 프로필 사진' if lang == 'ko' else 'Portrait of Seungmin Shin'}" width="1086" height="1448" fetchpriority="high">
      <p>{content['intro']}</p>
    </div>
    <nav class="section-nav" aria-label="{e(content['navLabel'])}">{nav}</nav>
    <div class="cv-grid">
      <main id="main-content">
        {blocks}
        <section class="section" id="publications" aria-labelledby="publications-heading">
          {heading('publications', labels)}<ol class="publication-list">{''.join(pubs)}</ol>
        </section>
        <section class="section awards" id="awards" aria-labelledby="awards-heading">
          {heading('awards', labels)}
          <h3><a href="https://www.aicrowd.com/challenges/orak-game-agent-challenge-2025">{e(content['awardTitle'])}</a></h3>
          <p class="award-result">{e(content['awardDetail'])}</p>
          <p class="award-note">{e(content['awardNote'])}</p>
        </section>
      </main>
      <aside class="sidebar">
        <section class="section" aria-labelledby="education-heading">{heading('education', labels)}{schools}</section>
        <section class="section" aria-labelledby="skills-heading">{heading('skills', labels)}{skills}</section>
        <section class="section" aria-labelledby="interests-heading">{heading('interests', labels)}<ul class="interest-list">{interests}</ul></section>
      </aside>
    </div>
    <footer><span>{e(content['updated'])}</span><button class="print-button" type="button" hidden><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 8V3h10v5M7 17H4V9h16v8h-3M7 14h10v7H7z"/></svg>{e(content['print'])}</button><a href="#top">{e(content['backToTop'])} ↑</a></footer>
  </div>
</body>
</html>
'''


def plain(text):
    from html import unescape
    return unescape(re.sub(r"<[^>]+>", "", text))


def markdown(content, lang):
    labels = content["sections"]
    lines = [f'# {content["name"]}', '', content["role"], '',
             'seungminshin00@gmail.com · +82 10 4522 0340 · https://github.com/seummin', '', plain(content["intro"]), '']
    for key in ("experience", "projects", "research"):
        lines.extend([f'## {labels[key]}', ''])
        for item in content[key]:
            lines.extend([f'### {item["title"]} | {item["date"]}', '', item["subtitle"], '', plain(item["summary"]), ''])
            lines.extend(f'- {plain(bullet)}' for bullet in item.get("bullets", []))
            if item.get("tags"):
                lines.extend(['', ' / '.join(item['tags'])])
            lines.extend(f'[{link["label"]}]({link["url"]})' for link in item.get('links', []))
            lines.append('')
    lines.extend([f'## {labels["publications"]}', ''])
    for item in content["publications"]:
        title = f'[{item["title"]}]({item["url"]})' if item.get('url') else item['title']
        lines.extend([f'- {title}', f'  {plain(item["authors"])}. {item["venue"]}. {item["status"]}.', ''])
    lines.extend([f'## {labels["awards"]}', '', content['awardTitle'], '', content['awardDetail'], '', content['awardNote'], ''])
    lines.extend([f'## {labels["education"]}', ''])
    for item in content["education"]:
        lines.extend([f'### {item["title"]}', '', f'{item["degree"]} | {item["date"]}', ''])
        lines.extend(f'- {plain(detail)}' for detail in item['details'])
        lines.append('')
    lines.extend([f'## {labels["skills"]}', ''])
    lines.extend(f'- {item["title"]}: {item["text"]}' for item in content['skills'])
    lines.extend(['', f'## {labels["interests"]}', '', ', '.join(content['interests']), ''])
    language_links = '[한국어 웹 이력서](https://seummin.github.io/CV/) · [English CV website](https://seummin.github.io/CV/en.html)\n\n[한국어 텍스트](./README.md) · [English text](./resume-en.md)'
    portrait = f'<img src="./portrait.png" alt="{"신승민 프로필 사진" if lang == "ko" else "Portrait of Seungmin Shin"}" width="108" align="right">'
    return language_links + '\n\n' + portrait + '\n\n' + '\n'.join(lines)


class PageCheck(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.anchors, self.files, self.headings = [], [], [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag in ('h1', 'h2', 'h3'):
            self.headings.append(tag)
        for attr in ('href', 'src'):
            value = attrs.get(attr, '')
            if value.startswith('#'):
                self.anchors.append(value[1:])
            elif value.startswith('./'):
                self.files.append(value[2:].split('?', 1)[0])

    def check(self):
        assert len(self.ids) == len(set(self.ids)), 'Duplicate ID'
        assert self.headings.count('h1') == 1, 'Expected one h1'
        assert self.headings.count('h2') == 8, 'Missing section'
        assert all(anchor in self.ids for anchor in self.anchors), 'Broken anchor'
        assert all((ROOT / filename).is_file() for filename in self.files), 'Broken relative link'


if __name__ == '__main__':
    assert set(DATA) == {'ko', 'en'}
    for key in ('experience', 'projects', 'research', 'publications', 'education', 'skills'):
        assert len(DATA['ko'][key]) == len(DATA['en'][key]), f'Language mismatch: {key}'
    for lang, filename in (('ko', 'index.html'), ('en', 'en.html')):
        (ROOT / filename).write_text(page(lang, DATA[lang]), encoding='utf-8')
        (ROOT / f'resume-{lang}.md').write_text(markdown(DATA[lang], lang), encoding='utf-8')
    (ROOT / 'README.md').write_text(markdown(DATA['ko'], 'ko'), encoding='utf-8')
    for filename in ('index.html', 'en.html'):
        parser = PageCheck()
        parser.feed((ROOT / filename).read_text(encoding='utf-8'))
        parser.check()
        print(f'{filename}: generated; headings, anchors, and local links verified')
