# Tópicos MQTT — borrador

**Propuesta previa, no contrato aprobado.** Rutas, QoS, retain y el uso de MQTT para configuración se revisarán dentro del [plan de trabajo](../plan-trabajo-flujos.md). La primera etapa parte de configuración manual mediante archivos.

El [borrador de 2.5](../flujos/2.5-configuracion-remota.md) propone HTTPS para consulta y reporte administrativo. Las filas MQTT de configuración siguientes son alternativas previas pendientes de conciliación; no implican dos fuentes de configuración simultáneamente activas.

Convención propuesta:

```text
e2/v1/{ámbito}/{identificador}/{familia}/{recurso}
```

## Plataforma y nodos

| Familia | Tópico propuesto | Publica | Consume | QoS inicial | Retain |
|---|---|---|---|---:|---|
| Heartbeat | `e2/v1/nodes/{node_id}/status/heartbeat` | E2 Agent | Plataforma/vecinos autorizados | 0 | No |
| Disponibilidad | `e2/v1/nodes/{node_id}/status/availability` | E2 Agent | Plataforma/vecinos autorizados | 1 | Sí, con expiración |
| Telemetría | `e2/v1/nodes/{node_id}/telemetry/{device_id}` | E2 Agent | Plataforma | 0/1 | No |
| Configuración | `e2/v1/nodes/{node_id}/config/desired` | Plataforma | E2 Agent | 1 | Sí |
| Configuración efectiva | `e2/v1/nodes/{node_id}/config/reported` | E2 Agent | Plataforma | 1 | Sí |
| Objetivo | `e2/v1/groups/{group_id}/operations/{operation_id}/objective` | Origen autorizado | Participantes | 1 | No; usar expiración |
| Flexibilidad | `e2/v1/groups/{group_id}/operations/{operation_id}/flexibility/{node_id}` | E2 Agent | Vecinos/coordinación | 1 | No |
| Iteración | `e2/v1/groups/{group_id}/operations/{operation_id}/consensus/{node_id}` | E2 Agent | Vecinos | Por validar | No |
| Resultado | `e2/v1/groups/{group_id}/operations/{operation_id}/result/{node_id}` | E2 Agent | Plataforma/coordinación | 1 | No |
| Alarma | `e2/v1/nodes/{node_id}/alarms/{severity}` | E2 Agent | Plataforma | 1 | No |

## Reglas preliminares

- Una consigna operativa no debe permanecer retenida indefinidamente.
- Toda operación debe tener fecha de expiración y un identificador no reutilizable.
- Los consumidores deben soportar mensajes duplicados y fuera de orden.
- Las ACL deben limitar publicación y suscripción por nodo, grupo y función.
- El bridge Mosquitto–EMQX debe replicar solamente tópicos autorizados.
- No deben viajar secretos dentro del payload.
- QoS, expiración y frecuencia del consenso deben validarse experimentalmente.
