from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

envfile = Path(__file__).resolve().parent.parent.parent.parent / ".env"
load_dotenv(envfile)

client = genai.Client()

config = types.GenerateContentConfig(
    safety_settings=[
        types.SafetySetting(
            category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"
        ),
        types.SafetySetting(
            category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"
        ),
        types.SafetySetting(
            category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"
        ),
        types.SafetySetting(
            category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"
        ),
    ]
)

previous_id = None

while True:
    domanda = input('Tu (digita "esci" per uscire): ')

    if domanda.lower() == "esci":
        print("Arrivederci")
        break

    kwargs = {"model": "gemini-3.5-flash", "input": domanda, "config": config}

    if previous_id:
        kwargs["previous_interaction_id"] = previous_id

    interaction = client.interactions.create(**kwargs)

    print(interaction.output_text)

    previous_id = interaction.id
