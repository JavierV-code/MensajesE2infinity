# Historial de cambios

## 0.3.7 — 2026-10-04

- Valida documentalmente 2.2 — Vinculación con E2 Infinity tras la aceptación de las propuestas de alta, acceso de personas y reemplazo.
- Define precreación del nodo con instalación y grupo, credencial técnica exclusiva vinculada al `node_id` y configuración manual inicial de la Raspberry.
- Distingue la cuenta titular y otras cuentas autorizadas de la credencial del agente; conserva el nodo lógico e historial al reemplazar la Raspberry y renueva su credencial.
- Deja los permisos detallados, la telemetría y la recuperación operativa en sus subfases; indica 2.5 como próxima conversación porque 2.3 y 2.4 ya estaban validadas. No fija endpoints, tópicos, esquemas ni valores reales de credenciales.

## 0.3.6 — 2026-10-04

- Valida documentalmente 2.1 — Registro de red privada mediante confirmación explícita.
- Define clave temporal de un solo uso por Raspberry, alta manual por el técnico y reporte de estado del cliente por el E2 Agent.
- Separa registro Headscale de conectividad a pares y del alta/autorización en E2 Infinity; remite la prueba tras caída de Headscale a VAL-16/corte 8.
- Corrige la matriz 1.3 y el mapa de arquitectura; conserva intacto el Draw.io histórico con una nota de vigencia en su índice.
- Actualiza la siguiente subfase a 2.2; no modifica APIs, mensajes, tópicos ni JSON Schema.

## 0.3.5 — 2026-10-03

- Valida documentalmente 1.4 — Recorridos generales mediante confirmación explícita.
- Conecta preparación, gestión local independiente, configuración HTTPS, meta común por MQTT, consenso entre vecinos, actuación y dos retornos diferenciados.
- Resume continuidad local ante pérdidas y remite el tratamiento detallado a sus subfases; mantiene el bridge Mosquitto–EMQX como pendiente de implementación.
- Actualiza la siguiente subfase a 2.1; no fija contratos, endpoints, tópicos ni criterios matemáticos nuevos.

## 0.3.4 — 2026-10-03

- Valida documentalmente 1.3 — Interfaces y sentidos de comunicación mediante confirmación explícita.
- Incorpora la matriz de interfaces, separando acciones manuales, llamadas internas, mensajes de aplicación y transporte.
- Distingue diseño acordado, propuesta, implementación pendiente y aspectos por verificar; mantiene el bridge Mosquitto–EMQX como pendiente.
- Actualiza el mapa Mermaid general y deja 1.4 — Recorridos generales como siguiente subfase; conserva el Draw.io histórico y no modifica APIs, tópicos ni esquemas.

## 0.3.3 — 2026-10-03

- Valida documentalmente 1.2 — Identificación y pertenencia mediante confirmación explícita.
- Define la relación entre organización, instalación, nodo lógico, equipos y grupo eléctrico; mantiene al grupo eléctrico separado de la topología de vecinos.
- Registra la asignación conceptual de `node_id` por E2 Infinity y `device_id` único dentro del nodo, sin fijar campos ni formatos.
- Actualiza la siguiente subfase a 1.3; conserva pendientes el flujo de alta de 2.2 y la topología de 6.5, sin modificar contratos ni esquemas.

## 0.3.2 — 2026-10-03

- Valida documentalmente 1.1 — Actores y responsabilidades mediante confirmación explícita.
- Distingue usuario, técnico y administrador de infraestructura; asigna a este último la administración central de Headscale.
- Confirma las fronteras entre backend, E2 Agent, comunicaciones, adaptadores y equipos; deja permisos, referencia de consenso e interfaces detalladas en sus subfases correspondientes.
- Actualiza el siguiente punto de conversación a 1.2; no modifica contratos, mensajes, APIs ni esquemas.

## 0.3.1 — 2026-10-03

- Crea `docs/definiciones-flujos.md` como fuente principal con secciones y anclas para las 46 subfases.
- Integra los detalles de MQTT y configuración, conservando la aprobación y fecha de 2.3 y 2.4 y el borrador de 2.5.
- Registra 1.1 como propuesta en conversación, preservando las decisiones explícitas y los asuntos pendientes sin marcarlo como validado.
- Actualiza el plan como índice único de estados y dependencias, más los índices, catálogo, guía y enlaces históricos.
- Mantiene Draw.io, JSON Schema y catálogo de mensajes como artefactos separados; no aprueba contratos, tópicos, endpoints ni campos nuevos.

## 0.3.0 — 2026-09-28

- Reorganiza el plan en ocho cortes y 46 subfases, con equivalencia individual para los 34 puntos anteriores.
- Incorpora arranque, gestión energética local sin consenso, prioridades y registro de decisiones.
- Explicita funciones de plataforma, información visible, envíos, recepciones e históricos.
- Amplía la plantilla con sentidos, disparadores y confirmaciones de transporte, procesamiento y ejecución.
- Renumera MQTT y configuración como 2.3, 2.4 y 2.5; conserva acuerdos, fechas y borrador, con enlaces desde las rutas anteriores.
- Conserva los diagramas v01 y añade su equivalencia histórica.
- Corrige el mapa general de flujos y la dependencia preliminar de CTL-01 para admitir decisiones locales.
- Amplía los escenarios de revisión y establece 1.1 — Actores y responsabilidades como siguiente conversación; APIs y JSON Schema sin cambios.

## 0.2.5 — 2026-09-27

- Amplía el borrador de 1.7 para configurar desde E2 Infinity parámetros persistentes del nodo, con validación y aplicación a cargo del agente.
- Separa preferencias energéticas, propuestas técnicas autorizadas, cambios sensibles de infraestructura y administración del sistema operativo.
- Conserva consulta y aplicación manuales como propuesta inicial; distingue adquisición automática de aplicación automática como evoluciones por acordar.
- Añade destinatario, permisos, revisión de partida, conflictos local/remoto y ejemplos, sin fijar contratos ni modificar APIs o JSON Schema.
- Mantiene 1.7 pendiente de validación explícita y separa configuración persistente de consignas operativas.

## 0.2.4 — 2026-09-27

- Añade un Draw.io editable del primer corte con tres pestañas: incorporación e identidad, conexiones MQTT y configuración local/remota.
- Exporta las tres vistas como PNG y SVG y las enlaza desde los índices documentales.
- Mantiene 1.4 como recorrido parcialmente acordado y 1.7 como borrador; no modifica los estados del plan, APIs, tópicos ni JSON Schema.
- Incorpora un generador reproducible con comprobación de recorridos ortogonales, entradas perpendiculares, límites y ausencia de cruces o superposiciones.

## 0.2.3 — 2026-09-27

- Prepara el borrador de 1.7 — Configuración remota, con secuencia Mermaid y estado pendiente de validación.
- Propone consulta manual HTTPS, comprobación local y aplicación según el acuerdo de 1.6.
- Distingue propuesta guardada, comprobada y aplicada; documenta alcance, permisos y conciliación pendientes.
- Enlaza el borrador y aclara el carácter provisional de los tópicos MQTT de configuración, sin modificar APIs ni JSON Schema.

## 0.2.2 — 2026-09-27

- Registra el acuerdo de 1.6 — Configuración local y su secuencia Mermaid.
- Documenta edición manual, comprobación previa y activación mediante reinicio controlado del E2 Agent.
- Distingue configuración propuesta, configuración aplicada y conexiones pendientes; conserva la última configuración válida ante rechazo.
- Enlaza el flujo desde los índices y establece configuración remota como siguiente conversación, sin modificar contratos JSON.

## 0.2.1 — 2026-09-27

- Registra la aprobación explícita de 1.5 — Conexión MQTT y enlaza su secuencia Mermaid desde los índices.
- Documenta los tres recorridos principales, el bridge selectivo con EMQX y las credenciales MQTT centrales propias por nodo.
- Distingue conexión, entrega y procesamiento; mantiene tópicos y contratos pendientes de revisión.
- Identifica el bridge central como pendiente de implementación y establece configuración local como siguiente conversación.

## 0.2.0 — 2026-09-27

- Incorpora el plan documental de seis bloques y 34 subpuntos pendientes de revisión individual.
- Añade seguimiento de dependencias, preguntas, documentos y acuerdos, junto con una plantilla común.
- Registra el aprovisionamiento manual y distingue aprobación documental de evidencia técnica.
- Enlaza el plan desde los índices e identifica mensajes, tópicos, diagramas y JSON Schema como propuestas previas.
- Establece actores y responsabilidades como próxima conversación, sin modificar APIs ni esquemas JSON.

## 0.1.0 — 2026-09-27

- Crea la estructura documental inicial.
- Separa los planos de configuración, supervisión, consenso y control físico.
- Incorpora un catálogo preliminar de mensajes y tópicos MQTT.
- Añade esquemas JSON iniciales para envolvente, configuración, heartbeat y estado iterativo.
- Registra decisiones abiertas y escenarios de validación.
