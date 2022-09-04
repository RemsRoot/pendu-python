from fonction_lecture import lecture_txt, random_word, enlever_accent

list_bouffe = ["O'tacos","speed burger"]

if __name__ == "__main__" :
    mot = random_word(lecture_txt())
    print(mot)
    print(enlever_accent(mot))