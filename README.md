<h1 align="center">Diagnóstico de Osteoartrite Femorotibia 🩺</h1>

<p align="center">
  <a href="#dart-sobre">Sobre</a> &#xa0; | &#xa0; 
  <a href="#warning-importante">Importante</a> &#xa0; | &#xa0; 
  <a href="#sparkles-funcionamento">Funcionamento</a> &#xa0; | &#xa0;
  <a href="#memo-autores">Autores</a> &#xa0; 
</p>

<br>

## :dart: Sobre ##

<div align="justify">
Desenvolvimento do primeiro trabalho acadêmico da disciplina de Processamento e Análise de Imagens - 8º período. Lecionada no curso de Engenharia de computação na Pontifícia Universidade Católica de Minas Gerais.
<br><br>
O objetivo deste trabalho é realizar o diagnóstico de Osteoartrite Femorotibial através de imagens de raio X.
</div>

## :warning: Importante ##

<div align="justify">
<li>Para a execução do programa é necessário instalar as dependências citadas no arquivo instalando_as_dependencias.txt</li>

```
pip install Pillow
pip install opencv-python
pip install opencv-contrib-python
pip install pygame
pip install easygui
python -m pip install -U pip setuptools
python -m pip install matplotlib
pip install matplotlib

sudo apt-get install python-matplotlib
sudo apt-get install python3-tk
sudo apt-get install python3-pygame
```

</div>

## :sparkles: Funcionamento ##

<div align="justify">
Ao iniciar o programa, o usuário logo será solicitado para selecionar a imagem A. Depois solicitado para selecionar a imagem B. Em seguida é aberta uma janela que exibe a imagem B, nessa janela é possível selecionar uma região arbitrária da imagem.
<br>
A região selecionada é salva em um novo arquivo com o nome semelhante ao anterior, concatenando o nome original (1) com "_recorte" (2). A imagem então é comparada com outra imagem selecionada, utilizando o método de correlação cruzada.
</div>

## :memo: Autores ##
<a href="https://github.com/DayaneCordeiro">
    <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/54179987?v=4" width="150px;" alt=""/>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/50596100?v=4" width="150px;" alt=""/>
    <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<sub><b>Paulo Henrique Luiz</b></sub>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <sub><b>Dayane Cordeiro</b></sub>
</a>
