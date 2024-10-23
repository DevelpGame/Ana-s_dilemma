# Definindo o script básico do Ren'Py

label start:
    scene bg classroom

    "Você é Ana, uma estudante do ensino médio que sempre se destacou em artes, mas enfrenta dificuldades em Matemática e Ciências. Com o semestre se aproximando do fim e o peso das notas pesando em seus ombros, você se sente pressionada a tomar uma decisão crucial."

    "O que você decide fazer?"

    menu:
        "Focar apenas em Matemática":
            jump foco_matematica
        
        "Estudar Ciências e Matemática em paralelo":
            jump estudo_paralelo

label foco_matematica:
    scene bg study_room

    "Ana acredita que dominar Matemática é sua única chance de recuperação. Ela mergulha em livros, assiste a vídeos tutoriais e dedica horas resolvendo exercícios. As aulas de Ciências, antes interessantes, são esquecidas."
    
    "No dia da prova de Matemática, seu coração bate acelerado. A confiança a acompanha, mas ao olhar para as questões, uma onda de insegurança a atinge. Conceitos-chave que ignorou a deixam confusa."

    "Ela sai da prova desmotivada, com uma nota baixa em mãos. A frustração se transforma em uma reflexão amarga: 'E se eu tivesse estudado Ciências também?'"

    "Resultado: Frustração em Matemática."
    "Você percebe que o esforço concentrado não trouxe os resultados esperados e que ignorar as outras disciplinas a deixou ainda mais ansiosa."

    return

label estudo_paralelo:
    scene bg study_group

    "Ana decide que, em vez de escolher, ela pode encontrar um equilíbrio. Ela cria um cronograma de estudos, dedicando dias alternados para Matemática e Ciências, e se junta a grupos de estudo."
    
    "A interação com colegas e a troca de ideias a fazem enxergar as matérias de forma mais clara. Aos poucos, os conceitos se tornam mais fáceis de entender, e sua confiança cresce."

    "Resultado: Sucesso nas duas disciplinas!"
    "As notas começam a subir, e Ana sente uma realização única. Ela percebe que, com esforço e planejamento, consegue equilibrar suas paixões e responsabilidades."

    return
