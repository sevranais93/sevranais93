import json
import time

# Simulation de scan réel et formatage automatique pour le site
print("[*] Scan des concessions allemandes en cours...")

# Exemple de données récupérées et filtrées
opportunites = [
    {
        "id": int(time.time() * 1000) + 1,
        "model": "VW Tiguan 2.0 TDI R-Line DSG7",
        "annee": 2021,
        "co2": 142,
        "prixDE": 26400,
        "prixFR": 32800
    },
    {
        "id": int(time.time() * 1000) + 2,
        "model": "BMW 320d Touring M-Sport BVA8",
        "annee": 2020,
        "co2": 136,
        "prixDE": 27900,
        "prixFR": 33900
    },
    {
        "id": int(time.time() * 1000) + 3,
        "model": "Audi Q3 Sportback 35 TDI S-Line",
        "annee": 2022,
        "co2": 138,
        "prixDE": 31800,
        "prixFR": 37500
    },
    {
        "id": int(time.time() * 1000) + 4,
        "model": "Mercedes-Benz CLA 200 AMG Line",
        "annee": 2021,
        "co2": 131,
        "prixDE": 25900,
        "prixFR": 31200
    }
]

# Sauvegarde dans le fichier deals.json
with open("deals.json", "w", encoding="utf-8") as f:
    json.dump(opportunites, f, ensure_ascii=False, indent=2)

print("[✓] Succès : Le fichier 'deals.json' a été généré avec les opportunités du jour !")