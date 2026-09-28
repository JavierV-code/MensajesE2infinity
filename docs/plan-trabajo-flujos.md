# Plan de documentación de flujos — E2 Infinity

Versión documental **0.3.0 — 28 de septiembre de 2026**.

## Propósito y alcance

Organizar la conversación, revisión y documentación de **8 cortes y 46 subfases**: funcionamiento local de la Raspberry, plataforma, equipos, participación distribuida y recuperación. Este documento es el índice único de seguimiento y conserva la equivalencia con los 34 puntos anteriores.

La entrega organiza recorridos, responsabilidades e información intercambiada. Los campos definitivos, reglas operativas y contratos se acordarán al desarrollar cada subfase. Cada fila se conversará individualmente; la aprobación de esta reorganización no valida automáticamente sus flujos.

La configuración inicial es manual mediante archivos y herramientas locales. La automatización remota se resolverá en 2.5. Los paneles, interfaces y servicios descritos representan el diseño objetivo; su evidencia de implementación se registra por separado.

El orden es una referencia de conversación, sin fechas ni duraciones comprometidas. Las dependencias de las tablas son documentales y tentativas: no obligan al nodo a disponer de nube o consenso para operar localmente.

## Recorridos y separación de responsabilidades

| Recorrido | Qué debe documentarse |
|---|---|
| Usuario/técnico–plataforma | Qué puede consultar, configurar y solicitar; permisos y resultado que finalmente ve |
| Técnico–nodo | Edición manual, comprobación y aplicación de configuración; diagnóstico local |
| Interno del nodo | Configuración, lecturas, decisión, máquina de estados, adaptadores y registro; indicar si es una llamada interna o un mensaje entre servicios |
| Agente–equipos | Lecturas, capacidades, órdenes, confirmaciones y resultados mediante EVCC/OCPP, adaptadores, ESP32 y pasarelas |
| Plataforma–nodo | HTTPS para incorporación y configuración administrativa; MQTT para intercambios operativos mediante EMQX y Mosquitto |
| Nodo–vecinos | Supervisión, disponibilidad y variables de coordinación; participación sujeta a condiciones locales |
| Infraestructura de red | Cliente Tailscale y Headscale para registro y coordinación de red privada; administración separada de la lógica energética |

E2 Agent comprueba y ejecuta las decisiones locales. EMQX y Mosquitto transportan publicaciones; Headscale coordina la red privada y los clientes Tailscale proporcionan su transporte. La caída del coordinador de red no debe confundirse automáticamente con pérdida de conectividad entre vecinos.

El recorrido local **3.3 → 4.3 → 4.4 → 4.5 → 4.6** funciona como escenario independiente del consenso. Cuando corresponde coordinación, 7.6 entrega una propuesta al mismo control local y recibe su resultado. El corte 5 documenta qué información recibe, procesa, envía y muestra la plataforma en esos recorridos.

Cada mensaje tiene un emisor y un receptor. Un flujo bidireccional puede reunir mensajes en ambos sentidos sin exigir una respuesta a cada publicación. Las confirmaciones de transporte, procesamiento y ejecución física se distinguen cuando correspondan.

## Seguimiento de las 46 subfases

Las filas mantienen los estados documentales registrados. Los nuevos temas comienzan pendientes. Los acuerdos conversados sin documento individual se conservan como antecedentes a formalizar, sin asignarles fechas o aprobaciones no registradas. Un enlace a un antecedente no implica validación.

### Corte 1 — Arquitectura y mapa completo de interacciones

Establecer quién participa y cómo se relacionan los componentes.

| ID | Subfase y objetivo | Estado | Dependencias documentales tentativas | Pregunta o pendiente | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 1.1 | **Actores y responsabilidades:** Usuario, técnico, plataforma, agente, servicios de comunicación y equipos. | Pendiente | Ninguna | ¿Qué recibe, procesa y emite cada componente? | [Arquitectura, antecedente](arquitectura/README.md) | Acuerdos conversados; consolidar alcance ampliado y referencia. |
| 1.2 | **Identificación y pertenencia:** Nodo, instalación, organización, equipos y grupo eléctrico. | Pendiente | 1.1 | ¿Qué identifica cada entidad y quién establece su asociación? | — | Acuerdos conversados; formalización y referencia pendientes. |
| 1.3 | **Interfaces y sentidos de comunicación:** Emisor, receptor, canal y recorridos unidireccionales o bidireccionales. | Pendiente | 1.1, 1.2 | ¿Qué mensajes circulan en cada sentido y cuáles requieren respuesta? | — | — |
| 1.4 | **Recorridos generales:** Configuración, supervisión, gestión local, coordinación y resultados hasta el usuario. | Pendiente | 1.1, 1.2, 1.3 | ¿Cómo se conectan los recorridos de punta a punta? | — | — |

### Corte 2 — Incorporación, configuración y arranque

Definir cómo se prepara el nodo y cómo aplica su configuración.

| ID | Subfase y objetivo | Estado | Dependencias documentales tentativas | Pregunta o pendiente | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 2.1 | **Registro de red privada:** Cliente Tailscale y Headscale. | Pendiente | 1.1, 1.2, 1.3 | ¿Cómo se registra el cliente y comprueba la conectividad privada? | — | Registro manual conversado; formalización y referencia pendientes. |
| 2.2 | **Vinculación con E2 Infinity:** Incorporación, asociación y autorización del nodo. | Pendiente | 1.1, 1.2, 1.3 | ¿Cómo valida la plataforma la asociación y autorización? | — | Cuenta técnica por nodo conversada; recorrido completo por validar. |
| 2.3 | **Conexiones MQTT:** Agente–Mosquitto, bridge con EMQX y brokers vecinos. | Validado | 1.2, 2.1, 2.2 | Tópicos, permisos detallados y confirmaciones por revisar en cada flujo. | [Conexiones MQTT](flujos/2.3-conexion-mqtt.md) | 2026-09-27: «lo valido», antes 1.5; se conserva el acuerdo. |
| 2.4 | **Configuración local:** Edición, comprobación, aplicación y resultado. | Validado | 1.1, 1.2, 1.3 | Archivos, comandos y aplicación ante operaciones en curso por definir. | [Configuración local](flujos/2.4-configuracion-local.md) | 2026-09-27: «me parece bien», antes 1.6; se conserva el acuerdo. |
| 2.5 | **Configuración remota:** Propuesta desde la plataforma, recepción, comprobación y aplicación. | Borrador | 2.2, 2.3, 2.4 | Validar alcance y etapa manual; acordar automatización posterior. | [Configuración remota](flujos/2.5-configuracion-remota.md) | Revisión 2026-09-27, antes 1.7; sin confirmación de validación. |
| 2.6 | **Coherencia de configuraciones:** Permisos, versiones y conflictos entre cambios locales y remotos. | Pendiente | 2.4, 2.5 | ¿Cómo se detecta y resuelve un conflicto sin sobrescribir silenciosamente? | — | — |
| 2.7 | **Arranque del nodo:** Carga de configuración, comprobación de servicios y habilitación de funciones disponibles. | Pendiente | 1.1, 2.4 | ¿Qué funciones pueden habilitarse con los recursos locales disponibles? | — | — |

### Corte 3 — Equipos, mediciones y supervisión local

Describir cómo el agente conoce sus recursos y su estado.

| ID | Subfase y objetivo | Estado | Dependencias documentales tentativas | Pregunta o pendiente | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 3.1 | **Inventario y capacidades:** Equipos existentes y sus capacidades de medición y control. | Pendiente | 1.2, 2.4 | ¿Cómo se identifican y verifican las capacidades reales? | — | — |
| 3.2 | **Interfaces con los equipos:** EVCC/OCPP, adaptadores, ESP32 y pasarelas. | Pendiente | 1.3, 3.1 | ¿Qué intercambios corresponden a cada adaptador y protocolo? | — | — |
| 3.3 | **Lecturas locales:** Adquisición, unidades, fecha y calidad de las mediciones. | Pendiente | 3.1, 3.2 | ¿Qué hace utilizable una lectura y cómo llega al agente? | — | — |
| 3.4 | **Heartbeat y salud de servicios:** Presencia del nodo y disponibilidad de sus componentes. | Pendiente | 1.3, 2.7 | ¿Quién supervisa cada componente y cómo informa pérdida de contacto? | — | — |
| 3.5 | **Alarmas locales:** Detección, registro y comunicación de fallos y recuperación. | Pendiente | 3.3, 3.4 | ¿Cómo se identifica, comunica y cierra una alarma? | — | — |

### Corte 4 — Gestión energética y ejecución local

Documentar cómo opera la Raspberry sin necesitar consenso.

| ID | Subfase y objetivo | Estado | Dependencias documentales tentativas | Pregunta o pendiente | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 4.1 | **Objetivos y preferencias locales:** Prioridades, reservas, horarios y límites. | Pendiente | 2.4, 3.1 | ¿Qué objetivo energético o económico se persigue y con qué restricciones? | — | — |
| 4.2 | **Tarifas y datos económicos:** Origen, recepción, vigencia y uso para la valoración local. | Pendiente | 2.4, 3.3 | ¿Qué datos aporta la plataforma y qué calcula o verifica el nodo? | — | — |
| 4.3 | **Ciclo de decisión local:** Mediciones y configuración que alimentan las decisiones energéticas. | Pendiente | 3.3, 4.1, 4.2 | ¿Qué inicia una decisión y qué información necesita? | — | — |
| 4.4 | **Prioridades y validación:** Solicitudes concurrentes, aceptación, limitación o rechazo y relación con la máquina de estados. | Pendiente | 2.4, 4.3 | ¿Cómo se resuelven prioridades entre propuestas locales, del usuario y del consenso? | — | — |
| 4.5 | **Orden y confirmación del equipo:** Adaptadores y distinción entre recepción, aceptación y actuación. | Pendiente | 3.2, 4.4 | ¿Qué orden se entrega y qué confirma realmente el equipo? | — | — |
| 4.6 | **Resultado medido y corrección local:** Comprobación del efecto y tratamiento de diferencias. | Pendiente | 3.3, 4.5 | ¿Cómo se compara lo solicitado con lo medido y se corrige localmente? | — | — |
| 4.7 | **Registro de decisiones:** Motivos, configuración utilizada y resultados. | Pendiente | 4.4, 4.6 | ¿Cómo se relacionan decisión, orden y resultado para su consulta? | — | — |

### Corte 5 — Plataforma, información visible e intercambios con el nodo

Definir E2 Infinity desde la perspectiva del usuario y de la Raspberry.

| ID | Subfase y objetivo | Estado | Dependencias documentales tentativas | Pregunta o pendiente | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 5.1 | **Funciones y permisos del usuario:** Qué puede consultar, configurar y solicitar desde la plataforma. | Pendiente | 1.1, 1.2, 2.2 | ¿Qué puede hacer cada rol y sobre qué instalación o nodo? | — | — |
| 5.2 | **Telemetría hacia E2 Infinity:** Datos enviados, destinatarios, condiciones y frecuencia por acordar. | Pendiente | 2.3, 3.3 | ¿Qué recibe y procesa la plataforma y con qué periodicidad? | — | — |
| 5.3 | **Información que muestra la plataforma:** Mediciones, equipos, disponibilidad, calidad y antigüedad de datos. | Pendiente | 3.4, 5.1, 5.2 | ¿Qué ve el usuario y cómo reconoce información desactualizada? | — | — |
| 5.4 | **Información enviada al nodo:** Recorrido de configuraciones y referencias autorizadas; enlazar sus definiciones. | Pendiente | 2.5; 6.3 para referencias energéticas | ¿Qué envía la plataforma, qué recibe el agente y qué respuesta corresponde? | — | — |
| 5.5 | **Resultados visibles:** Configuración solicitada y aplicada, aceptaciones, rechazos, actuaciones y alarmas. | Pendiente | 2.5, 3.5, 4.7, 5.2 | ¿Cómo se muestra el resultado efectivo sin confundir solicitud con ejecución? | — | — |
| 5.6 | **Históricos y consultas:** Almacenamiento, consulta, exportación y trazabilidad hasta el usuario. | Pendiente | 5.2, 5.5 | ¿Cómo consulta el usuario la información conservada y su procedencia? | — | — |

### Corte 6 — Preparación de la participación distribuida

Definir qué puede aportar el nodo y bajo qué condiciones.

| ID | Subfase y objetivo | Estado | Dependencias documentales tentativas | Pregunta o pendiente | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 6.1 | **Participación del usuario:** Habilitación, restricciones y entrada o salida de la coordinación. | Pendiente | 2.4, 4.1 | ¿Cómo se expresa la autorización y se cambia la participación? | — | — |
| 6.2 | **Disponibilidad energética:** Distinguir conectividad de capacidad efectiva para participar. | Pendiente | 3.1, 3.3, 3.4, 4.1 | ¿Qué recursos están realmente disponibles y durante cuánto tiempo? | — | — |
| 6.3 | **Referencias energéticas:** Origen, destinatarios, vigencia y dependencia de la medición del punto de conexión común. | Pendiente | 1.1, 1.3; formulación matemática | ¿Qué referencia exige el algoritmo y cómo llega a los participantes? | — | — |
| 6.4 | **Flexibilidad y valoración de la contribución:** Capacidad ofrecida compatible con necesidades locales y formulación matemática. | Pendiente | 4.2, 6.1, 6.2; formulación matemática | ¿Qué información describe una contribución factible y su valoración? | — | — |
| 6.5 | **Vecinos y grupo eléctrico:** Pertenencia, relaciones de comunicación y pesos locales cuando corresponda. | Pendiente | 1.2, 2.1, 2.2; formulación matemática | ¿Cómo se definen y actualizan participantes, vecinos y pesos? | — | — |

### Corte 7 — Consenso y coordinación entre vecinos

Documentar los intercambios respaldados por el algoritmo.

| ID | Subfase y objetivo | Estado | Dependencias documentales tentativas | Pregunta o pendiente | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 7.1 | **Activación y continuidad:** Condiciones que inician o mantienen la coordinación. | Pendiente | 6.1, 6.3, 6.5; formulación matemática | ¿Qué condición de operación establece el algoritmo? | [Consenso, antecedente](flujos/consenso.md) | — |
| 7.2 | **Intercambio iterativo:** Variables y mensajes necesarios entre participantes. | Pendiente | 6.4, 7.1; formulación matemática | ¿Qué información necesita cada vecino en cada actualización? | [Consenso, antecedente](flujos/consenso.md) | — |
| 7.3 | **Validez de información:** Retrasos, duplicados, ausencias y vigencia. | Pendiente | 3.4, 7.2; formulación matemática | ¿Cuándo se acepta o descarta una actualización? | — | — |
| 7.4 | **Convergencia:** Información que permite reconocer un resultado utilizable. | Pendiente | 7.2, 7.3; formulación matemática validada | ¿Qué evidencia permite utilizar el resultado del algoritmo? | — | — |
| 7.5 | **Falta de convergencia:** Comunicación del problema y continuidad posible. | Pendiente | 7.3, 7.4; formulación matemática | ¿Cómo se informa y qué funcionamiento puede mantenerse? | — | — |
| 7.6 | **Entrega y realimentación:** Propuesta al control local, resultado ejecutado y residuo devuelto a la coordinación. | Pendiente | 4.4, 4.6, 7.4, 7.5; formulación matemática | ¿Cómo se comunica la propuesta y se incorpora el resultado real? | — | — |

### Corte 8 — Fallos, recuperación y revisión completa

Comprobar la continuidad de los recorridos ante fallos.

| ID | Subfase y objetivo | Estado | Dependencias documentales tentativas | Pregunta o pendiente | Documento | Fecha y referencia del acuerdo |
|---|---|---|---|---|---|---|
| 8.1 | **Pérdida de servicios externos:** Distinguir fallos de API, EMQX y coordinación de red privada. | Pendiente | 2.1, 2.2, 2.3, 3.4, 4.4 | ¿Qué funciones continúan y qué mensajes quedan pendientes por servicio? | — | — |
| 8.2 | **Pérdida de vecinos:** Detección y cambios en la participación. | Pendiente | 3.4, 6.5, 7.5 | ¿Cómo cambia la coordinación ante un vecino ausente? | — | — |
| 8.3 | **Fallos internos y de equipos:** Agente, broker local, adaptadores, pasarelas y dispositivos. | Pendiente | 3.4, 3.5, 4.5, 6.2 | ¿Cómo se comunica una falla y se actualiza la capacidad disponible? | — | — |
| 8.4 | **Reinicio y recuperación:** Recuperar configuración y comprobar condiciones para volver a operar. | Pendiente | 2.4, 2.7, 8.1, 8.2, 8.3 | ¿Qué información se recupera y qué comprobaciones preceden a la operación? | — | — |
| 8.5 | **Sincronización pendiente:** Información conservada, reenviada o descartada al reconectar. | Pendiente | 4.7, 5.6, 8.1, 8.4 | ¿Cómo se sincroniza sin repetir actuaciones antiguas? | — | — |
| 8.6 | **Revisión de punta a punta:** Escenarios completos y detección de mensajes faltantes o responsabilidades ambiguas. | Pendiente | Todos los cortes anteriores | ¿Cada solicitud tiene destinatario, tratamiento y resultado trazable? | [Escenarios, antecedente](validacion/escenarios.md) | — |

## Equivalencias de la numeración anterior

La columna «Anterior» corresponde al plan de seis bloques (hasta 0.2.5). La columna «Actual» corresponde exclusivamente a esta versión. Cada punto anterior tiene una ubicación principal; las ampliaciones pueden compartir referencias sin duplicar la definición del flujo.

| Anterior | Actual | Subfase de destino |
|---|---|---|
| 1.1 | 1.1 | Actores y responsabilidades |
| 1.2 | 1.2 | Identificación y pertenencia |
| 1.3 | 2.1 | Registro de red privada |
| 1.4 | 2.2 | Vinculación con E2 Infinity |
| 1.5 | 2.3 | Conexiones MQTT |
| 1.6 | 2.4 | Configuración local |
| 1.7 | 2.5 | Configuración remota |
| 2.1 | 3.1 | Inventario y capacidades |
| 2.2 | 3.3 | Lecturas locales |
| 2.3 | 5.2 | Telemetría hacia E2 Infinity |
| 2.4 | 3.4 | Heartbeat y salud de servicios |
| 2.5 | 6.2 | Disponibilidad energética |
| 2.6 | 3.5 | Alarmas locales |
| 3.1 | 6.3 | Referencias energéticas |
| 3.2 | 6.1 | Participación del usuario |
| 3.3 | 4.2 | Tarifas y datos económicos |
| 3.4 | 6.4 | Flexibilidad y valoración de la contribución |
| 3.5 | 6.5 | Vecinos y grupo eléctrico |
| 4.1 | 7.1 | Activación y continuidad |
| 4.2 | 7.2 | Intercambio iterativo |
| 4.3 | 7.3 | Validez de información |
| 4.4 | 7.4 | Convergencia |
| 4.5 | 7.5 | Falta de convergencia |
| 4.6 | 7.6 | Entrega y realimentación |
| 5.1 | 4.4 | Prioridades y validación |
| 5.2 | 4.5 | Orden y confirmación del equipo |
| 5.3 | 4.5 | Orden y confirmación del equipo |
| 5.4 | 4.6 | Resultado medido y corrección local |
| 5.5 | 7.6 | Entrega y realimentación |
| 6.1 | 8.1 | Pérdida de servicios externos |
| 6.2 | 8.2 | Pérdida de vecinos |
| 6.3 | 8.3 | Fallos internos y de equipos |
| 6.4 | 8.4 | Reinicio y recuperación |
| 6.5 | 8.6 | Revisión de punta a punta |

La participación del usuario (antes 3.2, ahora 6.1) reutiliza las preferencias locales de 4.1. Orden y confirmación (antes 5.2 y 5.3) se revisan conjuntamente en 4.5. Entrega al control y residuo (antes 4.6 y 5.5) se reúnen en 7.6.

Los documentos individuales de MQTT y configuración conservan sus acuerdos y fechas bajo 2.3, 2.4 y 2.5. Sus rutas anteriores enlazan a los documentos renumerados. Los [diagramas v01](diagramas/README.md) y sus exportaciones conservan la numeración histórica, con una equivalencia junto a sus vistas.

## Método de conversación y documentación

1. Seleccionar una subfase y presentar una propuesta breve con un escenario concreto.
2. Conversar alternativas, participantes y dependencias; registrar lo acordado y lo pendiente.
3. Desarrollar el documento con la [plantilla común](flujos/plantilla-flujo.md).
4. Usar Draw.io para el mapa de interfaces y Mermaid para secuencias detalladas. El [catálogo](mensajes/catalogo-mensajes.md) mantiene una definición común por mensaje.
5. Obtener confirmación explícita antes de marcar la subfase como validada y registrar su referencia.
6. Actualizar esta fila y los enlaces de los índices; incorporar el avance mediante un commit identificable.

Cada documento registra propósito y disparador; participantes y qué reciben, procesan y envían; acciones manuales e internas; mensajes, sentido y canal; contenido mínimo y respuesta necesaria; confirmaciones de transporte, procesamiento y ejecución; información visible al usuario; errores, recuperación, dependencias y evidencia del acuerdo.

Los documentos individuales se crean al abordar cada subfase, sin generar archivos vacíos para todas ellas. Un borrador puede publicarse antes de su aprobación si conserva su estado documental. La máquina de estados sigue siendo un componente por definir, sin fijar sus estados en esta reorganización.

### Estados documentales

| Estado | Significado |
|---|---|
| Pendiente | Aún falta revisión individual o formalización de antecedentes |
| En conversación | Se están contrastando propuestas y preguntas |
| Borrador | Existe una propuesta documentada pendiente de confirmación |
| Validado | Hay confirmación explícita del acuerdo documental y su referencia |
| Por revisar | Un cambio de alcance o dependencia requiere reconsiderar el acuerdo |

La aprobación documental no equivale a software implementado ni a ensayo físico aprobado. Un acuerdo previo conserva su alcance; una ampliación requiere su propia revisión.

## Criterios transversales y comprobación

- Mantener 46 identificadores únicos en las filas de seguimiento y correspondencia para los 34 anteriores.
- Cubrir gestión local sin consenso, configuración remota, supervisión, coordinación y recuperación.
- Identificar en cada caso los envíos, recepciones y resultados visibles de la plataforma y la Raspberry.
- Revisar autorización, identidad, vigencia, duplicados, orden y trazabilidad según el flujo.
- Conservar el alcance y las fechas de los acuerdos, las rutas antiguas como referencias y los diagramas históricos.
- Verificar enlaces y evitar mensajes duplicados con definiciones divergentes.
- Resolver las variables, activación, pesos y convergencia del consenso contra la formulación matemática y su validación offline.

Los [tópicos MQTT](mensajes/topicos-mqtt.md), el [consenso conceptual](flujos/consenso.md) y los [JSON Schema](../schemas/README.md) conservan su condición de propuestas previas. Esta versión no establece nuevos endpoints ni modifica esquemas. La revisión de escenarios se desarrolla en 8.6 y en sus [antecedentes](validacion/escenarios.md).

## Próxima conversación

**1.1 — Actores y responsabilidades:** consolidar los acuerdos conversados con el alcance ampliado de plataforma y funcionamiento local. Configuración remota continúa como borrador en 2.5; los acuerdos de 2.3 y 2.4 se conservan.
