cuvant = 'onomatopee'
cuvant_de_ghicit = list(cuvant)

for index, litera in enumerate(cuvant):
    if litera != cuvant[0] and litera != cuvant[-1]:
        cuvant_de_ghicit[index] = '_'

print(cuvant_de_ghicit)

vieti = 7
litere_incercate = set()
while vieti != 0:
    literaUser = input("Alege o litera: ").lower()
    if not literaUser.isalpha() or len(literaUser) != 1:
        print("Sunt permise doar litere (una singura)")
        continue
    else:
        cuvant_de_ghicit = list(cuvant_de_ghicit)
        if literaUser in cuvant:
            for index, litera in enumerate(cuvant):
                if literaUser == litera:
                    cuvant_de_ghicit[index] = litera
            if '_' not in cuvant_de_ghicit:
                print(f"Ai castigat! Cuvantul era: {cuvant}")
                break
        else:
            if literaUser not in litere_incercate:
                vieti -= 1
                if vieti == 0:
                    print(f"Ai pierdut! Cuvantul era: {cuvant}")
                    break
                print(f"Mai ai {vieti} vieti")
            litere_incercate.add(literaUser)
        if len(list(litere_incercate)) != 0:
            print(f"Literele incercate sunt: {','.join(litere_incercate)}")
        cuvant_de_ghicit = ''.join(cuvant_de_ghicit)
        print(cuvant_de_ghicit)
