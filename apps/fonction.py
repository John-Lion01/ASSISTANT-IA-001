import time
import random

def Salutation() :
    slt = [
        "Bonjour." if int(time.strftime('%H')) < 12 else "Bonsoir.",
        "Salut.", 
        "Hello.",
    ]
    
    return random.choices(slt)[0]
    
def presenter() :
    opt = [
        "Je suis votre assistant IA.",
        "Je suis James, votre assistant.",
        "Je me nomme James et je suis votre assistant."
    ]
    
    return random.choices(opt)[0]