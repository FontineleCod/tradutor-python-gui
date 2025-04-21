
```markdown
# Tradutor Python com Interface Gráfica

![Imagem do Tradutor](https://placehold.co/600x400)

Descrição

Este é um tradutor simples feito em Python, com interface gráfica utilizando a biblioteca `tkinter`. Ele usa a API **Deep-Translator** para traduzir palavras e frases entre **Português** e **Inglês**. O projeto foi feito para ser leve e fácil de usar, com a opção de gerar um executável `.exe` para Windows, permitindo que você use o tradutor sem precisar instalar o Python.

---

Tecnologias Utilizadas

- **Python** 3.x
- **tkinter** (para a interface gráfica)
- **deep-translator** (para a tradução)
- **PyInstaller** (para criar o executável)

---

Como Rodar o Projeto

Clonar o Repositório

```bash
git clone https://github.com/FontineleCod/tradutor-python-gui.git
cd tradutor-python-gui
```

2. Instalar as Dependências

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Caso você não tenha o `requirements.txt`, crie com o comando:

```bash
pip freeze > requirements.txt
```

3. Rodar o Tradutor

Com as dependências instaladas, basta rodar o arquivo `tradutor.py`:

```bash
python tradutor.py
```

---

Gerar Executável (.exe) para Windows

Se você quiser gerar um arquivo `.exe` para Windows, basta rodar o seguinte comando:

```bash
pyinstaller --onefile tradutor.py
```

Isso criará um arquivo `.exe` na pasta `dist/` que pode ser executado diretamente no Windows, sem precisar de Python instalado.

---

Personalizações

Você pode modificar a aparência da interface gráfica facilmente alterando o arquivo `tradutor.py`:

- Cores: Alterando os valores no código `bg` e `fg` de cada componente.
- Fonte: Alterando a propriedade `font` dos widgets.
- Tamanho da janela: Ajustando as dimensões da janela `root.geometry()`.

---

Como Contribuir

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**. Fique à vontade para sugerir novas funcionalidades ou melhorar o código!

---

Licença

Esse projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Links úteis

- [Deep-Translator Documentation](https://pypi.org/project/deep-translator/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [PyInstaller Documentation](https://pyinstaller.org/)

---

Autor

**Marcelo Fontinele**  
[GitHub](https://github.com/FontineleCod)  
[LinkedIn](https://www.linkedin.com/in/marcelo-fontinele-1b2354165/)
```

Agora é só copiar e colar esse conteúdo no arquivo `README.md` do seu repositório, e pronto! Se quiser adicionar alguma imagem, logo, ou algum link adicional, é só editar o conteúdo conforme necessário. 😎🚀
