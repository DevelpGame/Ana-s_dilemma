define ana = Character("Ana")

image ana normal = "images/eileen happy.png"
image ana happy = "images/eileen vhappy.png"
image ana sad = "images/eileen concerned.png"

# Definindo o jogo
label start:

    # Tela de título
    scene bg_main with fade:
        zoom 2
    "O Dilema de Ana"
    
    # Apresentação da situação
    scene bg_lib with fade:
        zoom 2
    show ana normal at left
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
    scene bg_lib with fade:
        zoom 2
    show ana sad at left
    "Ana decide que precisa dominar Matemática. Ela estuda sozinha, passa horas resolvendo exercícios e ignora as aulas de Ciências."
    "No dia da prova de Matemática, ela se sente preparada, mas quando recebe a prova, percebe que não entendeu alguns conceitos-chave."
    "Ela acaba tirando uma nota baixa e fica frustrada por ter deixado Ciências de lado."
    
    # Exibir o resultado
    scene bg_math with fade:
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
    scene bg_lib with fade:
        zoom 2
    show ana happy at left
    "Ana decide que vai se concentrar em ambas as matérias. Ela cria um cronograma onde estuda Matemática em um dia e Ciências no outro, participando de grupos de estudo para as duas."
    "Com essa abordagem, ela começa a entender melhor os conceitos e se sente mais confiante."

    scene bg_classroom at center with fade:
        zoom 2
    "No dia das provas, Ana se sente tranquila e preparada para ambas as disciplinas."
    
    # Exibir o resultado
    scene bg_classroom at center with fade:
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
