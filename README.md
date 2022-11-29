# Pratica 6 - SEL0630 - Aplicação de Microprocessadores II

## Alunos

- Lucas Furco Granela - 11299978
- Murilo Mussatto - 11234245
- Pedro Ribas Serras - 11234328

---

## Parte 1 - Câmera

Para a primeira parte da prática foi desenvolvido o código "[camera.py](https://github.com/PedroRibasSerras/SEL0630/blob/main/camera.py)" para interagir com o módulo de câmera conectado à rapsberry pi. O ambiente virtual foi preparado instalando todas as bibliotecas necessárias para a prática e a placa foi configurada para utilizar o módulo da câmera.

Primeiramente, foi importada a biblioteca _"PiCamera"_ para fazer a conexão com a câmera. Em seguida, foi configurado uma rotação de 180 para que a imagem ficasse com a orientação correta no dia da prática. 

O restante do código está dividido em duas partes, na primeira é tirada uma foto com a câmera onde foi inserido um texto na parte superior da imagem. Na segunda parte, foi gravado um vídeo curto, de cinco segundos, mostrando os membros do grupo.

## Parte 2 - Dados Climáticos

Na segunda parte da prática, desenvolveu-se o script "[clima.py](https://github.com/PedroRibasSerras/SEL0630/blob/main/clima.py)" para acessar o banco de dados climáticos da UFSC. Primeiramente, foram importadas as bibliotecas _"requests"_ e _"json"_ para acessar o banco de dados e a biblioteca _"pprint"_ para mostrar os resultados no terminal. Em seguida, foram coletados os dados meteorológicos mais recentes da UFSC, os quais foram apresentados no terminal. 

Dentre os dados obtidos, foram selecionados 4 dados para serem incluídos em uma imagem capturada pela câmera conectada a rasp, utilizando um código similar ao utilizado na Parte 1. Os dados selecionados foram:

- _"updated\_by"_ --> Para mostrar o nome da instituição
- _"updated\_on"_ --> Para mostrar a data de atualização dos dados
- _"ambient\_temp"_ --> Para mostrar a temperatura registrada
- _"humidity"_ --> Para mostrar a umidade registrada

