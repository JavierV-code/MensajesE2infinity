# Plan tentativo de documentación de flujos — E2 Infinity

Versión documental 0.2.1 — 27 de septiembre de 2026.

## Propósito y alcance

Organizar la conversación, revisión y documentación de 34 subpuntos en seis bloques. Este es el índice único de seguimiento; los demás documentos enlazan aquí para consultar el orden y el estado del trabajo.

La incorporación y configuración inicial serán manuales mediante archivos editados por el equipo técnico. Esta entrega organiza la documentación: no implementa servicios, modifica APIs ni aprueba contratos de mensajes.

El orden es secuencial como referencia, sin fechas ni duraciones comprometidas. Las dependencias siguientes son tentativas y podrán corregirse al conversar cada punto. Si una definición está bloqueada, se podrá avanzar en puntos independientes.

## Separación de recorridos

| Recorrido | Información por revisar |
|---|---|
| Plataforma–nodo | Incorporación, configuración, referencias, telemetría y resultados; backend E2 Infinity, EMQX, Mosquitto y E2 Agent |
| Nodo–vecinos | Heartbeat, disponibilidad y variables de coordinación entre agentes mediante sus brokers |
| Agente–equipos | Lecturas, capacidades, consignas, confirmaciones y resultados a través de adaptadores y pasarelas |
| Infraestructura de red | Registro y coordinación entre cliente Tailscale y Headscale; administración independiente de la lógica energética |

En cada secuencia se distinguirán **acción manual**, **interacción interna** y **mensaje entre servicios**. Editar un archivo es una acción manual; leerlo y validarlo es una interacción interna. Ninguna de ellas implica por sí sola un mensaje de red.

## Seguimiento

Todos los subpuntos comienzan pendientes de revisión individual. En «Documento» solo se enlaza material que existe: «antecedente» indica un borrador previo, no un flujo validado. El guion indica que aún no hay documento o acuerdo. La fecha se registrará junto con una referencia al acuerdo explícito, sin inventar aprobaciones.

### Bloque 1 — Incorporación y configuración

| ID | Objetivo | Estado | Dependencias tentativas | Pregunta abierta | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 1.1 | Actores y responsabilidades: delimitar qué recibe, procesa y emite cada componente | Pendiente | Ninguna | ¿Dónde termina la responsabilidad de cada componente? | [Arquitectura, antecedente](arquitectura/README.md) | — |
| 1.2 | Identificación: relacionar nodo, instalación, equipos y grupo eléctrico | Pendiente | 1.1 | ¿Qué identificadores se conservan y quién los asigna? | — | — |
| 1.3 | Registro de red privada: describir registro y comprobación de conectividad | Pendiente | 1.1, 1.2 | ¿Qué intercambios confirman la conexión a la red privada? | — | — |
| 1.4 | Vinculación con E2 Infinity: reconocer y autorizar al nodo incorporado manualmente | Pendiente | 1.2 | ¿Cómo se comprueba la asociación y autorización central? | — | — |
| 1.5 | Conexión MQTT: verificar agente–Mosquitto, Mosquitto–EMQX y brokers vecinos | Validado | 1.2, 1.3, 1.4 | Tópicos, permisos detallados y confirmaciones de aplicación por definir en sus flujos | [Conexión MQTT](flujos/1.5-conexion-mqtt.md) | 2026-09-27: confirmación «lo valido», registrada en el documento |
| 1.6 | Configuración local: describir carga, validación y resultado | Pendiente | 1.1, 1.2 | ¿Cómo se informa la aceptación o el rechazo de la configuración manual? | — | — |
| 1.7 | Configuración remota: definir solicitudes de cambio y sus respuestas | Pendiente | 1.4, 1.6 | ¿Qué cambios se permiten y cómo conviven con las preferencias locales? | — | — |

### Bloque 2 — Equipos y supervisión

| ID | Objetivo | Estado | Dependencias tentativas | Pregunta abierta | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 2.1 | Equipos y capacidades: comunicar qué puede medir o controlar el nodo | Pendiente | 1.2, 1.6 | ¿Cómo se registra y actualiza la capacidad de cada equipo? | — | — |
| 2.2 | Lecturas locales: recorrer las mediciones desde equipos y ESP32 hasta el agente | Pendiente | 2.1 | ¿Qué identifica una lectura válida y reciente? | — | — |
| 2.3 | Telemetría central: definir qué se publica y bajo qué condiciones | Pendiente | 1.5, 2.2 | ¿Qué información requiere la plataforma y con qué frecuencia? | — | — |
| 2.4 | Heartbeat: describir presencia y detección de ausencia | Pendiente | 1.2, 1.5 | ¿Quién supervisa a quién y cuándo considera perdido el contacto? | — | — |
| 2.5 | Disponibilidad energética: comunicar capacidad real de participación | Pendiente | 2.1, 2.2, 2.4 | ¿Cómo se distingue conexión de disponibilidad para participar? | — | — |
| 2.6 | Alarmas: informar fallos y su recuperación | Pendiente | 2.1, 2.4 | ¿Quién recibe cada alarma y qué confirmación requiere? | — | — |

### Bloque 3 — Preparación de la coordinación

| ID | Objetivo | Estado | Dependencias tentativas | Pregunta abierta | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 3.1 | Referencias energéticas: precisar origen, destinatarios y vigencia | Pendiente | 1.1, 1.4, formulación matemática | ¿Qué referencia requiere el algoritmo y cómo llega a los participantes? | — | — |
| 3.2 | Participación del usuario: comunicar habilitación, reservas y prioridades | Pendiente | 1.6, 1.7 | ¿Cómo se expresan y actualizan las condiciones de participación? | — | — |
| 3.3 | Parámetros económicos: separar aportes centrales y cálculo o validación local | Pendiente | 1.7, 2.2, formulación matemática | ¿Qué información económica intercambian plataforma y nodo? | — | — |
| 3.4 | Flexibilidad local: describir aumento o reducción factible y duración | Pendiente | 2.5, 3.2, 3.3, formulación matemática | ¿Qué datos describen una contribución factible y vigente? | — | — |
| 3.5 | Vecinos y grupo eléctrico: comunicar pertenencia y relaciones autorizadas | Pendiente | 1.2, 1.3, 1.4, formulación matemática | ¿Cómo se actualizan vecinos y parámetros locales de comunicación? | — | — |

### Bloque 4 — Consenso entre vecinos

| ID | Objetivo | Estado | Dependencias tentativas | Pregunta abierta | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 4.1 | Activación y continuidad: describir cuándo inicia o se mantiene la coordinación | Pendiente | 3.1, 3.2, 3.5, formulación matemática | ¿Qué condición de operación establece el algoritmo? | [Consenso, antecedente](flujos/consenso.md) | — |
| 4.2 | Intercambio iterativo: identificar variables y actualización enviada | Pendiente | 3.3, 3.4, 3.5, 4.1, formulación matemática | ¿Qué variables necesita realmente cada vecino? | [Consenso, antecedente](flujos/consenso.md) | — |
| 4.3 | Validez de información: tratar datos atrasados, repetidos o ausentes | Pendiente | 2.4, 4.2, formulación matemática | ¿Cuándo se acepta o descarta una actualización? | — | — |
| 4.4 | Convergencia: comunicar la condición que permite utilizar el resultado | Pendiente | 4.2, 4.3, formulación matemática validada | ¿Qué evidencia de convergencia requiere cada agente? | — | — |
| 4.5 | Falta de convergencia: informar y determinar continuidad operativa | Pendiente | 4.3, 4.4, formulación matemática | ¿Qué intercambios corresponden cuando no se obtiene un resultado válido? | — | — |
| 4.6 | Entrega al control local: transferir la propuesta a la decisión del nodo | Pendiente | 4.4, 4.5 | ¿Qué información y vigencia acompañan al resultado entregado? | — | — |

### Bloque 5 — Ejecución y resultados

| ID | Objetivo | Estado | Dependencias tentativas | Pregunta abierta | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 5.1 | Validación local: informar aceptación, limitación o rechazo | Pendiente | 1.6, 2.5, 3.2, 4.6 | ¿Cómo se devuelve la decisión local y su motivo? | — | — |
| 5.2 | Orden al equipo: describir el recorrido agente–adaptador–dispositivo | Pendiente | 2.1, 5.1 | ¿Qué traduce cada adaptador y qué recibe el equipo? | — | — |
| 5.3 | Confirmación de ejecución: distinguir recepción, aceptación y actuación | Pendiente | 5.2 | ¿Qué confirma el equipo y qué debe verificar el agente? | — | — |
| 5.4 | Resultado medido: comparar solicitud y efecto físico | Pendiente | 2.2, 5.3 | ¿Qué mediciones respaldan el resultado comunicado? | — | — |
| 5.5 | Residuo y ajuste: comunicar diferencias para continuar la coordinación | Pendiente | 5.4, bloque 4, formulación matemática | ¿Cómo se incorpora la diferencia real al algoritmo? | — | — |

### Bloque 6 — Fallos e integración completa

| ID | Objetivo | Estado | Dependencias tentativas | Pregunta abierta | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 6.1 | Pérdida de plataforma: describir continuidad local y mensajes pendientes | Pendiente | 1.5, 1.6, 2.4, 5.1 | ¿Qué intercambios cesan y cuáles continúan localmente? | — | — |
| 6.2 | Pérdida de vecino: comunicar cambios de participantes | Pendiente | 2.4, 3.5, bloque 4 | ¿Cómo se informa la ausencia y se ajusta la coordinación? | — | — |
| 6.3 | Falla de equipo: actualizar disponibilidad y contribución | Pendiente | 2.5, 2.6, 5.3, 5.5 | ¿Cómo se comunica una actuación fallida o una capacidad reducida? | — | — |
| 6.4 | Reinicio y recuperación: recuperar información y resincronizar | Pendiente | 1.2, 1.6, 6.1, 6.2, 6.3 | ¿Qué información debe intercambiarse de nuevo antes de participar? | — | — |
| 6.5 | Revisión de extremo a extremo: recorrer escenarios completos | Pendiente | Todos los puntos anteriores | ¿Hay mensajes faltantes, contradictorios o sin receptor? | [Escenarios, antecedente](validacion/escenarios.md) | — |

## Método de conversación e integración

1. Seleccionar un subpunto y presentar una propuesta breve con un caso concreto.
2. Conversar alternativas, dependencias y responsabilidades.
3. Documentar el flujo utilizando la [plantilla común](flujos/plantilla-flujo.md), con secuencias Mermaid cuando corresponda.
4. Registrar acuerdos y preguntas abiertas. Solicitar confirmación explícita antes de marcar el punto como validado.
5. Actualizar su fila y enlazar el documento desde el mapa general y el catálogo, evitando duplicar definiciones.
6. Incorporar el avance mediante un commit identificable; por ejemplo, `docs: incorpora borrador del punto 1.1`.

Los documentos de cada punto se crearán al trabajarlo, con nombres como `docs/flujos/1.1-actores-responsabilidades.md`. No se crean 34 documentos vacíos en esta entrega. Un borrador puede versionarse antes de su aprobación siempre que conserve su estado documental.

### Estados documentales

| Estado | Significado |
|---|---|
| Pendiente | Aún no se ha revisado individualmente |
| En conversación | Se están contrastando propuestas y preguntas |
| Borrador | Existe una propuesta documentada pendiente de confirmación |
| Validado | El usuario confirmó explícitamente el acuerdo documental; se registra fecha y referencia |
| Por revisar | Una modificación o dependencia obliga a reconsiderar un acuerdo anterior |

Estos estados describen documentos, no la máquina de estados operativa del nodo. «Validado» no equivale a software implementado ni a ensayo físico aprobado: esas evidencias se registrarán por separado. Si falta información matemática o técnica, el punto conserva sus pendientes.

## Material previo y criterios transversales

El [catálogo](mensajes/catalogo-mensajes.md), los [tópicos MQTT](mensajes/topicos-mqtt.md), el [flujo conceptual de consenso](flujos/consenso.md) y los [JSON Schema](../schemas/README.md) son propuestas previas, no contratos aprobados. Sus rutas, campos, estados y secuencias deberán revisarse dentro de los subpuntos correspondientes.

La activación, variables, pesos y convergencia del consenso se cerrarán contra la formulación matemática y su validación offline. El diagrama previo por eventos no determina por sí solo el funcionamiento definitivo del algoritmo.

En cada flujo se revisarán autorización, identificadores, vigencia, duplicados, orden de mensajes y trazabilidad según su aplicación. Los fallos se tratarán desde cada punto; el último bloque comprobará coherencia entre todos ellos.

## Próxima conversación

**Punto 1.6 — Configuración local:** describir cómo el agente lee, valida y comunica el resultado de los parámetros ingresados manualmente. Los acuerdos anteriores de la conversación se incorporarán en sus documentos correspondientes; esta actualización registra específicamente la validación de 1.5.
