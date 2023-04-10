# Análise do código quebra_cabeca.py

### Autoteste de formatação em [markdown][tutor-md]

## **`O horoscopo`**
## Lê sua data de nascimento e lhe mosta uma mensagem de acordo com seu signo

>* [**06.png**][img-06]

O código da imagem 06 é uma função que remove acentos. A função é definida da seguinte maneira, usa-se a palavra-chave ` def `, seguida do nome da função, após é atribuido o parâmetro ` texto `. Em seguida a função importa a função [normalize] do módulo unecodedata, que retorna o formato normal para string unistr. Logo em sequência é criada uma variável `"texto"` que recebe "texto" formatado para string e em seguida retorna o texto sem os acentos. 

```python 
    def remover_acentos(texto):
        from unicodedata import normalize
        texto = str(texto)
        return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
```

>* [04.png][img-04]

O código abaixo, recebe um signo e retorna uma mensagem precedida do signo. Primeiro é definido o nome `horoscopo` e recebe o parâmetro `signo_formatado`, após é importado dois módulos python, [urllib.request] e ssl. Em seguida é criado uma variável `signo_formatado` que recebe a saída da função `remover_acentos(signo_desejado)` formatada para minúscula com a função interna `lower()` e a instrução seguinte concatena a variável "signo_formatado" à uma string de url e armazenada na variável `minha_url`.  Depois, a variável `requisicao` recebe, [-Esta parte é incerta-][urllib.request] o resultado da solicitação de acesso ao url. Inserindo os parametros _`url=str`_ e _`headers={}`_ no `urllib.request`.`Request`(url=str, headers={}), onde no código a str é substituida pelo `minha_url` e, adicionado os parâmetros ao headers, 'User-Agente':'Mozzilla/5.0'. Logo após uma serie de instruções para "alterar opções [ssl] internas". Depois das alterações, recebe mais instruçoes com relação a decodificação da página, e em seguida é criado variáveis `marcador_inicio` e `demarcador_final`, elas são usadas para demarcar qual parte será lida pelo programa. Após é criada uma variável com nome `inicio`, ela calcula qual a posição do `marcador_inicio` contando a quantidades de objetos dentro do "marcador_inicio" e a próxima variável é parecida mas, a variável `final` procura a posição do `marcador_final` em relação a posição retornada da variável `inicio`. E por fim a função retorna o __*signo*__ e em seguida uma mensagem retirada do intervalo entre o primeiro `marcador_inicio` e o primeiro `marcador_final` e removendo qualquer espaço com a função inerna `strip()`.

```python
def horoscopo(signo_desejado):
    import urllib.request, ssl
    signo_formatado = remover_acentos(signo_desejado).lower()
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

    requisicao = urllib.request.Request(
        url=minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    contexto_ssl = ssl.create_default_context()
    contexto_ssl.check_hostname = False
    contexto_ssl.verify_mode = ssl.CERT_NONE

    resposta = urllib.request.urlopen(requisicao, context=contexto_ssl)
    pagina = resposta.read().decode('utf-8')
    marcador_inicio = '<p class="text-pred">'
    marcador_final = '<a class="webshare-link">Compartilhar</a>'

    inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
    final = pagina.find(marcador_final, inicio)

    return signo_desejado + ': ' + pagina[inicio:final].strip()
```

>* [**03.png**][img-03]

O código a seguir é um separador de data, por exemplo se ele recebe 09042023 ele retorna separadamente ` a `
é 2023, ` m ` é 4 e ` d ` é 9.

```python
def separar_data(dma):
    a = dma % 10000
    dma //= 10000
    m = dma % 100
    dma //= 100
    d = dma
    return d, m, a
```

>* [**02.png**][img-02]

A função abaixo é a que descobre qual seu signo só com sua data de nascimento. Não é mágica, é uma sequencia de passos que a função segue para chegar. Dentro da função, primeiro checa se o parâmetro "mes" é igual a três, se sim o conteúdo identado abaixo desse ` if ` será executado e assim ele verifica até encontrar qual if corresponde a igualdade com "mes". Quando (`if`) passar no teste de igualdade, é executado a função `return` e mais uma vêz uma estrutura de comparação, agora testa se o parâmetro "dia" é menor que um determinado número, caso resulte em `True` retorna a primeira string, por exemplo "dia"= 9, e "mes"=3, retorna 'Peixes', mas, se caso contrário, "dia"=22, "22" é maior que 21 do comparador e então retornaria 'Áries'. 

```python
def signo(dia, mes):
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'
    if mes == 6:
        return 'Gêmeos' if dia < 22 else 'Câncer'
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sargitário'
    if mes == 12:
        return 'Sargitário' if dia < 22 else 'Capricórnio'
    if mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'
    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'
```

>* [**01.png**][img-01]

O código referente a imadem 01 é o da função `main()`, onde aqui que ocorre a entrada de dados direta com o usuário.

Primeiramente a função `main()` não vai parâmetros, e em seguida é onde ocorre a entrada de dados, onde quando executando, mostra a mensagem que está dentro do `input('mensagem')`, após o usuário digitar o que se pede, converte o dado recebido para inteiro e armazena na variável `nascimento`, depois este dado armazenado vai ser processado pela função `separar_data()`, e como esta função retorna três valores, foi criado três variáveis para atribuição, o terceiro valor é o "ano" mas como mais a frente só será processado "dia" e "mes" ele foi atribuido a uma variável qualquer. Seguindo, a variável "meu_signo" recebe uma string retornada do processamento de "dia" e "mes" pela função `signo()`, após a função `horoscopo(meu_signo)` processa a string armazenada na variável `meu_signo` e os dados retornados de `horoscopo(meu_signo)` serão atribuidos a variável ` horoscopo_de_hoje `. Por fim, a função interna ` print() `usada para saída de dados para o usuário, mostra na tela a mensagem guarda na variável `horoscopo_de_hoje` para o usuário.

```python
def main():
    # Entrada de dados
    nascimento = int(input('Digite sua data de nascimento no formato DDMMAAAA: '))

    # Processamento
    dia, mes, _ = separar_data(nascimento)
    meu_signo = signo(dia, mes)
    horoscopo_de_hoje = horoscopo(meu_signo)

    # Saída de dados
    print(horoscopo_de_hoje)
```

>* [**05.png**][img-05]

O código abaixo é o que inicializa o programa "chamando" uma função, no caso é a função `main()`.

É uma condição que verifica se está executando este módulo como o principal, e então executa seus identos.

```python   05.png
if __name__ == '__main__':
    main()
```

>    ! Agradeço qualquer comentário de correção, sei que tem muitos erros, mas espero consertar, então se não estou vendo, que esclareça para este pobre cego.

[img-01]:https://github.com/macielalves/python3/blob/main/SEM08/SEM08T3/img/01.png

[img-02]:https://github.com/macielalves/python3/blob/main/SEM08/SEM08T3/img/02.png

[img-03]:https://github.com/macielalves/python3/blob/main/SEM08/SEM08T3/img/03.png

[img-04]:https://github.com/macielalves/python3/blob/main/SEM08/SEM08T3/img/04.png

[img-05]:https://github.com/macielalves/python3/blob/main/SEM08/SEM08T3/img/05.png?raw=true

[img-06]:https://github.com/macielalves/python3/blob/main/SEM08/SEM08T3/img/06.png?raw=true

[normalize]:https://docs.python.org/pt-br/3/library/unicodedata.html?highlight=normalize

[urllib.request]:https://docs.python.org/pt-br/3/library/urllib.request.html#module-urllib.request

[ssl]:https://docs.python.org/pt-br/3/library/ssl.html?highlight=ssl#module-ssl

[tutor-md]:https://www.youtube.com/embed/vZaldeUg6D0