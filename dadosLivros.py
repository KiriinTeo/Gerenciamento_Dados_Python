import requests, json
from statLivros import CircularLinkedList

cll = CircularLinkedList()

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


def historicoResultado(dados, nome_arquivo):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso no arquivo: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar os dados no arquivo: {e}")

def pesquisarLivro():
    id_Exato = input("Olá! Deseja pesquisar através do ISBN? (s/n): ")
    if id_Exato.lower() == 's':
        isbn = input("Digite o ISBN: ")
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
        print("Então vamos á pesquisa por titulo e autor \n ")

    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor (opcional): ")

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
        print("\nDados insuficientes para filtrar.")
        break
    

saida = input("Deseja limpar o console? (s/n):")
if saida == 's':
    cll.limparSaida()
    exit()
else:
    cll.ImprimirLista()
    print("-" * 40)
    historicoResultado(resposta, 'resultado de pesquisa.json')
    exit()