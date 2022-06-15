# PROJETO PARA BRINCAR DE PEDRA, PAPEL E TESOURA.
from multiprocessing import Event
import random; 
import PySimpleGUI as sg;

class PedraPapelTesoura:
    def __init__(self) -> None:

        self.encerrar = False
        self.opcoes = [
            'Pedra',
            'Tesoura',
            'Papel'
        ]

    def Iniciar(self): 

        #layout

        layout = [
            [sg.Text('Pedra, Papel ou Tesoura: ', size=(20,0))],
            [sg.Input(size=(18,0),key = 'ValorUsuario')],
            [sg.Button('Jogar'), sg.Button('Tentar Novamente'), sg.Button('Sair')],
            [sg.Output(size=(50,30))]
        ]

        #criar janela

        self.janela = sg.Window('Pedra, Papel ou Tesoura', layout=layout);
    
        #fazer alguma coisa com esses valores
        try:
            while True:
                #receber Valores
                self.eventos, self.valores = self.janela.Read();
                if self.eventos == 'Jogar':
                    self.opcoes_usuario = self.valores['ValorUsuario'];
                    while self.encerrar == False:
                        self.opcoes_pc = random.choice(self.opcoes);
                        if self.opcoes_usuario == 'Pedra' and self.opcoes_pc == 'Papel':
                            self.encerrar = True;
                            print("Que pena, você PERDEU")
                            print('Sua Jogada: ', self.opcoes_usuario)
                            print("Jogada da máquina: ", self.opcoes_pc)
                            break;
                        elif self.opcoes_usuario == 'Pedra' and self.opcoes_pc == 'Tesoura':
                            self.encerrar = True;
                            print("PARABÉNS! VOCÊ GANHOU.")
                            print('Sua Jogada: ', self.opcoes_usuario)
                            print("Jogada da máquina: ", self.opcoes_pc)
                            break;
                            
                        elif self.opcoes_usuario == 'Tesoura' and self.opcoes_pc == 'Papel':
                            self.encerrar = True;
                            print("PARABÉNS! VOCÊ GANHOU.")
                            print('Sua Jogada: ', self.opcoes_usuario)
                            print("Jogada da máquina: ", self.opcoes_pc)
                            break;
                            
                        elif self.opcoes_usuario == 'Tesoura' and self.opcoes_pc == 'Pedra':
                            self.encerrar = True;
                            print("Que pena, você PERDEU") 
                            print('Sua Jogada: ', self.opcoes_usuario)
                            print("Jogada da máquina: ", self.opcoes_pc)
                            break;
                            
                        elif self.opcoes_usuario == 'Papel' and self.opcoes_pc == 'Pedra':
                            self.encerrar = True;
                            print("PARABÉNS! VOCÊ GANHOU.") 
                            print('Sua Jogada: ', self.opcoes_usuario)
                            print("Jogada da máquina: ", self.opcoes_pc)
                            break;
                            
                        elif self.opcoes_usuario == 'Papel' and self.opcoes_pc == 'Tesoura':
                            self.encerrar = True;
                            print("Que pena, você PERDEU") 
                            print('Sua Jogada: ', self.opcoes_usuario)
                            print("Jogada da máquina: ", self.opcoes_pc)
                            break;
                            
                        elif self.opcoes_usuario == self.opcoes_pc:
                            print('EMPATE! Jogue novamente.')
                            print('Sua Jogada: ', self.opcoes_usuario)
                            print("Jogada da máquina: ", self.opcoes_pc)
                            break;
                        else:
                            self.encerrar = True;
                            print('Erro na Aplicação');      
                if self.eventos == 'Sair':
                    self.janela.close();
                    
                if self.eventos == 'Tentar Novamente':
                    self.janela.close();
                    self.encerrar = False;
                    iniciar.Iniciar();
        except:
            print('Erro na aplicação');
    

iniciar = PedraPapelTesoura();
iniciar.Iniciar();