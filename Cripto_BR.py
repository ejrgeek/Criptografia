#Autor: ErlonJr(Cyborg)
#Versao: 2.0
#Descricao: Gerar WordList Customizadas
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
        frase = frase.replace("a", "1");frase = frase.replace("b", "2")
        frase = frase.replace("c", "3");frase = frase.replace("d", "4")
        frase = frase.replace("e", "5");frase = frase.replace("f", "9")
        frase = frase.replace("g", "8");frase = frase.replace("h", "7")
        frase = frase.replace("i", "6");frase = frase.replace("j", "!")
        frase = frase.replace("k", "@");frase = frase.replace("l", "#")
        frase = frase.replace("m", "$");frase = frase.replace("n", "%")
        frase = frase.replace("o", "¬");frase = frase.replace("p", "&")
        frase = frase.replace("q", "*");frase = frase.replace("r", "§")
        frase = frase.replace("s", "ª");frase = frase.replace("t", "º")
        frase = frase.replace("u", "?");frase = frase.replace("v", "+")
        frase = frase.replace("w", "-");frase = frase.replace("x", "/")
        frase = frase.replace("y", "|");frase = frase.replace("z", "¢")
        frase = frase.replace("ç", "£");frase = frase.replace(" ", "__")
        print(frase)

    elif op == '2':
        frase = str(input("\033[33mDescriptografar > "))
        frase = frase.lower()
        frase = frase.replace("1", "a");frase = frase.replace("2", "b")
        frase = frase.replace("3", "c");frase = frase.replace("4", "d")
        frase = frase.replace("5", "e");frase = frase.replace("9", "f")
        frase = frase.replace("8", "g");frase = frase.replace("7", "h")
        frase = frase.replace("6", "i");frase = frase.replace("!", "j")
        frase = frase.replace("@", "k");frase = frase.replace("#", "l")
        frase = frase.replace("$", "m");frase = frase.replace("%", "n")
        frase = frase.replace("¬", "o");frase = frase.replace("&", "p")
        frase = frase.replace("*", "q");frase = frase.replace("§", "r")
        frase = frase.replace("ª", "s");frase = frase.replace("º", "t")
        frase = frase.replace("?", "u");frase = frase.replace("+", "v")
        frase = frase.replace("-", "w");frase = frase.replace("/", "x")
        frase = frase.replace("|", "y");frase = frase.replace("¢", "z")
        frase = frase.replace("£", "ç");frase = frase.replace("__", " ")
        print(frase)

print("\033[1;36mObrigado por usar meu SoftWare")