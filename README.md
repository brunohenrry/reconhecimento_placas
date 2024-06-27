
# Reconhecimento de Placas de Carro usando Python

Este é um projeto simples de reconhecimento de placas de carro utilizando Python, OpenCV e Tesseract OCR.

## Instalação

Clone o repositório:
```bash
git clone https://github.com/brunohenrry/reconhecimento_placas
cd reconhecimento_placas
```
Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Usar
Certifique-se de ter o Tesseract OCR instalado em seu sistema. Você pode baixá-lo em [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract).

- Execute o script `select_image_file.py` para selecionar uma imagem contendo uma placa de carro.
- O script irá detectar a placa na imagem e reconhecer o texto usando Tesseract OCR.
- O texto reconhecido será exibido no console, e a imagem recortada da placa será salva como `placa_recortada.jpg`.



## Licença

[MIT](https://choosealicense.com/licenses/mit/)

