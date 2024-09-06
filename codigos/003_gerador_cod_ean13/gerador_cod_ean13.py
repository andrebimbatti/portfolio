
quantidade = int(input('Digite a quantidade de codigos que você deseja gerar: '))
numero_cnpj = input('Digite seu cnpj ou cpf: ')
id_produto = 1001

if not len(numero_cnpj) < 5:
    for qtde in range(0,quantidade,1):
        par = 0
        m_par = 0
        impar = 0
        prefixo = '789'
        id_produto_str = str(id_produto)
        doze_digitos = prefixo + numero_cnpj[0:5] + id_produto_str

        # Código para geração do digito verificador
        i = 0
        for i in range(0,12,2):
            impar += int(doze_digitos[i])

        i=0
        for i in range(1,12,2):
            m_par += int(doze_digitos[i])

        par = m_par * 3
        soma_numeros = par + impar

        if soma_numeros % 10 ==0:
            multiplo = soma_numeros
        else:
            multiplo = (soma_numeros // 10 + 1) * 10

        subtracao = multiplo - soma_numeros

        if subtracao == 10:
            digito_verificador = 0
        else:
            digito_verificador = subtracao

        codigo_de_barras = doze_digitos + str(digito_verificador)
        print(f'{codigo_de_barras}')
        id_produto += 1
else:
    print('numero cnpj ou cpf invalido')