#Autor: ErlonJr(Cyborg)
#Versao: 3.0
#Descricao: Mensagens Criptografadas
#GitHun: https://github.com/ejrgeek
op=""
banner="""\033[1;31m   ____     ____      _                         ____  
  / __ \   / ___|   _| |__   ___  _ __ __ _    / __ \ 
 / / _` | | |  | | | | '_ \ / _ \| '__/ _` |  / / _` |
| | (_| | | |__| |_| | |_) | (_) | | | (_| | | | (_| |
 \ \__,_|  \____\__, |_.__/ \___/|_|  \__, |  \ \__,_|
  \____/        |___/                 |___/    \____/ \033[1;0m
"""
print(banner)
menu="""\033[1;32m    @@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@  1 - criptografar     @@
    @@  2 - Descriptografar  @@
    @@  0 - Sair             @@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@
    """
print(menu)
while op != '0':
    op=str(input("\033[1;37mEscolha uma opção > "))

    if op == '1':
        frase = str(input("\033[1;35mCriptografar > "))
        frase=frase.lower()
        frase = frase.replace("a", "◉");frase = frase.replace("b", "☍")
        frase = frase.replace("c", "☺");frase = frase.replace("d", "✎")
        frase = frase.replace("e", "♞");frase = frase.replace("f", "✄")
        frase = frase.replace("g", "✖");frase = frase.replace("h", "∎")
        frase = frase.replace("i", "♨");frase = frase.replace("j", "●")
        frase = frase.replace("k", "@");frase = frase.replace("l", "#")
        frase = frase.replace("m", "$");frase = frase.replace("n", "%")
        frase = frase.replace("o", "¬");frase = frase.replace("p", "&")
        frase = frase.replace("q", "➧");frase = frase.replace("r", "§")
        frase = frase.replace("s", "ª");frase = frase.replace("t", "º")
        frase = frase.replace("u", "∞");frase = frase.replace("v", "☸")
        frase = frase.replace("w", "➲");frase = frase.replace("x", "☄")
        frase = frase.replace("y", "❧");frase = frase.replace("z", "¢")
        frase = frase.replace("ç", "£");frase = frase.replace(" ", "__")
        frase = frase.replace("?","♆");frase = frase.replace("!","✿")
        frase = frase.replace("1","☠");frase = frase.replace("2","☢")
        frase = frase.replace("3","☣");frase = frase.replace("4","☤")
        frase = frase.replace("5","❢");frase = frase.replace("6","♦")
        frase = frase.replace("7","♒");frase = frase.replace("8","☡")
        frase = frase.replace("9","☬");frase = frase.replace("0","ᴥ")
        frase = frase.replace(".","∘");frase = frase.replace(",","∙")
        print(frase)

    elif op == '2':
        frase = str(input("\033[33mDescriptografar > "))
        frase = frase.lower()
        frase = frase.replace("◉", "a");frase = frase.replace("☍", "b")
        frase = frase.replace("☺", "c");frase = frase.replace("✎", "d")
        frase = frase.replace("♞", "e");frase = frase.replace("✄", "f")
        frase = frase.replace("✖", "g");frase = frase.replace("∎", "h")
        frase = frase.replace("♨", "i");frase = frase.replace("●", "j")
        frase = frase.replace("@", "k");frase = frase.replace("#", "l")
        frase = frase.replace("$", "m");frase = frase.replace("%", "n")
        frase = frase.replace("¬", "o");frase = frase.replace("&", "p")
        frase = frase.replace("➧", "q");frase = frase.replace("§", "r")
        frase = frase.replace("ª", "s");frase = frase.replace("º", "t")
        frase = frase.replace("∞", "u");frase = frase.replace("☸", "v")
        frase = frase.replace("➲", "w");frase = frase.replace("☄", "x")
        frase = frase.replace("❧", "y");frase = frase.replace("¢", "z")
        frase = frase.replace("£", "ç");frase = frase.replace("__", " ")
        frase = frase.replace("♆","?");frase = frase.replace("✿","!")
        frase = frase.replace("☠","1");frase = frase.replace("☢","2")
        frase = frase.replace("☣","3");frase = frase.replace("☤","4")
        frase = frase.replace("❢","5");frase = frase.replace("♦","6")
        frase = frase.replace("♒","7");frase = frase.replace("☡","8")
        frase = frase.replace("☬","9");frase = frase.replace("ᴥ","0")
        frase = frase.replace("∘",".");frase = frase.replace("∙",",")
        print(frase)

print("\033[1;36mObrigado por usar meu SoftWare")