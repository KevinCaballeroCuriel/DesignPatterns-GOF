class EnglishSpeaker:
        def responseToGreeting(self):
                return "Hello to you too!"
        def responseToFarewell(self):
                return "Goodbye my friend."
 
class Translator:
        _englishSpeaker = None
        _englishToSpanishPhrases = {
                "Hello to you too!": "¡Hola a ti también!",
                "Goodbye my friend.": "Adios amigo mío"
                }
                 
        def __init__(self, englishSpeaker):
                self._englishSpeaker = englishSpeaker
         
class SpanishSpeaker:
        _englishToSpanishTranslator = None
 
        def __init__(self, englishToSpanishTranslator):
                self._englishToSpanishTranslator = englishToSpanishTranslator
 
        def exchangeGreetings(self):
                print("¡Hola!")
                print( self._englishToSpanishTranslator._englishToSpanishPhrases[  self._englishToSpanishTranslator._englishSpeaker.responseToGreeting()  ] )
 
        def exchangeFarewell(self):
                print("¡Adios!")
                print( self._englishToSpanishTranslator._englishToSpanishPhrases[  self._englishToSpanishTranslator._englishSpeaker.responseToFarewell()  ] )
 
englishSpeaker = EnglishSpeaker()
 
englishToSpanishTranslator = Translator(englishSpeaker)
 
spanishSpeaker = SpanishSpeaker(englishToSpanishTranslator)
 
spanishSpeaker.exchangeGreetings()
spanishSpeaker.exchangeFarewell()
