import pyjokes
import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser

conn = True

# Ecouter les commandes
def ecouter():
    if conn :
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Vous pouvez parler...")
            audio = r.listen(source)

            try:
                commande = ''
                while commande == '':
                    commande = r.recognize_google(audio, language="fr-FR")
                parler(f"Vous avez dit : {commande}")
                return commande.lower()
            except sr.UnknownValueError:
                parler("Désolé, je n'ai pas compris.")
                return ""
            except sr.RequestError:
                parler("Erreur de connexion.")
                return ""
    return input("Vous : ").lower()

# moteur vocale
def parler(msg):
    try:
        # Réinitialisation du moteur à chaque appel
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        
        # Sélectionner une voix (optionnel)
        voices = engine.getProperty('voices')
        # engine.setProperty('voice', voices[1].id)
        
        for voice in voices:
            if 'fr' in voice.name.lower() or 'french' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break

        print("Assistant :", msg)
        engine.say(msg)
        engine.runAndWait()

        # Libérer le moteur proprement
        engine.stop()
        del engine

    except Exception as e:
        print("Erreur dans parler() :", e)

# Blagues
def Blagues():
    return pyjokes.get_joke(language="fr", category="all")


#  Recherche wikipédia
wikipedia.set_lang("fr")
def recherche_wikipédia(sujet) :
    try:
        resultat = wikipedia.summary(sujet, sentences=3)
        parler(resultat)
    except wikipedia.exceptions.DisambiguationError as e:
        parler("Votre demande est ambiguë. Soyez plus précis.")
    except wikipedia.exceptions.PageError:
        parler("Je n'ai pas trouvé d'information sur ce sujet.")
    except Exception as e:
        # print("Erreur Wikipedia :", e)
        parler("Une erreur s'est produite lors de la recherche.")
        
def recherche_google(sujet) :
    url = f"https://www.google.com/search?q={sujet}"
    webbrowser.open(url)
    parler(f"Voici les résultats pour {sujet}.")