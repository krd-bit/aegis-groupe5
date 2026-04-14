import os
import json

mes_ports = os.popen("ss -tunlp").read()
mes_services = os.popen("systemctl list-units --type=service --state=running --no-pager").read()

mon_audit = {
    "nom_du_projet": "AEGIS",
    "auteur": "Mohamed - Membre B",
    "ports_trouves": mes_ports,
    "services_trouves": mes_services
}

with open("audit_report.json", "w") as fichier:
    json.dump(mon_audit, fichier, indent=4)

print("Audit terminé : Rapport JSON généré.")
