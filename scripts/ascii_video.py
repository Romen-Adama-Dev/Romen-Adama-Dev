#!/usr/bin/env python3
"""Convierte un vídeo o un GIF en un SVG animado de arte ASCII (cada carácter sale del brillo de su zona).

  python3 scripts/ascii_video.py entrada.mp4 assets/ascii.svg [--cols 120] [--fps 8] [--seg 4] [--desde 0]
                                 [--recorte ancho:alto:x:y] [--color '#a78bfa'] [--contraste 0.75] [--negro 30]

Calcula las filas con la proporción del vídeo para que no salga aplastado. Necesita ffmpeg y Pillow.
"""
import argparse
import subprocess
import tempfile
from html import escape
from pathlib import Path

from PIL import Image

TINTA = " .,:;i1tfLCG08@"
MONO = 'ui-monospace, "SF Mono", Menlo, Consolas, "DejaVu Sans Mono", monospace'
ANCHO, MARGEN = 880, 14

p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
p.add_argument("entrada"), p.add_argument("salida")
p.add_argument("--cols", type=int, default=120), p.add_argument("--fps", type=float, default=8)
p.add_argument("--seg", type=float, default=4), p.add_argument("--desde", type=float, default=0)
p.add_argument("--recorte", help="ancho:alto:x:y en píxeles del vídeo"), p.add_argument("--color", default="#a78bfa")
p.add_argument("--contraste", type=float, default=0.75, help="menos de 1 aclara los tonos medios")
p.add_argument("--negro", type=int, default=30, help="brillo (0-255) por debajo del cual no se dibuja nada")
a = p.parse_args()

if a.recorte:
    w, h = map(int, a.recorte.split(":")[:2])
else:
    w, h = map(int, subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                                             "-of", "csv=p=0:s=x", a.entrada], text=True).strip().split("x")[:2])
ch = (ANCHO - 2 * MARGEN) / a.cols          # ancho de cada letra
fuente = ch / 0.62                          # una letra monoespaciada mide ~0,62 de su tamaño
lh = fuente * 1.12                          # alto de cada fila
filas = max(4, round((ANCHO - 2 * MARGEN) * h / w / lh))
alto = round(filas * lh + 2 * MARGEN)

with tempfile.TemporaryDirectory() as tmp:
    filtro = (f"crop={a.recorte}," if a.recorte else "") + f"fps={a.fps},scale={a.cols}:{filas}:flags=area,format=gray"
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(a.desde), "-t", str(a.seg), "-i", a.entrada, "-vf", filtro, f"{tmp}/f%03d.png"], check=True)
    cuadros = []
    for f in sorted(Path(tmp).glob("f*.png")):
        px = Image.open(f).convert("L").load()
        cuadros.append(["".join(TINTA[min(len(TINTA) - 1, int(max(0.0, (px[x, y] - a.negro) / (255 - a.negro)) ** a.contraste * len(TINTA)))]
                                for x in range(a.cols)).rstrip() for y in range(filas)])
n = len(cuadros)
grupos = ""
for k, lineas in enumerate(cuadros):
    valores = ";".join("1" if i == k else "0" for i in range(n))
    tiempos = ";".join(f"{i / n:.4f}" for i in range(n))
    texto = "".join(f'<text x="{MARGEN}" y="{MARGEN + (i + 0.8) * lh:.1f}" textLength="{len(l) * ch:.1f}" lengthAdjust="spacing" xml:space="preserve">{escape(l)}</text>'
                    for i, l in enumerate(lineas) if l.strip())
    grupos += (f'<g opacity="{1 if k == 0 else 0}">{texto}<animate attributeName="opacity" values="{valores}" keyTimes="{tiempos}" '
               f'calcMode="discrete" dur="{n / a.fps:.2f}s" repeatCount="indefinite"/></g>')
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {alto}" width="{ANCHO}" height="{alto}" role="img" aria-label="Animación en arte ASCII">'
       f'<style>text{{font:700 {fuente:.1f}px {MONO};fill:{a.color}}}</style>'
       f'<rect x=".5" y=".5" width="{ANCHO - 1}" height="{alto - 1}" rx="14" fill="#0b0b0d" stroke="#27272a"/>{grupos}</svg>\n')
Path(a.salida).write_text(svg)
print(f"{n} fotogramas de {a.cols}×{filas} caracteres, {len(svg) // 1024} KB → {a.salida}")
