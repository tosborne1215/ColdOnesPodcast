
import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path

ENABLE_GOOGLE = False
ENABLE_GOOGLE_CLOUD = False
ENABLE_HOUNDIFY = True
ENABLE_SPHINX = False
ENABLE_BING = False
ENABLE_IBM = False
ENABLE_WIT = False

SPHINX_OUT_FILE = "transcriptions/sphinx"
GOOGLE_OUT_FILE = "transcriptions/google"
GCLOUD_OUT_FILE = "transcriptions/gcloud"
WIT_OUT_FILE = "transcriptions/wit"
HOUNDIFY_OUT_FILE = "transcriptions/houndify"
BING_OUT_FILE = "transcriptions/bing"
IBM_OUT_FILE = "transcriptions/ibm"

files = ["parts/out{0}.wav".format(str(i).zfill(9)) for i in range(0, 107)]
for fname in files:
    AUDIO_FILE = path.join(path.dirname(
        path.realpath(__file__)), fname)

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    if ENABLE_SPHINX:
        try:
            txt = r.recognize_sphinx(audio)
            with open(SPHINX_OUT_FILE, 'w') as file:
                file.write("This file: " + fname)
                file.write(txt)
            print("Sphinx thinks you said " + txt)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

    # recognize speech using Google Speech Recognition
    if ENABLE_GOOGLE:
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            txt = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + txt)
            with open(GOOGLE_OUT_FILE) as file:
                file.write(txt)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))

    if ENABLE_GOOGLE_CLOUD:
        # recognize speech using Google Cloud Speech
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
        try:

            txt = r.recognize_google_cloud(
                audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            print("Google Cloud Speech thinks you said " + txt)
            with open(GCLOUD_OUT_FILE) as file:
                file.write(txt)
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Cloud Speech service; {0}".format(e))

    # recognize speech using Wit.ai
    # Wit.ai keys are 32-character uppercase alphanumeric strings
    if ENABLE_WIT:
        WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"

        try:
            txt = r.recognize_wit(audio, key=WIT_AI_KEY)
            print("Wit.ai thinks you said " + txt)
            with open(WIT_OUT_FILE) as file:
                file.write(txt)
        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Wit.ai service; {0}".format(e))

    # recognize speech using Microsoft Bing Voice Recognition
    # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    if ENABLE_BING:
        BING_KEY = "INSERT BING API KEY HERE"
        try:

            txt = r.recognize_bing(audio, key=BING_KEY)
            print("Microsoft Bing Voice Recognition thinks you said " + txt)
            with open(BING_OUT_FILE) as file:
                file.write(txt)
        except sr.UnknownValueError:
            print("Microsoft Bing Voice Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

    # recognize speech using Houndify
    if ENABLE_HOUNDIFY:
        # Houndify client IDs are Base64-encoded strings
        HOUNDIFY_CLIENT_ID = "Xy1DZkp2-K_Y8K4fczLdfA=="
        # Houndify client keys are Base64-encoded strings
        HOUNDIFY_CLIENT_KEY = "JFQr_eJsoXXRl5nrBe6NJWF3-80vPivLm9ls6lYUtyqY4hzOMeUEyUnq8B0Okc1FEFzpoYhp4vxl-AsWzsauNA=="
        try:
            txt = r.recognize_houndify(
                audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)
            print("Houndify thinks you said " + txt)
            with open(HOUNDIFY_OUT_FILE, 'w') as file:
                file.write("This file: " + fname)
                file.write(txt)
        except sr.UnknownValueError:
            print("Houndify could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Houndify service; {0}".format(e))

    # recognize speech using IBM Speech to Text
    if ENABLE_IBM:
        # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
        IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"
        # IBM Speech to Text passwords are mixed-case alphanumeric strings
        IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"
        try:
            txt = r.recognize_ibm(
                audio, username=IBM_USERNAME, password=IBM_PASSWORD)
            print("IBM Speech to Text thinks you said " + txt)
            with open(IBM_OUT_FILE) as file:
                file.write(txt)
        except sr.UnknownValueError:
            print("IBM Speech to Text could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from IBM Speech to Text service; {0}".format(e))
