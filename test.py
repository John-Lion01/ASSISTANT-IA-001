import pyttsx3

def parler(msg):
    try:
        # Réinitialisation du moteur à chaque appel
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        
        # Sélectionner une voix (optionnel)
        voices = engine.getProperty('voices')
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


i=1
while 1 :
    parler(f"test numéro {i}")
    msg = input("Vous : ")
    parler(msg)
    if msg == "pp" :
        break
    i += 1

# Fonction pour écouter (version texte)
def ecouter():
    return input("Vous : ").lower()

# Fonction principale
def assistant():
    parler("Bonjour, je suis votre assistant IA. Tapez vos commandes.")
    parler("Je suis dispo")

    while True:
        commande = ecouter()

        if "heure" in commande:
            heure = datetime.datetime.now().strftime("%H:%M")
            parler(f"Il est {heure}.")

        elif "date" in commande:
            date = datetime.datetime.now().strftime("%d %B %Y")
            parler(f"Aujourd'hui, nous sommes le {date}.")

        elif "wikipédia" in commande:
            parler("Que voulez-vous savoir ?")
            sujet = ecouter()
            try:
                resultat = wikipedia.summary(sujet, sentences=2, lang="fr")
                parler(resultat)
            except Exception:
                parler("Je n'ai pas trouvé d'information sur ce sujet.")

        elif "blague" in commande:
            try:
                blague = pyjokes.get_joke(language="fr", category="neutral")  # Pas encore dispo en français
                parler(blague)
            except:
                parler("Je n'ai pas de blague pour l'instant.")

        elif "stop" in commande or "quitte" in commande or "au revoir" in commande:
            parler("Au revoir, à bientôt !")
            break

        else:
            parler("Je n'ai pas compris. Veuillez réessayer.")

