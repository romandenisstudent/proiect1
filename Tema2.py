text="Știința prelucrării informațiilor (datelor) cu ajutorul computerelor se numește informatică. Istoria informaticii începe cu mult timp înainte ca disciplina modernă a informaticii să apară în secolul al XX-lea. Progresia, de la invenții mecanice și teorii matematice până la mașini și concepte moderne, a format un domeniu major academic și baza unei industrii uriașe la nivel mondial."
print(text)
mijlocul=len(text)//2
print(mijlocul)
prima_parte=text[:mijlocul]
print(prima_parte)
a_doua_parte=text[mijlocul:]
print(a_doua_parte)
text_majuscule=prima_parte.upper()
print(text_majuscule)
text_without_space=text.replace(" ","")
print(text_without_space)
inversarea_cuvintelor=text_without_space[::-1]
print(inversarea_cuvintelor)
text_fara_punctuatie=text.translate(str.maketrans('', '', string.punctuation))
print(text_fara_punctuatie)
text_majuscule=cuvant.capitalize()
print(text_majuscule)