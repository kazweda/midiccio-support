---
title: Privacy Policy - MiDiccio
description: Privacy Policy for the MiDiccio app. This document describes how personal data is collected, used, and protected.
lastUpdated: 2026-03-28
lang: en
updatedLabel: Last updated
---

# Privacy Policy

Last updated: March 28, 2026

## Overview

**MiDiccio** is a local, personal vocabulary learning app. This policy explains how the app collects, uses, and protects personal data.

---

## 1. Data Collection

### 1.1 Data Stored (User-provided and Automatically Recorded)

**Following the principle of minimal data collection, only the following data is stored:**

| Data Type | Collection Method | Purpose | Storage |
|-----------|-------------------|---------|---------|
| Learned terms and meanings | User input | Learning database management | Hive (local storage) |
| Notes | User input | Supplemental context for learning | Hive (local storage) |
| Tags | User input | Vocabulary categorization and search | Hive (local storage) |
| Metadata (creation time) | Automatically recorded | Learning history management | Hive (local storage) |

### 1.2 Data We Do Not Collect

We **do not collect** any of the following:

- ❌ Personally identifiable information such as name, address, or phone number
- ❌ User profile or authentication credentials (no local account/auth)
- ❌ Location information
- ❌ Device IDs (including analytics use)
- ❌ Learning behavior analytics (access frequency, study time, etc.)
- ❌ Cookies or tracking data

---

## 2. Data Storage

### 2.1 Local Storage (On Device)

**All learning data is stored in secure local storage on your device.**

- **Technical method**: Hive local persistence
- **Location**: iOS/Android app sandbox
- **Owner**: User (removed automatically when the app is uninstalled)

### 2.2 Cloud Sync

In the current version, cloud sync runs at the following timing:

| Platform | Destination | Status |
|----------|-------------|--------|
| iOS | iCloud (CloudKit) | ✅ Implemented (manual + lightweight auto-sync) |
| Android | Google Drive (AppData) | ✅ Implemented (manual + lightweight auto-sync) |

**Important**:
- When a cloud sync client is enabled, the app issues auto-sync requests on app resume, after save, and after delete
- Users can also run manual sync from settings using **Sync Now**
- Network transfer occurs only when a sync execution runs (to iCloud on iOS, Google Drive on Android)

### 2.3 Data Transfer Security

| Item | Method | Status |
|------|--------|--------|
| Local on-device storage | OS sandbox / device encryption / screen lock | ✅ Automatic (iOS/Android OS) |
| Android Device ↔ Google Drive | SSL/TLS | ✅ Google API |
| iOS Device ↔ iCloud | SSL/TLS | ✅ Apple CloudKit |

*: Locally stored data is protected at the OS level via sandboxing, device encryption, and lock-screen protections.
*: In the current version, cloud transfer occurs only when sync executes, either by manual sync or lightweight auto-sync triggers.

---

## 3. Data Sharing

### 3.1 Sharing with Third Parties

**We do not share personal data with third parties.**

Cloud sync transfers data only to the user's own iCloud or Google Drive. The developer has no access to any user data.

### 3.2 Cloud Provider Privacy Policies

When cloud sync is used, the following privacy policies also apply:

- **Google Drive (Android)**: [Google Privacy Policy](https://policies.google.com/privacy)
- **iCloud (iOS)**: [Apple Privacy Policy](https://www.apple.com/privacy/)

MiDiccio integrates these services as a licensee and does not perform secondary data usage.

---

## 4. User Rights

### 4.1 Right to Access Data

Users can access data by:

1. **In-app**: View data in learning screens
2. **Backup file**: Complete export available in JSON format
3. **Android cloud sync**: Check sync status and logs in settings
4. **iOS cloud sync**: Check sync status and logs in settings

### 4.2 Right to Delete Data (Right to be Forgotten)

Users can delete data by:

| Method | Scope | Timing |
|--------|-------|--------|
| Individual or bulk deletion in app | Selected data only | Immediate |
| Replace via backup restore | Replace local data with backup content | At restore time |
| Uninstall app | Delete all local data | At uninstall |
| Disconnect Google account on Android | Stops future cloud sync | Immediate |
| iOS cloud sync | In-app deletion propagates to iCloud deletion (at sync time) | At sync time |

### 4.3 Right to Data Portability

Users can export data anytime:

```
[Menu] → [Backup/Restore] → [Save Backup]
```

Export files are JSON and can be processed by other tools.

---

## 5. Security Measures

### 5.1 Currently Implemented

- ✅ **Local storage**: Hive with native sandboxing
- ✅ **Input validation**: Required UI form validation + Hive type consistency
- ✅ **Network communication**: SSL/TLS during iOS iCloud sync and Android Google Drive sync
- ✅ **Access control**: Accessible only by the device owner
- ✅ **Offline-first**: No server dependency

### 5.2 Encryption

The app does not implement its own application-level encryption. Data protection relies on the mechanisms provided by the OS and platform:

- **Local data**: OS sandbox, device encryption, and screen lock (iOS/Android OS)
- **Data in transit**: SSL/TLS (Apple CloudKit / Google Drive API)

### 5.3 Security Reporting

If you find a security vulnerability, please report it through a private channel instead of a public issue:

```
- Use “Report a vulnerability” from the repository Security tab (Private vulnerability reporting)
- See SECURITY.md for details
```

---

## 6. Compliance

### 6.1 Applicable Privacy Regulations

This app aligns with:

| Regulation | Scope | Status |
|------------|-------|--------|
| **Act on the Protection of Personal Information (Japan)** | Personal data collection/use | ✅ Aligned*1 |
| **GDPR** | EU users | ✅ Aligned*2 |
| **Child protection** | Users under 18 | ✅ No personally identifying information collected |

*1: Local-only storage and no third-party sharing minimize personal information handling.
*2: EU users are protected by the same privacy principles above.

### 6.2 Regions Covered by This Policy

- Japan
- Other countries/regions (including GDPR-covered regions)

---

## 7. Changes to This Privacy Policy

When this policy changes, updates are communicated as follows:

1. **Major changes**: In GitHub release notes and this document
2. **Minor updates**: In GitHub release notes

The update date is always reflected in “Last updated”.

---

## 8. Contact

If you have questions or concerns regarding privacy or security, please open an issue on GitHub:

```
GitHub Issues: https://github.com/kazweda/midiccio/issues
```

---

## 9. Policy Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-28 | Initial publication |
| 1.1 | 2026-03-13 | Added iCloud / Google Drive cloud sync descriptions |
| 1.2 | 2026-03-14 | Corrected implementation status descriptions |
| 1.3 | 2026-03-14 | Reflected iOS CloudKit manual sync completion |
| 1.4 | 2026-03-15 | Reflected lightweight auto-sync triggers (resume, save, delete) |
| 1.5 | 2026-03-20 | Removed Android Google Drive dedicated backup buttons; added bulk delete |
| 1.6 | 2026-03-20 | Simplified Section 3.1: removed exception list; clarified developer has no data access |
| 1.7 | 2026-03-28 | Updated Section 1.1 title to "Data Stored (locally)"; added Section 5.2 clarifying no app-level encryption (OS-dependent) |

---

**This policy will be updated as the app evolves.**
