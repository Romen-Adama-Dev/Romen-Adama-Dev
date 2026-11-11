# Romén Adama Caetano Ramírez

Ingeniero informático (ULPGC, 2025) y Junior Project Manager de IT. Acabo de entregar el Trabajo Fin de Máster en Gestión de Proyectos: un asistente de IA que funciona entero en un servidor propio.

Trabajo con un ecosistema de agentes de IA (Claude Code, Codex y modelos locales con Ollama) conectados por MCP y por una red privada con Tailscale. Me sirve para entregar antes sin perder el control: yo defino la arquitectura y los criterios de aceptación, reviso cada pull request y hago el despliegue. Cada cambio entra por una rama y una PR revisada.

## En qué trabajo ahora

[jarvis-local](https://github.com/Romen-Adama-Dev/jarvis-local) es un asistente para jefes de proyecto. Responde sobre la documentación propia citando documento y página, y dice que no lo sabe cuando no encuentra evidencia. La inferencia y el RAG corren en local (Ollama, Qdrant, FastAPI, PostgreSQL), y desde Telegram gestiona tareas, hitos y riesgos en OpenProject, convierte una grabación en acta y prepara correos que solo salen si los confirmo. Antes de elegir modelo comparé cuatro en una GPU de 8 GB y descarté el más rápido porque inventaba respuestas que el contexto no tenía. Se levanta con `docker compose up`.

`erp-esignature-connector-demo` (en preparación) recrea con datos ficticios un patrón de integración que he llevado en empresa: un conector en Python entre un ERP simulado y una plataforma de firma electrónica autoalojada, con procesamiento por lotes, reintentos y tests.

Un caso de estudio de `supernodo` (en preparación) contará cómo opero un servidor propio como nodo central de agentes: memoria compartida entre ellos, una rama y una PR por tarea, revisión cruzada y aprobación por Telegram para las acciones que no tienen vuelta atrás.

Antes, en el Trabajo Fin de Grado, hice [ITC Dashboard](https://github.com/Romen-Adama-Dev/ITC-Dashboard), una librería de componentes Angular para montar cuadros de mando arrastrando y soltando.

## Stack

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![Angular](https://img.shields.io/badge/Angular-DD0031?logo=angular&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?logo=nextdotjs&logoColor=white)

![Ollama](https://img.shields.io/badge/Ollama-LLM%20local-000000?logo=ollama&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-RAG-DC244C?logo=qdrant&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-herramientas%20de%20agentes-555555?logo=modelcontextprotocol&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude%20Code-agentes-D97757?logo=anthropic&logoColor=white)
![Codex](https://img.shields.io/badge/Codex-revisi%C3%B3n%20de%20PR-412991?logo=openai&logoColor=white)

![Docker](https://img.shields.io/badge/Docker%20Compose-2496ED?logo=docker&logoColor=white)
![Tailscale](https://img.shields.io/badge/Tailscale-242424?logo=tailscale&logoColor=white)
![systemd](https://img.shields.io/badge/Linux%20%2B%20systemd-FCC624?logo=linux&logoColor=black)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?logo=grafana&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

Gestión de proyectos: planifico con WBS, registro RAID y Gantt, y dejo las decisiones de arquitectura escritas como ADR. Uso OpenProject y Plane (también Jira y Confluence) con Scrum, Kanban o enfoques híbridos según el proyecto.

## Actividad

<p>
  <img height="165" alt="Estadísticas de GitHub" src="https://github-readme-stats.vercel.app/api?username=Romen-Adama-Dev&show_icons=true&hide_border=true&theme=transparent&count_private=true" />
  <img height="165" alt="Lenguajes más usados" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Romen-Adama-Dev&layout=compact&hide_border=true&theme=transparent" />
</p>

## Contacto

LinkedIn: <!-- linkedin -->

Español nativo. Inglés B2, preparando el C1.

---

<details>
<summary>English</summary>

Computer engineer (ULPGC, 2025) and junior IT project manager. My master's thesis in project management is an AI assistant that runs entirely on a self-hosted server.

I work with an ecosystem of AI agents (Claude Code, Codex and local models on Ollama) connected through MCP and a private Tailscale network. It lets me deliver faster while I keep control: I define the architecture and acceptance criteria, review every pull request and handle deployment.

Current work: [jarvis-local](https://github.com/Romen-Adama-Dev/jarvis-local), a local RAG assistant for project managers that cites its sources, abstains without evidence and manages OpenProject from Telegram. Before picking a model I benchmarked four on an 8 GB GPU and dropped the fastest one because it made up answers. Coming soon: an ERP to e-signature connector demo with fictional data, and a case study on running a self-hosted server as the hub for coding agents.

</details>
