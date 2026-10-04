# Catálogo preliminar de mensajes

**Propuestas previas, no contratos aprobados.** Los identificadores se conservan como referencias del borrador; los nombres, campos, rutas y aplicabilidad pueden cambiar durante la revisión.

El [plan de trabajo](../plan-trabajo-flujos.md) mantiene el estado de las 46 subfases de los ocho cortes y enlaza sus documentos. Al revisar un mensaje, se añadirá aquí la referencia a su flujo detallado en el [documento maestro de definiciones](../definiciones-flujos.md), evitando duplicar su definición. La incorporación inicial será manual; los mensajes de registro y las referencias al panel son antecedentes por revisar, no requisitos ya aprobados para esa etapa.

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
| `CTL-01` | Consigna interna validada | E2 Agent | Adaptador local | Interno | Propuesta local o del consenso validada según 4.4; límites respetados | Borrador |
| `RES-01` | Resultado de ejecución | E2 Agent | Plataforma/vecinos | MQTT | Acción ejecutada o rechazada | Borrador |
| `RES-02` | Residuo de operación | E2 Agent | Coordinación | MQTT | Medición posterior | Pendiente |
| `ALM-01` | Alarma técnica | E2 Agent | Plataforma/panel | MQTT/HTTPS | Falla detectada | Borrador |

## Cobertura y sentidos

El catálogo se ampliará al conversar cada subfase. El corte 4 cubre el control local independiente del consenso; el corte 5 cubre lo que la plataforma recibe, procesa, envía y muestra. Los cortes 6 y 7 definen participación y coordinación, y el corte 8 su recuperación.

Cada mensaje se describe en un sentido emisor → receptor. Un intercambio bidireccional enlaza los mensajes de ida y vuelta que correspondan, sin suponer una respuesta obligatoria a toda publicación. Los mensajes de retorno indicarán a qué solicitud o actuación responden cuando sea necesario.

La revisión distinguirá confirmación de transporte, procesamiento de aplicación y ejecución física. Las acciones manuales y llamadas internas necesarias se documentan en el flujo sin presentarlas como nuevos mensajes de red. Esta versión amplía la cobertura y corrige la dependencia de `CTL-01`; no añade contratos, endpoints ni campos JSON.

## Campos transversales

Los recorridos de transporte están descritos en [2.3 — Conexiones MQTT](../definiciones-flujos.md#flow-2-3). Su aprobación documental no aprueba automáticamente los mensajes y campos de este catálogo.

Las solicitudes e informes locales de configuración se describen en [2.4 — Configuración local](../definiciones-flujos.md#flow-2-4). Se realizan inicialmente mediante herramientas de terminal y registros; el canal remoto y la correspondencia definitiva con `CFG-01` y `CFG-02` quedan pendientes de revisión.

El [acuerdo de 2.5 — Configuración remota](../definiciones-flujos.md#flow-2-5) describe propuesta central, consulta HTTPS periódica y resultados administrativos diferenciados. Los intercambios todavía no están aprobados como contratos ni fijan endpoints nuevos.

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
