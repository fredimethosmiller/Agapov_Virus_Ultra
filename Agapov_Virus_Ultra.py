
import tkinter as tk
import os
import time
import random

image_folder = "images"
images = ["image1.png", "image2.png", "image3.png"]

def show_random_image(img_path):
    win = tk.Toplevel()
    win.title(img_path)

    # random window position and size
    w = random.randint(200, 600)
    h = random.randint(200, 600)
    x = random.randint(0, 800)
    y = random.randint(0, 400)
    win.geometry(f"{w}x{h}+{x}+{y}")

    img = tk.PhotoImage(file=img_path)
    label = tk.Label(win, image=img)
    label.image = img  # keep a reference
    label.pack(expand=True, fill="both")

root = tk.Tk()
root.withdraw()

index = 0
print("""Меня зовут Михаил Агапов,и ты призвал меня, не очистив Mandadi haldur и оставив свой аккаунт GitHub уязвимым.
Чтобы очистить Mandadi haldur, тебе прежде всего нужно открыть его в проводнике, а после этого открыть Windows mandaat.
Там ты найдёшь свой git-аккаунт (если ты что-то пушил или входил в свой аккаунт через IDE). Нажми на него и выбери Emalda — теперь твои данные в безопасности.

А теперь скажи мне: после всего, что я тебе рассказал, ты будешь очищать Mandadi haldur за собой впредь?""")

while True:
    try:
        answer = input("(Y-Да), (N-Нет) Введите 'Y' или 'N': ").strip().upper()
        if answer not in ("Y", "N"):
            raise ValueError("Неверный ввод. Допустимы только 'Y' или 'N'.")
        break
    except ValueError as e:
        print(e)

if answer == "Y":
    print("Хорошо! Рад это слышать.")
else:
    while True:
        img_path = os.path.join(image_folder, images[index % len(images)])
        show_random_image(img_path)
        root.update()
        index += 1
