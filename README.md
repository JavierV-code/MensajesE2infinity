# Mensajes E2 Infinity

Repositorio de trabajo para definir, revisar y versionar los flujos de comunicación de la arquitectura E2 Infinity.

## Estado

**Documentación 0.3.0 — 28 de septiembre de 2026.**

El contenido describe una propuesta de diseño. No constituye todavía un contrato definitivo de integración ni una especificación lista para producción. Las variables matemáticas del consenso deben conciliarse con la formulación y validación offline del algoritmo.

El [plan tentativo de documentación de flujos](docs/plan-trabajo-flujos.md) organiza 46 subfases en ocho cortes. Los puntos [2.3 — Conexiones MQTT](docs/flujos/2.3-conexion-mqtt.md) y [2.4 — Configuración local](docs/flujos/2.4-configuracion-local.md) tienen acuerdos documentales registrados. La incorporación inicial será manual mediante archivos editados por el equipo técnico.

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
├── arquitectura/       Mapa general y responsabilidades
├── decisiones/         Registros de decisiones de arquitectura (ADR)
├── diagramas/          Draw.io editable y vistas de revisión
├── flujos/             Secuencias de extremo a extremo
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

El orden, las dependencias y los estados se mantienen únicamente en el [plan de trabajo](docs/plan-trabajo-flujos.md). Conversaremos un subpunto por vez, lo documentaremos con la [plantilla común](docs/flujos/plantilla-flujo.md) y registraremos su confirmación antes de marcarlo como validado.

La siguiente conversación comienza en **1.1 — Actores y responsabilidades**, consolidando lo ya conversado con el alcance ampliado de plataforma y funcionamiento local. La validación documental se distingue de la evidencia de implementación y de los ensayos físicos.

El [borrador de 2.5](docs/flujos/2.5-configuracion-remota.md) está en conversación: contempla proponer desde E2 Infinity cambios energéticos y técnicos autorizados del agente, con consulta HTTPS iniciada manualmente y aplicación conforme a 2.4. Distingue configuración persistente de consignas temporales; la automatización y la administración del sistema operativo quedan fuera de la etapa inicial.

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
