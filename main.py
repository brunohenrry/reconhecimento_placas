import cv2
import pytesseract
import numpy as np
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detect_and_recognize_plate(image_path):
    if not os.path.isfile(image_path):
        print(f"Erro: arquivo {image_path} não encontrado.")
        return

    image = cv2.imread(image_path)
    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edged = cv2.Canny(gray, 30, 200)
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    plate = None
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)

        if len(approx) == 4:
            plate = approx
            break

    if plate is None:
        print("Placa não encontrada")
        return

    mask = np.zeros(gray.shape, np.uint8)
    cv2.drawContours(mask, [plate], -1, 255, -1)

    (x, y, w, h) = cv2.boundingRect(plate)
    cropped = gray[y:y+h, x:x+w]

    text = pytesseract.image_to_string(cropped, config='--psm 8')
    print(f"Placa reconhecida: {text.strip()}")

    cv2.imwrite("placa_recortada.jpg", cropped)  # Salvar a imagem recortada para referência
    print(f"Imagem recortada da placa salva como: placa_recortada.jpg")
    print(f"Texto reconhecido: {text.strip()}")

def select_image_file():
    Tk().withdraw()
    file_path = askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        detect_and_recognize_plate(file_path)
    else:
        print("Nenhum arquivo selecionado")

select_image_file()
