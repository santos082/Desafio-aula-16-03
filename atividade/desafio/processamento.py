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

def gerar_relatorio(recuperacao, top_student, medias):
    f = open("resultado.txt", "w")

    f.write("=== RELATÓRIO ACADÊMICO ===\n\n")

    f.write("Todas as Médias:\n")
    for nome, media in medias:
        f.write(nome + ": " + str(round(media, 2)) + "\n")

    f.write("\nAlunos em Recuperação:\n")
    if len(recuperacao) > 0:
        for nome, media in recuperacao:
            f.write(nome + ": " + str(round(media, 2)) + "\n")
    else:
        f.write("Nenhum aluno em recuperação\n")

    f.write("\nTop Student:\n")
    f.write(top_student[0] + ": " + str(round(top_student[1], 2)) + "\n")

    f.close()