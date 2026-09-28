"""Generate the editable first-cut overview; validate independent orthogonal routes."""
from pathlib import Path
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parents[1] / 'docs' / 'diagramas'
ROOT = ET.Element('mxfile', host='app.diagrams.net', type='device', version='26.0.0')
INK, ACCENT, LIGHT = '#29383D', '#336976', '#EDF4F5'


def style(values):
    return ''.join(f'{key}={value};' for key, value in values.items())


class Page:
    def __init__(self, name, width, height):
        diagram = ET.SubElement(ROOT, 'diagram', id=f'corte1-{len(ROOT)}', name=name)
        model = ET.SubElement(diagram, 'mxGraphModel', grid='1', gridSize='10',
                              page='1', pageScale='1', pageWidth=str(width),
                              pageHeight=str(height), background='#FFFFFF')
        self.root = ET.SubElement(model, 'root')
        ET.SubElement(self.root, 'mxCell', id='0')
        ET.SubElement(self.root, 'mxCell', id='1', parent='0')
        self.name, self.rects, self.groups, self.routes = name, {}, set(), {}
        self.width, self.height = width, height

    def box(self, name, text, x, y, w, h, **options):
        props = dict(rounded=1, arcSize=7, html=1, whiteSpace='wrap',
                     fontFamily='Arial', fontSize=20, fontColor=INK,
                     fillColor='#FFFFFF', strokeColor='#A7B5B8', strokeWidth=1.5,
                     align='center', verticalAlign='middle', spacing=12)
        props.update(options)
        cell = ET.SubElement(self.root, 'mxCell', id=name, value=text, vertex='1',
                             parent='1', style=style(props))
        ET.SubElement(cell, 'mxGeometry', x=str(x), y=str(y), width=str(w),
                      height=str(h), attrib={'as': 'geometry'})
        self.rects[name] = (x, y, w, h)
        return name

    def text(self, name, value, x, y, w, h, size=18, **options):
        props = dict(fillColor='none', strokeColor='none', spacing=0,
                     align='left', fontSize=size)
        props.update(options)
        return self.box(name, value, x, y, w, h, **props)

    def group(self, name, x, y, w, h):
        self.box(name, '', x, y, w, h, fillColor='#F7F8F8', strokeColor='#D4DCDD')
        self.groups.add(name)

    def label(self, name, value, x, y, w, h=35):
        self.text(name, value, x, y, w, h, 17, fontColor=ACCENT, align='center')

    def edge(self, name, src, dst, pts, bidirectional=False, draft=False):
        def port(target, point):
            x, y, w, h = self.rects[target]
            px, py = (point[0] - x) / w, (point[1] - y) / h
            assert 0 <= px <= 1 and 0 <= py <= 1
            assert px in (0, 1) or py in (0, 1)
            return px, py
        sx, sy = port(src, pts[0])
        tx, ty = port(dst, pts[-1])
        for a, b, px, py in ((pts[0], pts[1], sx, sy), (pts[-1], pts[-2], tx, ty)):
            assert (px in (0, 1) and a[1] == b[1]) or (py in (0, 1) and a[0] == b[0])
        props = dict(edgeStyle='none', noEdgeStyle=1, rounded=0, curved=0,
                     html=1, strokeColor=ACCENT, strokeWidth=2,
                     startArrow='block' if bidirectional else 'none', endArrow='block',
                     startFill=1, endFill=1, exitX=sx, exitY=sy, entryX=tx, entryY=ty,
                     exitPerimeter=0, entryPerimeter=0, exitDx=0, exitDy=0,
                     entryDx=0, entryDy=0, dashed=1 if draft else 0, dashPattern='6 5')
        cell = ET.SubElement(self.root, 'mxCell', id=name, edge='1', parent='1',
                             source=src, target=dst, style=style(props))
        geom = ET.SubElement(cell, 'mxGeometry', relative='1', attrib={'as': 'geometry'})
        if len(pts) > 2:
            waypoints = ET.SubElement(geom, 'Array', attrib={'as': 'points'})
            for x, y in pts[1:-1]:
                ET.SubElement(waypoints, 'mxPoint', x=str(x), y=str(y))
        self.routes[name] = (src, dst, pts)

    def validate(self):
        def intersects(a, b, c, d):
            ah, ch = a[1] == b[1], c[1] == d[1]
            if ah == ch:
                q = 1 if ah else 0
                return a[q] == c[q] and max(min(a[1-q], b[1-q]), min(c[1-q], d[1-q])) <= min(max(a[1-q], b[1-q]), max(c[1-q], d[1-q]))
            if not ah:
                a, b, c, d = c, d, a, b
            return min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and min(c[1], d[1]) <= a[1] <= max(c[1], d[1])
        segments = []
        for name, (_, _, points) in self.routes.items():
            for a, b in zip(points, points[1:]):
                assert a != b and (a[0] == b[0] or a[1] == b[1]), name
                segments.append((name, a, b))
        for i, (name, a, b) in enumerate(segments):
            for other, c, d in segments[i+1:]:
                if other != name:
                    assert not intersects(a, b, c, d), f'{name} overlaps/crosses {other}'
            src, dst, _ = self.routes[name]
            for target, (x, y, w, h) in self.rects.items():
                if target in self.groups or target in (src, dst):
                    continue
                if a[1] == b[1]:
                    hit = y < a[1] < y+h and max(min(a[0], b[0]), x) < min(max(a[0], b[0]), x+w)
                else:
                    hit = x < a[0] < x+w and max(min(a[1], b[1]), y) < min(max(a[1], b[1]), y+h)
                assert not hit, f'{name} intersects text/block {target}'
        items = list(self.rects.items())
        for i, (name, (x, y, w, h)) in enumerate(items):
            assert 0 <= x and 0 <= y and x+w <= self.width and y+h <= self.height, name
            if name in self.groups:
                continue
            for other, (xx, yy, ww, hh) in items[i+1:]:
                if other in self.groups:
                    continue
                assert not (max(x, xx) < min(x+w, xx+ww) and max(y, yy) < min(y+h, yy+hh)), f'{name} overlaps {other}'
        for cell in self.root:
            keys = [part.split('=', 1)[0] for part in cell.get('style', '').split(';') if part]
            assert len(keys) == len(set(keys)), cell.get('id')
        print(f'PASS {self.name}: {len(self.routes)} orthogonal routes, separate paths, unique styles')


def heading(p, title, subtitle):
    p.text('title', '<b>E2 Infinity</b> · '+title, 60, 35, p.width-120, 55, 31)
    p.text('subtitle', subtitle, 60, 100, p.width-430, 44, 19)
    p.text('version', 'v01 · 27 septiembre 2026', p.width-360, 100, 300, 35, 17, align='right')


p = Page('01 · Incorporación e identidad', 1780, 1230)
heading(p, 'Primer corte · Incorporación', '1.1–1.4 · Responsabilidades, identidad, red privada y vinculación con plataforma')
p.group('network', 40, 180, 1700, 340)
p.text('network-title', '<b>1.3 · Registro de red privada</b> · acuerdo en conversación', 70, 200, 1600, 35, 22)
p.box('manual-network', '<b>Técnico</b><br><br>Configura nombre, dirección<br>de Headscale y clave compartida<br>reutilizable', 70, 270, 350, 180)
p.box('tailscale', '<b>Raspberry · cliente Tailscale</b><br><br>Solicita registro<br>Conserva su identidad de red<br>Establece conectividad privada', 650, 270, 390, 180, fillColor=LIGHT)
p.box('headscale', '<b>Headscale</b><br><br>Autoriza el registro<br>Entrega información de red<br>Administración independiente', 1310, 270, 390, 180)
p.edge('manual-ts', 'manual-network', 'tailscale', [(420,360),(650,360)])
p.label('manual-ts-label', 'Configuración manual', 435, 295, 200, 40)
p.edge('ts-hs', 'tailscale', 'headscale', [(1040,360),(1310,360)], bidirectional=True)
p.label('ts-hs-label', 'Registro / respuesta', 1070, 295, 210, 40)
p.text('network-check', 'Comprobación: registro aceptado + dirección privada + comunicación con otro equipo autorizado.', 70, 475, 1580, 30, 18)

p.group('platform', 40, 550, 1700, 480)
p.text('platform-title', '<b>1.4 · Vinculación con E2 Infinity</b> · cuenta por nodo acordada; recorrido por confirmar', 70, 570, 1600, 40, 21)
p.box('manual-platform', '<b>Técnico</b><br><br>Crea o selecciona instalación<br>Prepara cuenta técnica por nodo<br>Configura asociación local', 70, 750, 350, 180)
p.box('agent', '<b>Raspberry · E2 Agent</b><br><br>Solicita autenticación<br>Consulta instalación autorizada<br>Comprueba correspondencia', 650, 750, 390, 180, fillColor=LIGHT, dashed=1)
p.box('api', '<b>API E2 Infinity</b><br><br>Instalaciones y propietarios<br>Cuentas y asociaciones<br>Comprueba acceso', 1310, 750, 390, 180)
p.edge('manual-agent', 'manual-platform', 'agent', [(420,840),(650,840)], draft=True)
p.label('manual-agent-label', 'Parámetros locales', 435, 780, 200, 40)
p.edge('agent-api', 'agent', 'api', [(1040,840),(1310,840)], bidirectional=True, draft=True)
p.label('agent-api-label', 'HTTPS · acceso / consulta', 1060, 780, 230, 45)
p.edge('manual-api', 'manual-platform', 'api', [(245,750),(245,670),(1505,670),(1505,750)], draft=True)
p.label('manual-api-label', 'Alta administrativa manual · cuenta técnica e instalación', 700, 620, 650, 35)
p.text('platform-check', 'Resultado propuesto: autenticación, autorización y asociación comprobadas. MQTT se verifica en la vista 02.', 70, 960, 1590, 35, 18)

p.text('identity', '<b>1.2 · Identificación acordada</b><br>Nodo lógico → instalación → equipos; pertenencia al grupo eléctrico. Reemplazar la Raspberry conserva la identidad del nodo.', 65, 1060, 1650, 70, 19)
p.text('scope', '<b>1.1 · Responsabilidades acordadas</b> · técnico configura; servicios transportan; agente procesa y valida localmente.<br>Acuerdos de conversación: 1.1–1.3. Línea discontinua: recorrido pendiente de confirmación. Esquema documental, sin ejecución de servicios.', 65, 1145, 1650, 60, 17)
p.validate()

p = Page('02 · Conexiones MQTT', 1900, 1690)
heading(p, 'Primer corte · Conexiones MQTT', '1.5 · Recorridos validados documentalmente · bridge central pendiente de implementación')
p.box('backend', '<b>Backend E2 Infinity</b><br><br>Procesa información de plataforma<br>Publica mensajes autorizados', 800, 190, 400, 140)
p.box('central', '<b>EMQX central</b><br><br>Distribuye publicaciones<br>según suscripciones y permisos', 800, 440, 400, 140)
p.edge('backend-central', 'backend', 'central', [(1000,330),(1000,440)], bidirectional=True)
p.label('backend-central-label', 'MQTT', 1030, 365, 160, 35)
p.group('pi', 50, 720, 1220, 660)
p.text('pi-title', '<b>Raspberry A · servicios locales</b>', 80, 745, 630, 40, 23)
p.box('agent', '<b>E2 Agent</b><br><br>Publica y recibe<br>Procesa información del nodo', 100, 840, 380, 140, fillColor=LIGHT)
p.box('local', '<b>Mosquitto local</b><br><br>Broker del nodo<br>Bridges selectivos<br>Plataforma, vecinos y equipos', 800, 820, 400, 180, fillColor=LIGHT)
p.edge('agent-local', 'agent', 'local', [(480,910),(800,910)], bidirectional=True)
p.label('agent-local-label', 'Mensajes del agente', 495, 850, 290, 40)
p.edge('local-central', 'local', 'central', [(1000,820),(1000,580)], bidirectional=True)
p.label('local-central-label', 'Bridge MQTT selectivo<br><b>Pendiente de implementación</b>', 1030, 635, 580, 65)
p.box('neighbor-b', '<b>Raspberry B · Mosquitto</b><br><br>Agente vecino autorizado<br>Transporte por red privada', 1440, 760, 350, 140)
p.box('neighbor-c', '<b>Raspberry C · Mosquitto</b><br><br>Agente vecino autorizado<br>Transporte por red privada', 1440, 1060, 350, 140)
p.edge('local-b', 'local', 'neighbor-b', [(1200,860),(1440,860)], bidirectional=True)
p.label('local-b-label', 'Disponibilidad<br>y coordinación', 1215, 785, 210, 50)
p.edge('local-c', 'local', 'neighbor-c', [(1200,960),(1320,960),(1320,1130),(1440,1130)], bidirectional=True)
p.label('local-c-label', 'Disponibilidad y coordinación', 1350, 970, 490, 40)
p.box('devices', '<b>Equipos MQTT locales</b><br>Lecturas y respuestas<br>Detalle en el bloque 2', 800, 1170, 400, 120)
p.edge('local-devices', 'local', 'devices', [(1000,1000),(1000,1170)], bidirectional=True)
p.label('local-devices-label', 'MQTT local', 1020, 1060, 270, 40)
p.text('local-note', 'La selección de vecinos se define en 3.5. Headscale coordina la red; los clientes Tailscale transportan los datos.', 80, 1320, 1140, 40, 18)
p.text('auth', '<b>Accesos acordados</b><br>Credenciales propias por nodo en EMQX, independientes del acceso API. Identificador propio para cada cliente o bridge.', 70, 1420, 1740, 70, 19)
p.text('verification', '<b>Comprobaciones distintas</b> · conexión admitida → entrega al destinatario → procesamiento de aplicación.<br>Las flechas dobles muestran intercambio; no exigen dos conexiones duplicadas por par.', 70, 1515, 1740, 60, 18)
p.text('prototype', '<b>Prototipo actual:</b> el simulador publica directamente a EMQX y también a Mosquitto local; existen bridges entre brokers de Raspberry.<br>Este esquema representa el diseño objetivo. No fija tópicos, payloads ni variables definitivas del consenso.', 70, 1600, 1740, 60, 17)
p.validate()

p = Page('03 · Configuración local y remota', 2080, 1780)
heading(p, 'Primer corte · Configuración', '1.6 validado · 1.7 en borrador · acciones manuales e intercambios diferenciados')
p.group('local', 40, 180, 1990, 660)
p.text('local-title', '<b>1.6 · Configuración local</b> · validada documentalmente', 70, 200, 1860, 40, 23)
p.box('edit', '<b>Técnico</b><br><br>Edita archivos propuestos<br>Solicita comprobación', 70, 270, 300, 130)
p.box('validate', '<b>E2 Agent · comprobar</b><br><br>Estructura e identidades<br>Límites y coherencia', 500, 270, 350, 130, fillColor=LIGHT)
p.box('apply', '<b>Técnico + E2 Agent</b><br><br>Reinicio controlado<br>Aplicar propuesta comprobada', 990, 270, 360, 130, fillColor=LIGHT)
p.box('report', '<b>E2 Agent · verificar e informar</b><br><br>Configuración activa<br>Conexiones disponibles o pendientes', 1510, 270, 430, 130)
p.edge('edit-validate', 'edit', 'validate', [(370,335),(500,335)])
p.label('edit-validate-label', 'Local', 385, 285, 100, 30)
p.edge('validate-apply', 'validate', 'apply', [(850,335),(990,335)])
p.label('validate-apply-label', 'Válida', 860, 285, 120, 30)
p.edge('apply-report', 'apply', 'report', [(1350,335),(1510,335)])
p.label('apply-report-label', 'Resultado', 1360, 285, 130, 30)
p.box('reject', '<b>Propuesta rechazada</b><br><br>Campo y motivo del error<br>Corregir antes de aplicar', 500, 610, 350, 130)
p.box('previous', '<b>Conservar configuración</b><br><br>Última válida aplicada<br>Sin sustituirla por la propuesta', 70, 610, 300, 130)
p.box('active', '<b>Registro local</b><br><br>Identifica y conserva<br>la configuración aplicada', 990, 610, 360, 130)
p.edge('validate-reject', 'validate', 'reject', [(675,400),(675,610)])
p.label('validate-reject-label', 'Errores de configuración', 700, 465, 280, 55)
p.edge('reject-previous', 'reject', 'previous', [(500,675),(370,675)])
p.label('reject-previous-label', 'Conservar', 380, 625, 110, 30)
p.edge('apply-active', 'apply', 'active', [(1170,400),(1170,610)])
p.label('apply-active-label', 'Configuración efectiva', 1200, 465, 290, 55)
p.text('local-note', 'Una configuración válida puede tener conexiones pendientes. Primer arranque sin configuración válida: diagnóstico disponible, actuación energética sin habilitar.', 70, 770, 1870, 45, 18)

p.group('remote', 40, 890, 1990, 750)
p.text('remote-title', '<b>1.7 · Configuración remota</b><br>Borrador pendiente de validación', 70, 915, 760, 65, 22)
p.box('request', '<b>Usuario o técnico autorizado</b><br><br>Solicita un cambio<br>para su instalación', 70, 1060, 300, 160, dashed=1)
p.box('api', '<b>API E2 Infinity</b><br><br>Comprueba permisos<br>Guarda la propuesta<br>Entrega por HTTPS', 500, 1060, 350, 160, dashed=1)
p.box('fetch', '<b>E2 Agent</b><br><br>Consulta iniciada manualmente<br>Comprueba propuesta remota<br>Respeta condiciones locales', 990, 1060, 360, 160, fillColor=LIGHT, dashed=1)
p.box('remote-apply', '<b>Técnico + E2 Agent</b><br><br>Aplicación manual según 1.6<br>Resultado y conexiones<br>Configuración activa identificada', 1510, 1060, 430, 160, dashed=1)
p.edge('request-api', 'request', 'api', [(370,1140),(500,1140)], bidirectional=True, draft=True)
p.label('request-api-label', 'HTTPS', 385, 1085, 100, 30)
p.edge('fetch-api', 'fetch', 'api', [(990,1140),(850,1140)], bidirectional=True, draft=True)
p.label('fetch-api-label', 'HTTPS', 865, 1085, 110, 30)
p.edge('fetch-apply', 'fetch', 'remote-apply', [(1350,1140),(1510,1140)], draft=True)
p.label('fetch-apply-label', 'Válida', 1365, 1085, 125, 30)
p.edge('result-api', 'remote-apply', 'api', [(1725,1060),(1725,1000),(675,1000),(675,1060)], draft=True)
p.label('result-api-label', 'Resultado efectivo hacia la plataforma · interfaz objetivo', 900, 940, 670, 35)
p.box('remote-reject', '<b>Rechazo local</b><br>Informa motivo<br>Conserva configuración válida', 990, 1440, 360, 110, dashed=1)
p.edge('fetch-reject', 'fetch', 'remote-reject', [(1170,1220),(1170,1440)], draft=True)
p.label('fetch-reject-label', 'Identidad, parámetros<br>o condiciones incompatibles', 1200, 1280, 430, 70)
p.text('remote-note', 'Propuesta guardada ≠ comprobada ≠ aplicada. El formato y los permisos detallados se revisarán después; los contratos JSON siguen en borrador.', 70, 1580, 1870, 40, 18)
p.text('scope', 'Línea continua: recorrido validado. Discontinua: propuesta por validar. Las interacciones locales no implican mensajes de red.<br>La configuración administrativa y las consignas operativas tienen flujos diferentes; aquí se documenta la configuración.', 65, 1680, 1910, 65, 18)
p.validate()

OUT.mkdir(parents=True, exist_ok=True)
ET.indent(ROOT, space='  ')
path = OUT / 'Flujos_Primer_Corte_E2_Infinity_v01.drawio'
ET.ElementTree(ROOT).write(path, encoding='utf-8', xml_declaration=True)
print(path)
