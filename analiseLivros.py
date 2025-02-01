import pandas as pd
from dadosLivros import pesquisarLivro

def formatacaoDados(info):
    if info:
        colunas_Principais = ['title', 'author_name', 'first_publish_year', 'isbn', 'publisher']
        df = pd.DataFrame(info['docs'], columns=colunas_Principais)

        df.rename(columns={
            'title': 'Título',
            'author_name': 'Autor',
            'first_publish_year': 'Ano de Publicação',
            'isbn': 'ISBN',
            'publisher': 'Editora',
            'subjects': 'Temas',
            'ratings_average': 'Nota Média'
        }, inplace=True)
    
        df = df.astype(str).fillna('Desconhecido')
        
        return df
    else:
        print("Nenhum dado retornado pela função pesquisarLivro().")
        return None

def filtragemAvancada(df, filtros):
    if df is None:
        return None
        
    ftr_unico = input("Deseja filtrar por itens específicos? (s/n):")
    if ftr_unico.lower() == 's':
        coluna = list(df.columns)
    else:
        return df
        
    while True:
        print("\nColunas disponíveis para múltiplos filtros:")
        for i, col in enumerate(coluna, start=1):
            print(f"{i}. {col}")

        escolha_col = int(input("\nEscolha o número correspondente das colunas que deseja filtrar (ou 0 para sair): ")) - 1
        if escolha_col < 0:
            break

        coluna_selecionada = coluna[escolha_col]

        if escolha_col == 2:  
            escolha_ano = input(f"Coluna Escolhida: {coluna_selecionada}, deseja filtrar por margem de anos? (s/n):")
            if escolha_ano.lower() == 's':
                min_ano = int(input("Informe o ano mínimo: "))
                max_ano = int(input("Informe o ano máximo: "))
                df_filtrado = df[(df['Ano de Publicação'] >= min_ano) & (df['Ano de Publicação'] <= max_ano)]
                print(df_filtrado)
                return df_filtrado

        criterio = input(f"Informe o critério de filtragem para '{coluna_selecionada}': ")
        filtros[coluna_selecionada] = criterio

        add_ftr = input("Deseja adicionar outro filtro? (s/n): ")
        if add_ftr.lower() != 's':
            break

    df_filtrado = df
    for coluna, criterio in filtros.items():
        # linha para filtros que se parecem com o resultado real. tipo uma palavra dentro de outras
        regex_criterio = ''.join([f'(?=.*{word})' for word in criterio.split()])
        df_filtrado = df_filtrado[df_filtrado[coluna].astype(str).str.contains(regex_criterio, case=False, na=False, regex=True)]
        
    print("\nResultados com múltiplos filtros aplicados:")
    print(df_filtrado)

    return df_filtrado

def mediasDados(df):
    if df is None:
        return None
    
    print("Dados por Categoria. \n")
    print(df.groupby('Autor')['Ano de Publicação'].max())

mediasDados(formatacaoDados(pesquisarLivro(isbn='9780140328721')))