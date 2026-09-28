# Mensajes E2 Infinity

Repositorio de trabajo para definir, revisar y versionar los flujos de comunicación de la arquitectura E2 Infinity.

## Estado

**Documentación 0.2.2 — 27 de septiembre de 2026.**

El contenido describe una propuesta de diseño. No constituye todavía un contrato definitivo de integración ni una especificación lista para producción. Las variables matemáticas del consenso deben conciliarse con la formulación y validación offline del algoritmo.

El [plan tentativo de documentación de flujos](docs/plan-trabajo-flujos.md) organiza 34 subpuntos en seis bloques. Los puntos [1.5 — Conexión MQTT](docs/flujos/1.5-conexion-mqtt.md) y [1.6 — Configuración local](docs/flujos/1.6-configuracion-local.md) tienen acuerdos documentales registrados. La incorporación inicial será manual mediante archivos editados por el equipo técnico.

## Objetivos

- Separar configuración, supervisión, coordinación distribuida y control físico.
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

## Estructura

```text
docs/
├── arquitectura/       Mapa general y responsabilidades
├── decisiones/         Registros de decisiones de arquitectura (ADR)
├── flujos/             Secuencias de extremo a extremo
├── mensajes/           Catálogo y tópicos MQTT
└── validacion/          Escenarios y criterios de prueba
schemas/                 Contratos JSON preliminares
```

## Cómo trabajaremos

El orden, las dependencias y los estados se mantienen únicamente en el [plan de trabajo](docs/plan-trabajo-flujos.md). Conversaremos un subpunto por vez, lo documentaremos con la [plantilla común](docs/flujos/plantilla-flujo.md) y registraremos su confirmación antes de marcarlo como validado.

La siguiente conversación comienza en **1.7 — Configuración remota**. La validación documental se distingue de la evidencia de implementación y de los ensayos físicos.

Los mensajes, tópicos, diagramas y [JSON Schema existentes](schemas/README.md) son propuestas previas que se revisarán durante este proceso.

## Decisiones abiertas principales

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
