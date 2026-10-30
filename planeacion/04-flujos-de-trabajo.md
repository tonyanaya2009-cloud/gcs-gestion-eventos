# 4. Flujos de trabajo (estilo BPMN)

Cada diagrama tiene carriles por participante (Organizador, Sistema, Asistente o Miembro del equipo). Notación: círculo = inicio, doble círculo = fin, rombo = decisión, rectángulo = actividad.

## 4.1 Creación de un evento

~~~mermaid
flowchart TB
    subgraph L1["Organizador"]
        A((Inicio)) --> B["Abre 'Nuevo evento'"]
        B --> C["Captura nombre, tipo, fechas,<br/>zona horaria, modalidad, cliente y cupo"]
        C --> D{"¿Modalidad?"}
        D -->|Presencial / Híbrido| E["Selecciona sede"]
        D -->|Virtual| F["Captura enlace del webinar"]
        E --> G["Guarda como borrador"]
        F --> G
        J["Revisa el evento"] --> K{"¿Publicar?"}
        K -->|No| L["Sigue editando"] --> J
        K -->|Sí| M["Publica el evento"]
    end
    subgraph L2["Sistema"]
        G --> H{"¿Datos válidos?<br/>fin ≥ inicio, cupo > 0,<br/>sede o enlace"}
        H -->|No| I["Muestra errores"] --> C
        H -->|Sí| H2["Guarda evento en estado Borrador"] --> J
        M --> N["Cambia estado a Publicado"]
        N --> O["Habilita formulario de registro<br/>y lo muestra en el calendario"]
        O --> P["Programa recordatorio 24 h antes"]
        P --> Q(((Fin)))
    end
~~~

## 4.2 Registro y seguimiento de asistentes

~~~mermaid
flowchart TB
    subgraph L1["Asistente"]
        A((Inicio)) --> B["Abre la invitación y el<br/>formulario de registro"]
        B --> C["Captura nombre, correo,<br/>empresa, cargo y país"]
        R1["Recibe correo de confirmación"]
        R2["Recibe correo: en lista de espera"]
        R3["Recibe recordatorio 24 h antes"]
    end
    subgraph L2["Sistema"]
        C --> D{"¿Evento publicado<br/>y correo no registrado?"}
        D -->|No| E["Muestra aviso"] --> X(((Fin)))
        D -->|Sí| F{"¿Hay cupo?"}
        F -->|Sí| G["Crea registro Confirmado"] --> R1
        F -->|No| H["Crea registro En espera"] --> R2
        S1["Si un confirmado cancela,<br/>promueve al primero en espera"]
        T1["Envía recordatorio a confirmados"] --> R3
    end
    subgraph L3["Organizador"]
        R1 --> I["Consulta lista de asistentes<br/>y totales por estado"]
        R2 --> I
        I --> J{"¿Cambios manuales?"}
        J -->|Cancelar registro| S1
        J -->|No| K["Día del evento:<br/>registra check-in"]
        S1 --> K
        K --> T1
        R3 --> L["Revisa asistencia y exporta CSV"]
        L --> Z(((Fin)))
    end
~~~

## 4.3 Asignación y gestión de tareas

~~~mermaid
flowchart TB
    subgraph L1["Organizador"]
        A((Inicio)) --> B["Abre el tablero de tareas<br/>del evento"]
        B --> C["Crea tarea: título, responsable,<br/>prioridad y fecha límite"]
        M["Revisa avance en el panel<br/>del evento"] --> N{"¿Todas las tareas<br/>hechas?"}
        N -->|No| O["Reasigna o ajusta fechas"] --> M
        N -->|Sí| Z(((Fin)))
    end
    subgraph L2["Sistema"]
        C --> D{"¿Campos obligatorios<br/>completos?"}
        D -->|No| E["Muestra errores"] --> C
        D -->|Sí| F["Guarda tarea en Pendiente"]
        F --> G["Notifica al responsable"]
        J["Actualiza tablero y<br/>panel del evento"] --> M
        V["Revisión diaria:<br/>marca tareas vencidas y avisa"] --> J
    end
    subgraph L3["Miembro del equipo"]
        G --> H["Ve la tarea en 'Mis tareas'"]
        H --> I["Mueve a En curso"]
        I --> K["Termina y mueve a Hecha"]
        I -.->|si no avanza| V
        K --> J
    end
~~~
