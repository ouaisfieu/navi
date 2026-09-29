"""Petits composants HTML réutilisés dans le contenu des pages."""
import html as _html


def esc(s):
    return _html.escape(str(s), quote=True)


def L(slug, text):
    """Lien interne ; '@/' est remplacé au build par le chemin relatif."""
    return f'<a href="@/{slug}">{text}</a>'


def kpis(items):
    out = ['<div class="kpis">']
    for value, label in items:
        out.append(f'<div class="kpi"><span class="kpi-v">{value}</span><span class="kpi-l">{label}</span></div>')
    out.append('</div>')
    return "\n".join(out)


def bars(title, rows, unit="", note="", maxv=None):
    """Diagramme en barres horizontales à une seule série (valeurs lisibles en texte)."""
    maxv = maxv or max(abs(r[1]) for r in rows)
    out = [f'<figure class="chart" role="group" aria-label="{esc(title)}">',
           f'<figcaption class="chart-title">{title}</figcaption>',
           '<table class="bars"><thead><tr><th scope="col">Élément</th><th scope="col">Valeur</th></tr></thead><tbody>']
    for r in rows:
        label, v = r[0], r[1]
        disp = r[2] if len(r) > 2 else f"{v}{unit}"
        pct = max(1.5, 100 * abs(v) / maxv)
        out.append(
            f'<tr><th scope="row">{label}</th><td><span class="bar" style="--w:{pct:.1f}%" '
            f'title="{esc(label)} : {esc(disp)}"></span><span class="bar-v">{disp}</span></td></tr>')
    out.append('</tbody></table>')
    if note:
        out.append(f'<p class="chart-note">{note}</p>')
    out.append('</figure>')
    return "\n".join(out)


def table(headers, rows, caption=""):
    out = ['<div class="table-wrap"><table class="data">']
    if caption:
        out.append(f'<caption>{caption}</caption>')
    out.append('<thead><tr>' + ''.join(f'<th scope="col">{h}</th>' for h in headers) + '</tr></thead><tbody>')
    for row in rows:
        cells = ''.join((f'<th scope="row">{c}</th>' if i == 0 else f'<td>{c}</td>') for i, c in enumerate(row))
        out.append(f'<tr>{cells}</tr>')
    out.append('</tbody></table></div>')
    return "\n".join(out)


def callout(text, kind="info", title=""):
    t = f'<p class="callout-t">{title}</p>' if title else ""
    return f'<aside class="callout callout-{kind}">{t}{text}</aside>'


def levels(macro, meso, micro):
    """Encadré de lecture multi-échelle."""
    return (
        '<div class="scales">'
        f'<div class="scale scale-macro"><span class="badge badge-macro">Macro</span><p>{macro}</p></div>'
        f'<div class="scale scale-meso"><span class="badge badge-meso">Méso</span><p>{meso}</p></div>'
        f'<div class="scale scale-micro"><span class="badge badge-micro">Micro</span><p>{micro}</p></div>'
        '</div>')


def video(vid, title, desc=""):
    return (
        f'<figure class="video">'
        f'<div class="yt" data-id="{vid}" data-title="{esc(title)}">'
        f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="Miniature de la vidéo : {esc(title)}" loading="lazy" width="480" height="360">'
        f'<button class="yt-play" type="button" aria-label="Lire la vidéo : {esc(title)}"><svg viewBox="0 0 68 48" aria-hidden="true"><path d="M66.5 7.7a8.5 8.5 0 0 0-6-6C55.3.3 34 .3 34 .3s-21.3 0-26.5 1.4a8.5 8.5 0 0 0-6 6C.1 12.9.1 24 .1 24s0 11.1 1.4 16.3a8.5 8.5 0 0 0 6 6C12.7 47.7 34 47.7 34 47.7s21.3 0 26.5-1.4a8.5 8.5 0 0 0 6-6c1.4-5.2 1.4-16.3 1.4-16.3s0-11.1-1.4-16.3z" class="yt-bg"/><path d="M45 24 27 14v20z" fill="#fff"/></svg></button>'
        f'<noscript><a href="https://www.youtube.com/watch?v={vid}">Voir la vidéo sur YouTube</a></noscript>'
        f'</div>'
        f'<figcaption>{desc} <a href="https://www.youtube.com/watch?v={vid}" rel="noopener">Ouvrir sur YouTube</a>.</figcaption>'
        f'</figure>')
