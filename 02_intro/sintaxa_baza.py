salariu = 99
nivel_salariu = "Salariul este ok"
if salariu > 100 and (salariu_net := salariu - 30) and salariu_net > 70:
    nivel_salariu_net = "Salariu ok"
elif salariu <= 100 and (salariu_net := salariu - 20) and salariu_net < 60:
    nivel_salariu = "Salariu mic"

print(nivel_salariu)