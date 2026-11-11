#!/usr/bin/env python3
"""Convierte fotogramas en gris (PNG) en un SVG animado de arte ASCII: cada carácter sale del brillo de su píxel.
Uso: python3 scripts/ascii_video.py <carpeta con f01.png…> assets/ascii.svg"""
import sys
from html import escape
from pathlib import Path

from PIL import Image

TINTA = " .,:;i1tfLCG08@"
MONO = 'ui-monospace, "SF Mono", Menlo, Consolas, "DejaVu Sans Mono", monospace'
carpeta, salida = Path(sys.argv[1]), Path(sys.argv[2])
fotos = sorted(carpeta.glob("f*.png"))
n = len(fotos)
cuadros = []
for f in fotos:
    im = Image.open(f).convert("L")
    w, h = im.size
    px = im.load()
    filas = []
    for y in range(h):
        fila = "".join(TINTA[min(len(TINTA) - 1, int(max(0.0, (px[x, y] - 34) / 221) ** 0.75 * len(TINTA)))] for x in range(w))
        filas.append(fila.rstrip())
    cuadros.append(filas)
ANCHO, ALTO, CH, LH = 880, 48 * 9 + 34, 8.9, 9
grupos = ""
for k, filas in enumerate(cuadros):
    valores = ";".join("1" if i == k else "0" for i in range(n))
    tiempos = ";".join(f"{i / n:.4f}" for i in range(n))
    texto = "".join(f'<text x="14" y="{26 + i * LH}" textLength="{round(len(l) * CH, 1)}" lengthAdjust="spacing" xml:space="preserve">{escape(l)}</text>'
                    for i, l in enumerate(filas) if l.strip())
    grupos += (f'<g opacity="{1 if k == 0 else 0}">{texto}<animate attributeName="opacity" values="{valores}" keyTimes="{tiempos}" '
               f'calcMode="discrete" dur="{n / 6:.2f}s" repeatCount="indefinite"/></g>')
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {ALTO}" width="{ANCHO}" height="{ALTO}" role="img" '
       f'aria-label="Animación en arte ASCII: la tapa de un procesador se levanta sobre el chip">'
       f'<style>text{{font:700 9px {MONO};fill:#a78bfa}}</style>'
       f'<rect x=".5" y=".5" width="{ANCHO - 1}" height="{ALTO - 1}" rx="14" fill="#0b0b0d" stroke="#27272a"/>{grupos}</svg>\n')
salida.write_text(svg)
print(n, "fotogramas,", len(svg) // 1024, "KB")
