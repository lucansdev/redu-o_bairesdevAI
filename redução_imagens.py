from PIL import Image
import os
CAMINHO_IMG = os.path.join("flor.jpg")

def gray_scale(image:os.path) -> Image:
    gray_img = Image.open(image).convert("L")
    return gray_img


def black_white(image:os.path) -> Image:
    bw_img = Image.open(image).convert("1")
    return bw_img
    
if os.path.isfile(CAMINHO_IMG):
    img_gray = gray_scale(CAMINHO_IMG)
    bw_img = black_white(CAMINHO_IMG)

    img_gray.show()
    bw_img.show()
    
