---
title: Politique de Confidentialité - MiDiccio
description: Politique de confidentialité de l'application MiDiccio. Ce document décrit comment les données personnelles sont collectées, utilisées et protégées.
lastUpdated: 2026-03-28
lang: fr
updatedLabel: Dernière mise à jour
---

# Politique de Confidentialité

Dernière mise à jour : 28 mars 2026

## Présentation

**MiDiccio** est une application locale et personnelle d'apprentissage du vocabulaire. Cette politique explique comment l'application collecte, utilise et protège les données personnelles.

---

## 1. Collecte de données

### 1.1 Données stockées (fournies par l'utilisateur et enregistrées automatiquement)

**Conformément au principe de collecte minimale de données, seules les données suivantes sont stockées :**

| Type de données | Méthode de collecte | Finalité | Stockage |
|-----------------|---------------------|----------|----------|
| Termes et significations appris | Saisie utilisateur | Gestion de la base de données d'apprentissage | Hive (stockage local) |
| Notes | Saisie utilisateur | Contexte supplémentaire pour l'apprentissage | Hive (stockage local) |
| Étiquettes | Saisie utilisateur | Catégorisation et recherche de vocabulaire | Hive (stockage local) |
| Métadonnées (date de création) | Enregistrement automatique | Gestion de l'historique d'apprentissage | Hive (stockage local) |

### 1.2 Données que nous ne collectons pas

Nous **ne collectons pas** les données suivantes :

- ❌ Informations d'identification personnelle telles que le nom, l'adresse ou le numéro de téléphone
- ❌ Profil utilisateur ou identifiants d'authentification (pas de compte local ni d'authentification)
- ❌ Informations de localisation
- ❌ Identifiants d'appareils (y compris à des fins analytiques)
- ❌ Analyse du comportement d'apprentissage (fréquence d'accès, temps d'étude, etc.)
- ❌ Cookies ou données de suivi

---

## 2. Stockage des données

### 2.1 Stockage local (sur l'appareil)

**Toutes les données d'apprentissage sont stockées dans le stockage local sécurisé de votre appareil.**

- **Méthode technique** : Persistance locale Hive
- **Emplacement** : Sandbox de l'application iOS/Android
- **Propriétaire** : L'utilisateur (supprimé automatiquement lors de la désinstallation de l'application)

### 2.2 Synchronisation cloud

Dans la version actuelle, la synchronisation cloud s'exécute aux moments suivants :

| Plateforme | Destination | État |
|------------|-------------|------|
| iOS | iCloud (CloudKit) | ✅ Implémenté (synchronisation manuelle + synchronisation automatique légère) |
| Android | Google Drive (AppData) | ✅ Implémenté (synchronisation manuelle + synchronisation automatique légère) |

**Important** :
- Lorsqu'un client de synchronisation cloud est activé, l'application envoie des demandes de synchronisation automatique à la reprise de l'application, après la sauvegarde et après la suppression
- Les utilisateurs peuvent également exécuter une synchronisation manuelle depuis les paramètres en utilisant **Synchroniser maintenant**
- Le transfert réseau s'effectue uniquement lors de l'exécution d'une synchronisation (vers iCloud sur iOS, Google Drive sur Android)

### 2.3 Sécurité du transfert de données

| Élément | Méthode | État |
|---------|---------|------|
| Stockage local sur l'appareil | Sandbox du SE / chiffrement de l'appareil / verrouillage d'écran | ✅ Automatique (SE iOS/Android) |
| Appareil Android ↔ Google Drive | SSL/TLS | ✅ API Google |
| Appareil iOS ↔ iCloud | SSL/TLS | ✅ Apple CloudKit |

*: Les données stockées localement sont protégées au niveau du SE par le sandbox, le chiffrement de l'appareil et les protections de l'écran de verrouillage.
*: Dans la version actuelle, le transfert cloud s'effectue uniquement lors de l'exécution de la synchronisation, que ce soit par synchronisation manuelle ou par déclencheurs de synchronisation automatique légère.

---

## 3. Partage de données

### 3.1 Partage avec des tiers

**Nous ne partageons pas de données personnelles avec des tiers.**

La synchronisation cloud transfère les données uniquement vers l'iCloud ou Google Drive de l'utilisateur. Le développeur n'a accès à aucune donnée utilisateur.

### 3.2 Politiques de confidentialité des fournisseurs cloud

Lors de l'utilisation de la synchronisation cloud, les politiques de confidentialité suivantes s'appliquent également :

- **Google Drive (Android)** : [Politique de confidentialité de Google](https://policies.google.com/privacy)
- **iCloud (iOS)** : [Politique de confidentialité d'Apple](https://www.apple.com/privacy/)

MiDiccio intègre ces services en tant que licencié et n'effectue pas d'utilisation secondaire des données.

---

## 4. Droits des utilisateurs

### 4.1 Droit d'accès aux données

Les utilisateurs peuvent accéder aux données de la manière suivante :

1. **Dans l'application** : Consulter les données dans les écrans d'apprentissage
2. **Fichier de sauvegarde** : Export complet disponible au format JSON
3. **Synchronisation cloud Android** : Vérifier l'état et les journaux de synchronisation dans les paramètres
4. **Synchronisation cloud iOS** : Vérifier l'état et les journaux de synchronisation dans les paramètres

### 4.2 Droit à l'effacement (Droit à l'oubli)

Les utilisateurs peuvent supprimer des données de la manière suivante :

| Méthode | Portée | Moment |
|---------|--------|--------|
| Suppression individuelle ou en masse dans l'application | Données sélectionnées uniquement | Immédiat |
| Remplacement via restauration de sauvegarde | Remplacer les données locales par le contenu de la sauvegarde | Au moment de la restauration |
| Désinstaller l'application | Supprimer toutes les données locales | À la désinstallation |
| Déconnecter le compte Google sur Android | Arrête la future synchronisation cloud | Immédiat |
| Synchronisation cloud iOS | La suppression dans l'application se propage à la suppression dans iCloud (au moment de la synchronisation) | Au moment de la synchronisation |

### 4.3 Droit à la portabilité des données

Les utilisateurs peuvent exporter des données à tout moment :

```
[Menu] → [Sauvegarde/Restauration] → [Enregistrer la sauvegarde]
```

Les fichiers d'export sont au format JSON et peuvent être traités par d'autres outils.

---

## 5. Mesures de sécurité

### 5.1 Actuellement implémentées

- ✅ **Stockage local** : Hive avec sandbox natif
- ✅ **Validation des entrées** : Validation des formulaires UI requise + cohérence des types Hive
- ✅ **Communication réseau** : SSL/TLS lors de la synchronisation iCloud iOS et Google Drive Android
- ✅ **Contrôle d'accès** : Accessible uniquement par le propriétaire de l'appareil
- ✅ **Offline-first** : Aucune dépendance serveur

### 5.2 Chiffrement

L'application n'implémente pas son propre chiffrement au niveau applicatif. La protection des données repose sur les mécanismes fournis par le SE et la plateforme :

- **Données locales** : Sandbox du SE, chiffrement de l'appareil et verrouillage d'écran (SE iOS/Android)
- **Données en transit** : SSL/TLS (Apple CloudKit / API Google Drive)

### 5.3 Signalement de vulnérabilités de sécurité

Si vous trouvez une vulnérabilité de sécurité, veuillez la signaler via un canal privé plutôt que par un issue public :

```
- Utilisez "Report a vulnerability" depuis l'onglet Security du dépôt (Signalement privé de vulnérabilités)
- Consultez SECURITY.md pour plus de détails
```

---

## 6. Conformité réglementaire

### 6.1 Réglementations de confidentialité applicables

Cette application est conforme à :

| Réglementation | Portée | État |
|----------------|--------|------|
| **Loi sur la protection des informations personnelles (Japon)** | Collecte/utilisation des données personnelles | ✅ Conforme*1 |
| **RGPD** | Utilisateurs de l'UE | ✅ Conforme*2 |
| **Protection des mineurs** | Utilisateurs de moins de 18 ans | ✅ Aucune information d'identification personnelle collectée |

*1 : Le stockage uniquement local et l'absence de partage avec des tiers minimisent le traitement des informations personnelles.
*2 : Les utilisateurs de l'UE sont protégés par les mêmes principes de confidentialité ci-dessus.

### 6.2 Régions couvertes par cette politique

- Japon
- Autres pays/régions (y compris les régions couvertes par le RGPD)

---

## 7. Modifications de cette politique de confidentialité

Lorsque cette politique change, les mises à jour sont communiquées comme suit :

1. **Modifications importantes** : Dans les notes de version GitHub et ce document
2. **Mises à jour mineures** : Dans les notes de version GitHub

La date de mise à jour est toujours reflétée dans « Dernière mise à jour ».

---

## 8. Contact

Si vous avez des questions ou des préoccupations concernant la confidentialité ou la sécurité, veuillez ouvrir un issue sur GitHub :

```
GitHub Issues: https://github.com/kazweda/midiccio/issues
```

---

## 9. Historique des versions de la politique

| Version | Date | Modifications |
|---------|------|---------------|
| 1.0 | 2026-02-28 | Publication initiale |
| 1.1 | 2026-03-13 | Ajout des descriptions de synchronisation cloud iCloud / Google Drive |
| 1.2 | 2026-03-14 | Correction des descriptions du statut d'implémentation |
| 1.3 | 2026-03-14 | Prise en compte de la finalisation de la synchronisation manuelle iOS CloudKit |
| 1.4 | 2026-03-15 | Prise en compte des déclencheurs de synchronisation automatique légère (reprise, sauvegarde, suppression) |
| 1.5 | 2026-03-20 | Suppression des boutons de sauvegarde dédiés Android Google Drive ; ajout de la suppression en masse |
| 1.6 | 2026-03-20 | Simplification de la Section 3.1 : suppression de la liste des exceptions ; clarification que le développeur n'a pas accès aux données |
| 1.7 | 2026-03-28 | Mise à jour du titre de la Section 1.1 en « Données stockées (localement) » ; ajout de la Section 5.2 clarifiant l'absence de chiffrement au niveau applicatif (dépendant du SE) |

---

**Cette politique sera mise à jour au fur et à mesure de l'évolution de l'application.**
