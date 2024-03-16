import streamlit as st
import requests

def zoek_uitspraken(onderwerp, zaaknummer, ecli):
    base_url = "http://data.rechtspraak.nl/uitspraken/zoeken"
    params = {}
    
    if onderwerp:
        # Aangezien 'onderwerp' niet direct als parameter gebruikt kan worden,
        # zouden we andere gerelateerde parameters moeten overwegen.
        # Deze placeholder moet mogelijk aangepast worden naar een passende implementatie.
        # Voor deze demo, simuleren we een generieke zoekparameter.
        params['q'] = onderwerp  # Dit is een fictieve parameter voor demonstratiedoeleinden
    
    if zaaknummer:
        # Zoeken op zaaknummer, indien deze parameter beschikbaar en correct is
        params['zaaknummer'] = zaaknummer

    if ecli:
        # Direct zoeken op ECLI
        params['ecli'] = ecli

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

if st.button('Zoek'):
    with st.spinner('Zoeken...'):
        resultaten = zoek_uitspraken(onderwerp, zaaknummer, ecli)
        st.write(resultaten)  # Aanpassing nodig voor nette presentatie van resultaten