#!/usr/bin/env python3
"""Genera las tarjetas SVG del perfil (assets/). Sin servicios externos: se ven siempre.
Uso: python3 scripts/tarjetas.py"""
from html import escape
from pathlib import Path

A = Path(__file__).resolve().parents[1] / "assets"
F = '-apple-system, "Segoe UI", Helvetica, Arial, sans-serif'

PROYECTOS = [
    ("jarvis", "jarvis-local", ["Asistente de IA local para jefes de proyecto.", "Cita sus fuentes y se abstiene sin evidencia."],
     [("53", "PR fusionadas"), ("4", "modelos comparados"), ("9", "perfiles de despliegue")]),
    ("erp", "erp-esignature-connector-demo", ["Integración ERP y firma electrónica, con datos", "ficticios. Lotes, reintentos e idempotencia."],
     [("18", "tests"), ("6", "decisiones (ADR)"), ("WBS", "RAID y plan")]),
    ("itc", "ITC Dashboard", ["Librería de componentes Angular para montar", "cuadros de mando arrastrando y soltando."],
     [("157", "commits propios"), ("WCAG", "accesibilidad"), ("i18n", "internacionalización")]),
    ("supernodo", "supernodo", ["Servidor propio que coordina agentes de IA,", "despliega lo aprobado y avisa por Telegram."],
     [("40", "servicios systemd"), ("234", "tests"), ("4", "agentes coordinados")]),
]


def tarjeta(titulo, lineas, cifras):
    desc = "".join(f'<text x="28" y="{78 + i * 22}" class="d">{escape(l)}</text>' for i, l in enumerate(lineas))
    cif = "".join(f'<text x="{28 + i * 142}" y="158" class="n">{escape(n)}</text><text x="{28 + i * 142}" y="178" class="e">{escape(e)}</text>'
                  for i, (n, e) in enumerate(cifras))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 204" width="460" height="204" role="img" aria-label="{escape(titulo)}">
  <style>.t{{font:700 21px {F};fill:#fafafa}}.d{{font:400 14.5px {F};fill:#a1a1aa}}.n{{font:700 24px {F};fill:#fafafa}}.e{{font:400 12.5px {F};fill:#a78bfa}}</style>
  <rect x=".5" y=".5" width="459" height="203" rx="14" fill="#0d0d0f" stroke="#27272a"/>
  <rect x="28" y="24" width="34" height="4" rx="2" fill="#8b5cf6"/>
  <text x="28" y="54" class="t">{escape(titulo)}</text>
  {desc}
  <line x1="28" y1="124" x2="432" y2="124" stroke="#27272a"/>
  {cif}
</svg>
'''


def flujo():
    pasos = [("Alcance", "criterios y riesgos"), ("Rama y PR", "un agente, una tarea"), ("Revisión cruzada", "otro agente audita"),
             ("Mi revisión", "apruebo o rechazo"), ("Despliegue", "automático y repetible"), ("Medición", "tiempos y aciertos")]
    w, g = 146, 10
    cajas = ""
    for i, (t, s) in enumerate(pasos):
        x = 4 + i * (w + g)
        cajas += (f'<rect x="{x}" y="6" width="{w}" height="92" rx="12" fill="#0d0d0f" stroke="#27272a"/>'
                  f'<circle cx="{x + 24}" cy="30" r="12" fill="#8b5cf6"/><text x="{x + 24}" y="35" class="k">{i + 1}</text>'
                  f'<text x="{x + 14}" y="66" class="t">{escape(t)}</text><text x="{x + 14}" y="84" class="s">{escape(s)}</text>')
        if i < len(pasos) - 1:
            cajas += f'<path d="M{x + w + 1} 52 h{g - 2}" stroke="#8b5cf6" stroke-width="2"/>'
    ancho = 4 + len(pasos) * (w + g)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} 104" width="{ancho}" height="104" role="img" aria-label="Cómo trabajo: alcance, rama y PR, revisión cruzada, mi revisión, despliegue y medición">
  <style>.t{{font:650 14.5px {F};fill:#fafafa}}.s{{font:400 11.5px {F};fill:#a1a1aa}}.k{{font:700 13px {F};fill:#fff;text-anchor:middle}}</style>
  {cajas}
</svg>
'''


for clave, titulo, lineas, cifras in PROYECTOS:
    (A / f"tarjeta-{clave}.svg").write_text(tarjeta(titulo, lineas, cifras))
(A / "flujo.svg").write_text(flujo())
print("tarjetas:", len(PROYECTOS) + 1)
