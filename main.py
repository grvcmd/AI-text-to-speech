url = "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/d6ead7c1-f9de-4fe2-bd4f-8037b2a9ef3d"
apiKey = "ih5BXLexAIs0QzlGBkc5CsH5ZbBmGnfPXPCBF6kRJmV9"

from ibm_watson import TextToSpeechV1  # Allows us to work with TTS service
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator  # Allow authentication to TTS

# Setup Service
authenticator = IAMAuthenticator(apiKey)
# New TTS Service
tts = TextToSpeechV1(authenticator=authenticator)
# Set Service URL
tts.set_service_url(url)

# Convert a string
with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize("Hello Creator - Ken. This is an audio file from the project titled AI text to speech.",
                         accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)

#  Convert from a file
with open('churchill.txt', 'r') as f:
    text = f.readlines()

text = [line.replace('\n', '') for line in text]
text = ''.join(str(line) for line in text)

with open('./churchill.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
