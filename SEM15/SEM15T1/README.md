# sem-15-t1


#### cidades.py

```py
def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )

    arquivo.close()
    return resultado


cidades = carrega_cidades()
print(cidades[:3] + cidades[-2:])
```

Código base utilizado na resolução dos exercícios.
Para que o código funcione é necessário que o arquivo cidades.csv esteja na pasta.