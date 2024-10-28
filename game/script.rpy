define gui.main_menu_background = "images/backgrounds/bg_main.jpg"

define ana = Character("Ana")

# Personagens
image ana normal = "images/chars/eileen/eileen happy.png"
image ana happy = "images/chars/eileen/eileen vhappy.png"
image ana sad = "images/chars/eileen/eileen concerned.png"

# Fundos
# image main = "images/backgrounds/bg_main.jpg"
image math = "images/backgrounds/bg_math.jpg"
image lib = "images/backgrounds/bg_lib.jpg"
image classroom = "images/backgrounds/bg_classroom.jpg"

label start:

    # Tela de título
    "Boas Vindas ao jogo 'O Dilema de Ana'"

    # Apresentação da situação
    scene lib with fade:
        zoom 2
    show ana normal at left
    with dissolve
    "Ana estava enfrentando dificuldades na escola, especialmente em Matemática e Ciências. Com o semestre se aproximando do fim, ela precisava decidir como melhorar suas notas."

    # Introdução à decisão
    "Você é Ana. O que você decide fazer?"

    # Opções para o jogador
    menu:
        "Focar apenas em Matemática":
            jump matematica_focus

        "Estudar Ciências e Matemática em paralelo":
            jump balanced_focus

# Resultado da escolha de focar apenas em Matemática
label matematica_focus:
    scene lib with fade:
        zoom 2
    show ana sad at left
    "Ana decide que precisa dominar Matemática. Ela estuda sozinha, passa horas resolvendo exercícios e ignora as aulas de Ciências."
    "No dia da prova de Matemática, ela se sente preparada, mas quando recebe a prova, percebe que não entendeu alguns conceitos-chave."
    "Ela acaba tirando uma nota baixa e fica frustrada por ter deixado Ciências de lado."

    # Exibir o resultado
    scene math with fade:
        zoom 2
    show ana sad at left
    "Você se sente desanimada e percebe que não conseguiu melhorar em nenhuma das disciplinas."
    "O peso da frustração é enorme. Será que você fez a escolha certa?"

    # Encaminhamento para final ou reinício
    menu:
        "Recomeçar?":
            jump start
        "Finalizar":
            return

# Resultado da escolha de estudar ambas as disciplinas
label balanced_focus:
    scene lib with fade:
        zoom 2
    show ana happy at left
    "Ana decide que vai se concentrar em ambas as matérias. Ela cria um cronograma onde estuda Matemática em um dia e Ciências no outro, participando de grupos de estudo para as duas."
    "Com essa abordagem, ela começa a entender melhor os conceitos e se sente mais confiante."

    scene classroom at center with fade:
        zoom 2
    "No dia das provas, Ana se sente tranquila e preparada para ambas as disciplinas."

    # Exibir o resultado
    scene classroom at center with fade:
        zoom 2
    show ana happy at left
    "Você vê suas notas subirem e se sente realizada, sabendo que sua decisão foi a melhor."
    "O equilíbrio trouxe o sucesso que você esperava."

    # Encaminhamento para final ou reinício
    menu:
        "Recomeçar?":
            jump start
        "Finalizar":
            return
