import subprocess


# scripts = [
#     'second_task\\producer.py',
#     'second_task\\consumer_email.py',
#     'second_task\\consumer_sms.py'
# ]


# def run_scripts():
#     for script in scripts:
#         subprocess.Popen([r'C:\Users\MikeK\PycharmProjects\in_process\goit-pyweb-hw-08\.venv\Scripts\python', script])
#         print(f"Запущено {script}")


# for script in scripts:
#     subprocess.Popen([r'C:\Users\MikeK\PycharmProjects\in_process\goit-pyweb-hw-08\.venv\Scripts\python', script])
#     print(f"Запущено {script}")


# if __name__ == "__main__":
#     run_scripts()


# python second_task\run_all.py


import tkinter as tk
from subprocess import Popen

def run_script(script):
    Popen(script, shell=True)

app = tk.Tk()
app.title("Запускач скриптів")

frame = tk.Frame(app)
frame.pack(pady=20)

# Кнопки для запуску кожного скрипту
btn_producer = tk.Button(frame, text="Запустити Producer", command=lambda: run_script("dist/producer.exe"))
btn_producer.pack(side=tk.LEFT, padx=10)

btn_consumer_email = tk.Button(frame, text="Запустити Consumer Email", command=lambda: run_script("dist/consumer_email.exe"))
btn_consumer_email.pack(side=tk.LEFT, padx=10)

btn_consumer_sms = tk.Button(frame, text="Запустити Consumer SMS", command=lambda: run_script("dist/consumer_sms.exe"))
btn_consumer_sms.pack(side=tk.LEFT, padx=10)

app.mainloop()

