def mostrar_menu():
    print('\n' * 5)
    print('-------- Avaliação BSM --------')
    print('Escolha um tópico:')
    print('1 - Avaliação Diagnóstica de BSM')
    print('2 - Avaliação Formativa de BSM')
    print('3 - Avaliação BSM Somativa')
    print('4 - Avaliações Técnicas Formativas')
    print('5 - Avaliações Técnicas Somativas')
    print('6 - Participação Ativa')
    print('9 - Sair')
    print('-------------------------------')

def processar_escolha(opcao):
    if opcao == '1':
        print("\n-> Você escolheu: Avaliação Diagnóstica de BSM")
        print("A autoavaliação diagnóstica de BSMs no início do programa serve como ponto de partida "
            "para medir e desenvolver as soft skills dos participantes.\n")

    elif opcao == '2':
        print("\n-> Você escolheu: Avaliação Formativa de BSM")
        print("A avaliação formativa de BSM mede o progresso das habilidades socioemocionais "
            "ao longo do programa por meio de autorreflexão, avaliação em grupo e dramatizações.\n")

    elif opcao == '3':
        print("\n-> Você escolheu: Avaliação BSM Somativa")
        print("As Avaliações Somativas de BSM marcam o encerramento do programa, medindo a compreensão "
            "e aplicação dos BSMs por meio de autorreflexão, avaliação entre pares e simulações finais.")
        print("\nEssa avaliação é realizada ao final do programa para verificar a compreensão geral "
            "e a aplicação dos BSMs adquiridos pelas pessoas participantes.\n")

    elif opcao == '4':
        print("\n-> Você escolheu: Avaliações Técnicas Formativas")
        print("As avaliações técnicas formativas buscam medir o aprendizado técnico e acompanhar o "
            "processo de desenvolvimento, servindo como ferramenta para ajustar rotas com base nas "
            "informações coletadas. Mais do que comprovar conhecimento, o foco é entender a curva de aprendizado.\n")

    elif opcao == '5':
        print("\n-> Você escolheu: Avaliações Técnicas Somativas")
        print("A avaliação técnica somativa serve para verificar, ao final de um ciclo de aprendizagem, "
            "o quanto os participantes dominaram os conhecimentos e habilidades trabalhados.\n")

    elif opcao == '6':
        print("\n-> Você escolheu: Participação Ativa")
        print("As atividades em grupo promovem reflexão e engajamento, incentivando o pensamento crítico "
            "e coletando feedbacks para aprimorar a experiência das pessoas participantes.\n")

    elif opcao == '9':
        print("Saindo do programa...")
        return False
        
    else:
        print("\nOpção inválida. Tente novamente.\n")

    return True 

def main():
    while True:
        mostrar_menu()
        escolha = input("Digite o número da sua escolha: ").strip()
        
        continuar = processar_escolha(escolha)
        
        if not continuar:
            break
        input("\n...Pressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    main()