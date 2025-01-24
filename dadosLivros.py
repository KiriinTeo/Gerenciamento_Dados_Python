import requests, json
from statLivros import CircularLinkedList as cll

def consultaLivro(titulo = None, autor = None, isbn = None):
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

titulo = input("Digite o título do livro: ")
autor = input("Digite o autor (opcional): ")
isbn = input("Digite o ISBN (opcional): ")

dados = consultaLivro(titulo=titulo, autor=autor, isbn=isbn)
print(consultaLivro())

if 'docs' in dados:
    for livro in dados['docs']:
        print(f"Título: {livro.get('title', 'N/A')}")
        print(f"Autor: {', '.join(livro.get('author_name', ['N/A']))}")
        print(f"ISBN: {', '.join(livro.get('isbn', ['N/A']))}")
        print(f"Primeira publicação: {livro.get('first_publish_year', 'N/A')}")
        print("-" * 40)
else:
    print("Nenhum livro encontrado.")

'''json.loads(dados['docs'])'''

def filtrarConsulta(dados):
    filtro_titulo = input("Informe um título para filtrar: ")
    filtro_autor = input("Informe um autor para filtrar: ")
    filtro_ano = input("Informe um ano para filtrar: ")

    livros_filtrados = [
        livro for livro in dados['docs']
        if (not filtro_titulo or livro.get('title') == filtro_titulo) and
           (not filtro_autor or filtro_autor in livro.get('author_name', [])) and
           (not filtro_ano or str(livro.get('first_publish_year', '')) == filtro_ano)
    ]
    
    plus = input("Deseja ver livro filtrado: (s/n):")
    if plus.lower() == 's':
        for livro in livros_filtrados:
            print(f"\nLivro: {livro.get('title', 'N/A')}")
            print(f"Autor: {', '.join(livro.get('author_name', ['N/A']))}")
            print(f"Ano: {livro.get('first_publish_year', 'N/A')}")
            print(f"ISBN: {', '.join(livro.get('isbn', 'N/A'))}")
            print("-" * 40)

filtrarConsulta(dados)

saida = input("Deseja limpar o console? (s/n):")
if saida == 's':
    cll.limparSaida(None) 
    exit()
else:
    exit()