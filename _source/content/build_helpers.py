import re, html

def slug(t):
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).lower()
    rep = {"à": "a", "â": "a", "ä": "a", "é": "e", "è": "e", "ê": "e", "ë": "e", "î": "i", "ï": "i",
           "ô": "o", "ö": "o", "ù": "u", "û": "u", "ü": "u", "ç": "c", "œ": "oe", "’": "-", "'": "-", "₂": "2"}
    for a, b in rep.items():
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]
