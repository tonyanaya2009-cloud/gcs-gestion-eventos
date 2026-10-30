# 6. Plan de sprints

- **Duración:** 4 sprints de 1 semana, del 2 al 29 de noviembre de 2026. La fase 1 (este avance) fue el Sprint 0 de planeación, del 26 al 31 de octubre.
- **Equipo Scrum (Equipo 1):** Antonio Anaya (Product Owner), Stephanie Ramos Lozano (Scrum Master), David Alfonso Lorenzo, Calixto Isaac Galeana Medrano y Uziel García (Development Team).
- **Capacidad y velocidad:** 3 desarrolladores con unas 10 horas por semana cada uno, más el apoyo de la Scrum Master. La velocidad planeada es de **unos 20 puntos por sprint** y se ajustará con la velocidad real del Sprint 1.
- **Eventos de cada sprint:** Sprint Planning el lunes (1 h), Daily Scrum de lunes a viernes (15 min), y Sprint Review (45 min) y Retrospectiva (30 min) el domingo.
- **Definición de terminado (DoD):** cumple sus criterios de aceptación, el código está revisado en un *pull request*, pasa las pruebas en GitHub Actions, está desplegado y el Product Owner lo aceptó.

## Resumen

| Sprint | Fechas | Objetivo del sprint | Historias | Puntos |
|---|---|---|---|---|
| Sprint 1 – Base y eventos | 02/11 – 08/11 | El organizador puede iniciar sesión, crear, editar y consultar eventos, y un asistente puede registrarse a un evento. | HU-01, HU-02, HU-03, HU-04, HU-05 | 21 |
| Sprint 2 – Asistentes y tareas | 09/11 – 15/11 | El organizador da seguimiento a los asistentes (cupo, lista de espera, check-in) y asigna tareas al equipo en un tablero por evento. | HU-06, HU-07, HU-08, HU-09, HU-10 | 21 |
| Sprint 3 – Comunicación y notificaciones | 16/11 – 22/11 | Los asistentes reciben confirmaciones, avisos de cambios y recordatorios automáticos, y el equipo ve sus tareas pendientes y vencidas. | HU-11, HU-12, HU-13, HU-14, HU-15 | 19 |
| Sprint 4 – Calendario y seguimiento | 23/11 – 29/11 | GCS visualiza sus eventos en un calendario global y mide inscritos, asistencia y avance de tareas por evento. | HU-16, HU-17, HU-18, HU-19, HU-20, HU-21 | 20 |
| **Total** | | | **21** | **81** |

## Sprint 1 – Base y eventos (02 al 08 de noviembre)

**Objetivo:** El organizador puede iniciar sesión, crear, editar y consultar eventos, y un asistente puede registrarse a un evento.

| Historia | Puntos | Prioridad | Responsable |
|---|---|---|---|
| HU-01 · Iniciar sesión con mi rol | 5 | Alta | David |
| HU-02 · Crear un evento | 5 | Alta | Isaac |
| HU-03 · Editar, publicar o cancelar un evento | 3 | Alta | Isaac |
| HU-04 · Consultar la lista de eventos con filtros | 3 | Alta | David |
| HU-05 · Registrarme a un evento | 5 | Alta | Uziel |
| **Total** | **21** | | |

## Sprint 2 – Asistentes y tareas (09 al 15 de noviembre)

**Objetivo:** El organizador da seguimiento a los asistentes (cupo, lista de espera, check-in) y asigna tareas al equipo en un tablero por evento.

| Historia | Puntos | Prioridad | Responsable |
|---|---|---|---|
| HU-06 · Ver y buscar asistentes de un evento | 3 | Alta | Uziel |
| HU-07 · Controlar cupo y lista de espera | 5 | Alta | David |
| HU-08 · Registrar asistencia (check-in) | 3 | Media | Uziel |
| HU-09 · Crear y asignar tareas de un evento | 5 | Alta | David |
| HU-10 · Tablero de tareas por evento | 5 | Alta | Isaac |
| **Total** | **21** | | |

## Sprint 3 – Comunicación y notificaciones (16 al 22 de noviembre)

**Objetivo:** Los asistentes reciben confirmaciones, avisos de cambios y recordatorios automáticos, y el equipo ve sus tareas pendientes y vencidas.

| Historia | Puntos | Prioridad | Responsable |
|---|---|---|---|
| HU-11 · Ver mis tareas pendientes y vencidas | 3 | Media | Isaac |
| HU-12 · Confirmación de registro por correo | 3 | Alta | Uziel |
| HU-13 · Avisar a los asistentes cambios o cancelaciones | 5 | Alta | David |
| HU-14 · Recordatorio automático antes del evento | 5 | Alta | Uziel |
| HU-15 · Enviar un mensaje a todos los asistentes | 3 | Media | Stephanie |
| **Total** | **19** | | |

## Sprint 4 – Calendario y seguimiento (23 al 29 de noviembre)

**Objetivo:** GCS visualiza sus eventos en un calendario global y mide inscritos, asistencia y avance de tareas por evento.

| Historia | Puntos | Prioridad | Responsable |
|---|---|---|---|
| HU-16 · Calendario de eventos | 5 | Alta | Isaac |
| HU-17 · Filtrar el calendario y abrir el detalle | 3 | Media | Isaac |
| HU-18 · Panel de seguimiento del evento | 5 | Media | David |
| HU-19 · Historial de notificaciones | 2 | Baja | Uziel |
| HU-20 · Exportar asistentes a CSV | 2 | Baja | Uziel |
| HU-21 · Administrar usuarios del equipo | 3 | Media | Stephanie |
| **Total** | **20** | | |

## Carga por integrante

| Integrante | Rol | Puntos | Historias |
|---|---|---|---|
| David | Development Team (backend y datos) | 28 | HU-01, HU-04, HU-07, HU-09, HU-13, HU-18 |
| Isaac | Development Team (interfaz) | 24 | HU-02, HU-03, HU-10, HU-11, HU-16, HU-17 |
| Uziel | Development Team (registro, correo y pruebas) | 23 | HU-05, HU-06, HU-08, HU-12, HU-14, HU-19, HU-20 |
| Stephanie | Scrum Master | 6 | HU-15, HU-21 |
| Antonio | Product Owner | — | Prioriza el backlog, redacta criterios de aceptación y acepta las historias |

## Criterios de priorización
1. **Valor y dependencia:** primero lo que habilita todo lo demás (acceso, crear eventos y registrar asistentes).
2. **Riesgo técnico al inicio:** el control de cupo y las tareas van en el Sprint 2, antes de las notificaciones, que dependen de ellos.
3. **Incremento usable en cada sprint:** al cerrar cada sprint, GCS puede usar algo nuevo de principio a fin.
