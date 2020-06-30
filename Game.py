class play:

    def __init__(self, cords = [0, 0, 0, 0, 0, 0, 0, 0, 0]):
        self.__cords = cords
        pass

    def getValueCordByIndex(self, index):
        return self.__cords[index]

    def setValueCordByIndex(self, index, value):
        self.__cords[index] = value

    def getHorizontalWinner(self, index):
        return self.__cords[index] if self.__cords[index] == self.__cords[index + 1] and self.__cords[index] == self.__cords[index + 2] and self.__cords[index] != 0 else False

    def getVerticalWinner(self, index):
        return self.__cords[index] if self.__cords[index] == self.__cords[index + 3] and self.__cords[index] == self.__cords[index + 6] and self.__cords[index] != 0 else False

    def getWinner(self):
        if self.getHorizontalWinner(0) != False:
            return self.returnPrintDecisionByCord(self.getHorizontalWinner(0))
        elif self.getHorizontalWinner(3) != False:
            return self.returnPrintDecisionByCord(self.getHorizontalWinner(3))
        elif self.getHorizontalWinner(6) != False:
            return self.returnPrintDecisionByCord(self.getHorizontalWinner(6))
        elif self.getVerticalWinner(0) != False:
            return self.returnPrintDecisionByCord(self.getVerticalWinner(0))
        elif self.getVerticalWinner(1) != False:
            return self.returnPrintDecisionByCord(self.getVerticalWinner(1))
        elif self.getVerticalWinner(2) != False:
            return self.returnPrintDecisionByCord(self.getVerticalWinner(2))
        elif self.__cords[0] == self.__cords[4] and self.__cords[0] == self.__cords[8] and self.__cords[0] != 0:
            return self.returnPrintDecisionByCord(self.__cords[0])
        elif self.__cords[2] == self.__cords[4] and self.__cords[2] == self.__cords[6] and self.__cords[2] != 0:
            return self.returnPrintDecisionByCord(self.__cords[2])
        else:
            return False

    def returnIfContainValue(self, index):
        return True if self.__cords[index] != 0 else False

    def returnDraw(self):
        return True if self.__cords.count(0) == 0 else False

    def returnPrintDecisionByCord(self, cord):
        return 'X' if cord == 1 else '' + 'O' if cord == 2 else '' + ' ' if cord == 0 else ''

    def printTable(self):
        print(self.returnPrintDecisionByCord(self.__cords[0]) + '|' + self.returnPrintDecisionByCord(self.__cords[1]) + '|' + self.returnPrintDecisionByCord(self.__cords[2]))
        print(self.returnPrintDecisionByCord(self.__cords[3]) + '|' + self.returnPrintDecisionByCord(self.__cords[4]) + '|' + self.returnPrintDecisionByCord(self.__cords[5]))
        print(self.returnPrintDecisionByCord(self.__cords[6]) + '|' + self.returnPrintDecisionByCord(self.__cords[7]) + '|' + self.returnPrintDecisionByCord(self.__cords[8]))


import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def start(option):
    g = play()

    while (True):
        position = int(input("Digite uma posição (1-9): "))
        while (position < 1 or position > 9):
            position = int(input("Digite uma posição (1-9): "))

        if not g.returnIfContainValue(position - 1):
            g.setValueCordByIndex(position - 1, option)
            if g.getWinner() != False :
                g.printTable()
                input1
                ("{} Venceu".format(g.getWinner()))
                break
            if g.returnDraw():
                g.printTable()
                input("Deu Velha")
                break
            positionCPU = random.randint(0, 8)
            while g.returnIfContainValue(positionCPU):
                positionCPU = random.randint(0, 8)
            g.setValueCordByIndex(positionCPU, 2 if option == 1 else 1)
            if g.getWinner() != False :
                g.printTable()
                input("{} Venceu".format(g.getWinner()))
                break
            if g.returnDraw():
                g.printTable()
                input("Deu Velha")
                break
            g.printTable()

while True:
    cls()
    print("Menu")
    print("1 - Jogar")
    print("2 - Sair")
    option = int(input())
    if option == 1:
        print("Selecione seu marcador")
        print("1 - X")
        print("2 - O")
        tag = int(input())
        while(tag != 1 and tag != 2):
            tag = int(input("Tente novamente: "))
        start(tag)
    elif option == 2:
        print("Bye")
        exit()

