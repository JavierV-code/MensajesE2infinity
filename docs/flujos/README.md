# Flujos de extremo a extremo

## Dependencia general

```mermaid
flowchart TD
    A[Identidad local] --> B[Incorporación autorizada]
    B --> C[Configuración válida]
    C --> D[Equipos disponibles]
    D --> E[Flexibilidad calculada]
    E --> F[Coordinación / consenso]
    F --> G[Validación local]
    G --> H[Ejecución física]
    H --> I[Medición del resultado]
    I --> J[Corrección o cierre]
```

## Flujos que se documentarán

1. Aprovisionamiento del nodo.
2. Configuración local.
3. Configuración remota.
4. Registro y descubrimiento de equipos.
5. Heartbeat y disponibilidad.
6. Publicación de telemetría.
7. Inicio de coordinación energética.
8. Oferta de flexibilidad.
9. Iteraciones del consenso.
10. Detección de convergencia.
11. Validación y ejecución local.
12. Resultado y corrección del residuo.
13. Pérdida de un vecino.
14. Pérdida de plataforma.
15. Recuperación y resincronización.

