#############CALCULADORA DE VALOR DE FRETE PROPORCIONAL####################################

# DESENVOLVIDA POR ANDRE BIMBATTI

# GITHUB: https://github.com/andrebimbatti

###########################################################################################


import os
from rich import print


class ValorFrete:

    def __init__(self):
        self.vl_total_compra = 0.0
        self.vl_custo_produto = 0.0
        self.vl_total_frete = 0.0

    def iniciar_interface(self):
        os.system('cls')
        print('*' * 125)
        print('''
█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀▄ █▀█ █▀█ ▄▀█   █▀▄ █▀▀   █▀▀ █▀█ █▀▀ ▀█▀ █▀▀   █▀█ █▀█ █▀█ █▀█ █▀█ █▀█ █▀▀ █ █▀█ █▄░█ ▄▀█ █░░
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▄▀ █▄█ █▀▄ █▀█   █▄▀ ██▄   █▀░ █▀▄ ██▄ ░█░ ██▄   █▀▀ █▀▄ █▄█ █▀▀ █▄█ █▀▄ █▄▄ █ █▄█ █░▀█ █▀█ █▄▄''')
        print('')
        print('*' * 125)
        print('')


    def calc_valor_custo(self):
        entrada = input('\nDigite o valor de custo unitário do produto que você comprou: R$ ')
        entrada = entrada.replace(',', '.')
        try:
            self.vl_custo_produto = float(entrada)
        except ValueError:
            return f'Por favor digite um numero válido'
    
    def calc_valor_compra(self):
        entrada = input('\nDigite o valor total dessa compra: R$ ')
        entrada = entrada.replace(',', '.')
        try:
            self.vl_total_compra = float(entrada)
        except ValueError:
            return f'Por favor digite um numero válido'
    
    def calc_valor_frete(self):
        entrada = input('\nDigite o valor total do frete dessa compra: R$ ')
        entrada = entrada.replace(',', '.')
        try:
            self.vl_total_frete = float(entrada)
        except ValueError:
            return f'Por favor digite um numero válido'
        
    def calc_frete_proporcional(self):
        calculo_frete = round((self.vl_custo_produto / self.vl_total_compra) * self.vl_total_frete, 2)
        calculo_frete = round(calculo_frete, 2)
        print(f'\nO valor proporcional do seu produto é: [green]R$ {calculo_frete:.2f}[/green]')
        opcao = input(f'\nDigite 4 se deseja sair ou digite qualquer outra tecla para continuar: ')
        if opcao == '4':
            print(f'\nObrigado por usar meu script')
        else:
            self.main()
      
    def main(self):
        self.iniciar_interface()
        self.calc_valor_custo()
        self.calc_valor_compra()
        self.calc_valor_frete()
        self.calc_frete_proporcional()

if __name__ == '__main__':
    iniciar_programa = ValorFrete()
    iniciar_programa.main()