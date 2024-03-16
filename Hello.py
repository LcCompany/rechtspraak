import streamlit as st
import requests

def zoek_uitspraken(onderwerp, zaaknummer, ecli, sorteer):
    base_url = "http://data.rechtspraak.nl/uitspraken/zoeken"
    params = {}
    
    if onderwerp:
        params['q'] = onderwerp
    
    if zaaknummer:
        params['zaaknummer'] = zaaknummer

    if ecli:
        params['ecli'] = ecli

    if sorteer:
        params['sort'] = 'date desc'  # Aannemende dat 'date desc' de API zal instrueren om aflopend te sorteren op datum

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return response.text
    else:
        return "Geen resultaten gevonden of een fout opgetreden."

# Streamlit UI componenten
st.title('Zoeken naar rechterlijke uitspraken')
onderwerp = st.text_input("Onderwerp")
zaaknummer = st.text_input("Zaaknummer")
ecli = st.text_input("ECLI")
sorteer = st.checkbox("Sorteer op nieuwste uitspraken eerst", value=True)

if st.button('Zoek'):
    with st.spinner('Zoeken...'):
        resultaten = zoek_uitspraken(onderwerp, zaaknummer, ecli, sorteer)
        st.write(resultaten)  # Aanpassing nodig voor nette presentatie van resultaten