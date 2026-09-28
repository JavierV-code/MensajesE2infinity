# Escenarios de validación de mensajes

| ID | Escenario | Resultado esperado | Estado |
|---|---|---|---|
| `VAL-01` | Tres nodos operativos | Intercambio autorizado y trazable | Pendiente |
| `VAL-02` | Configuración remota inválida | Rechazo sin perder última configuración válida | Pendiente |
| `VAL-03` | Mensaje duplicado | Procesamiento idempotente | Pendiente |
| `VAL-04` | Consigna vencida | No se ejecuta y se registra el motivo | Pendiente |
| `VAL-05` | Nodo sin flexibilidad | Publica cero o rechazo justificado | Pendiente |
| `VAL-06` | Pérdida de vecino durante consenso | Reconfiguración o aborto según regla acordada | Pendiente |
| `VAL-07` | Pérdida de plataforma | Continúan límites y control local seguro | Pendiente |
| `VAL-08` | Equipo no confirma actuación | Resultado fallido y residuo cuantificado | Pendiente |
| `VAL-09` | Reinicio de Raspberry | Recupera configuración y evita repetir órdenes vencidas | Pendiente |
| `VAL-10` | Convergencia numérica | Comparación contra óptimo centralizado offline | Pendiente |

