#クラス＝(設計図の作成)
class Character:
    def __init__(self,name,hp,power):
        self.name=name #データ(属性)
        self.hp=hp #データ(属性)
        self.power=power
    def attack(self): #動き(メゾッド)
         print(f"{self.name}の攻撃!")

aki = Character("アキ",100,30) #実物(インスタンス)
aki.attack()
mina = Character("ミナ",80,45)
mina.attack()
$git add .
$git commit -m "Add character classes and instances"
$git push
