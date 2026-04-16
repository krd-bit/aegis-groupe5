import os
import json

mes_ports = os.popen("ss -tunlp").read()
mes_services = os.popen("systemctl list-units --type=service --state=running --no-pager").read()

status_ufw_brut = os.popen("sudo ufw status").read()
ufw_ok = "OUI" if "active" in status_ufw_brut.lower() else "NON / DANGER"

conf_ssh = os.popen("grep '^PermitRootLogin no' /etc/ssh/sshd_config").read()
ssh_root_ok = "SÉCURISÉ" if conf_ssh else "DANGER (Root autorisé)"

mon_audit = {
    "auteur": "Mohamed - Membre B",
    "date_audit": "Mercredi - Phase Sécurisation",
    "verifications_cles": {
        "pare_feu_actif": ufw_ok,
        "ssh_root_interdit": ssh_root_ok
    },
    "details": {
        "ports": mes_ports,
        "services": mes_services,
        "statut_ufw_complet": status_ufw_brut
    }
}

with open("src/audit_report.json", "w") as fichier:
    json.dump(mon_audit, fichier, indent=4)

print(f"Audit terminé ! Firewall: {ufw_ok} | SSH Root: {ssh_root_ok}")
