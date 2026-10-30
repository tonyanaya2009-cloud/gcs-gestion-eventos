# Genera planeacion/05-product-backlog.md y planeacion/06-plan-de-sprints.md a partir de .github/backlog.json
import json
d=json.load(open('.github/backlog.json'))
H=d['historias'];S=d['sprints'];E={e['id']:e['nombre'] for e in d['epicas']}
o=["# 5. Product Backlog","",
"Historias de usuario en el formato *Como [rol], quiero [acción], para [beneficio]*, ordenadas por prioridad. Cada una existe como **issue** en el repositorio, con sus criterios de aceptación como lista de verificación.","",
"## Técnica de estimación","Se usó **Planning Poker** con la serie de Fibonacci (1, 2, 3, 5, 8). Cada integrante vota en secreto y, si hay diferencia, quienes votaron más alto y más bajo explican su razonamiento antes de volver a votar. Como referencia, **HU-04 (lista de eventos con filtros) = 3 puntos**.","",
"| Puntos | Significado |","|---|---|","| 1–2 | Cambio pequeño, sin lógica nueva |","| 3 | Una pantalla o regla sencilla |","| 5 | Pantalla con lógica de negocio o integración (correo, cupo) |","| 8 | Funcionalidad grande: se divide antes de entrar a un sprint |","",
"## Épicas","","| Épica | Nombre | Historias | Puntos |","|---|---|---|---|"]
for e in d['epicas']:
    hs=[h for h in H if h['epica']==e['id']]
    o.append(f"| {e['id']} | {e['nombre']} | {', '.join(h['id'] for h in hs)} | {sum(h['puntos'] for h in hs)} |")
o.append(f"| | **Total** | **{len(H)} historias** | **{sum(h['puntos'] for h in H)}** |")
o+=["","## Historias de usuario","","| ID | Historia de usuario | Épica | Prioridad | Puntos | Sprint | Responsable |","|---|---|---|---|---|---|---|"]
for h in H:
    o.append(f"| {h['id']} | **{h['titulo']}.** {h['historia']} | {h['epica']} | {h['prioridad']} | {h['puntos']} | {h['sprint']} | {h['responsable']} |")
o+=["","## Criterios de aceptación",""]
for h in H:
    o.append(f"**{h['id']} · {h['titulo']}**")
    o+= [f"- {c}" for c in h['criterios']]
    o.append("")
open('planeacion/05-product-backlog.md','w').write("\n".join(o))

p=["# 6. Plan de sprints","",
"- **Duración:** 4 sprints de 1 semana, del 2 al 29 de noviembre de 2026. La fase 1 (este avance) fue el Sprint 0 de planeación, del 26 al 31 de octubre.",
"- **Equipo Scrum (Equipo 1):** Antonio Anaya (Product Owner), Stephanie Ramos Lozano (Scrum Master), David Alfonso Lorenzo, Calixto Isaac Galeana Medrano y Uziel García (Development Team).",
"- **Capacidad y velocidad:** 3 desarrolladores con unas 10 horas por semana cada uno, más el apoyo de la Scrum Master. La velocidad planeada es de **unos 20 puntos por sprint** y se ajustará con la velocidad real del Sprint 1.",
"- **Eventos de cada sprint:** Sprint Planning el lunes (1 h), Daily Scrum de lunes a viernes (15 min), y Sprint Review (45 min) y Retrospectiva (30 min) el domingo.",
"- **Definición de terminado (DoD):** cumple sus criterios de aceptación, el código está revisado en un *pull request*, pasa las pruebas en GitHub Actions, está desplegado y el Product Owner lo aceptó.","",
"## Resumen","","| Sprint | Fechas | Objetivo del sprint | Historias | Puntos |","|---|---|---|---|---|"]
for i,s in enumerate(S,1):
    hs=[h for h in H if h['sprint']==i]
    p.append(f"| {s['titulo']} | {s['inicio'][8:]}/11 – {s['fin'][8:]}/11 | {s['objetivo']} | {', '.join(h['id'] for h in hs)} | {sum(h['puntos'] for h in hs)} |")
p.append(f"| **Total** | | | **{len(H)}** | **{sum(h['puntos'] for h in H)}** |")
for i,s in enumerate(S,1):
    hs=[h for h in H if h['sprint']==i]
    p+=["",f"## {s['titulo']} ({s['inicio'][8:]} al {s['fin'][8:]} de noviembre)","",f"**Objetivo:** {s['objetivo']}","","| Historia | Puntos | Prioridad | Responsable |","|---|---|---|---|"]
    p+=[f"| {h['id']} · {h['titulo']} | {h['puntos']} | {h['prioridad']} | {h['responsable']} |" for h in hs]
    p.append(f"| **Total** | **{sum(h['puntos'] for h in hs)}** | | |")
p+=["","## Carga por integrante","","| Integrante | Rol | Puntos | Historias |","|---|---|---|---|"]
roles={'David':'Development Team (backend y datos)','Isaac':'Development Team (interfaz)','Uziel':'Development Team (registro, correo y pruebas)','Stephanie':'Scrum Master','Antonio':'Product Owner'}
for n in ['David','Isaac','Uziel','Stephanie']:
    hs=[h for h in H if h['responsable']==n]
    p.append(f"| {n} | {roles[n]} | {sum(h['puntos'] for h in hs)} | {', '.join(h['id'] for h in hs)} |")
p.append("| Antonio | Product Owner | — | Prioriza el backlog, redacta criterios de aceptación y acepta las historias |")
p+=["","## Criterios de priorización","1. **Valor y dependencia:** primero lo que habilita todo lo demás (acceso, crear eventos y registrar asistentes).","2. **Riesgo técnico al inicio:** el control de cupo y las tareas van en el Sprint 2, antes de las notificaciones, que dependen de ellos.","3. **Incremento usable en cada sprint:** al cerrar cada sprint, GCS puede usar algo nuevo de principio a fin.",""]
open('planeacion/06-plan-de-sprints.md','w').write("\n".join(p))
print("Documentos generados")
