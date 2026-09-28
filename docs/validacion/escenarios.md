# Escenarios de validación de mensajes

Estos escenarios alimentan la revisión 8.6 del [plan de 46 subfases](../plan-trabajo-flujos.md). Son criterios por desarrollar y comprobar, no ensayos ejecutados. Se revisarán también desde cada flujo, con resultados observables en el nodo y en la plataforma cuando corresponda.

| ID | Escenario | Resultado esperado | Estado |
|---|---|---|---|
| `VAL-01` | Tres nodos operativos | Intercambio autorizado y trazable | Pendiente |
| `VAL-02` | Configuración remota inválida | Rechazo sin perder última configuración válida | Pendiente |
| `VAL-03` | Mensaje duplicado | Procesamiento idempotente | Pendiente |
| `VAL-04` | Consigna vencida | No se ejecuta y se registra el motivo | Pendiente |
| `VAL-05` | Nodo sin flexibilidad | Publica cero o rechazo justificado | Pendiente |
| `VAL-06` | Pérdida de vecino durante consenso | Reconfiguración o aborto según regla acordada | Pendiente |
| `VAL-07` | Pérdida de plataforma | Continúan límites y control local seguro | Pendiente |
| `VAL-08` | Equipo no confirma actuación | Informar ausencia de confirmación sin asumir éxito; medir el efecto y comunicar residuo si corresponde a coordinación | Pendiente |
| `VAL-09` | Reinicio de Raspberry | Recupera configuración y evita repetir órdenes vencidas | Pendiente |
| `VAL-10` | Convergencia numérica | Comparación contra óptimo centralizado offline | Pendiente |
| `VAL-11` | Gestión local con consenso deshabilitado y configuración válida | Lectura → decisión local → validación → orden → medición → registro, respetando preferencias y límites | Pendiente |
| `VAL-12` | Arranque con recursos locales y plataforma inaccesible | Identificar servicios disponibles y funciones locales habilitables según las reglas acordadas | Pendiente |
| `VAL-13` | Configuración guardada en plataforma sin aplicación manual | Mostrar propuesta pendiente y configuración realmente activa, sin anunciar el cambio como aplicado | Pendiente |
| `VAL-14` | API inaccesible con mensajería MQTT disponible | Distinguir fallo administrativo de mensajería; no declarar caído todo el nodo | Pendiente |
| `VAL-15` | EMQX inaccesible con comunicación local y vecinos disponibles | Conservar funciones locales y coordinación que puedan sostenerse; registrar tramo central pendiente | Pendiente |
| `VAL-16` | Headscale inaccesible | Comprobar conectividad efectiva entre clientes; distinguir pérdida de coordinación de red de pérdida del transporte existente | Pendiente |
| `VAL-17` | Reconexión con mensajes o resultados pendientes | Aplicar la política acordada de sincronización, distinguir históricos de datos actuales y evitar repetir órdenes antiguas | Pendiente |
| `VAL-18` | Lectura atrasada en la plataforma | Mostrar su fecha y calidad; no presentarla como medición actual | Pendiente |
| `VAL-19` | Recepción de transporte sin aceptación del agente o actuación del equipo | Mostrar el nivel de confirmación disponible, sin confundir entrega con ejecución física | Pendiente |
| `VAL-20` | Solicitud local y propuesta coordinada incompatibles | Resolver mediante las prioridades acordadas en 4.4 e informar qué fue aceptado, limitado o rechazado | Pendiente |

La cobertura incluye configuración (corte 2), equipos (3), gestión local (4), plataforma (5), participación y consenso (6–7) y recuperación (8). Al desarrollar cada escenario se enlazará su flujo y evidencia; los umbrales técnicos y las políticas pendientes se fijarán en sus subfases.
