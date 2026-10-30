# 2. Modelo de datos

El modelo soporta las cinco funcionalidades clave: eventos, asistentes, tareas, notificaciones y calendario. El calendario no necesita una entidad propia: es una vista de EVENTO por fecha, tipo y región.

## Diagrama entidad-relación (ERD)

~~~mermaid
erDiagram
    CLIENTE ||--o{ EVENTO : "contrata"
    SEDE |o--o{ EVENTO : "aloja"
    USUARIO ||--o{ EVENTO : "organiza"
    EVENTO ||--o{ REGISTRO : "recibe"
    ASISTENTE ||--o{ REGISTRO : "realiza"
    EVENTO ||--o{ TAREA : "requiere"
    USUARIO ||--o{ TAREA : "es responsable de"
    EVENTO ||--o{ NOTIFICACION : "genera"
    NOTIFICACION ||--|{ DESTINATARIO : "se envía a"
    ASISTENTE |o--o{ DESTINATARIO : "recibe"
    USUARIO |o--o{ DESTINATARIO : "recibe"

    USUARIO {
        int id PK
        string nombre
        string correo UK
        string rol "Administrador | Organizador | Miembro"
        string region
        bool activo
    }
    CLIENTE {
        int id PK
        string empresa
        string contacto
        string correo
        string pais
    }
    SEDE {
        int id PK
        string nombre
        string direccion
        string ciudad
        string pais
        string region
        int capacidad
    }
    EVENTO {
        int id PK
        string nombre
        string tipo "Conferencia | Capacitación | Webinar | Reunión ejecutiva"
        string descripcion
        datetime fecha_inicio
        datetime fecha_fin
        string zona_horaria
        string modalidad "Presencial | Virtual | Híbrido"
        string enlace_virtual
        int cupo_maximo
        bool solo_invitacion
        string estado "Borrador | Publicado | Cancelado | Finalizado"
        int cliente_id FK
        int sede_id FK
        int organizador_id FK
    }
    ASISTENTE {
        int id PK
        string nombre
        string apellidos
        string correo UK
        string empresa
        string cargo
        string telefono
        string pais
    }
    REGISTRO {
        int id PK
        int evento_id FK
        int asistente_id FK
        datetime fecha_registro
        string estado "Confirmado | En espera | Cancelado"
        int posicion_espera
        bool asistio
        datetime fecha_checkin
    }
    TAREA {
        int id PK
        int evento_id FK
        int responsable_id FK
        string titulo
        string descripcion
        string prioridad "Alta | Media | Baja"
        string estado "Pendiente | En curso | Hecha"
        date fecha_limite
    }
    NOTIFICACION {
        int id PK
        int evento_id FK
        string tipo "Confirmación | Cambio | Recordatorio | Cancelación | Mensaje | Tarea"
        string asunto
        string mensaje
        string canal "Correo | App"
        datetime fecha_programada
        datetime fecha_envio
        string estado "Programada | Enviada | Fallida"
    }
    DESTINATARIO {
        int id PK
        int notificacion_id FK
        int asistente_id FK "nulo si es usuario"
        int usuario_id FK "nulo si es asistente"
        string estado_entrega "Pendiente | Entregado | Rebotado"
        datetime fecha_lectura
    }
~~~

## Entidades y relaciones

| Entidad | Para qué sirve | Relaciones clave |
|---|---|---|
| **USUARIO** | Miembros de GCS que usan la aplicación (administradores, organizadores y miembros del equipo). | Organiza eventos (1:N), es responsable de tareas (1:N) y recibe avisos de tareas (1:N con DESTINATARIO). |
| **CLIENTE** | Empresa para la que GCS organiza el evento. | Un cliente contrata muchos eventos (1:N). |
| **SEDE** | Lugar físico del evento. Los webinars no tienen sede y usan enlace_virtual. | Una sede aloja muchos eventos; un evento tiene 0 o 1 sede. |
| **EVENTO** | Entidad central: conferencias, capacitaciones, webinars y reuniones ejecutivas en distintas regiones. | Recibe registros, requiere tareas y genera notificaciones (todas 1:N). |
| **ASISTENTE** | Persona externa que participa en uno o más eventos. | Relación N:M con EVENTO a través de REGISTRO. |
| **REGISTRO** | Entidad intermedia Evento–Asistente. Guarda el estado (confirmado o en espera), la posición en la lista de espera y el check-in. | Pertenece a un evento y a un asistente; el par (evento, asistente) es único. |
| **TAREA** | Trabajo interno del equipo para preparar un evento. | Pertenece a un evento y tiene un responsable (USUARIO). |
| **NOTIFICACION** | Mensaje enviado o programado: confirmación, cambio, recordatorio, cancelación, mensaje masivo o aviso de tarea. | Pertenece a un evento y se envía a muchos destinatarios. |
| **DESTINATARIO** | Entidad intermedia Notificación–Persona. Guarda el estado de entrega de cada envío. | Apunta a un ASISTENTE o a un USUARIO (uno de los dos). |

### Reglas del modelo
- **Cupo:** si los REGISTROS confirmados alcanzan cupo_maximo, los nuevos registros quedan En espera con su posicion_espera.
- **Unicidad:** un asistente no puede registrarse dos veces al mismo evento (evento_id + asistente_id únicos).
- **Fechas:** fecha_fin ≥ fecha_inicio, y las fechas se guardan en UTC con la zona_horaria del evento para mostrarlas correctamente en cada región.
- **Borrado lógico:** los eventos cancelados y los usuarios desactivados no se borran, para conservar el historial.
