#!/usr/bin/env python3
"""Genera assets/terminal.svg: una terminal animada con anillos en ASCII y órdenes que se escriben solas.
Solo SVG con animación SMIL: GitHub la muestra tal cual, sin scripts. Uso: python3 scripts/terminal.py"""
import math
from html import escape
from pathlib import Path

A = Path(__file__).resolve().parents[1] / "assets"
MONO = 'ui-monospace, "SF Mono", Menlo, Consolas, "DejaVu Sans Mono", monospace'
ANCHO, ALTO = 880, 330
COLS, FILAS, FOTOGRAMAS = 40, 19, 10
TINTA = " .:-=+*#@"


def fotograma(fase):
    cx, cy = (COLS - 1) / 2, (FILAS - 1) / 2
    lineas = []
    for y in range(FILAS):
        fila = ""
        for x in range(COLS):
            d = math.hypot((x - cx) * 0.5, y - cy)
            if d > 9.4:
                fila += " "
                continue
            v = (math.sin(d * 1.55 - fase) + 1) / 2 * (1 - d / 13)
            fila += "@" if d < 0.8 else TINTA[min(len(TINTA) - 1, int(v * len(TINTA)))]
        lineas.append(fila.rstrip())
    return lineas


def ascii_animado(x0, y0):
    paso, dur = 1 / FOTOGRAMAS, 1.8
    grupos = ""
    for k in range(FOTOGRAMAS):
        valores = ";".join("1" if i == k else "0" for i in range(FOTOGRAMAS))
        tiempos = ";".join(f"{i * paso:.3f}" for i in range(FOTOGRAMAS))
        filas = "".join(f'<text x="{x0}" y="{y0 + i * 13}" xml:space="preserve">{escape(l)}</text>' for i, l in enumerate(fotograma(k * 2 * math.pi / FOTOGRAMAS)) if l.strip())
        grupos += (f'<g opacity="{1 if k == 0 else 0}">{filas}'
                   f'<animate attributeName="opacity" values="{valores}" keyTimes="{tiempos}" calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/></g>')
    return f'<g class="ascii">{grupos}</g>'


LINEAS = [  # (texto, clase, cuándo empieza a escribirse, cuánto tarda)
    ("$ whoami", "o", 0.4, 0.7), ("Romén Adama · Technical Project Manager", "r", 1.3, 0.5),
    ("$ ls proyectos/", "o", 2.6, 0.9), ("jarvis-local  erp-esignature-demo  itc-dashboard", "r", 3.7, 0.5),
    ("$ cat metodo.txt", "o", 5.0, 0.9), ("alcance > rama y PR > revisión > despliegue", "r", 6.1, 0.5),
    ("$ agentes --estado", "o", 7.4, 1.0), ("claude  codex  antigravity  jarvis   [ok]", "v", 8.6, 0.5),
]
CICLO = 13.0


def escritura(x0, y0):
    salida = ""
    for i, (texto, clase, ini, dur) in enumerate(LINEAS):
        y = y0 + i * 27
        w = round(len(texto) * 9.05 + 6)
        t0, t1 = ini / CICLO, (ini + dur) / CICLO
        salida += (f'<clipPath id="c{i}"><rect x="{x0 - 2}" y="{y - 17}" height="24" width="0">'
                   f'<animate attributeName="width" values="0;0;{w};{w};0" keyTimes="0;{t0:.4f};{t1:.4f};0.97;1" dur="{CICLO}s" repeatCount="indefinite"/></rect></clipPath>'
                   f'<text x="{x0}" y="{y}" class="{clase}" clip-path="url(#c{i})" xml:space="preserve">{escape(texto)}</text>')
    yc = y0 + len(LINEAS) * 27
    salida += (f'<rect x="{x0}" y="{yc - 15}" width="9" height="18" fill="#a78bfa">'
               '<animate attributeName="opacity" values="1;0" keyTimes="0;0.5" calcMode="discrete" dur="1s" repeatCount="indefinite"/></rect>')
    return salida


svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {ALTO}" width="{ANCHO}" height="{ALTO}" role="img" aria-label="Terminal animada: quién soy, mis proyectos, mi método y los agentes que coordino">
  <style>
    text {{ font: 15px {MONO}; }}
    .ascii text {{ font: 700 11px {MONO}; fill: #8b5cf6; letter-spacing: .6px; }}
    .o {{ fill: #fafafa; font-weight: 600; }} .r {{ fill: #a1a1aa; }} .v {{ fill: #a78bfa; }}
    .tit {{ font: 12.5px {MONO}; fill: #71717a; }}
  </style>
  <rect x=".5" y=".5" width="{ANCHO - 1}" height="{ALTO - 1}" rx="14" fill="#0b0b0d" stroke="#27272a"/>
  <path d="M1 38 H{ANCHO - 1}" stroke="#27272a"/>
  <circle cx="24" cy="20" r="6" fill="#8b5cf6"/><circle cx="44" cy="20" r="6" fill="#3f3f46"/><circle cx="64" cy="20" r="6" fill="#3f3f46"/>
  <text x="{ANCHO / 2}" y="24" class="tit" text-anchor="middle">romen@supernodo: ~</text>
  {ascii_animado(26, 66)}
  {escritura(372, 82)}
</svg>
'''
(A / "terminal.svg").write_text(svg)
print("terminal.svg", len(svg) // 1024, "KB")
