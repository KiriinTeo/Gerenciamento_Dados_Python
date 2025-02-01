import matplotlib.pyplot as plt
from analiseLivros import formatacaoDados, pesquisarLivro

df = formatacaoDados(pesquisarLivro(titulo="The Hobbit", autor="J.R.R. Tolkien"))
df['Ano de Publicação'].value_counts().sort_index().plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title("Contagem de Livros por Ano de Publicação")
plt.xlabel("Ano de Publicação")
plt.ylabel("Quantidade")
plt.show()
