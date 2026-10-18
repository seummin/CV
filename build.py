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


def entry(item):
    bullets = "".join(f"<li>{line}</li>" for line in item.get("bullets", []))
    tags = "".join(f"<li>{e(tag)}</li>" for tag in item.get("tags", []))
    links = "".join(f'<a href="{e(link["url"])}">{e(link["label"]) }</a>' for link in item.get("links", []))
    results = "".join(f'<div><strong>{e(result["value"])}</strong><span>{e(result["label"])}</span></div>' for result in item.get("results", []))
    return f'''<article class="entry">
      <div class="entry-heading"><h3>{e(item['title'])}</h3><p class="date">{e(item['date'])}</p></div>
      <p class="entry-subtitle">{e(item['subtitle'])}</p>
      <p class="entry-summary">{item['summary']}</p>
      {f'<div class="project-results">{results}</div>' if results else ''}
      {f'<ul class="entry-bullets">{bullets}</ul>' if bullets else ''}
      {f'<ul class="tags" aria-label="Technologies">{tags}</ul>' if tags else ''}
      {f'<div class="entry-links">{links}</div>' if links else ''}
    </article>'''



def page(lang, content):
    labels = content["sections"]
    blocks = "".join(f'<section class="section" id="{key}" aria-labelledby="{key}-heading">{heading(key, labels)}{"".join(entry(item) for item in content[key])}</section>' for key in ("experience", "projects", "research"))
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
  <link rel="stylesheet" href="./styles.css?v=8">
  <script src="./print.js" defer></script>
</head>
<body id="top">
  <a class="skip-link" href="#main-content">{e(content['skip'])}</a>
  <div class="resume">
    <header class="header">
      <div class="identity">
        <nav class="language-switch" aria-label="Language / 언어">
          <a href="./index.html" lang="ko" hreflang="ko"{ko_current}>한국어</a>
          <a href="./en.html" lang="en" hreflang="en"{en_current}>English</a>
        </nav>
        <h1>{e(content['name'])}</h1>
        <p class="alternate-name">{e(content['alternateName'])}</p>
        <p class="role">{e(content['role'])}</p>
      </div>
      <address aria-label="{e(content['contactLabel'])}">
        <a href="mailto:seungminshin00@gmail.com"><span>seungminshin00@gmail.com</span></a>
        <a href="tel:+821045220340"><span>+82 10 4522 0340</span></a>
        <a href="https://github.com/seummin"><span>github.com/seummin</span></a>
        <span class="location"><span>{e(content['location'])}</span></span>
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
    <footer><span>{e(content['updated'])}</span><button class="print-button" type="button" hidden>{e(content['print'])}</button><a href="#top">{e(content['backToTop'])}</a></footer>
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
