import requests, json
from statLivros import CircularLinkedList as cll

def consultaLivro(titulo=None, autor=None, isbn=None):
    url_Basica = "https://openlibrary.org/search.json"

    if isbn:
        url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    else:
        params = []
        if titulo:
            params.append(f"title={titulo}")
        if autor:
            params.append(f"author={autor}")
        query_Busca = "&".join(params)
        url = f"{url_Basica}?{query_Busca}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao acessar a API: {response.status_code}")

def pesquisarLivro(isbn=None, titulo=None, autor=None):
    if isbn:
        dados = consultaLivro(isbn=isbn)
        if dados:
            for key, livro in dados.items():
                print(f"Título: {livro.get('title', 'N/A')}")
                print(f"Autor: {', '.join(livro.get('authors', [{'name': 'N/A'}])[0].get('name', 'N/A'))}")
                print(f"ISBN: {isbn}")
                print(f"Primeira publicação: {livro.get('publish_date', 'N/A')}")
                print(f"Editora: {', '.join(livro.get('publishers', [{'name': 'N/A'}])[0].get('name', 'N/A'))}")
                print("-" * 40)
            return dados
        else:
            print("Nenhum livro corresponde ao ISBN informado.")
    else:
        dados = consultaLivro(titulo=titulo, autor=autor)
        if 'docs' in dados:
            for livro in dados['docs']:
                print(f"Título: {livro.get('title', 'N/A')}")
                print(f"Autor: {', '.join(livro.get('author_name', ['N/A']))}")
                print(f"ISBN: {', '.join(livro.get('isbn', ['N/A']))}")
                print(f"Primeira publicação: {livro.get('first_publish_year', 'N/A')}")
                print(f"Editora: {', '.join(livro.get('publisher', ['N/A']))}")
                print("-" * 40)
            return dados
        else:
            print("Nenhum livro encontrado.")

def filtrarConsulta(dados, filtro_titulo=None, filtro_autor=None, filtro_ano=None):
    livros_filtrados = [
        livro for livro in dados['docs']
        if (not filtro_titulo or livro.get('title') == filtro_titulo) and
           (not filtro_autor or filtro_autor in livro.get('author_name', [])) and
           (not filtro_ano or str(livro.get('first_publish_year', '')) == filtro_ano)
    ]
    
    for livro in livros_filtrados:
        print(f"\nLivro: {livro.get('title', 'N/A')}")
        print(f"Autor: {', '.join(livro.get('author_name', ['N/A']))}")
        print(f"Ano: {livro.get('first_publish_year', 'N/A')}")
        print(f"ISBN: {', '.join(livro.get('isbn', ['N/A']))}")
        print(f"Editora: {', '.join(livro.get('publisher', ['N/A']))}")
        print("-" * 40)

    return livros_filtrados

def adicionarLivro(dados):
    for livro in dados:
        titulo = livro.get('title', 'N/A')
        autor = ', '.join(livro.get('author_name', ['N/A']))
        ano = livro.get('first_publish_year', 'N/A')
        isbn = ', '.join(livro.get('isbn', ['N/A']))
        editora = ', '.join(livro.get('publisher', ['N/A']))
        
        cll.AdicionarUltimo(titulo, autor, ano, editora, isbn)
        
    print("Sucesso na adição de dados!!!")

def mini_Menu():
    while True:
        resposta = pesquisarLivro()
        if resposta:
            plus = input("\nDeseja filtrar sua pesquisa? (s/n): ")
            if plus.lower() == 's':
                filtro = filtrarConsulta(resposta)
                adicionarLivro(filtro)
            
                plus = input("Deseja realizar uma nova pesquisa?: (s/n)")
                if plus.lower() == 's':
                    continue
                else:
                    break
            else: 
                break
        else:
            print("\nDados insuficientes para filtrar.")
            break

    saida = input("Deseja limpar o console? (s/n):")
    if saida == 's':
        cll.limparSaida()
        #exit()
    else:
        cll.ImprimirLista()
        print("-" * 40, '\n')
        #historicoResultado(resposta, 'resultado de pesquisa.json')
        exit()
