
def jogo(erros,nome,vit,der) :

    if erros == 0 :

        #print ()
        print ("|----- ")
        print ("|    | ")
        print ("|      ")
        print ("|      ")
        print ("|      ")
        print ("|      ")
        print ("_      ")
        print ()

    elif erros == 1 :

      #  print ()
        print ("|----- ")
        print ("|    | ")
        print ("|    O ")
        print ("|      ")
        print ("|      ")
        print ("|      ")
        print ("_      ")
        print ()

    elif erros == 2 :

      #  print ()
        print ("|----- ")
        print ("|    | ")
        print ("|    O ")
        print ("|    | ")
        print ("|    |  ")
        print ("|      ")
        print ("_      ")
        print ()

    elif erros == 3:

      #  print ()
        print ("|----- ")
        print ("|    | ")
        print ("|    O ")
        print ("|   /| ")
        print ("|    |  ")
        print ("|      ")
        print ("_      ")
        print ()

    elif erros == 4:

      #  print ()
        print ("|----- ")
        print ("|    | ")
        print ("|    O ")
        print ("|   /|\ ")
        print ("|    |  ")
        print ("|      ")
        print ("_      ")
        print ()

    elif erros == 5:

      #  print ()
        print ("|----- ")
        print ("|    | ")
        print ("|    O ")
        print ("|   /|\ ")
        print ("|    |  ")
        print ("|   /   ")
        print ("_      ")
        print ()

    elif erros == 6 :


        print ("|----- ")
        print ("|    | ")
        print ("|    O ")
        print ("|   /|\ ")
        print ("|    | ")
        print ("|   / \ ")
        print ("_      ")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        print ('\033[1;31m Oh não!\033[m')
        print ('\033[1;31m Você perdeu, mas tente de novo, na próxima você consegue\033[m')
        print ()

def inicio():
    x = 'JOGO  DA  FORCA'

    print ('#' * 30)
    print ('{:^30}'.format (x))
    print ('#' * 30)
