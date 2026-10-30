# 7. Plan de recursos y cronograma

## 7.1 Recursos

**Personal (Equipo 1)**
| Integrante | Rol | Dedicación | Responsabilidad principal |
|---|---|---|---|
| Antonio Anaya | Product Owner | 6 h/semana | Visión del producto, prioridad del backlog, criterios de aceptación y aceptación de historias. |
| Stephanie Ramos Lozano | Scrum Master | 8 h/semana | Facilita los eventos Scrum, elimina impedimentos, mantiene el tablero y apoya con historias de administración y comunicación. |
| David Alfonso Lorenzo | Desarrollador backend y datos | 10 h/semana | Base de datos, API, autenticación, reglas de cupo, tareas y notificaciones. |
| Calixto Isaac Galeana Medrano | Desarrollador de interfaz | 10 h/semana | Pantallas de eventos, tablero de tareas y calendario. |
| Uziel García | Desarrollador y QA | 10 h/semana | Registro de asistentes, correos, pruebas y exportaciones. |

**Herramientas**
| Herramienta | Uso | Costo |
|---|---|---|
| GitHub (repositorio, Issues, Projects, Actions, Pages) | Código, backlog, sprints, seguimiento, CI/CD y hospedaje de la interfaz | Gratis |
| Cloudflare Workers + D1 | API y base de datos | Gratis (plan Free) |
| Servicio de correo transaccional | Envío de notificaciones | Gratis hasta el límite mensual |
| Visual Studio Code | Desarrollo | Gratis |
| Microsoft Teams / WhatsApp | Daily Scrum y comunicación del equipo | Gratis |

**Tiempo:** 1 semana de planeación más 4 sprints de 1 semana, unas 44 horas-persona por sprint.

## 7.2 Tareas y dependencias

| ID | Tarea | Responsable | Duración | Depende de |
|---|---|---|---|---|
| T1 | Objetivos y funcionalidades | Antonio | 1 día | — |
| T2 | Modelo de datos y ERD | David | 1 día | T1 |
| T3 | Product Backlog y estimación (Planning Poker) | Equipo | 1 día | T1 |
| T4 | Arquitectura | David | 1 día | T2 |
| T5 | Flujos de trabajo (BPMN) | Stephanie | 1 día | T1 |
| T6 | Wireframes y prototipo navegable | Isaac | 2 días | T1, T5 |
| T7 | Plan de sprints, recursos y cronograma | Stephanie | 1 día | T3 |
| T8 | Configurar repositorio, GitHub Projects y Actions | Antonio | 1 día | T3 |
| S1 | Sprint 1: acceso, eventos y registro (21 pts) | Equipo | 1 semana | T2, T4, T6, T8 |
| S2 | Sprint 2: asistentes y tareas (21 pts) | Equipo | 1 semana | S1 (eventos y registro) |
| S3 | Sprint 3: notificaciones (19 pts) | Equipo | 1 semana | S2 (cupo, lista de espera y tareas) |
| S4 | Sprint 4: calendario y seguimiento (20 pts) | Equipo | 1 semana | S1 (eventos), S2 (tareas) |
| P1 | Pruebas finales y despliegue | Uziel | 2 días | S4 |
| P2 | Entrega final | Antonio | 1 día | P1 |

**Dependencias críticas:** no se pueden registrar asistentes (HU-05) sin eventos publicados (HU-02 y HU-03); las notificaciones de cambios y recordatorios (HU-13 y HU-14) necesitan el registro y el control de cupo (HU-05 y HU-07); el panel del evento (HU-18) necesita registros y tareas (HU-07 y HU-09).

## 7.3 Cronograma

~~~mermaid
gantt
    title Gestión de Eventos GCS · Cronograma
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    todayMarker off

    section Fase 1 · Planeación (Sprint 0)
    Objetivos y funcionalidades          :done, t1, 2026-10-26, 1d
    Modelo de datos y ERD                :done, t2, after t1, 1d
    Product Backlog y estimación         :done, t3, after t1, 1d
    Arquitectura                         :done, t4, after t2, 1d
    Flujos de trabajo BPMN               :done, t5, after t1, 1d
    Wireframes y prototipo               :done, t6, after t5, 2d
    Plan de sprints y cronograma         :done, t7, after t3, 1d
    Repositorio y GitHub Projects        :done, t8, 2026-10-30, 1d
    Entrega del avance                   :milestone, m0, 2026-10-31, 0d

    section Fase 2 · Desarrollo
    Sprint 1 · Base y eventos (21 pts)           :s1, 2026-11-02, 7d
    Sprint 2 · Asistentes y tareas (21 pts)      :s2, after s1, 7d
    Sprint 3 · Notificaciones (19 pts)           :s3, after s2, 7d
    Sprint 4 · Calendario y seguimiento (20 pts) :s4, after s3, 7d

    section Cierre
    Pruebas finales y despliegue         :p1, 2026-11-30, 2d
    Entrega final                        :milestone, m1, 2026-12-02, 0d
~~~

## 7.4 Progreso esperado (burn-up)

| Fin de | Puntos acumulados | % del backlog |
|---|---|---|
| Sprint 1 (8 nov) | 21 | 26% |
| Sprint 2 (15 nov) | 42 | 52% |
| Sprint 3 (22 nov) | 61 | 75% |
| Sprint 4 (29 nov) | 81 | 100% |

El avance se sigue en **GitHub Projects**: el progreso de cada milestone (sprint) muestra las historias cerradas, y la vista de cronograma muestra los sprints en el tiempo. Si al cierre de un sprint la velocidad real es menor a la planeada, el Product Owner mueve las historias de prioridad baja (HU-19 y HU-20) al siguiente sprint.
