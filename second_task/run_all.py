import subprocess


scripts = [
    'second_task\\producer.py',
    'second_task\\consumer_email.py',
    'second_task\\consumer_sms.py'
]


# def run_scripts():
#     for script in scripts:
#         subprocess.Popen([r'C:\Users\MikeK\PycharmProjects\in_process\goit-pyweb-hw-08\.venv\Scripts\python', script])
#         print(f"Запущено {script}")


for script in scripts:
    subprocess.Popen([r'C:\Users\MikeK\PycharmProjects\in_process\goit-pyweb-hw-08\.venv\Scripts\python', script])
    print(f"Запущено {script}")


# if __name__ == "__main__":
#     run_scripts()


# python second_task\run_all.py
