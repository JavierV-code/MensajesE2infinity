# Catálogo preliminar de mensajes

**Propuestas previas, no contratos aprobados.** Los identificadores se conservan como referencias del borrador; los nombres, campos, rutas y aplicabilidad pueden cambiar durante la revisión.

El [plan de trabajo](../plan-trabajo-flujos.md) mantiene el estado de los 34 subpuntos y enlaza sus documentos. Al revisar un mensaje, se añadirá aquí la referencia a su flujo detallado en el [índice de flujos](../flujos/README.md), evitando duplicar su definición. La incorporación inicial será manual; los mensajes de registro y las referencias al panel son antecedentes por revisar, no requisitos ya aprobados para esa etapa.

| ID | Mensaje | Emisor | Receptor | Canal | Dependencia | Estado |
|---|---|---|---|---|---|---|
| `REG-01` | Solicitud de incorporación | E2 Agent | API E2 Infinity | HTTPS | Identidad local | Borrador |
| `REG-02` | Resultado de asociación | API E2 Infinity | E2 Agent | HTTPS | Validación central | Borrador |
| `CFG-01` | Configuración efectiva | API/panel local | E2 Agent | HTTPS/archivo local | Nodo incorporado | Borrador |
| `CFG-02` | Confirmación de configuración | E2 Agent | API/panel | HTTPS | Validación local | Borrador |
| `STA-01` | Heartbeat del nodo | E2 Agent | Vecinos/plataforma | MQTT | Sesión activa | Borrador |
| `STA-02` | Disponibilidad energética | E2 Agent | Vecinos | MQTT | Equipos y configuración válidos | Borrador |
| `TEL-01` | Telemetría agregada | E2 Agent | Plataforma | MQTT | Medición válida | Borrador |
| `OBJ-01` | Referencia u objetivo autorizado | Plataforma o evento acordado | Participantes | MQTT | Decisión arquitectónica pendiente | Pendiente |
| `FLX-01` | Oferta de flexibilidad | E2 Agent | Vecinos/coordinación | MQTT | `STA-02` vigente | Borrador |
| `CON-01` | Inicio de operación coordinada | Origen por definir | Participantes | MQTT | `OBJ-01` válido | Pendiente |
| `CON-02` | Estado iterativo del consenso | E2 Agent | Vecinos | MQTT | Operación activa | Pendiente de algoritmo |
| `CON-03` | Convergencia local | E2 Agent | Vecinos/registro | MQTT | Criterio por definir | Pendiente de algoritmo |
| `CTL-01` | Consigna interna validada | E2 Agent | Adaptador local | Interno | Convergencia y límites válidos | Borrador |
| `RES-01` | Resultado de ejecución | E2 Agent | Plataforma/vecinos | MQTT | Acción ejecutada o rechazada | Borrador |
| `RES-02` | Residuo de operación | E2 Agent | Coordinación | MQTT | Medición posterior | Pendiente |
| `ALM-01` | Alarma técnica | E2 Agent | Plataforma/panel | MQTT/HTTPS | Falla detectada | Borrador |

## Campos transversales

Los recorridos de transporte están descritos en [1.5 — Conexión MQTT](../flujos/1.5-conexion-mqtt.md). Su aprobación documental no aprueba automáticamente los mensajes y campos de este catálogo.

Las solicitudes e informes locales de configuración se describen en [1.6 — Configuración local](../flujos/1.6-configuracion-local.md). Se realizan inicialmente mediante herramientas de terminal y registros; el canal remoto y la correspondencia definitiva con `CFG-01` y `CFG-02` quedan pendientes de revisión.

Todo mensaje operativo debería incluir, según corresponda:

- versión del esquema;
- identificador único del mensaje;
- identidad del emisor;
- marca temporal UTC;
- correlación u operación asociada;
- vigencia o expiración;
- número de secuencia o iteración;
- calidad y unidad de medida;
- estado y motivo de rechazo;
- información de trazabilidad sin secretos.
