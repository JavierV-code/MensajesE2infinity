# Plantilla de documentación de un subpunto

Copiar esta plantilla al comenzar un subpunto del [plan de trabajo](../plan-trabajo-flujos.md). Los campos entre corchetes se completan durante la conversación; lo no resuelto queda explícitamente pendiente.

- Identificador y nombre: [ID — nombre]
- Estado documental: [pendiente / en conversación / borrador / validado / por revisar]
- Dependencias: [otros subpuntos o evidencia necesaria]
- Fecha y referencia del acuerdo: [solo si existe confirmación explícita]
- Evidencia de implementación o ensayo: [enlace o no realizada]

## 1. Propósito y escenario concreto

[Qué situación inicia el flujo y qué se busca resolver.]

## 2. Participantes y responsabilidades

| Participante | Recibe | Procesa o decide | Envía |
|---|---|---|---|
| [Actor] | [Información] | [Responsabilidad] | [Información] |

Indicar el recorrido aplicable: plataforma–nodo, nodo–vecinos, agente–equipos o infraestructura de red.

## 3. Condiciones previas y resultado esperado

- Condiciones previas: [identificación, configuración, disponibilidad u otras]
- Resultado esperado: [qué debe poder comprobarse al finalizar]

## 4. Secuencia de intercambios

| Paso | Tipo de interacción | Origen | Destino | Acción o mensaje | Resultado esperado |
|---|---|---|---|---|---|
| [N] | [Manual / interna / entre servicios] | [Actor] | [Actor] | [Acción o ID] | [Resultado] |

Añadir un diagrama de secuencia Mermaid basado en esta tabla cuando corresponda. Etiquetar las acciones manuales y las interacciones internas; la edición de archivos no es un mensaje de red. Las flechas de mensajes llevarán el ID del catálogo y una descripción breve.

## 5. Mensajes necesarios y contenido mínimo

| ID del catálogo | Propósito | Emisor | Receptor | Canal | Información mínima |
|---|---|---|---|---|---|
| [Existente o propuesto] | [Motivo] | [Actor] | [Actor] | [Canal o pendiente] | [Contenido sin fijar JSON prematuramente] |

Enlazar el [catálogo común](../mensajes/catalogo-mensajes.md) y registrar allí los mensajes para evitar definiciones divergentes. Los campos del consenso requieren respaldo de la formulación matemática.

## 6. Confirmaciones, errores y recuperación

[Qué respuesta se espera, cómo se comunica un rechazo y qué sucede ante ausencia, retraso, duplicado o pérdida de conexión. Indicar lo que no aplica o continúa pendiente.]

Revisar permisos, identidad, vigencia, orden de mensajes y registro de evidencias según el flujo. Distinguir recepción, aceptación y ejecución cuando sean relevantes.

## 7. Acuerdos, pendientes y ejemplos de validación

- Acuerdos confirmados: [definición, fecha y referencia]
- Preguntas abiertas: [pregunta y dependencia para resolverla]
- Ejemplo de operación normal: [condición y resultado esperado]
- Ejemplo de error o recuperación: [condición y resultado esperado]
- Evidencia técnica requerida: [simulación, prueba de software o ensayo físico, si aplica]

La aprobación documental requiere confirmación explícita del usuario. No implica que la implementación o las pruebas hayan sido realizadas. Actualizar el estado y el enlace en el plan al integrar el documento.
