# 3. Arquitectura de la aplicación

Con autorización del profesor, el proyecto usa **GitHub** en lugar de Siemens Mendix. Para mantener la idea de Mendix de desarrollar rápido y sin servidores propios, la aplicación se plantea como una **aplicación web por capas, sin servidor**, con servicios gratuitos o de bajo costo.

## Vista general

~~~mermaid
flowchart LR
    subgraph U["Usuarios"]
        ORG["Organizador / Miembro<br/>(navegador)"]
        ASI["Asistente<br/>(navegador o correo)"]
    end

    subgraph FE["Capa de presentación · GitHub Pages"]
        UI["Aplicación web (HTML, CSS, JS)<br/>Eventos · Asistentes · Tareas<br/>Calendario · Notificaciones · Usuarios"]
        REG["Formulario público<br/>de registro"]
    end

    subgraph BE["Capa de lógica · Cloudflare Workers (API REST)"]
        AUTH["Autenticación y roles (JWT)"]
        API["Servicios: eventos, registros,<br/>tareas, notificaciones, calendario"]
        CRON["Tareas programadas (Cron)<br/>recordatorios 24 h · tareas vencidas"]
    end

    subgraph DATA["Capa de datos"]
        DB[("Cloudflare D1 (SQL)<br/>tablas del modelo ER")]
    end

    MAIL["Servicio de correo<br/>transaccional"]
    GH["GitHub<br/>repositorio · Projects · Actions (CI/CD)"]

    ORG --> UI
    ASI --> REG
    UI -->|HTTPS + JSON| AUTH
    REG -->|HTTPS + JSON| API
    AUTH --> API
    API --> DB
    CRON --> DB
    API --> MAIL
    CRON --> MAIL
    MAIL -->|confirmaciones, cambios,<br/>recordatorios| ASI
    GH -.->|despliegue automático| FE
    GH -.->|despliegue automático| BE
~~~

## Capas y componentes

| Capa | Componente | Responsabilidad |
|---|---|---|
| Presentación | Aplicación web en GitHub Pages | Pantallas del organizador y del equipo: inicio, eventos, detalle del evento, asistentes, tareas, calendario y notificaciones. |
| Presentación | Formulario público de registro | Página que el asistente abre desde la invitación para registrarse, sin cuenta. |
| Lógica | API REST en Cloudflare Workers | Reglas de negocio: validaciones, control de cupo y lista de espera, cambio de estado de tareas, creación de notificaciones. |
| Lógica | Autenticación (JWT) | Inicio de sesión y permisos por rol (administrador, organizador, miembro). |
| Lógica | Tareas programadas (Cron Triggers) | Enviar recordatorios 24 h antes, marcar tareas vencidas y reintentar envíos fallidos. |
| Datos | Cloudflare D1 (SQL) | Tablas del modelo entidad-relación con llaves foráneas e índices por evento, fecha y correo. |
| Integración | Servicio de correo transaccional | Envío de los correos a asistentes y miembros del equipo. |
| Operación | GitHub Actions | Pruebas y despliegue automático en cada cambio a la rama principal. |

## Módulos (organización del código)

~~~text
/frontend
  /eventos        lista, formulario, detalle y panel del evento
  /asistentes     registro público, lista, check-in, exportación CSV
  /tareas         tablero por evento y "Mis tareas"
  /calendario     vistas mes / semana
  /notificaciones historial y envío de mensajes
  /usuarios       inicio de sesión y administración
/api
  /routes         un archivo por módulo (eventos, registros, tareas, notificaciones, usuarios)
  /services       reglas de negocio (cupo, lista de espera, recordatorios)
  /db             esquema SQL y migraciones
  /jobs           tareas programadas
/tests            pruebas automáticas que corren en GitHub Actions
~~~

## Estructura de la base de datos
Las tablas siguen el [modelo de datos](02-modelo-de-datos.md): usuario, cliente, sede, evento, asistente, registro, tarea, notificacion y destinatario.
- **Índices:** evento(fecha_inicio, region), registro(evento_id, estado), tarea(responsable_id, fecha_limite) y asistente(correo) único.
- **Integridad:** llaves foráneas en todas las relaciones y restricción única registro(evento_id, asistente_id).

## Buenas prácticas y escalabilidad
- **Separación por capas:** la interfaz no accede a la base de datos; todo pasa por la API.
- **Módulos independientes:** cada funcionalidad clave tiene su módulo de interfaz y sus rutas en la API, así se pueden repartir entre el equipo y crecer sin afectar a los demás.
- **Sin servidor:** Workers y D1 escalan automáticamente con la demanda de eventos en distintas regiones.
- **Fechas en UTC:** se guardan en UTC y se muestran en la zona horaria del evento o del usuario.
- **Seguridad:** HTTPS, contraseñas con hash, tokens con expiración y validación de datos en la API.
- **Integración y despliegue continuos:** cada *pull request* corre pruebas en GitHub Actions antes de unirse a la rama principal.

## Herramientas y justificación

| Herramienta | Uso en el proyecto | Por qué se eligió |
|---|---|---|
| **GitHub (repositorio)** | Código, documentación, diagramas y control de versiones | Sustituye a Mendix (autorizado); el equipo trabaja en paralelo con ramas y *pull requests*. |
| **GitHub Projects** | Product Backlog, plan de sprints, tablero y cronograma | Equivale a las herramientas de seguimiento de la plataforma online de Mendix (Epics) y se integra con los issues. |
| **GitHub Issues y Milestones** | Historias de usuario y sprints | Cada historia tiene criterios de aceptación, puntos, responsable y sprint. |
| **GitHub Actions** | Creación del backlog, pruebas y despliegue | Automatiza tareas repetitivas, como el despliegue en un clic que ofrece Mendix. |
| **GitHub Pages** | Prototipo navegable y, en la fase 2, la aplicación web | Hospedaje gratuito, accesible para el profesor y los usuarios. |
| **Prototipo HTML (wireframes)** | Diseño de las pantallas principales | Cumple el papel de Figma o Adobe XD y además se puede navegar con clics. |
| **Mermaid** | ERD, arquitectura, flujos y cronograma | GitHub lo muestra como diagrama y se versiona junto con el código. |
| **Cloudflare Workers y D1** | API y base de datos (fase 2) | Plan gratuito, sin administrar servidores, con SQL y escalado automático. |
