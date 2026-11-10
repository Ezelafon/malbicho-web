"""Construye la página estática para Cloudflare Pages; no requiere dependencias."""
from pathlib import Path
from urllib.parse import urlsplit
import base64
import os
import shutil

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "public"
OUTPUT = ROOT / "dist"
origin = (os.environ.get("SITE_URL") or os.environ.get("CF_PAGES_URL") or "https://malbicho.ar").strip().rstrip("/")
url = urlsplit(origin)
if url.scheme not in ("http", "https") or not url.netloc or url.path or url.query or url.fragment:
    raise ValueError("SITE_URL debe ser solo el origen, por ejemplo https://malbicho.ar")

if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
OUTPUT.mkdir()
for source in sorted(SOURCE.rglob("*")):
    if not source.is_file():
        continue
    relative = source.relative_to(SOURCE)
    if source.suffix == ".b64":
        target = OUTPUT / relative.with_suffix("")
        data = base64.b64decode(b"".join(source.read_bytes().split()), validate=True)
    elif source.suffix == ".html":
        target = OUTPUT / relative
        data = source.read_text(encoding="utf-8").replace("__SITE_ORIGIN__", origin).encode("utf-8")
    else:
        target = OUTPUT / relative
        data = source.read_bytes()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)

# Sirve la landing tanto al abrir el dominio como en /redes/.
(OUTPUT / "redes").mkdir()
shutil.copyfile(OUTPUT / "index.html", OUTPUT / "redes/index.html")
print(f"Sitio listo en dist/ · URL canónica: {origin}/redes/")
