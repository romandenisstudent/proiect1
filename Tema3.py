meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ['guias'] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Ionut", "Costel", "Alex", "Robi", "Daniel"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
while studenti and comenzi and tavi:
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    tava = tavi.pop()
    istoric_comenzi.append(comanda)
    print(f"{student} a comandat {comanda}.")
    print("\nIstoricul comenzilor:")
    print(istoric_comenzi)
    from collections import Counter
comenzi_count = Counter(istoric_comenzi)
print("\nS-au comandat:", end=' ')
for produs in ['guias', 'ceafa', 'papanasi']:
    print(f"{comenzi_count[produs]} {produs}, ", end=' ')
print()
tavi_ramase = len(tavi)
print(f"Mai sunt {tavi_ramase} tavi.")
stocuri = {
    "papanasi": meniu.count('papanasi'),
    "ceafa": meniu.count('ceafa'),
    "guias": meniu.count('guias')
}
print(f"Mai este ceafa: {stocuri['ceafa'] > 0}.")
print(f"Mai sunt papanasi: {stocuri['papanasi'] > 0}.")
print(f"Mai sunt guias: {stocuri['guias'] > 0}.")
total_incasari = sum(comenzi[produs] * pret[1] for produs, pret in preturi if produs in comenzi)
print(f"\nCantina a încasat: {total_incasari} lei.")
produse_mici = [produs for produs in preturi if produs[1] <= 7]
print(f"Produse care costă cel mult 7 lei: {produse_mici}.")
