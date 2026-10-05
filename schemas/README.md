# JSON Schema — propuestas previas

Los cuatro esquemas existentes son borradores de la primera iteración. No son contratos aprobados ni demuestran que sus campos o estados estén implementados.

Su revisión seguirá el [plan de documentación de flujos](../docs/plan-trabajo-flujos.md). Primero se acuerda el flujo y su contenido mínimo; después se ajusta el esquema correspondiente. Los campos y estados del consenso deben contrastarse con la formulación matemática validada.

La versión documental 0.4.0 organiza esta revisión en las siete subfases pendientes del [corte 9 — Contratos de mensajes por flujo](../docs/definiciones-flujos.md#cut-9). Los esquemas conservarán el enlace a su contrato y sus flujos; aprobar el recorrido no aprueba automáticamente su estructura.

| Esquema | Revisión prevista |
|---|---|
| [Envolvente común](common-envelope.schema.json) | [9.1](../docs/definiciones-flujos.md#flow-9-1): identificación y criterios transversales de mensajes |
| [Configuración](configuration.schema.json) | [9.2](../docs/definiciones-flujos.md#flow-9-2): configuración local y remota |
| [Heartbeat](heartbeat.schema.json) | [9.3](../docs/definiciones-flujos.md#flow-9-3): supervisión de presencia y disponibilidad |
| [Consenso](consensus-state.schema.json) | [9.6](../docs/definiciones-flujos.md#flow-9-6): intercambio iterativo, validez y convergencia |

Esta entrega documental no modifica los esquemas JSON ni sus interfaces.
