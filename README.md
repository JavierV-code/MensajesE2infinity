# Mensajes E2 Infinity

Repositorio de trabajo para definir, revisar y versionar los flujos de comunicación de la arquitectura E2 Infinity.

## Estado

**Documentación 0.3.14 — 4 de octubre de 2026.**

El contenido describe una propuesta de diseño. No constituye todavía un contrato definitivo de integración ni una especificación lista para producción. Las variables matemáticas del consenso deben conciliarse con la formulación y validación offline del algoritmo.

El [plan de trabajo](docs/plan-trabajo-flujos.md) conserva el seguimiento único de estados y dependencias de 46 subfases en ocho cortes. El [documento maestro de definiciones](docs/definiciones-flujos.md) es la fuente principal; el corte 2 incluye [conexiones MQTT](docs/definiciones-flujos.md#flow-2-3), [configuración local](docs/definiciones-flujos.md#flow-2-4), [configuración remota](docs/definiciones-flujos.md#flow-2-5), [coherencia](docs/definiciones-flujos.md#flow-2-6) y [arranque](docs/definiciones-flujos.md#flow-2-7). La incorporación inicial de identidad y archivos técnicos será manual; las preferencias autorizadas se consultarán periódicamente por HTTPS y se aplicarán localmente tras validación.

Los [diagramas editables del primer corte histórico](docs/diagramas/README.md) reúnen incorporación e identidad, conexiones MQTT y configuración local/remota en tres pestañas de Draw.io, con vistas PNG para revisión. Conservan la numeración de la versión anterior y disponen de una tabla de equivalencias.

## Objetivos

- Describir el funcionamiento local de cada nodo, la plataforma y sus intercambios completos.
- Separar configuración, supervisión, gestión energética local, coordinación distribuida y control físico.
- Definir quién emite, transporta, procesa y ejecuta cada mensaje.
- Mantener un catálogo trazable de mensajes y tópicos.
- Versionar estructuras JSON antes de implementarlas en los servicios.
- Documentar decisiones, dependencias, fallos y criterios de validación.
- Vincular posteriormente cada contrato con su implementación y sus pruebas.

## Principios de diseño

1. La plataforma no controla directamente los actuadores: el E2 Agent valida y ejecuta localmente.
2. Cada nodo ofrece únicamente la flexibilidad compatible con límites eléctricos, equipos, reservas y preferencias del usuario.
3. Headscale coordina la red privada; no implementa la lógica energética.
4. EMQX y Mosquitto transportan mensajes; no toman decisiones energéticas.
5. HTTPS se utiliza para incorporación y configuración administrativa; MQTT para operación, eventos y coordinación.
6. Una consigna vencida, duplicada o no autorizada no debe ejecutarse.
7. La pérdida de plataforma no elimina los límites ni la última configuración local válida.
8. La coordinación distribuida requiere conectividad entre vecinos.
9. El nodo puede gestionar sus equipos localmente con los recursos disponibles; participar en el consenso es una función adicional.
10. La plataforma distingue datos recibidos, configuración solicitada/aplicada y resultados físicos observados.

## Estructura

```text
docs/
├── definiciones-flujos.md  Fuente principal de las 46 subfases
├── arquitectura/       Mapa general y responsabilidades
├── decisiones/         Registros de decisiones de arquitectura (ADR)
├── diagramas/          Draw.io editable y vistas de revisión
├── flujos/             Índice, mapas y referencias históricas
├── mensajes/           Catálogo y tópicos MQTT
└── validacion/          Escenarios y criterios de prueba
schemas/                 Contratos JSON preliminares
```

## Organización actual

| Corte | Subfases | Propósito |
|---|---:|---|
| 1. Arquitectura y mapa completo de interacciones | 4 | Participantes, identidades, interfaces y recorridos |
| 2. Incorporación, configuración y arranque | 7 | Preparar, configurar y habilitar el nodo |
| 3. Equipos, mediciones y supervisión local | 5 | Conocer recursos, mediciones y salud |
| 4. Gestión energética y ejecución local | 7 | Decidir, actuar y medir sin depender del consenso |
| 5. Plataforma, información visible e intercambios con el nodo | 6 | Configuración, información y resultados para el usuario |
| 6. Preparación de la participación distribuida | 5 | Participación, disponibilidad, referencias y flexibilidad |
| 7. Consenso y coordinación entre vecinos | 6 | Iteraciones, convergencia y realimentación |
| 8. Fallos, recuperación y revisión completa | 6 | Continuidad y revisión de punta a punta |

La [equivalencia de los 34 puntos anteriores](docs/plan-trabajo-flujos.md#equivalencias-de-la-numeración-anterior) permite seguir usando las referencias históricas.

## Cómo trabajaremos

El orden, las dependencias y los estados se mantienen únicamente en el [plan de trabajo](docs/plan-trabajo-flujos.md). Conversaremos un subpunto por vez, lo documentaremos con la [plantilla común del documento maestro](docs/definiciones-flujos.md#plantilla-comun) y registraremos su confirmación antes de marcarlo como validado.

**1.1–1.4** quedaron validadas documentalmente el 3 de octubre de 2026 y los **cortes 2 y 3 completos** conservan sus acuerdos. [4.1 — Objetivos y preferencias locales](docs/definiciones-flujos.md#flow-4-1) inicia el corte 4 con límites técnicos, preferencias del usuario y prioridad de la utilidad local. El banco A/B/C y los servicios reales siguen sujetos a comprobación física. La siguiente conversación comenzará por **4.2 — Tarifas y datos económicos**. El bridge Mosquitto–EMQX sigue pendiente de implementación.

En [2.5](docs/definiciones-flujos.md#flow-2-5), las preferencias energéticas autorizadas se consultan automáticamente por HTTPS y se activan sin reinicio en el siguiente punto seguro de decisión. Las propuestas técnicas permanecen bajo comprobación y aplicación local del técnico según 2.4. Una consigna temporal usa su propio recorrido operativo.

Los mensajes, tópicos, diagramas y [JSON Schema existentes](schemas/README.md) son propuestas previas que se revisarán durante este proceso.

## Decisiones abiertas principales

- Funciones del nodo durante el arranque y operación local independiente.
- Prioridades entre decisiones locales y solicitudes autorizadas del usuario o la coordinación.
- Información y resultados visibles en la plataforma, permisos y conflictos de configuración.
- Condición exacta que inicia el consenso y función del backend en ese inicio.
- Variables y ley digital definitivas del algoritmo.
- Selección de vecinos y pesos locales.
- Criterio de convergencia, timeout y tratamiento de nodos perdidos.
- Confirmación de ejecución y mecanismo de redistribución del residuo.
- Autorización y vigencia de cambios remotos en parámetros económicos.

## Seguridad

Este repositorio es público. No deben subirse credenciales, claves de Headscale/Tailscale, contraseñas MQTT, certificados, archivos `.env`, direcciones privadas reales ni datos de usuarios.

## Licencia

No se ha definido una licencia de reutilización. Esta decisión debe ser acordada por el proyecto antes de publicar una licencia.
