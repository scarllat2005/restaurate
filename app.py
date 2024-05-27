from Classes.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

restaurante_mexicano = Restaurante('Mexicano', 'comida')
restaurante_mexicano.receber_avaliacao('gui' ,5)

restaurante_Larissa = Restaurante ('Larrisinha', 'x-salada')
restaurante_Larissa.receber_avaliacao('Daniel' ,4.2)
restaurante_Larissa.receber_avaliacao('gaby',3.5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()