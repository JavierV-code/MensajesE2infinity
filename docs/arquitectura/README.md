# Mapa general de comunicaciones

Esta vista separa infraestructura de transporte, lógica energética y control físico.

```mermaid
flowchart LR
    U[Usuario / Frontend]
    CORE[Backend E2 Infinity]
    EMQX[EMQX central]
    HS[Headscale\nAdministración independiente]

    subgraph NODE[Raspberry / nodo E2]
        PANEL[Panel local]
        AGENT[E2 Agent\nConfiguración, flexibilidad, consenso y control]
        MOSQ[Mosquitto local]
        TS[Cliente Tailscale]
        ADP[Adaptadores\nOCPP / Modbus / MQTT]
    end

    NEIGHBOR[Agente vecino]
    ESP[ESP32 + TTL-RS485]
    EQUIP[Cargador, inversor, medidor y cargas]

    U <-->|HTTPS| CORE
    PANEL <-->|HTTPS / API local| AGENT
    CORE <-->|HTTPS: incorporación y configuración| AGENT
    CORE <-->|Mensajería operativa| EMQX
    EMQX <-->|Bridge MQTT selectivo| MOSQ
    MOSQ <-->|Mensajes locales| AGENT
    MOSQ <-->|Heartbeat y consenso| NEIGHBOR
    TS <-->|Registro y coordinación de red| HS
    AGENT -->|Gestión local del cliente| TS
    AGENT <-->|Comandos y estados| ADP
    ADP <-->|MQTT| ESP
    ESP <-->|Modbus RTU| EQUIP
    ADP <-->|OCPP / Modbus| EQUIP
```

## Responsabilidades

| Componente | Responsabilidad principal | No debe hacer |
|---|---|---|
| Backend E2 Infinity | Usuarios, organizaciones, instalaciones, configuración, referencias autorizadas, históricos y auditoría | Accionar directamente un dispositivo sin validación local |
| Headscale | Coordinar identidad y direccionamiento de la red privada | Calcular consignas o participar en el consenso energético |
| EMQX | Transportar mensajería central | Tomar decisiones energéticas |
| Mosquitto local | Intercambiar mensajes del nodo, vecinos y bridge | Sustituir la lógica del E2 Agent |
| E2 Agent | Calcular flexibilidad, participar en el consenso y aplicar control local | Exceder límites o reservas locales |
| ESP32 | Adquirir datos y actuar como pasarela de campo | Resolver la coordinación global |

## Canales

| Canal | Uso |
|---|---|
| HTTPS | Aprovisionamiento, asociación, configuración administrativa y consulta |
| MQTT | Eventos, telemetría, disponibilidad, coordinación y resultados |
| Tailscale/Headscale | Transporte privado y descubrimiento entre nodos autorizados |
| OCPP | Integración con cargadores |
| Modbus | Medidores, inversores y otros equipos de campo |

