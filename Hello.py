from dotenv import load_dotenv
import os
import openai
import requests

load_dotenv()  # laadt de variabelen uit .env

# Omgevingsvariabelen ophalen
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configureer OpenAI met de API sleutel
openai.api_key = OPENAI_API_KEY

def openai_summarize(question):
    try:
        response = openai.Completion.create(
          model="gpt-4",  # Zorg dat je het model naar GPT-4 update
          prompt=f"Geef een samenvatting in zoekwoorden van deze juridische vraag: '{question}'",
          temperature=0.5,
          max_tokens=60,
          n=1,
          stop=None,
          language="nl"
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Fout bij het aanroepen van OpenAI: {e}")
        return ""

def search_jurisprudence(keywords):
    # Dit is een placeholder. Implementeer je eigen logica om te zoeken in de rechtspraak database.
    print(f"Zoekresultaten voor: {keywords}")
    # Stel je voor dat dit de zoekresultaten retourneert.
    return "10 meest relevante zoekresultaten"

def main():
    user_question = input("Voer je juridische vraag in: ")
    keywords = openai_summarize(user_question)
    if keywords:
        print(f"Zoekwoorden gegenereerd door GPT-4: {keywords}")
        search_results = search_jurisprudence(keywords)
        print(search_results)
    else:
        print("Kon geen zoekwoorden genereren. Probeer het opnieuw.")

if __name__ == "__main__":
    main()