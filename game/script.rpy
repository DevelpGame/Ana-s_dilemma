define gui.main_menu_background = "images/backgrounds/bg_main.jpg"

define ana = Character("Ana")
define michael = Character("Michael")

# Personagens
image ana normal = "images/chars/eileen/eileen happy.png"
image ana happy = "images/chars/eileen/eileen vhappy.png"
image ana sad = "images/chars/eileen/eileen concerned.png"

image michael normal = "images/chars/michael/michael_talking.png"
image michael happy = "images/chars/michael/michael_happy.png"
image michael sad = "images/chars/michael/michael_thinking.png"

# Fundos
image math = "images/backgrounds/bg_math.jpg"
image lib = "images/backgrounds/bg_lib.jpg"
image classroom = "images/backgrounds/bg_classroom.jpg"

label start:
    play music "audio/music/9th_Symphony.mp3"
    
    "Escolha a história desejada: "
        # Opções para o jogador
    menu:
        "O Dilema de Ana":
            jump anas_dilemma

        "Superando Desafios em Sala de Aula (Em construção)\nIniciando 'O dilema de Ana'":
            jump anas_dilemma

label anas_dilemma:
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
    "Ana decide que vai focar em Matemática, pois acredita que dominar essa matéria é o suficiente para se sair bem na escola. Ela estuda sozinha, passa horas resolvendo exercícios e ignora as aulas de Ciências."
    "No dia da prova de Matemática, ela se sente preparada, mas ao começar a prova, percebe que faltam alguns conceitos importantes que ela não entendeu completamente."
    "Apesar do esforço, Ana tira uma nota abaixo do esperado e fica frustrada por ter negligenciado Ciências."

    # Exibir o resultado
    scene math with fade:
        zoom 2
    show ana sad at left
    "Você percebe que focar apenas em Matemática não foi o ideal. Não conseguiu se destacar em nenhuma das disciplinas, e o sentimento de frustração é inevitável."
    "Será que escolher estudar apenas o que gosta ou domina foi a decisão certa?"

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
    "Ana decide se dedicar igualmente a Matemática e Ciências, mesmo sabendo que não domina ou não tem tanto gosto por uma das matérias. Ela monta um cronograma, estudando Matemática em um dia e Ciências no outro, e participa de grupos de estudo para ajudar na compreensão dos temas."
    "Com essa abordagem equilibrada, Ana passa a entender melhor os conceitos e se sente mais segura."

    scene classroom at center with fade:
        zoom 2
    "No dia das provas, Ana se sente preparada para ambas as disciplinas e encara os desafios com tranquilidade."

    # Exibir o resultado
    scene classroom at center with fade:
        zoom 2
    show ana happy at left
    "Você vê suas notas melhorarem e sente a satisfação de ter tomado a melhor decisão. Dedicar-se a ambas as matérias, mesmo com as dificuldades, trouxe o sucesso e aprendizado que você esperava."
    "O equilíbrio foi essencial para alcançar o objetivo de passar o ano letivo com confiança e segurança."

    stop music

    # Encaminhamento para final ou reinício
    menu:
        "Recomeçar?":
            jump start
        "Finalizar":
            return

# História 2
label overcoming_challenges_in_the_classroom:
    # Introdução
    scene classroom at center with dissolve:
        zoom 1.5
    narrator "Um novo professor chega à Escola Central, onde muitos alunos têm dificuldade em aprender."
    
    # Reflexões do professor
    narrator "Você pensa: 'A sala está cheia de alunos, mas parece que eles estão desmotivados. Qual será a principal dificuldade deles?'"

    # Introdução ao conflito
    narrator "Após observar um pouco, você percebe um conflito no modo como os alunos abordam as frações: alguns acham as aulas rápidas demais, outros querem mais explicações práticas."

    # Primeira escolha do jogador: Identificação do conflito
    narrator "Existe um conflito: os alunos querem aprender rapidamente para não se atrasar no currículo, mas precisam de mais prática para entender."

    menu:
        "Explorar o conflito entre tempo e aprendizado":
            jump identificar_conflito
        "Ignorar o conflito e continuar com aulas normais":
            jump continuar_aulas_normais

# Cena de identificação do conflito
label identificar_conflito:
    scene conflict_cloud with dissolve
    narrator "Você começa a montar uma nuvem de conflitos. De um lado, os alunos precisam seguir em frente para completar o currículo, mas de outro, eles precisam de mais tempo para praticar frações."

    narrator "Você pensa: 'Preciso encontrar uma forma de reconciliar essas necessidades opostas.'"

    menu:
        "Dividir a turma em dois grupos, com ritmos diferentes":
            jump divisao_grupos
        "Propor atividades em pares para que alunos mais rápidos ajudem os outros":
            jump atividades_em_pares

# Cena de divisão de grupos
label divisao_grupos:
    narrator "Você divide a turma em dois grupos: um para alunos que avançam rapidamente e outro para aqueles que precisam de mais prática."
    student1 "Isso me ajudou muito, professora! Agora posso praticar sem me sentir pressionado."
    student2 "Também achei ótimo, posso avançar sem ficar esperando."

    narrator "Você pensa: 'Dividir os alunos ajudou a atender melhor às suas necessidades.'"
    jump reflexao_final

# Cena de atividades em pares
label atividades_em_pares:
    narrator "Você propõe que os alunos trabalhem em pares, onde um aluno mais avançado ajuda outro com dificuldades."
    student1 "Agora eu entendo melhor! Meu colega explicou de uma forma diferente."
    student2 "Foi bom para mim também, ajudando outras pessoas eu entendi ainda mais."

    narrator "Você pensa: 'As atividades em pares ajudaram os alunos a aprender colaborativamente.'"
    jump reflexao_final

# Cena de continuar aulas normais
label continuar_aulas_normais:
    narrator "Você decide continuar com as aulas normais, sem abordar o conflito diretamente."
    narrator "Com o tempo, alguns alunos ficam para trás, enquanto outros avançam mais rapidamente, o que gera frustração."
    jump reflexao_final

# Cena de reflexão final
label reflexao_final:
    scene teacher_desk with dissolve
    narrator "Ao refletir sobre o dia, você percebe o impacto de abordar ou ignorar o conflito central nas aulas."
    
    narrator "Você pensa: 'Resolver o conflito fez uma diferença significativa no engajamento dos alunos.'"

    # Fim do jogo
    return
