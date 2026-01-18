from gtts import gTTS
import os
from gtts.lang import tts_langs

langs=tts_langs()

for code, name in langs.items():
    print(code,':',name)

again="yes"


while again != 'yes' and again != 'no':
    print('please input yes or no for the program to proceed ')
    again = input('yes/no? ').lower()

while again == "yes":
    lang1=input('select the language/accent to convert to: ')
    tosay = input('word to say: ')
    savefile=(input('The name of the file you want the file to be saved as- ')+'.mp3')
    tts=gTTS(text=tosay, lang=lang1)
    tts.save(savefile)

    os.startfile(savefile)

    again = input('again? (yes/no) ').lower()
    while again != 'yes' and again != 'no':
        print('please input yes or no')
        again = input('yes/no? ').lower()

print('thankyou')
