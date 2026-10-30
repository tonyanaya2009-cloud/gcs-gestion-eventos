# 5. Product Backlog

Historias de usuario en el formato *Como [rol], quiero [acción], para [beneficio]*, ordenadas por prioridad. Cada una existe como **issue** en el repositorio, con sus criterios de aceptación como lista de verificación.

## Técnica de estimación
Se usó **Planning Poker** con la serie de Fibonacci (1, 2, 3, 5, 8). Cada integrante vota en secreto y, si hay diferencia, quienes votaron más alto y más bajo explican su razonamiento antes de volver a votar. Como referencia, **HU-04 (lista de eventos con filtros) = 3 puntos**.

| Puntos | Significado |
|---|---|
| 1–2 | Cambio pequeño, sin lógica nueva |
| 3 | Una pantalla o regla sencilla |
| 5 | Pantalla con lógica de negocio o integración (correo, cupo) |
| 8 | Funcionalidad grande: se divide antes de entrar a un sprint |

## Épicas

| Épica | Nombre | Historias | Puntos |
|---|---|---|---|
| E1 | Gestión de eventos | HU-02, HU-03, HU-04, HU-18 | 16 |
| E2 | Registro y seguimiento de asistentes | HU-05, HU-06, HU-07, HU-08, HU-20 | 18 |
| E3 | Asignación y seguimiento de tareas | HU-09, HU-10, HU-11 | 13 |
| E4 | Comunicación y notificaciones | HU-12, HU-13, HU-14, HU-15, HU-19 | 18 |
| E5 | Calendario de eventos | HU-16, HU-17 | 8 |
| E6 | Acceso y administración | HU-01, HU-21 | 8 |
| | **Total** | **21 historias** | **81** |

## Historias de usuario

| ID | Historia de usuario | Épica | Prioridad | Puntos | Sprint | Responsable |
|---|---|---|---|---|---|---|
| HU-01 | **Iniciar sesión con mi rol.** Como miembro del equipo de GCS, quiero iniciar sesión con mi correo y contraseña, para acceder solo a las funciones que corresponden a mi rol (administrador, organizador o miembro). | E6 | Alta | 5 | 1 | David |
| HU-02 | **Crear un evento.** Como organizador, quiero crear un evento con su tipo, fechas, zona horaria, modalidad, sede o enlace virtual, cliente y cupo, para dejar de planificarlo en hojas de cálculo. | E1 | Alta | 5 | 1 | Isaac |
| HU-03 | **Editar, publicar o cancelar un evento.** Como organizador, quiero editar, publicar o cancelar un evento, para mantener la información actualizada. | E1 | Alta | 3 | 1 | Isaac |
| HU-04 | **Consultar la lista de eventos con filtros.** Como organizador, quiero ver todos los eventos y filtrarlos por tipo, región, estado y fecha, para encontrar rápido el que necesito. | E1 | Alta | 3 | 1 | David |
| HU-05 | **Registrarme a un evento.** Como asistente, quiero registrarme a un evento con un formulario sencillo, para asegurar mi lugar sin enviar correos. | E2 | Alta | 5 | 1 | Uziel |
| HU-06 | **Ver y buscar asistentes de un evento.** Como organizador, quiero ver la lista de asistentes de un evento y buscarlos por nombre, empresa o estado, para dar seguimiento a cada participante. | E2 | Alta | 3 | 2 | Uziel |
| HU-07 | **Controlar cupo y lista de espera.** Como organizador, quiero que el sistema controle el cupo y mande a lista de espera a quien se registre cuando el evento esté lleno, para no sobrevender lugares. | E2 | Alta | 5 | 2 | David |
| HU-08 | **Registrar asistencia (check-in).** Como organizador, quiero marcar la asistencia de cada participante el día del evento, para saber quién asistió realmente. | E2 | Media | 3 | 2 | Uziel |
| HU-09 | **Crear y asignar tareas de un evento.** Como organizador, quiero crear tareas ligadas a un evento y asignarlas a un miembro del equipo con prioridad y fecha límite, para repartir el trabajo sin usar correos. | E3 | Alta | 5 | 2 | David |
| HU-10 | **Tablero de tareas por evento.** Como miembro del equipo, quiero ver las tareas de un evento en un tablero (Pendiente, En curso, Hecha) y cambiar su estado, para que todos vean el avance. | E3 | Alta | 5 | 2 | Isaac |
| HU-11 | **Ver mis tareas pendientes y vencidas.** Como miembro del equipo, quiero ver en una sola pantalla mis tareas de todos los eventos, ordenadas por fecha límite, para organizar mi día. | E3 | Media | 3 | 3 | Isaac |
| HU-12 | **Confirmación de registro por correo.** Como asistente, quiero recibir un correo que confirme mi registro con los datos del evento, para tener la información a la mano. | E4 | Alta | 3 | 3 | Uziel |
| HU-13 | **Avisar a los asistentes cambios o cancelaciones.** Como organizador, quiero que los asistentes reciban un aviso automático cuando cambie la fecha, la sede o el enlace, o cuando se cancele el evento, para que nadie se quede sin enterarse. | E4 | Alta | 5 | 3 | David |
| HU-14 | **Recordatorio automático antes del evento.** Como asistente, quiero recibir un recordatorio 24 horas antes del evento, para no olvidarlo. | E4 | Alta | 5 | 3 | Uziel |
| HU-15 | **Enviar un mensaje a todos los asistentes.** Como organizador, quiero enviar un mensaje a todos los asistentes de un evento, para compartir materiales o indicaciones. | E4 | Media | 3 | 3 | Stephanie |
| HU-16 | **Calendario de eventos.** Como organizador, quiero ver los eventos programados en un calendario mensual y semanal, para detectar empalmes y planificar el año. | E5 | Alta | 5 | 4 | Isaac |
| HU-17 | **Filtrar el calendario y abrir el detalle.** Como organizador, quiero filtrar el calendario por región y tipo y abrir el detalle de un evento desde ahí, para navegar sin cambiar de pantalla. | E5 | Media | 3 | 4 | Isaac |
| HU-18 | **Panel de seguimiento del evento.** Como organizador, quiero ver en el detalle del evento los inscritos contra el cupo, la asistencia y el avance de tareas, para saber si el evento va en tiempo. | E1 | Media | 5 | 4 | David |
| HU-19 | **Historial de notificaciones.** Como organizador, quiero consultar las notificaciones enviadas de un evento, para comprobar qué se comunicó y a quién. | E4 | Baja | 2 | 4 | Uziel |
| HU-20 | **Exportar asistentes a CSV.** Como organizador, quiero exportar la lista de asistentes a un archivo CSV, para compartirla con el cliente. | E2 | Baja | 2 | 4 | Uziel |
| HU-21 | **Administrar usuarios del equipo.** Como administrador, quiero dar de alta y de baja a los miembros del equipo y asignarles un rol, para controlar quién accede a la aplicación. | E6 | Media | 3 | 4 | Stephanie |

## Criterios de aceptación

**HU-01 · Iniciar sesión con mi rol**
- Solo usuarios dados de alta pueden entrar
- El menú muestra únicamente las opciones del rol
- Tras 5 intentos fallidos la cuenta se bloquea 15 minutos

**HU-02 · Crear un evento**
- Tipos: conferencia, capacitación, webinar o reunión ejecutiva
- La fecha de fin no puede ser anterior a la de inicio
- Si es virtual se pide enlace; si es presencial, sede
- El evento se guarda como Borrador hasta publicarlo

**HU-03 · Editar, publicar o cancelar un evento**
- Solo los eventos publicados aceptan registros
- Cancelar pide un motivo y no borra los datos
- Cada cambio queda registrado con fecha y usuario

**HU-04 · Consultar la lista de eventos con filtros**
- Muestra nombre, tipo, fecha, región, estado e inscritos/cupo
- Los filtros se pueden combinar
- Ordena por fecha de inicio de forma predeterminada

**HU-05 · Registrarme a un evento**
- Pide nombre, correo, empresa, cargo y país
- No permite registrar dos veces el mismo correo en un evento
- Si hay cupo el registro queda Confirmado

**HU-06 · Ver y buscar asistentes de un evento**
- Muestra estado del registro y si asistió
- Búsqueda por nombre, correo o empresa
- Muestra totales: confirmados, en espera y cancelados

**HU-07 · Controlar cupo y lista de espera**
- Al llegar al cupo, los nuevos registros quedan En espera
- Si alguien cancela, el primero en espera pasa a Confirmado
- El organizador puede confirmar o cancelar manualmente

**HU-08 · Registrar asistencia (check-in)**
- Solo disponible el día del evento
- Guarda la hora del check-in
- Se puede buscar al asistente por nombre o correo

**HU-09 · Crear y asignar tareas de un evento**
- Cada tarea pertenece a un evento
- Tiene responsable, prioridad y fecha límite obligatorios
- El responsable recibe un aviso al asignársela

**HU-10 · Tablero de tareas por evento**
- Se puede mover una tarea entre columnas
- Muestra responsable y fecha límite en cada tarjeta
- Las tareas vencidas se marcan en rojo

**HU-11 · Ver mis tareas pendientes y vencidas**
- Agrupa por Vencidas, Hoy y Próximas
- Permite filtrar por evento
- Abre el detalle de la tarea con un clic

**HU-12 · Confirmación de registro por correo**
- Se envía en menos de 1 minuto tras registrarse
- Incluye fecha y hora en la zona horaria del evento, sede o enlace
- Si quedó en espera, el correo lo indica

**HU-13 · Avisar a los asistentes cambios o cancelaciones**
- Se dispara al guardar un cambio en fecha, sede, enlace o estado
- Se envía a confirmados y en espera
- Queda registrado en el historial de notificaciones

**HU-14 · Recordatorio automático antes del evento**
- Se programa al publicar el evento
- Solo se envía a registros confirmados
- Si el evento cambia de fecha, el recordatorio se reprograma

**HU-15 · Enviar un mensaje a todos los asistentes**
- Permite elegir destinatarios por estado del registro
- Muestra vista previa antes de enviar
- Queda en el historial de notificaciones

**HU-16 · Calendario de eventos**
- Vistas mes y semana
- Cada evento se muestra con un color por tipo
- Las horas se muestran en la zona horaria del usuario

**HU-17 · Filtrar el calendario y abrir el detalle**
- Filtros por región, tipo y estado
- Al hacer clic se abre el resumen del evento
- Desde el resumen se llega al detalle completo

**HU-18 · Panel de seguimiento del evento**
- Muestra % de cupo ocupado y % de asistencia
- Muestra tareas hechas contra totales y vencidas
- Se actualiza al cambiar registros o tareas

**HU-19 · Historial de notificaciones**
- Muestra tipo, asunto, fecha y número de destinatarios
- Indica envíos fallidos
- Permite ver los destinatarios de cada envío

**HU-20 · Exportar asistentes a CSV**
- Respeta los filtros aplicados
- Incluye estado del registro y asistencia
- El archivo abre correctamente en Excel

**HU-21 · Administrar usuarios del equipo**
- Roles: administrador, organizador y miembro
- Desactivar un usuario no borra su historial
- Solo el administrador ve esta pantalla
