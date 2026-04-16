# aegis-groupe5

Projet AEGIS - Groupe 5 . 

Membre A : Admin Sys Zineddine ZOUGARI

Membre B : Auditeur/Développeur Mohamed KAAROUD

Membre C : Rédacteur/Sécu Ali KADDOUR-DJEBBAR

## 🛡️ Journal de bord - Membre B (Mohamed)

En tant qu'**Auditeur**, ma mission a consisté à analyser les vulnérabilités de l'infrastructure TechSud, à automatiser le contrôle de conformité et à valider la mise en place des mesures de sécurité.

### ✅ Travail réalisé (Lundi - Mercredi) :

#### 1. Phase de Reconnaissance & Analyse
* **Scan Réseau Initial** : Utilisation de `nmap` pour cartographier les services exposés. Identification des ports critiques (FTP 21, HTTP 80) ayant permis l'incident de sécurité de TechSud.
* **Audit de Configuration** : Analyse des fichiers systèmes pour identifier les faiblesses (accès root autorisé, ports standards utilisés).

#### 2. Infrastructure & Collaboration
* **Déploiement VM** : Création et configuration du compte utilisateur `mohamed` sur le serveur de production.
* **Liaison GitHub** : Configuration de l'environnement Git local via **Personal Access Token (PAT)** et sécurisation des accès avec `credential.helper store` pour une collaboration fluide avec le Membre A (Zino) et le Membre C (Ali).
* **Arborescence** : Mise en place de la structure du dépôt (`/src`, `/docs`, `/scripts`).

#### 3. Automatisation de l'Audit (Python)
* **Développement de `src/audit_aegis.py`** : Création d'un script d'audit automatisé en Python 3.
* **Fonctionnalités clés** :
    * Inventaire temps réel des ports et services actifs.
    * Vérification automatique du statut du pare-feu (**UFW**).
    * Contrôle de conformité du durcissement SSH (**PermitRootLogin no**).
* **Reporting** : Génération automatique d'un rapport de conformité au format **JSON** (`audit_report.json`).

#### 4. Sécurisation & Validation (Hardening)
* **Contrôle du Pare-feu** : Validation de la politique de "moindre privilège" (Tout interdire sauf le port SSH sécurisé **2222**).
* **Tests de robustesse** : Nouveau scan `nmap` post-sécurisation pour confirmer la fermeture des ports critiques et l'efficacité du filtrage.
* **Surveillance** : Validation de l'installation et de l'activation de **Fail2ban** pour la protection contre les attaques par force brute.

### 📊 État de conformité actuel :
* **Pare-feu** : Actif (Seul port 2222/TCP ouvert)
* **Accès Root** : Désactivé



Autres membres : Sami REY;Wassim BENSEFIA;Messoud ABDELLAHI
