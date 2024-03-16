import streamlit as st
import requests

def zoek_uitspraken(onderwerp, zaaknummer, ecli):
    # Base URL voor het opvragen van uitspraakdocumenten
    base_url = "http://data.rechtspraak.nl/uitspraken/zoeken"
    params = {}
    
    if ecli:
        params['id'] = ecli  # Zoeken op ECLI
    if onderwerp:
        params['subject'] = onderwerp  # Zoeken op rechtsgebied, als benadering van 'onderwerp'
    if zaaknummer:
        params['psi:zaaknummer'] = zaaknummer  # Direct zoeken op zaaknummer indien beschikbaar

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return response.text
    else:
        return "Geen resultaten gevonden of een fout opgetreden."

# Streamlit UI
st.title('Zoeken naar rechterlijke uitspraken')

onderwerp = st.text_input("Onderwerp")
zaaknummer = st.text_input("Zaaknummer")
ecli = st.text_input("ECLI")

if st.button('Zoek'):
    with st.spinner('Zoeken...'):
        resultaten = zoek_uitspraken(onderwerp, zaaknummer, ecli)
        st.write(resultaten)  # Aanpassing nodig voor nette presentatie van resultaten