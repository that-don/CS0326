from google import genai
import pandas as pd
import os


client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

df = pd.read_csv("auth.log.csv")
suspicious = df[df['message'].str.contains('Failed', case=False, na=False)].head(20)

log_text = suspicious.to_string()

prompt = f"analizza questi log SSH e identifica potenziali attacchi:\n{log_text}"
response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)


file = open("log-analysis.json", 'w')
file.write(response.text)
file.close()


# import os
# from google import genai
# from google.genai import types
# import pandas as pd

# client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# df = pd.read_csv("auth.log.csv")
# suspicious = df[
#     df['message'].str.contains('Failed', case=False, na=False)
# ].head(20)

# log_text = suspicious.to_string()

# # Prompt aggiornato per indicare la struttura JSON desiderata
# prompt = f"""Analizza questi log SSH e identifica potenziali attacchi.
# Restituisci l'analisi esclusivamente in formato JSON valido, con una struttura chiara (ad esempio una lista di oggetti con campi come 'timestamp', 'ip', 'dettagli_attacco', 'livello_rischio').

# Log da analizzare:
# {log_text}"""

# # Chiediamo al modello di restituire un JSON strutturato
# response = client.models.generate_content(
#     model='gemini-2.5-flash',
#     contents=prompt,
#     config=types.GenerateContentConfig(
#         response_mime_type='application/json',
#     ),
# )

# # Salviamo la risposta in un file .json
# output_filename = 'log-analysis.json'
# with open(output_filename, 'w', encoding='utf-8') as f:
#  # Se Gemini risponde con una stringa JSON valida, la scriviamo direttamente
#   f.write(response.text)

# print(f'File JSON salvato correttamente come {output_filename}')