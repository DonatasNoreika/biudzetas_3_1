from biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    veiksmas = int(input("1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - ataskaita\n4 - balansas\n0 - išeiti\n"))
    match veiksmas:
        case 1:
            biudzetas.prideti_pajamu_irasa()
        case 2:
            biudzetas.prideti_islaidu_irasa()
        case 3:
            biudzetas.gauti_ataskaita()
        case 4:
            biudzetas.gauti_balansa()
        case 0:
            break
        case _:
            print("Nera tokio pasirinkimo")
