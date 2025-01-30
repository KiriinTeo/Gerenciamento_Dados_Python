import pandas as pd
from dadosLivros import pesquisarLivro

def formatacaoDados():
    info = pesquisarLivro()
    if info:
        print("Colunas do DataFrame:")
        colunas_Principais = ['title', 'author_name', 'first_publish_year', 'isbn', 'publisher']
        df = pd.DataFrame(info['docs'], columns = colunas_Principais)

        df.rename(columns={
        'title': 'Título',
        'author_name': 'Autor',
        'first_publish_year': 'Ano de Publicação',
        'isbn': 'ISBN',
        'publisher': 'Editora'
        }, inplace=True)
    
        print(df.describe(include='all'))
        print('\n', df)
        
        ftr_unico = input("Deseja filtrar por itens específicos? (s/n):")
        if ftr_unico.lower() == 's':
            coluna = []
            for col in df.columns:
                coluna.append(col)
        else:
            return df
        
        filtros = {}
        while True:
            print("\nColunas disponíveis para múltiplos filtros:")
            for i, col in enumerate(coluna, start=1):
                print(f"{i}. {col}")

            escolha_col = int(input("\nEscolha o número correspondente das colunas que deseja filtrar (ou 0 para sair): ")) - 1
            if escolha_col < 0:
                break

            coluna_selecionada = coluna[escolha_col]

            criterio = input(f"Informe o critério de filtragem para '{coluna_selecionada}': ")
            filtros[coluna_selecionada] = criterio

            add_ftr = input("Deseja adicionar outro filtro? (s/n): ")
            if add_ftr.lower() != 's':
                break

        df_filtrado = df
        for coluna, criterio in filtros.items():
        #.astype(str) evita erros com NaN no df, .str.contains(criterio, case=False, na=False) verifica o critério, ignora o Upper ou Lower case do contéudo e 'na' ignora os NaN como resultado
            df_filtrado = df_filtrado[df_filtrado[coluna].astype(str).str.contains(criterio, case=False, na=False)] 
        
        print("\nResultados com múltiplos filtros aplicados:")
        print(df_filtrado)

        return df_filtrado

    else:
        print("Nenhum dado retornado pela função pesquisarLivro().")

formatacaoDados()