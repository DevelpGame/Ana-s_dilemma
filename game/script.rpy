define gui.main_menu_background = "images/backgrounds/bg_main.jpg"

# Configurando posições fixas
define center_above = Position(xalign=1.0, yalign= 0.7)
define left_above = Position(xalign=0.01, yalign=0.7)

define ana = Character("Ana")
define michael = Character("Michael")
define julia = Character("Júlia")

# Personagens
image ana normal = im.Scale("images/chars/ana/ana happy.png", 200, 200)
image ana happy = im.Scale("images/chars/ana/ana vhappy.png", 200, 200)
image ana sad = im.Scale("images/chars/ana/ana concerned.png", 200, 200)
image ana inormal = im.Scale("images/chars/ana/i - ana happy.png", 200, 200)
image ana ihappy = im.Scale("images/chars/ana/i - ana vhappy.png", 200, 200)
image ana isad = im.Scale("images/chars/ana/i - ana concerned.png", 200, 200)


image michael normal = im.Scale("images/chars/michael/michael_talking.png", 200, 200)
image michael happy = im.Scale("images/chars/michael/michael_happy.png", 200, 200)
image michael sad = im.Scale("images/chars/michael/michael_thinking.png", 200, 200)

image julia normal = im.Scale("images/chars/julia/julia_talking.png", 200, 200)
image julia happy = im.Scale("images/chars/julia/julia_happy.png", 200, 200)
image julia sad = im.Scale("images/chars/julia/julia_sad.png", 200, 200)

# Fundos
image math = "images/backgrounds/bg_math.jpg"
image lib = "images/backgrounds/bg_lib.jpg"
image classroom = "images/backgrounds/bg_classroom.jpg"

label start:
    play music "audio/music/9th_Symphony.mp3"

    # "Escolha a história desejada:"
    # menu:
        #"O Dilema de Ana":
    jump anas_dilemma

        # "Superando Desafios em Sala de Aula (Em construção)\nIniciando 'O dilema de Ana'":
        #     jump overcoming_challenges_in_the_classroom

label anas_dilemma:
    # Introdução à história principal
    scene lib with fade:
        zoom 2
    with dissolve
    narrator "Ana estava preocupada. Matemática e Ciências estavam puxadas, e as provas finais chegavam cada vez mais perto."
    narrator "Ela sabia que precisava melhorar suas notas, mas não sabia por onde começar."
    
    # Novo evento: Visita de Júlia
    show ana inormal at left_above
    show julia normal at center_above
    julia "Oi, Ana! Está ocupada?"
    ana "Oi, Júlia! Meio que sim... Estou tentando organizar meus estudos."
    julia "Tenho uma novidade incrível! Consegui ingressos para o show da Roberta Machado no fim de semana. São passes VIP com acesso ao backstage!"
    julia "O que acha de irmos juntas?"

    # Opções para o jogador
    menu:
        "Aceitar o convite de Júlia e ir ao evento":
            jump accept_invitation
        "Recusar o convite para focar nos estudos":
            jump decline_invitation

# Cena de aceitar o convite
label accept_invitation:
    scene event with fade:
        zoom 2
    show ana ihappy at left_above
    show julia happy at center_above
    ana "Uau! Isso é demais! Claro que vou!"
    "Ana decide ir ao evento com Júlia. Elas aproveitam o fim de semana inteiro, curtindo o show e as atividades."
    scene lib with fade:
        zoom 2
    show ana isad at left_above
    narrator "Ao voltar para casa, Ana percebe que perdeu um tempo precioso para estudar. Suas notas acabam sofrendo com isso."
    narrator "Apesar de se divertir, ela sente que a escolha trouxe mais consequências do que esperava."

    menu:
        "Recomeçar?":
            jump start
        "Finalizar":
            return

# Cena de recusar o convite
label decline_invitation:
    scene lib with fade:
        zoom 2
    show ana isad at left_above
    ana "Júlia, eu adoraria ir, mas tenho exames importantes chegando. Preciso focar nos estudos."
    show julia normal at center_above
    julia "Ah, que pena... Mas entendo. Boa sorte com os estudos!"
    scene lib with fade:
        zoom 2
    show ana ihappy at left_above
    narrator "Ana se dedica aos estudos durante o fim de semana. Embora sinta que perdeu uma chance de diversão, ela fica orgulhosa ao ver os resultados positivos nas provas."

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
