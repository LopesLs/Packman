from random import randint

class Mapa:
    
    def criar_mapa(self):
        self.mapa = [
         ['g', '', '', '', ''],
         ['', '', '', '', ''],
         ['', '', 'y', '', ''],
         ['', '', '', '', ''],
         ['', '', '', '', '']
        ]
        
        return self.mapa

    
class Pacman:
    
    def __init__(self, direcao, mapa):
        self.direcao = direcao
        self.atual = ''
        self.mapa = mapa
        self.start = True

        for z, k in enumerate(self.mapa):
            try:
                coluna = mapa[z].index('y')
            
            except:
                pass
            
            else:
                self.spawn_row = z
                self.spawn_column = coluna
                self.atual = [self.spawn_row, self.spawn_column]

    def andar(self):
        
        if self.direcao.lower() == 'frente':
            self.atual[0] = self.atual[0] - 1
             
        elif self.direcao.lower() == 'trás':
            self.atual[0] = self.atual[0] + 1

        elif self.direcao.lower() == 'direita':
            self.atual[1] = self.atual[1] + 1 
        
        elif self.direcao.lower() == 'esquerda':
            self.atual[1] = self.atual[1] - 1 
        
        else:
            print("Erro comum, as direções possíveis são; direita, esquerda, frente e trás.")
    
    def update_map(self, direcao):
        self.mapa[self.spawn_row].remove('y')
        self.mapa[self.spawn_row].insert(self.spawn_column, '')
        
        if direcao == 'frente' or direcao == 'trás':
    
            if self.mapa[self.atual[0]][self.atual[1]] == 'g':
                print('\nVocê morreu o fantasma te pegou!')
                self.start = False
                
            else:
                self.mapa[self.atual[0]].remove('')
                self.mapa[self.atual[0]].insert(self.atual[1], 'y')
        
        elif direcao == 'direita' or direcao == 'esquerda':
            if self.mapa[self.atual[0]][self.atual[1]] == 'g':
                print('\nVocê morreu o fantasma te pegou!')
                self.start = False
            
            else:
                self.mapa[self.atual[0]].remove('')
                self.mapa[self.atual[0]].insert(self.atual[1], 'y')


        else:
            pass
        
        if self.start == True:
            for y in self.mapa:
                print(y, end ='\n')
        else:
            pass
       

class Vantagens:
    def __init__(self, direcao, mapa):
        self.local = direcao
        self.mapa = mapa
        
    def gerar_moedas(self):
        self.spawn_row = randint(1, 5)
        self.spawn_column = randint(1, 5)
        
        if self.mapa[self.spawn_row][self.spawn_column] == '':
            self.mapa = self.mapa[self.spawn_row][self.spawn_column].replace('', 'coin')
        else:
            pass

    def gerar_powerup():
        pass

class Fantasma:
    
    def __init__(self, mapa):
        self.atual = ''
        self.mapa = mapa

        for z, k in enumerate(self.mapa):
            try:
                coluna = mapa[z].index('g')
            except:
                pass
            else:
                self.spawn_row = z
                self.spawn_column = coluna
                self.atual = [self.spawn_row, self.spawn_column]

    def andar(self):
        direcao = randint(1, 4)

        if direcao == 1:
            self.atual[0] = self.atual[0] - 1
        
        elif direcao == 2:
            self.atual[0] = self.atual[0] + 1
        
        elif direcao == 3:
            self.atual[1] = self.atual[1] + 1 

        elif direcao == 4:
            self.atual[1] = self.atual[1] - 1 
        
        else:
            pass
    
    def update_map(self):
        self.mapa[self.spawn_row].remove('g')
        self.mapa[self.spawn_row].insert(self.spawn_column, '')
        
        self.mapa[self.atual[0]].remove('')
        self.mapa[self.atual[0]].insert(self.atual[1], 'g')
        
map = Mapa()
map = map.criar_mapa()

for x in map:
        print(x, end = '\n')

while True:
    direcao = input('\nInforme qual direção deseja ir: ')

    player = Pacman(mapa = map, direcao = direcao)
    
    player.andar()
    
    player.update_map(direcao = direcao)
    
    if player.start == True:
        pass
    else:
        break
    
    npc = Fantasma(map)

    npc.andar()

    npc.update_map()