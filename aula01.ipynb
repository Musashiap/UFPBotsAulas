{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "-"
    }
   },
   "source": [
    "# Aula 1: introdução"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.1 Bibliotecas"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "-"
    }
   },
   "source": [
    "Primeiramente, em nosso curso, vamos entender um pouco sobre as bibliotecas que usaremos. \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "O OpenCV :\n",
    "OpenCV (Open Source Computer Vision Library). Originalmente, desenvolvida pela Intel, em 2000, é uma biblioteca multiplataforma, para o desenvolvimento de aplicativos na área de Visão computacional. O OpenCV possui módulos de Processamento de Imagens e Video I/O, Estrutura de dados, Álgebra Linear, GUI (Interface Gráfica do Usuário) Básica com sistema de janelas independentes, Controle de mouse e teclado, além de mais de 350 algoritmos de Visão computacional como: Filtros de imagem, calibração de câmera, reconhecimento de objetos, análise estrutural e outros. O seu processamento é em tempo real de imagens.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Numpy:\n",
    "NumPy é um pacote para a linguagem Python que suporta arrays e matrizes multidimensionais, possuindo uma larga coleção de funções matemáticas para trabalhar com estas estruturas. No nosso curso eles será usado para construir matrizes e vetores que nos ajude a trabalhar com cores, diagramação de imagens e fatores como saturação, brilho e intensidade."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.2 Primeiras funções "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Agora que já temos uma noção bem básica das bibliotecas, vamos entender um pouco sobre o conceito de imagem.\n",
    "A primeira coisa que temos que ter em mente é que a menor unidade de imagem é formada por pixels, por mais que você não possa enxergar eles numa imagem, são eles que definem as cores de uma imagem, sua saturação e sua resolução. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import Image\n",
    "Image(filename='jardiml3.png')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Em nosso curso iremos aprender como manipular esses pixels de varias formas (alterando suas cores,saturação e posições)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "O primeiro passo é aprender como abrir uma imagem utilizando o OpenCV. Uma coisa que facilita muito o processo, é salvar a imagem na mesma pasta que o programa esta sendo salvo, assim não precisamos digitar todo o diretório da imagem."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parâmetros: .imread(\"imagem a ser lida\")\n",
    "            .imshow(\"nome da imagem\", imagem fonte)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "#import numpy as np\n",
    "#import matplotlib.pyplot as plt\n",
    "img = cv2.imread(\"lena512.bmp\")\n",
    "cv2.imshow(\"imagem\",img)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Agora iremos aprender como salvar uma imagem, no mesmo ou em outro formato."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "img = cv2.imread(\"lena512.bmp\")\n",
    "cv2.imshow(\"lena\",img)\n",
    "cv2.imwrite(\"lena512.jpeg\",img)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parâmetros: .imwrite(\"novo nome da imagem.novoformato\", imagem fonte)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "a próxima função que iremos aprender é a .shape, que mostra as dimenções da imagem, através da quantidade de pixels, verticais e horizontais, nessa ordem especificamente, e mostra, também, o sistema de cores utilizado. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(480, 500, 3)\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "img = cv2.imread(\"baboon.bmp\")\n",
    "cv2.imshow(\"MM\",img)\n",
    "print(img.shape)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Vamos, a partir das próximas funções, aprender como manipular pixels e obter informações deles. a fuções são: .item() e .itemset() "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Atraves da função .item(), podemos verificar a intensidade de uma certa coloração em um determinado pixel. É importante citar que o sistema RGB(RED,GREEN,BLUE) no opencv é utilizado de forma inversa, ou seja, BGR."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "54\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "img = cv2.imread(\"baboon.bmp\")\n",
    "cv2.imshow(\"MM\",img)\n",
    "print(img.item(147,109,2))\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Usando a função .itemset(), podemos alterar a cor de pixel. Vamos utilizar o mesmo pixel do exemplo anterior e alterar sua cor.É importante informar no código qual a intensidade de cada canal de cor, lembrando que pela ordem: 0=azul;1=verde;2=vermelho."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "54\n",
      "(480, 500, 3)\n"
     ]
    }
   ],
   "source": [
    "img = cv2.imread(\"baboon.bmp\")\n",
    "print(img.item(147,109,2))\n",
    "print(img.shape)\n",
    "img.itemset((410,290,0),150)\n",
    "img.itemset((410,290,1),0)\n",
    "img.itemset((410,290,2),0)\n",
    "cv2.imshow(\"MM\",img)\n",
    "cv2.imwrite(\"baboon.jpeg\",img)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parâmetros: .item(linha,coluna,codigo de cores do pixel)\n",
    "            .itemset((linha,coluna,codigo de cores do pixel),nova cor do pixel)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Atividade"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Com as funções ensinadas hoje, tente resolver a seguinte atividade:\n",
    "Elabore um programa que mostre uma imagem, leia os valores digitados por um usuário e armazene os valores de coordenadas (y e x), e qual cor ele quer que seja verificado a intensidade e depois mostre esses valores. Além disso faça outras variáveis que permitam a alteração de um pixel específico, escolhidos pelo usuário.\n",
    "Dica: lembre das funções do python (def)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "celltoolbar": "Slideshow",
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
