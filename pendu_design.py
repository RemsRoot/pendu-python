design0 = """


    
    
    
  
                """

design1 = """


    
    
    
  _____
                """

design2 = """

    |
    |
    |
    |
  __|__
                """

design3 = """
    _______
    |/
    |
    |
    |
  __|__
                """

design4 = """
    _______
    |/    |
    |
    |
    |
  __|__
                """

design5 = """
    _______
    |/    |
    |     0
    |
    |
  __|__
                """

design6 = """
    _______
    |/    |
    |     0
    |     |
    |
  __|__
                """

design7 = """
    _______
    |/    |
    |     0
    |     |-
    |
  __|__
                """

design8 = """
    _______
    |/    |
    |     0
    |    -|-
    |
  __|__
                """

design9 = """
    _______
    |/    |
    |     0
    |    -|-
    |    /
  __|__
                """

design10 = """
    _______
    |/    |
    |     0
    |    -|-
    |    / \\
  __|__
                """

Hangman_games = """

    HANGMAN GAMES

       WELCOME

"""

loose = """

   YOU LOOSE !!!!

      RETRY ?

"""

win = """

    YOU WIN !!!

"""

design = [design0, design1, design2, design3, design4, design5, design6, design7, design8, design9, design10]

def design_life_pendu(life):
    return design[10-life]