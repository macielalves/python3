nivel_criminal = 0

if input("Telefonou para a vítima ?").strip() == 'S':
    nivel_criminal += 1
if input("Esteve no local do crime ?").strip() == 'S':
    nivel_criminal += 1
if input("Mora perto da vítima ?").strip() == 'S':
    nivel_criminal += 1
if input("Devia para a vítima ?").strip() == 'S':
    nivel_criminal += 1
if input("Já trabalhou com a vítima ?").strip() == 'S':
    nivel_criminal += 1


if nivel_criminal == 2:
    print("Suspeito")

elif nivel_criminal == 3 or nivel_criminal == 4:
    print("Cúmplice")

elif nivel_criminal == 5:
    print("Assassino")

else:
    print("Inocente")
