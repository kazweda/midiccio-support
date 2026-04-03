---
title: Política de Privacidad - MiDiccio
description: Política de privacidad de la aplicación MiDiccio. Este documento describe cómo se recopilan, utilizan y protegen los datos personales.
lastUpdated: 2026-03-28
lang: es
updatedLabel: Última actualización
---

# Política de Privacidad

Última actualización: 28 de marzo de 2026

## Descripción general

**MiDiccio** es una aplicación local y personal para el aprendizaje de vocabulario. Esta política explica cómo la aplicación recopila, utiliza y protege los datos personales.

---

## 1. Recopilación de datos

### 1.1 Datos almacenados (proporcionados por el usuario y registrados automáticamente)

**Siguiendo el principio de recopilación mínima de datos, solo se almacenan los siguientes datos:**

| Tipo de dato | Método de recopilación | Finalidad | Almacenamiento |
|--------------|------------------------|-----------|----------------|
| Términos y significados aprendidos | Entrada del usuario | Gestión de la base de datos de aprendizaje | Hive (almacenamiento local) |
| Notas | Entrada del usuario | Contexto suplementario para el aprendizaje | Hive (almacenamiento local) |
| Etiquetas | Entrada del usuario | Categorización y búsqueda de vocabulario | Hive (almacenamiento local) |
| Metadatos (fecha de creación) | Registro automático | Gestión del historial de aprendizaje | Hive (almacenamiento local) |

### 1.2 Datos que no recopilamos

**No recopilamos** ninguno de los siguientes datos:

- ❌ Información de identificación personal como nombre, dirección o número de teléfono
- ❌ Perfil de usuario o credenciales de autenticación (sin cuenta local ni autenticación)
- ❌ Información de ubicación
- ❌ Identificadores de dispositivo (incluido el uso analítico)
- ❌ Análisis del comportamiento de aprendizaje (frecuencia de acceso, tiempo de estudio, etc.)
- ❌ Cookies o datos de seguimiento

---

## 2. Almacenamiento de datos

### 2.1 Almacenamiento local (en el dispositivo)

**Todos los datos de aprendizaje se almacenan en el almacenamiento local seguro de su dispositivo.**

- **Método técnico**: Persistencia local con Hive
- **Ubicación**: Sandbox de la aplicación iOS/Android
- **Propietario**: El usuario (se elimina automáticamente al desinstalar la aplicación)

### 2.2 Sincronización en la nube

En la versión actual, la sincronización en la nube se ejecuta en los siguientes momentos:

| Plataforma | Destino | Estado |
|------------|---------|--------|
| iOS | iCloud (CloudKit) | ✅ Implementado (sincronización manual + sincronización automática ligera) |
| Android | Google Drive (AppData) | ✅ Implementado (sincronización manual + sincronización automática ligera) |

**Importante**:
- Cuando el cliente de sincronización en la nube está habilitado, la aplicación emite solicitudes de sincronización automática al reanudarse, después de guardar y después de eliminar
- Los usuarios también pueden ejecutar la sincronización manual desde los ajustes usando **Sincronizar ahora**
- La transferencia de datos solo ocurre cuando se ejecuta una sincronización (a iCloud en iOS, Google Drive en Android)

### 2.3 Seguridad en la transferencia de datos

| Elemento | Método | Estado |
|----------|--------|--------|
| Almacenamiento local en el dispositivo | Sandbox del SO / cifrado del dispositivo / bloqueo de pantalla | ✅ Automático (SO iOS/Android) |
| Dispositivo Android ↔ Google Drive | SSL/TLS | ✅ API de Google |
| Dispositivo iOS ↔ iCloud | SSL/TLS | ✅ Apple CloudKit |

*: Los datos almacenados localmente están protegidos a nivel del SO mediante sandbox, cifrado del dispositivo y protecciones de pantalla de bloqueo.
*: En la versión actual, la transferencia en la nube solo ocurre cuando se ejecuta la sincronización, ya sea por sincronización manual o disparadores de sincronización automática ligera.

---

## 3. Compartir datos

### 3.1 Compartir con terceros

**No compartimos datos personales con terceros.**

La sincronización en la nube transfiere datos únicamente al iCloud o Google Drive del propio usuario. El desarrollador no tiene acceso a ningún dato del usuario.

### 3.2 Políticas de privacidad del proveedor de nube

Cuando se utiliza la sincronización en la nube, también se aplican las siguientes políticas de privacidad:

- **Google Drive (Android)**: [Política de privacidad de Google](https://policies.google.com/privacy)
- **iCloud (iOS)**: [Política de privacidad de Apple](https://www.apple.com/privacy/)

MiDiccio integra estos servicios como licenciatario y no realiza un uso secundario de los datos.

---

## 4. Derechos del usuario

### 4.1 Derecho de acceso a los datos

Los usuarios pueden acceder a los datos de las siguientes maneras:

1. **En la aplicación**: Ver datos en las pantallas de aprendizaje
2. **Archivo de copia de seguridad**: Exportación completa disponible en formato JSON
3. **Sincronización en la nube Android**: Consultar el estado y los registros de sincronización en los ajustes
4. **Sincronización en la nube iOS**: Consultar el estado y los registros de sincronización en los ajustes

### 4.2 Derecho a eliminar datos (Derecho al olvido)

Los usuarios pueden eliminar datos de las siguientes maneras:

| Método | Alcance | Momento |
|--------|---------|---------|
| Eliminación individual o masiva en la aplicación | Solo datos seleccionados | Inmediato |
| Reemplazar mediante restauración de copia de seguridad | Reemplazar datos locales con el contenido de la copia de seguridad | En el momento de la restauración |
| Desinstalar la aplicación | Eliminar todos los datos locales | Al desinstalar |
| Desconectar la cuenta de Google en Android | Detiene la sincronización futura en la nube | Inmediato |
| Sincronización en la nube iOS | La eliminación en la aplicación se propaga a la eliminación en iCloud (en el momento de la sincronización) | En el momento de la sincronización |

### 4.3 Derecho a la portabilidad de datos

Los usuarios pueden exportar datos en cualquier momento:

```
[Menú] → [Copia de seguridad/Restaurar] → [Guardar copia de seguridad]
```

Los archivos de exportación están en formato JSON y pueden ser procesados por otras herramientas.

---

## 5. Medidas de seguridad

### 5.1 Actualmente implementadas

- ✅ **Almacenamiento local**: Hive con sandbox nativo
- ✅ **Validación de entrada**: Validación de formularios UI requerida + consistencia de tipos Hive
- ✅ **Comunicación de red**: SSL/TLS durante la sincronización de iCloud en iOS y Google Drive en Android
- ✅ **Control de acceso**: Accesible solo por el propietario del dispositivo
- ✅ **Offline-first**: Sin dependencia de servidor

### 5.2 Cifrado

La aplicación no implementa su propio cifrado a nivel de aplicación. La protección de datos depende de los mecanismos proporcionados por el SO y la plataforma:

- **Datos locales**: Sandbox del SO, cifrado del dispositivo y bloqueo de pantalla (SO iOS/Android)
- **Datos en tránsito**: SSL/TLS (Apple CloudKit / API de Google Drive)

### 5.3 Informe de vulnerabilidades de seguridad

Si encuentra una vulnerabilidad de seguridad, infórmela a través de un canal privado en lugar de un issue público:

```
- Utilice "Report a vulnerability" desde la pestaña Security del repositorio (Informe privado de vulnerabilidades)
- Consulte SECURITY.md para más detalles
```

---

## 6. Cumplimiento normativo

### 6.1 Normativas de privacidad aplicables

Esta aplicación se alinea con:

| Normativa | Ámbito | Estado |
|-----------|--------|--------|
| **Ley de Protección de Información Personal (Japón)** | Recopilación/uso de datos personales | ✅ Alineado*1 |
| **RGPD** | Usuarios de la UE | ✅ Alineado*2 |
| **Protección de menores** | Usuarios menores de 18 años | ✅ No se recopila información de identificación personal |

*1: El almacenamiento únicamente local y la ausencia de intercambio con terceros minimizan el manejo de información personal.
*2: Los usuarios de la UE están protegidos por los mismos principios de privacidad anteriores.

### 6.2 Regiones cubiertas por esta política

- Japón
- Otros países/regiones (incluidas las regiones cubiertas por el RGPD)

---

## 7. Cambios en esta política de privacidad

Cuando esta política cambie, las actualizaciones se comunicarán de la siguiente manera:

1. **Cambios importantes**: En las notas de versión de GitHub y en este documento
2. **Actualizaciones menores**: En las notas de versión de GitHub

La fecha de actualización siempre se refleja en "Última actualización".

---

## 8. Contacto

Si tiene preguntas o inquietudes sobre privacidad o seguridad, abra un issue en GitHub:

```
GitHub Issues: https://github.com/kazweda/midiccio/issues
```

---

## 9. Historial de versiones de la política

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | 2026-02-28 | Publicación inicial |
| 1.1 | 2026-03-13 | Se añadieron descripciones de sincronización en la nube con iCloud / Google Drive |
| 1.2 | 2026-03-14 | Se corrigieron las descripciones del estado de implementación |
| 1.3 | 2026-03-14 | Se reflejó la finalización de la sincronización manual de iOS CloudKit |
| 1.4 | 2026-03-15 | Se reflejaron los disparadores de sincronización automática ligera (reanudar, guardar, eliminar) |
| 1.5 | 2026-03-20 | Se eliminaron los botones de copia de seguridad dedicados de Android Google Drive; se añadió eliminación masiva |
| 1.6 | 2026-03-20 | Se simplificó la Sección 3.1: se eliminó la lista de excepciones; se aclaró que el desarrollador no tiene acceso a los datos |
| 1.7 | 2026-03-28 | Se actualizó el título de la Sección 1.1 a "Datos almacenados (localmente)"; se añadió la Sección 5.2 aclarando que no hay cifrado a nivel de aplicación (dependiente del SO) |

---

**Esta política se actualizará a medida que la aplicación evolucione.**
