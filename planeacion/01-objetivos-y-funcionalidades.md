# 1. Objetivos y funcionalidades clave

## Problema
Global Consulting Services (GCS) organiza conferencias, capacitaciones, webinars y reuniones ejecutivas para sus clientes en distintas regiones del mundo. Hoy lo hace con hojas de cálculo y correos, lo que provoca errores de planificación, registros duplicados o perdidos, tareas sin responsable claro y asistentes que no se enteran de los cambios.

## Objetivo general
Diseñar, desarrollar y desplegar con Scrum una aplicación web de gestión de eventos que centralice la creación de eventos, el registro de asistentes, la asignación de tareas y la comunicación con los participantes, para reducir errores y tiempos de organización en GCS.

## Objetivos específicos
| # | Objetivo | Indicador de éxito |
|---|---|---|
| O1 | Centralizar la creación y gestión de eventos en una sola aplicación. | 100% de los eventos se crean en la app; ninguno en hojas de cálculo. |
| O2 | Automatizar el registro y seguimiento de asistentes, con control de cupo y lista de espera. | Cero registros duplicados y cero eventos con sobrecupo. |
| O3 | Asignar y dar seguimiento a las tareas del equipo organizador por evento. | Toda tarea tiene responsable y fecha límite; las vencidas se ven en el tablero. |
| O4 | Comunicar automáticamente a los asistentes confirmaciones, cambios y recordatorios. | Confirmación en menos de 1 minuto; recordatorio 24 h antes en el 100% de los eventos publicados. |
| O5 | Visualizar en un calendario todos los eventos programados en las distintas regiones. | Calendario mensual y semanal con filtros por región y tipo. |
| O6 | Entregar la aplicación en 4 sprints de 1 semana usando Scrum. | 81 puntos de historia completados al 29 de noviembre de 2026. |

## Funcionalidades clave
| Funcionalidad | Qué incluye | Épica | Historias |
|---|---|---|---|
| **Creación y gestión de eventos** | Crear, editar, publicar y cancelar eventos; tipo, modalidad, sede o enlace, cliente, cupo y zona horaria; lista con filtros; panel de seguimiento. | E1 | HU-02, 03, 04, 18 |
| **Registro y seguimiento de asistentes** | Formulario de registro, control de cupo y lista de espera, búsqueda de asistentes, check-in y exportación a CSV. | E2 | HU-05, 06, 07, 08, 20 |
| **Asignación y seguimiento de tareas** | Tareas por evento con responsable, prioridad y fecha límite; tablero Pendiente / En curso / Hecha; vista "Mis tareas". | E3 | HU-09, 10, 11 |
| **Comunicación y notificaciones** | Confirmación de registro, aviso de cambios y cancelaciones, recordatorio 24 h antes, mensajes masivos e historial de envíos. | E4 | HU-12, 13, 14, 15, 19 |
| **Calendario de eventos** | Vistas mes y semana, colores por tipo, filtros por región y tipo, acceso al detalle. | E5 | HU-16, 17 |
| **Acceso y administración** | Inicio de sesión por rol y administración de usuarios. | E6 | HU-01, 21 |

## Usuarios de la aplicación
- **Administrador:** gestiona usuarios y tiene acceso total.
- **Organizador:** crea eventos, gestiona asistentes, asigna tareas y envía comunicaciones.
- **Miembro del equipo:** consulta y actualiza sus tareas.
- **Asistente (externo):** se registra a eventos y recibe notificaciones; no necesita cuenta.

## Requisitos no funcionales
- **Usabilidad:** interfaz en español, navegación con menú lateral fijo y máximo 3 clics para llegar a cualquier pantalla.
- **Seguridad:** acceso por rol, contraseñas cifradas, conexión HTTPS y datos de asistentes visibles solo para el equipo.
- **Rendimiento:** listas y calendario cargan en menos de 2 segundos con hasta 1,000 eventos.
- **Internacionalización:** fechas guardadas en UTC y mostradas en la zona horaria del evento o del usuario.
- **Escalabilidad y mantenimiento:** módulos independientes y despliegue automático con GitHub Actions.
