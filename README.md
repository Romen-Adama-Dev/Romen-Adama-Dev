<p align="center">
  <img src="assets/banner.svg" alt="Romén Adama Caetano Ramírez, Technical Project Manager y orquestador de IA" width="100%" />
</p>

<p align="center">
  <img alt="Technical PM" src="https://img.shields.io/badge/Technical%20PM-8b5cf6?style=for-the-badge" />
  <img alt="AI Orchestration" src="https://img.shields.io/badge/AI%20Orchestration-0d0d0d?style=for-the-badge" />
  <img alt="Local-first" src="https://img.shields.io/badge/Local--first-0d0d0d?style=for-the-badge" />
  <img alt="ES / EN" src="https://img.shields.io/badge/ES%20%2F%20EN-0d0d0d?style=for-the-badge" />
</p>

Ingeniero informático (ULPGC, 2025) y Junior Project Manager de IT. Acabo de entregar el Trabajo Fin de Máster en Gestión de Proyectos: un asistente de IA que funciona entero en un servidor propio.

Trabajo con un ecosistema de agentes de IA (Claude Code, Codex y modelos locales con Ollama) conectados por MCP y por una red privada con Tailscale. Me sirve para entregar antes sin perder el control: yo defino la arquitectura y los criterios de aceptación, reviso cada pull request y hago el despliegue. Cada cambio entra por una rama y una PR revisada.

## En qué trabajo ahora

[jarvis-local](https://github.com/Romen-Adama-Dev/jarvis-local) es un asistente para jefes de proyecto. Responde sobre la documentación propia citando documento y página, y dice que no lo sabe cuando no encuentra evidencia. La inferencia y el RAG corren en local (Ollama, Qdrant, FastAPI, PostgreSQL), y desde Telegram gestiona tareas, hitos y riesgos en OpenProject, convierte una grabación en acta y prepara correos que solo salen si los confirmo. Antes de elegir modelo comparé cuatro en una GPU de 8 GB y descarté el más rápido porque inventaba respuestas que el contexto no tenía. Se levanta con `docker compose up`.

[erp-esignature-connector-demo](https://github.com/Romen-Adama-Dev/erp-esignature-connector-demo) recrea con datos ficticios un patrón de integración que he llevado en empresa: un conector en Python entre un ERP simulado y una plataforma de firma electrónica autoalojada, con procesamiento por lotes, reintentos, envíos que no se duplican y registros sin datos personales. Lleva su WBS, su registro RAID, el plan y las decisiones de diseño.

Un caso de estudio de `supernodo` (en preparación) contará cómo opero un servidor propio como nodo central de agentes: memoria compartida entre ellos, una rama y una PR por tarea, revisión cruzada y aprobación por Telegram para las acciones que no tienen vuelta atrás.

<p>
  <a href="https://github.com/Romen-Adama-Dev/jarvis-local"><img height="130" alt="jarvis-local" src="https://github-readme-stats.vercel.app/api/pin/?username=Romen-Adama-Dev&repo=jarvis-local&bg_color=0d0d0d&title_color=a78bfa&text_color=e4e4e7&icon_color=8b5cf6&border_color=27272a&border_radius=10" /></a>
  <a href="https://github.com/Romen-Adama-Dev/ITC-Dashboard"><img height="130" alt="ITC-Dashboard" src="https://github-readme-stats.vercel.app/api/pin/?username=Romen-Adama-Dev&repo=ITC-Dashboard&bg_color=0d0d0d&title_color=a78bfa&text_color=e4e4e7&icon_color=8b5cf6&border_color=27272a&border_radius=10" /></a>
</p>

Antes, en el Trabajo Fin de Grado, hice [ITC Dashboard](https://github.com/Romen-Adama-Dev/ITC-Dashboard), una librería de componentes Angular para montar cuadros de mando arrastrando y soltando.

## Stack

![Python](https://img.shields.io/badge/Python-0d0d0d?style=flat-square&logo=python&logoColor=a78bfa) ![FastAPI](https://img.shields.io/badge/FastAPI-0d0d0d?style=flat-square&logo=fastapi&logoColor=a78bfa) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0d0d0d?style=flat-square&logo=postgresql&logoColor=a78bfa) ![Redis](https://img.shields.io/badge/Redis-0d0d0d?style=flat-square&logo=redis&logoColor=a78bfa) ![TypeScript](https://img.shields.io/badge/TypeScript-0d0d0d?style=flat-square&logo=typescript&logoColor=a78bfa) ![Angular](https://img.shields.io/badge/Angular-0d0d0d?style=flat-square&logo=angular&logoColor=a78bfa) ![Next.js](https://img.shields.io/badge/Next.js-0d0d0d?style=flat-square&logo=nextdotjs&logoColor=a78bfa)

![Ollama](https://img.shields.io/badge/Ollama-0d0d0d?style=flat-square&logo=ollama&logoColor=a78bfa) ![Qdrant](https://img.shields.io/badge/Qdrant-0d0d0d?style=flat-square&logo=qdrant&logoColor=a78bfa) ![MCP](https://img.shields.io/badge/MCP-0d0d0d?style=flat-square&logo=modelcontextprotocol&logoColor=a78bfa) ![Claude Code](https://img.shields.io/badge/Claude%20Code-0d0d0d?style=flat-square&logo=anthropic&logoColor=a78bfa) ![Codex](https://img.shields.io/badge/Codex-0d0d0d?style=flat-square&logo=openai&logoColor=a78bfa) ![Antigravity](https://img.shields.io/badge/Antigravity-0d0d0d?style=flat-square&logo=google&logoColor=a78bfa)

![Docker Compose](https://img.shields.io/badge/Docker%20Compose-0d0d0d?style=flat-square&logo=docker&logoColor=a78bfa) ![Tailscale](https://img.shields.io/badge/Tailscale-0d0d0d?style=flat-square&logo=tailscale&logoColor=a78bfa) ![Linux y systemd](https://img.shields.io/badge/Linux%20y%20systemd-0d0d0d?style=flat-square&logo=linux&logoColor=a78bfa) ![Prometheus](https://img.shields.io/badge/Prometheus-0d0d0d?style=flat-square&logo=prometheus&logoColor=a78bfa) ![Grafana](https://img.shields.io/badge/Grafana-0d0d0d?style=flat-square&logo=grafana&logoColor=a78bfa) ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-0d0d0d?style=flat-square&logo=githubactions&logoColor=a78bfa)

![OpenProject](https://img.shields.io/badge/OpenProject-0d0d0d?style=flat-square&logo=openproject&logoColor=a78bfa) ![Plane](https://img.shields.io/badge/Plane-0d0d0d?style=flat-square) ![WBS](https://img.shields.io/badge/WBS-0d0d0d?style=flat-square) ![RAID](https://img.shields.io/badge/RAID-0d0d0d?style=flat-square) ![Gantt](https://img.shields.io/badge/Gantt-0d0d0d?style=flat-square) ![ADR](https://img.shields.io/badge/ADR-0d0d0d?style=flat-square) ![Scrum y Kanban](https://img.shields.io/badge/Scrum%20y%20Kanban-0d0d0d?style=flat-square)

Gestión de proyectos: planifico con WBS, registro RAID y Gantt, y dejo las decisiones de arquitectura escritas como ADR. Uso OpenProject y Plane (también Jira y Confluence) con Scrum, Kanban o enfoques híbridos según el proyecto.

## Actividad

<p>
  <img height="170" alt="Estadísticas de GitHub" src="https://github-readme-stats.vercel.app/api?username=Romen-Adama-Dev&show_icons=true&count_private=true&rank_icon=github&ring_color=8b5cf6&bg_color=0d0d0d&title_color=a78bfa&text_color=e4e4e7&icon_color=8b5cf6&border_color=27272a&border_radius=10" />
  <img height="170" alt="Lenguajes más usados" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Romen-Adama-Dev&layout=compact&langs_count=8&bg_color=0d0d0d&title_color=a78bfa&text_color=e4e4e7&icon_color=8b5cf6&border_color=27272a&border_radius=10" />
</p>

## Contacto

LinkedIn: <!-- linkedin -->

Español nativo. Inglés B2, preparando el C1.

---

<details>
<summary>English</summary>

Computer engineer (ULPGC, 2025) and junior IT project manager. My master's thesis in project management is an AI assistant that runs entirely on a self-hosted server.

I work with an ecosystem of AI agents (Claude Code, Codex and local models on Ollama) connected through MCP and a private Tailscale network. It lets me deliver faster while I keep control: I define the architecture and acceptance criteria, review every pull request and handle deployment.

Current work: [jarvis-local](https://github.com/Romen-Adama-Dev/jarvis-local), a local RAG assistant for project managers that cites its sources, abstains without evidence and manages OpenProject from Telegram. Before picking a model I benchmarked four on an 8 GB GPU and dropped the fastest one because it made up answers. Also: [erp-esignature-connector-demo](https://github.com/Romen-Adama-Dev/erp-esignature-connector-demo), an ERP to e-signature connector with fictional data, tests and its project artifacts (WBS, RAID log, plan, ADRs). Coming soon: a case study on running a self-hosted server as the hub for coding agents.

</details>
