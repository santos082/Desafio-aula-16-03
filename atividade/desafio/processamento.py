def validar_notas(notas):
    if type(notas) != list or len(notas) == 0:
        return False

    for nota in notas:
        if type(nota) != int and type(nota) != float:
            return False

    return True

def calcular_media(notas):
    return sum(notas) / len(notas)

def analisar_alunos(dados):
    recuperacao = []
    medias = []

    for item in dados:
        nome = item[0]
        notas = item[1]

        if not validar_notas(notas):
            print("[ERRO] Dados inválidos para", nome)
            continue

        media = calcular_media(notas)
        medias.append((nome, media))

        if media < 7:
            recuperacao.append((nome, media))

  
    if len(medias) > 0:
        top_student = medias[0]

        for aluno in medias:
            if aluno[1] > top_student[1]:
                top_student = aluno
    else:
        top_student = ("Nenhum", 0)

    return recuperacao, top_student, medias
