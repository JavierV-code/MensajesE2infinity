# Plantilla de documentación de una subfase

Utilizar esta plantilla al desarrollar una subfase del [plan de trabajo](../plan-trabajo-flujos.md). Completar los campos durante la conversación y registrar explícitamente lo pendiente.

- Identificador y nombre: [ID actual — nombre]
- Referencia anterior, si existe: [ID histórico y equivalencia]
- Estado documental: [pendiente / en conversación / borrador / validado / por revisar]
- Dependencias: [otras subfases o evidencia necesaria]
- Fecha y referencia del acuerdo: [confirmación explícita, cuando exista]
- Evidencia de implementación o ensayo: [enlace o no realizada]

## 1. Propósito, disparador y escenario

[Qué situación inicia el flujo, qué función cumple y qué resultado se espera. Indicar si el nodo actúa localmente, con plataforma o con vecinos.]

## 2. Participantes y responsabilidades

| Participante | Información que recibe | Qué procesa o decide | Información que envía |
|---|---|---|---|
| [Usuario, técnico, servicio o componente] | [Entrada] | [Responsabilidad] | [Salida] |

Indicar los recorridos aplicables: usuario/técnico–plataforma, técnico–nodo, interno del nodo, agente–equipos, plataforma–nodo, nodo–vecinos o infraestructura de red. En un intercambio con E2 Infinity describir ambos extremos y el resultado que puede consultar el usuario.

## 3. Condiciones previas y resultado esperado

- Condiciones previas: [identificación, permisos, configuración, recursos y datos necesarios]
- Dependencias de conectividad: [qué requiere el flujo y qué puede continuar sin cada conexión]
- Resultado esperado: [qué debe poder comprobarse]
- Información visible al usuario/técnico: [qué verá y cómo distinguirá solicitud, aplicación y resultado]

Las dependencias documentales no implican que toda operación local requiera plataforma o consenso.

## 4. Secuencia e interfaces

| Paso | Tipo de interacción | Origen | Destino | Acción o mensaje | Canal o medio | Resultado o respuesta esperada |
|---|---|---|---|---|---|---|
| [N] | [Manual / interna / entre servicios] | [Actor] | [Actor] | [Acción o ID] | [Archivo, llamada interna, HTTPS, MQTT, protocolo de equipo o pendiente] | [Resultado] |

Describir por separado los mensajes en cada dirección. Cada mensaje tiene emisor y receptor; un flujo bidireccional no obliga a que cada publicación tenga una respuesta. Editar archivos es una acción manual, no un mensaje de red.

Utilizar Draw.io para las interfaces y Mermaid para la secuencia detallada. Etiquetar las acciones manuales e internas; los mensajes de aplicación enlazan al catálogo. La doble flecha de un mapa de interfaces se descompone en los intercambios concretos de la secuencia.

## 5. Mensajes y contenido mínimo

| ID del catálogo | Propósito y disparador | Emisor → receptor | Canal | Información mínima | Respuesta o confirmación necesaria |
|---|---|---|---|---|---|
| [Existente o propuesto] | [Por qué y cuándo se genera] | [Sentido individual] | [Canal o pendiente] | [Contenido mínimo] | [Respuesta, publicación posterior, ninguna o pendiente] |

Enlazar el [catálogo común](../mensajes/catalogo-mensajes.md), que conserva una definición por mensaje. Registrar frecuencia, vigencia y correlación cuando se acuerden; evitar fijar JSON o endpoints prematuramente. Los campos del consenso requieren respaldo de la formulación matemática.

## 6. Confirmaciones, errores y recuperación

| Etapa, si corresponde | Qué demuestra | Evidencia y cómo se informa |
|---|---|---|
| Transporte | Recepción en el extremo de transporte correspondiente | [Confirmación o mecanismo acordado] |
| Procesamiento | Aceptación, rechazo o tratamiento por la aplicación | [Respuesta, motivo y referencia] |
| Ejecución | Actuación y resultado físico comprobable | [Estado del equipo y medición] |

[Tratar ausencia de respuesta, retraso, duplicados, pérdida de conexión y recuperación; indicar lo que no aplica o continúa pendiente.]

Revisar permisos, identidad, vigencia, orden y trazabilidad. Distinguir dato recibido, propuesta guardada, configuración aplicada y efecto medido. Indicar qué conserva el nodo y qué muestra la plataforma cuando falta una confirmación.

## 7. Acuerdos, pendientes y escenarios de validación

- Acuerdos confirmados: [definición, fecha y referencia]
- Preguntas abiertas: [pregunta y dependencia]
- Escenario normal: [condición, recorrido y resultado]
- Escenario de error o recuperación: [condición, recorrido y resultado]
- Evidencia técnica requerida: [simulación, software o ensayo físico, cuando corresponda]

La validación documental requiere confirmación explícita. La implementación y los ensayos tienen evidencia separada. Actualizar la fila del plan y sus enlaces al integrar el documento; conservar el alcance de acuerdos anteriores y registrar las ampliaciones pendientes.
