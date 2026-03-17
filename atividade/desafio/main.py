from processamento import analisar_alunos, gerar_relatorio

def main():
    alunos = [
        ("João", [7, 8, 6]),
        ("Maria", [9, 10, 8]),
        ("Pedro", []),
        ("Ana", [5, 6, 6]),
        ("Lucas", [10, 9, 9]),
        ("Carla", ["erro", 8, 7])  # inválido
    ]

    recuperacao, top_student, medias = analisar_alunos(alunos)

    print("\n=== RESULTADO ===")
    print("Recuperação:", recuperacao)
    print("Top Student:", top_student)

    gerar_relatorio(recuperacao, top_student, medias)


if __name__ == "__main__":
    main()