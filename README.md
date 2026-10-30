# Gestión de Eventos GCS

Aplicación de gestión de eventos para **Global Consulting Services (GCS)**: creación de eventos, registro y seguimiento de asistentes, asignación de tareas del equipo, notificaciones a los asistentes y calendario de eventos.

Proyecto final de **Metodologías ágiles** · Universidad Tecmilenio · **Equipo 1**
Con autorización del profesor, se usa **GitHub** en lugar de Siemens Mendix.

| Rol Scrum | Integrante |
|---|---|
| Product Owner | Antonio Anaya |
| Scrum Master | Stephanie Ramos Lozano |
| Development Team | David Alfonso Lorenzo · Calixto Isaac Galeana Medrano · Uziel García |

## Fase 1 · Conceptualización y planificación (avance)

| # | Entregable | Dónde está |
|---|---|---|
| 1 | Objetivos y funcionalidades clave | [planeacion/01-objetivos-y-funcionalidades.md](planeacion/01-objetivos-y-funcionalidades.md) |
| 2 | Modelo de datos y diagrama entidad-relación | [planeacion/02-modelo-de-datos.md](planeacion/02-modelo-de-datos.md) |
| 3 | Arquitectura y justificación de herramientas | [planeacion/03-arquitectura.md](planeacion/03-arquitectura.md) |
| 4 | Flujos de trabajo (BPMN): crear evento, asistentes y tareas | [planeacion/04-flujos-de-trabajo.md](planeacion/04-flujos-de-trabajo.md) |
| 5 | Product Backlog con estimación (Planning Poker) | [planeacion/05-product-backlog.md](planeacion/05-product-backlog.md) y [Issues](../../issues) |
| 6 | Plan de sprints | [planeacion/06-plan-de-sprints.md](planeacion/06-plan-de-sprints.md) y [Milestones](../../milestones) |
| 7 | Plan de recursos, dependencias y cronograma | [planeacion/07-plan-de-recursos-y-cronograma.md](planeacion/07-plan-de-recursos-y-cronograma.md) |
| 8 | Wireframes (prototipo navegable) | [Abrir prototipo](https://tonyanaya2009-cloud.github.io/gcs-gestion-eventos/) · código en [docs/index.html](docs/index.html) |
| 9 | Seguimiento del equipo | GitHub Projects: **Gestión de Eventos GCS · Scrum** |

## Resumen del plan

- **21 historias de usuario · 81 puntos · 6 épicas**
- **4 sprints de 1 semana** (2 al 29 de noviembre de 2026), unos 20 puntos por sprint

| Sprint | Objetivo | Puntos |
|---|---|---|
| 1 · Base y eventos | Iniciar sesión, crear y consultar eventos, registro de asistentes | 21 |
| 2 · Asistentes y tareas | Cupo, lista de espera, check-in y tablero de tareas | 21 |
| 3 · Comunicación y notificaciones | Confirmaciones, avisos de cambio, recordatorios y mensajes | 19 |
| 4 · Calendario y seguimiento | Calendario, panel del evento, historial y exportación | 20 |

## Cómo se usa GitHub en el proyecto

- **Issues:** cada historia de usuario, con criterios de aceptación, puntos, prioridad, épica y responsable (etiquetas).
- **Milestones:** cada sprint, con su objetivo, fechas y progreso.
- **Projects:** tablero Scrum (Product Backlog → Sprint Backlog → En curso → En revisión → Terminado), vista del plan por sprint y cronograma.
- **Actions:** el flujo [Crear Product Backlog](.github/workflows/crear-backlog.yml) genera etiquetas, sprints e historias a partir de [backlog.json](.github/backlog.json). En la fase 2 también correrá pruebas y despliegue.
- **Pages:** publica el prototipo navegable y, en la fase 2, la aplicación.
