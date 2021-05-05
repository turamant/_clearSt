import random
class Card:
    id = 0
    list_card_eng = []
    def __init__(self, word, translate):
        self.word = word
        self.translate = translate
        Card.id += 1
        self.idd = Card.id

    def addingCard(self):
        self.list_card_eng.append(self)

    @staticmethod
    def printingCard():
        for i in Card.list_card_eng:
            print("Номер карточки: ", i.idd)
            print(f"Word: {i.word}, Translate: {i.translate}")

    @staticmethod
    def play_game():
        while True:
            i = 0
            print("Для выхода введите букву 'q'")
            random.shuffle(Card.list_card_eng)
            max = len(Card.list_card_eng)
            print(Card.list_card_eng[0].word)
            answer = str(input("Перевод: "))
            if answer == 'q':
                break
            while True:
                if Card.list_card_eng[0].translate[i] == answer:
                    print("True")
                    print(Card.list_card_eng[0].translate)
                    break
                else:
                    print("False")
                    i += 1
                    if i > max:
                        i = 0
                    answer = str(input("Перевод: "))




def add_new_card(obj):
    trans = []
    word = str(input("Слово: "))
    while True:
        t = str(input("Перевод: "))
        if t == 'q':
            break
        trans.append(t)
    card = obj(word, trans)
    return card

def show_all_cards(obj):
    obj.printingCard()

def play_game_cards(obj):
    obj.play_game()

if __name__=="__main__":
    while True:
        print("1 - create new words")
        print("2 - show all cards")
        print("3 - play game cards")
        print("4 - quit")
        nomer = int(input("выберите выши действия: "))
        if nomer == 1:
            crd1 = add_new_card(Card)
            crd1.addingCard()
        if nomer == 2:
            show_all_cards(Card)
        if nomer == 3:
            play_game_cards(Card)
        if nomer == 4:
            break
        else:
            print("Ввводи цифры!")
            continue
