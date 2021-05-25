url = "ih5BXLexAIs0QzlGBkc5CsH5ZbBmGnfPXPCBF6kRJmV9"
apiKey = "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/d6ead7c1-f9de-4fe2-bd4f-8037b2a9ef3d"

from ibm_watson import TextToSpeechV1  # Allows us to work with TTS service
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator  # Allow authentication to TTS

# Setup Service
authenticator = IAMAuthenticator(apiKey)
# New TTS Service
tts = TextToSpeechV1(authenticator=authenticator)
# Set Service URL
tts.set_service_url(url)


