import random


cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

incercari_ramase = 6
litere_incercate = []

print("Salutare,haide sa jucam Spanzuratoarea!")
print("Cuvantul care trebuie ghicit arata asa: " + " ".join(progres))
print(f"Incercari ramase: {incercari_ramase}")

while "_" in progres and incercari_ramase > 0:

    litera = input("Introdu o litera: ").lower()


    if len(litera) != 1 or not litera.isalpha():
        print("Introdu doar o singura litera valida.")
        continue

    if litera in litere_incercate:
        print("Ai incercat deja aceasta litera. Introdu una noua.")
        continue

    litere_incercate.append(litera)
    if litera in cuvant_de_ghicit:
        for index, caracter in enumerate(cuvant_de_ghicit):
            if caracter == litera:
                progres[index] = litera
        print("Bravo! Litera se afla in cuvat.")

    else:
        incercari_ramase -= 1
        print("Upss, litera nu este in cuvant. Incercari ramase: " + str(incercari_ramase))

    print("Cuvantul care trebuie ghicit arata asa: " + " ".join(progres))
    print(f"Incercari ramase: {incercari_ramase}")

if "_" not in progres:
    print("URAAAA! Ai aflat cuvantul corect: " + cuvant_de_ghicit)

else:
    print("Ai pierdut :(! Cuvantul a fost: " + cuvant_de_ghicit)
