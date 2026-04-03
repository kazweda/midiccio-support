---
title: Informativa sulla Privacy - MiDiccio
description: Informativa sulla privacy dell'app MiDiccio. Questo documento descrive come vengono raccolti, utilizzati e protetti i dati personali.
lastUpdated: 2026-03-28
lang: it
updatedLabel: Ultimo aggiornamento
---

# Informativa sulla Privacy

Ultimo aggiornamento: 28 marzo 2026

## Panoramica

**MiDiccio** è un'app locale e personale per l'apprendimento del vocabolario. Questa informativa spiega come l'app raccoglie, utilizza e protegge i dati personali.

---

## 1. Raccolta dei dati

### 1.1 Dati memorizzati (forniti dall'utente e registrati automaticamente)

**Seguendo il principio di raccolta minima dei dati, vengono memorizzati solo i seguenti dati:**

| Tipo di dato | Metodo di raccolta | Finalità | Archiviazione |
|--------------|-------------------|----------|---------------|
| Termini e significati appresi | Input dell'utente | Gestione del database di apprendimento | Hive (archiviazione locale) |
| Note | Input dell'utente | Contesto supplementare per l'apprendimento | Hive (archiviazione locale) |
| Etichette | Input dell'utente | Categorizzazione e ricerca del vocabolario | Hive (archiviazione locale) |
| Metadati (data di creazione) | Registrazione automatica | Gestione della cronologia di apprendimento | Hive (archiviazione locale) |

### 1.2 Dati che non raccogliamo

**Non raccogliamo** nessuno dei seguenti dati:

- ❌ Informazioni di identificazione personale come nome, indirizzo o numero di telefono
- ❌ Profilo utente o credenziali di autenticazione (nessun account locale né autenticazione)
- ❌ Informazioni sulla posizione
- ❌ Identificatori del dispositivo (incluso l'uso analitico)
- ❌ Analisi del comportamento di apprendimento (frequenza di accesso, tempo di studio, ecc.)
- ❌ Cookie o dati di tracciamento

---

## 2. Archiviazione dei dati

### 2.1 Archiviazione locale (sul dispositivo)

**Tutti i dati di apprendimento sono memorizzati nell'archiviazione locale sicura del dispositivo.**

- **Metodo tecnico**: Persistenza locale Hive
- **Posizione**: Sandbox dell'app iOS/Android
- **Proprietario**: L'utente (rimosso automaticamente quando l'app viene disinstallata)

### 2.2 Sincronizzazione cloud

Nella versione attuale, la sincronizzazione cloud viene eseguita nei seguenti momenti:

| Piattaforma | Destinazione | Stato |
|-------------|--------------|-------|
| iOS | iCloud (CloudKit) | ✅ Implementato (sincronizzazione manuale + sincronizzazione automatica leggera) |
| Android | Google Drive (AppData) | ✅ Implementato (sincronizzazione manuale + sincronizzazione automatica leggera) |

**Importante**:
- Quando un client di sincronizzazione cloud è abilitato, l'app invia richieste di sincronizzazione automatica alla ripresa dell'app, dopo il salvataggio e dopo l'eliminazione
- Gli utenti possono anche eseguire la sincronizzazione manuale dalle impostazioni usando **Sincronizza ora**
- Il trasferimento di rete avviene solo quando viene eseguita una sincronizzazione (verso iCloud su iOS, Google Drive su Android)

### 2.3 Sicurezza nel trasferimento dei dati

| Elemento | Metodo | Stato |
|----------|--------|-------|
| Archiviazione locale sul dispositivo | Sandbox SO / crittografia dispositivo / blocco schermo | ✅ Automatico (SO iOS/Android) |
| Dispositivo Android ↔ Google Drive | SSL/TLS | ✅ API Google |
| Dispositivo iOS ↔ iCloud | SSL/TLS | ✅ Apple CloudKit |

*: I dati archiviati localmente sono protetti a livello SO tramite sandbox, crittografia del dispositivo e protezioni della schermata di blocco.
*: Nella versione attuale, il trasferimento cloud avviene solo quando viene eseguita la sincronizzazione, tramite sincronizzazione manuale o trigger di sincronizzazione automatica leggera.

---

## 3. Condivisione dei dati

### 3.1 Condivisione con terze parti

**Non condividiamo dati personali con terze parti.**

La sincronizzazione cloud trasferisce i dati solo all'iCloud o Google Drive dell'utente. Lo sviluppatore non ha accesso ad alcun dato dell'utente.

### 3.2 Politiche sulla privacy dei provider cloud

Quando si utilizza la sincronizzazione cloud, si applicano anche le seguenti politiche sulla privacy:

- **Google Drive (Android)**: [Informativa sulla privacy di Google](https://policies.google.com/privacy)
- **iCloud (iOS)**: [Informativa sulla privacy di Apple](https://www.apple.com/privacy/)

MiDiccio integra questi servizi come licenziatario e non effettua un utilizzo secondario dei dati.

---

## 4. Diritti dell'utente

### 4.1 Diritto di accesso ai dati

Gli utenti possono accedere ai dati nei seguenti modi:

1. **Nell'app**: Visualizzare i dati nelle schermate di apprendimento
2. **File di backup**: Esportazione completa disponibile in formato JSON
3. **Sincronizzazione cloud Android**: Controllare lo stato e i log di sincronizzazione nelle impostazioni
4. **Sincronizzazione cloud iOS**: Controllare lo stato e i log di sincronizzazione nelle impostazioni

### 4.2 Diritto alla cancellazione dei dati (Diritto all'oblio)

Gli utenti possono eliminare i dati nei seguenti modi:

| Metodo | Ambito | Tempistica |
|--------|--------|------------|
| Eliminazione individuale o in blocco nell'app | Solo i dati selezionati | Immediato |
| Sostituzione tramite ripristino del backup | Sostituire i dati locali con il contenuto del backup | Al momento del ripristino |
| Disinstallare l'app | Eliminare tutti i dati locali | Alla disinstallazione |
| Disconnettere l'account Google su Android | Interrompe la futura sincronizzazione cloud | Immediato |
| Sincronizzazione cloud iOS | L'eliminazione nell'app si propaga all'eliminazione su iCloud (al momento della sincronizzazione) | Al momento della sincronizzazione |

### 4.3 Diritto alla portabilità dei dati

Gli utenti possono esportare i dati in qualsiasi momento:

```
[Menu] → [Backup/Ripristino] → [Salva backup]
```

I file di esportazione sono in formato JSON e possono essere elaborati da altri strumenti.

---

## 5. Misure di sicurezza

### 5.1 Attualmente implementate

- ✅ **Archiviazione locale**: Hive con sandbox nativo
- ✅ **Validazione input**: Validazione dei moduli UI richiesta + coerenza dei tipi Hive
- ✅ **Comunicazione di rete**: SSL/TLS durante la sincronizzazione iCloud iOS e Google Drive Android
- ✅ **Controllo degli accessi**: Accessibile solo dal proprietario del dispositivo
- ✅ **Offline-first**: Nessuna dipendenza dal server

### 5.2 Crittografia

L'app non implementa la propria crittografia a livello applicativo. La protezione dei dati si basa sui meccanismi forniti dal SO e dalla piattaforma:

- **Dati locali**: Sandbox SO, crittografia del dispositivo e blocco schermo (SO iOS/Android)
- **Dati in transito**: SSL/TLS (Apple CloudKit / API Google Drive)

### 5.3 Segnalazione di vulnerabilità di sicurezza

Se si trova una vulnerabilità di sicurezza, segnalarla tramite un canale privato anziché un issue pubblico:

```
- Utilizzare "Report a vulnerability" dalla scheda Security del repository (Segnalazione privata di vulnerabilità)
- Consultare SECURITY.md per i dettagli
```

---

## 6. Conformità normativa

### 6.1 Normative sulla privacy applicabili

Questa app è allineata con:

| Normativa | Ambito | Stato |
|-----------|--------|-------|
| **Legge sulla protezione delle informazioni personali (Giappone)** | Raccolta/utilizzo dei dati personali | ✅ Allineato*1 |
| **GDPR** | Utenti UE | ✅ Allineato*2 |
| **Protezione dei minori** | Utenti sotto i 18 anni | ✅ Nessuna informazione di identificazione personale raccolta |

*1: L'archiviazione solo locale e l'assenza di condivisione con terze parti minimizzano il trattamento delle informazioni personali.
*2: Gli utenti UE sono protetti dagli stessi principi di privacy di cui sopra.

### 6.2 Regioni coperte da questa informativa

- Giappone
- Altri paesi/regioni (incluse le regioni coperte dal GDPR)

---

## 7. Modifiche a questa informativa sulla privacy

Quando questa informativa cambia, gli aggiornamenti vengono comunicati come segue:

1. **Modifiche importanti**: Nelle note di rilascio di GitHub e in questo documento
2. **Aggiornamenti minori**: Nelle note di rilascio di GitHub

La data di aggiornamento è sempre riflessa in "Ultimo aggiornamento".

---

## 8. Contatti

Per domande o dubbi sulla privacy o sulla sicurezza, aprire un issue su GitHub:

```
GitHub Issues: https://github.com/kazweda/midiccio/issues
```

---

## 9. Cronologia delle versioni dell'informativa

| Versione | Data | Modifiche |
|----------|------|-----------|
| 1.0 | 2026-02-28 | Pubblicazione iniziale |
| 1.1 | 2026-03-13 | Aggiunte descrizioni della sincronizzazione cloud iCloud / Google Drive |
| 1.2 | 2026-03-14 | Corrette le descrizioni dello stato di implementazione |
| 1.3 | 2026-03-14 | Riflessa il completamento della sincronizzazione manuale iOS CloudKit |
| 1.4 | 2026-03-15 | Riflessi i trigger di sincronizzazione automatica leggera (ripresa, salvataggio, eliminazione) |
| 1.5 | 2026-03-20 | Rimossi i pulsanti di backup dedicati Android Google Drive; aggiunta eliminazione in blocco |
| 1.6 | 2026-03-20 | Semplificata la Sezione 3.1: rimossa la lista delle eccezioni; chiarito che lo sviluppatore non ha accesso ai dati |
| 1.7 | 2026-03-28 | Aggiornato il titolo della Sezione 1.1 in "Dati memorizzati (localmente)"; aggiunta la Sezione 5.2 che chiarisce l'assenza di crittografia a livello applicativo (dipendente dal SO) |

---

**Questa informativa verrà aggiornata con l'evoluzione dell'app.**
