import random
import csv
import time

prenume = ["Andrei", "Georgescu", "Elena", "Gavrila", "Alex", "Rony", "Denis", "Ioana"]
nume_familie = ["Popescu", "Calin", "Lasconi", "Georgescu", "Radu", "Moldovan"]

judete_populatie = {
    "Bucuresti": 8.78, "Iasi": 3.60, "Prahova": 3.55, "Cluj": 3.40, "Timis": 3.28, "Constanta": 3.18,
    "Dolj": 3.07, "Bacau": 2.87, "Arges": 2.85, "Suceava": 2.96, "Brasov": 2.57, "Galati": 2.51,
    "Bihor": 2.69, "Neamt": 2.20, "Mures": 2.58, "Dambovita": 2.43, "Maramures": 2.24, "Buzau": 2.11,
    "Botosani": 1.93, "Valcea": 1.74, "Satu Mare": 1.54, "Mehedinti": 1.24, "Salaj": 1.05,
    "Giurgiu": 1.32, "Teleorman": 1.68, "Hunedoara": 1.84, "Covasna": 0.98, "Harghita": 1.42,
    "Alba": 1.52, "Arad": 1.90, "Braila": 1.49, "Bistrita-Nasaud": 1.29, "Calarasi": 1.33,
    "Caras-Severin": 1.38, "Ialomita": 1.21, "Ilfov": 2.27, "Olt": 1.82, "Tulcea": 0.99,
    "Vaslui": 1.85, "Gorj": 1.57, "Vrancea": 1.52
}


def generate_cnp():
    s = random.choice([1, 2])
    aa = random.randint(50, 99)
    ll = random.randint(1, 12)
    zz = random.randint(1, 28)
    jj = random.randint(1, 42)
    nnn = random.randint(100, 999)
    return f"{s}{aa:02}{ll:02}{zz:02}{jj:02}{nnn:03}{random.randint(0, 9)}"


def type_sex(cnp):
    return "Masculin" if cnp[0] in "1357" else "Feminin"


def generate_csv(filename="cnp_data.csv", num=1000000):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["CNP", "Nume", "Sex", "Judet", "Procentaj"])
        for _ in range(num):
            cnp = generate_cnp()
            nume = f"{random.choice(prenume)} {random.choice(nume_familie)}"
            sex = type_sex(cnp)
            judet = random.choice(list(judete_populatie.keys()))
            procentaj = judete_populatie[judet]
            writer.writerow([cnp, nume, sex, judet, f"{procentaj}%"])


generate_csv()


class HashTable:
    def __init__(self, size=100003):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None


hash_table = HashTable()

with open("cnp_data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        hash_table.insert(row[0], row[1:])

all_cnp_keys = [key for bucket in hash_table.table for key, _ in bucket]
sample_cnp = random.sample(all_cnp_keys, min(1000, len(all_cnp_keys)))

found_count = sum(1 for cnp in sample_cnp if hash_table.search(cnp))

print(f"CNP-uri gasite: {found_count} din 1000")


def search_single_cnp(cnp):
    start_time = time.time()
    result = hash_table.search(cnp)
    end_time = time.time()

    if result:
        nume, sex, judet, procentaj = result
        print(f"CNP: {cnp} gasit! Nume: {nume}, Sex: {sex}, Judet: {judet}, Procentaj: {procentaj}")
    else:
        print(f"CNP: {cnp} nu a fost gasit!")

    print(f"Timp de cautare: {end_time - start_time:.6f} secunde")


test_cnp = random.choice(all_cnp_keys)
search_single_cnp(test_cnp)
