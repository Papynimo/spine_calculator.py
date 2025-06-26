import streamlit as st
from spine_dynamic_estimator import calcul_spine_dynamique

st.set_page_config(page_title="Spine dynamique d'une flèche bois", layout="centered")
st.title("🏹 Évaluation du spine dynamique d'une flèche bois")

st.markdown("Entrez les caractéristiques du fût de flèche :")

spine_statique = st.number_input("Spine statique (en livres)", min_value=20, max_value=80, value=40, step=1)
poids_fut = st.number_input("Poids du fût (en grains)", min_value=200, max_value=600, value=350, step=5)
diametre = st.selectbox("Diamètre du fût", ["5/16", "11/32"], index=0)
materiau = st.selectbox("Matériau", ["pin", "cedre"], index=0)

st.markdown("Caractéristiques de la flèche montée :")
allonge_archer = st.number_input("Allonge de l'archer (en pouces)", min_value=20.0, max_value=34.0, value=28.0, step=0.25)
longueur_fleche = allonge_archer + 1
poids_pointe = st.number_input("Poids de la pointe (en grains)", min_value=50, max_value=300, value=100, step=5)
empennage = st.selectbox("Type d'empennage", ["plumes", "vannes"], index=0)

spine_requis = st.number_input("Spine requis par l'archer (en livres)", min_value=20, max_value=80, value=40, step=1)

if st.button("📊 Calculer le spine dynamique"):
    resultat = calcul_spine_dynamique(
        spine_statique,
        poids_fut,
        diametre,
        longueur_fleche,
        poids_pointe,
        materiau,
        empennage,
        spine_requis
    )

    st.subheader("📋 Résultats")
    st.write(f"**Longueur totale de la flèche :** {longueur_fleche:.2f} pouces")
    st.write(f"**Spine dynamique estimé :** {resultat['spine_dynamique_lbs']} lbs")
    st.write(f"**Écart par rapport au spine requis :** {resultat['ecart_lbs']} lbs")

    interpretation = resultat['delta_interpretation']
    if interpretation == "Correct":
        st.success("✅ Spine adapté à l'archer.")
    elif interpretation == "Trop rigide":
        st.warning("⚠️ Flèche trop rigide. Risque de mauvais comportement.")
    else:
        st.error("❌ Flèche trop souple. Risque de surcharge ou imprécision.")

