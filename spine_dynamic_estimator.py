"""
spine_dynamic_estimator.py

Ce module calcule le spine dynamique d'une flèche en bois à partir :
- du spine statique
- de la masse du fût
- du diamètre
- du matériau
- de la longueur de flèche
- du poids de la pointe
- du type d'empennage

Il compare aussi le spine dynamique obtenu avec un spine requis (fourni par l'archer).
"""

def calcul_spine_dynamique(
    spine_statique_lbs,
    poids_fut_grains,
    diametre_pouce,
    longueur_pouce,
    poids_pointe_grains,
    materiau,
    empennage,
    spine_requis_lbs
):
    # Correction de base selon matériau
    coef_materiau = {"pin": 0.95, "cedre": 1.0}
    coef_m = coef_materiau.get(materiau.lower(), 1.0)

    # Correction selon empennage
    empennage_offset = -2 if empennage == "plumes" else 0

    # Correction diamètre
    diam_correction = -5 if diametre_pouce == "5/16" else 0

    # Correction poids de pointe
    pointe_offset = -5 * ((poids_pointe_grains - 100) / 100)

    # Correction longueur
    ref_length = 28
    long_offset = -2 * (longueur_pouce - ref_length)

    # Correction masse du fût
    masse_offset = -0.015 * (poids_fut_grains - 350)

    # Calcul final
    spine_dynamique = (
        spine_statique_lbs * coef_m
        + empennage_offset
        + diam_correction
        + pointe_offset
        + long_offset
        + masse_offset
    )

    ecart = spine_dynamique - spine_requis_lbs

    return {
        "spine_dynamique_lbs": round(spine_dynamique, 1),
        "ecart_lbs": round(ecart, 1),
        "delta_interpretation": "Trop rigide" if ecart > 5 else "Trop souple" if ecart < -5 else "Correct"
    }
