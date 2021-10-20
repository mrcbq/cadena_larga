import os
# import ast

os.system('cls')

def run():
    word_init = ['estrella', 'explosión', 'guitarra', 'plástico', 'navaja', 'martillo', 'libros', 'lápiz', 'lapicera', 'aluminio', 'embarcación','letra', 'agujeta','ventana', 'librería', 'sonido', 'universidad', 'rueda', 'perro', 'llaves', 'camisa', 'pelo', 'papá'] # Cadena usada para iniciliazr en caso de no dogotar nada
    words = []
    words_length = []
    # lenght_word = 0
    i=0

    words = input('Please, Give an array whit strings separated by commas only: ')
    if len(words) == 0 :
        words = word_init
    else:
        words = words.strip('][').split(', ') #Aqui trasformo el string de entrada para quitarle los [] y separar el contenido por comas pasandolo de esta manera a un tipo de dato list, ya que es el mas parecido a un array en python
        # words = ast.literal_eval(words)
        # number_of_words = len(words)
        # word_larger = list(range(number_of_words))
        # for word in words :
        #     lenght_word = len(word)
        #     word_larger[word] = lenght_word
    
    for word in words:
        words_length.append(len(word)) #Creo la lista que contendra la lngitud de cada palabra o string
        # print(words)
        # print(type(words))
        # print(i)
        # print(len(word))
        # print(words_length)
        i = i+1
    # if len(words_length) > 0:
    #     for x in range(len(words_length)-1):
    #         if words_length[x] > words_length[x+1]:
    # print(words_length)
    # print(max(words_length))
    # print(words_length.index(max(words_length)))
    index_find = words_length.index(max(words_length)) #Selecciono el indice de la lista que busco, es decir la palabra mas larga.
    # print(words[index_find])
    print("The string that you gave me was:\n", words, '\n')
    print("The first larger string in the array that you gave me is: " + words[index_find])

if __name__ == '__main__':
    run()