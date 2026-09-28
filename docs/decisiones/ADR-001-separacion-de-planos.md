# ADR-001 — Separación de configuración, mensajería y control

- **Estado:** Propuesta
- **Fecha:** 2026-09-27

## Contexto

La arquitectura contiene incorporación administrativa, mensajería operativa, coordinación distribuida y actuación física. Mezclar estas responsabilidades dificulta la seguridad, la validación y la operación sin plataforma.

## Decisión propuesta

- HTTPS para incorporación y configuración administrativa.
- MQTT para eventos, telemetría, disponibilidad, coordinación y resultados.
- E2 Agent como responsable de validar y ejecutar decisiones locales.
- Headscale/Tailscale exclusivamente como infraestructura de red privada.
- OCPP, Modbus y MQTT local como interfaces de equipos.

## Consecuencias

- Un nodo puede rechazar una solicitud incompatible con sus límites.
- La plataforma no debe accionar directamente los equipos.
- La mensajería debe distinguir configuración deseada, configuración efectiva y operación temporal.
- Se necesitan contratos y permisos diferentes para cada plano.

## Validación requerida

- Revisar coherencia con la formulación definitiva del consenso.
- Confirmar el origen de las referencias energéticas.
- Ensayar pérdida de plataforma y pérdida de vecino.

