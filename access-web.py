from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
import signal
import sys

# Função para capturar o sinal de interrupção (Ctrl + C)
def signal_handler(sig, frame):
    print('Interrupção recebida, finalizando...')
    driver.quit()
    sys.exit(0)

# Configurações do navegador em modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa sem interface gráfica
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Caminho do driver do Chromium
service = Service("/usr/bin/chromedriver")  # Ajuste o caminho se necessário

# Inicia o WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Lista de URLs para visitar
URLS = [
    "https://clikdin.com/",
    "https://clikdin.com/cabos-e-conectores-para-sistemas-off-grid-qual-escolher/",
    "https://clikdin.com/como-limpar-conectores-e-cabos-para-melhorar-o-desempenho-de-sistemas-off-grid/",
    "https://clikdin.com/manutencao-de-inversores-off-grid-o-que-verificar-periodicamente/",
    "https://clikdin.com/sustentabilidade-na-educacao-o-papel-da-energia-solar-para-escolas-isoladas/",
    "https://clikdin.com/manutencao-preventiva-de-baterias-off-grid/",
    "https://clikdin.com/como-testar-a-eficiencia-de-paineis-solares-com-multimetro/",
    "https://clikdin.com/melhorando-a-eficiencia-de-paineis-solares-com-suportes-ajustaveis/",
    "https://clikdin.com/dicas-para-armazenamento-seguro-de-paineis-solares-portateis/",
    "https://clikdin.com/top-5-power-banks-solares-para-acessorios-off-grid/",
    "https://clikdin.com/sistemas-off-grid-com-energia-renovavel-mitos-e-verdades-sobre-sustentabilidade/",
    "https://clikdin.com/top-5-equipamentos-sustentaveis-para-viver-fora-da-rede-eletrica/",
    "https://clikdin.com/energia-solar-portatil-para-acampamentos-como-reduzir-seu-impacto-ambiental-na-natureza/",
    "https://clikdin.com/carregadores-portateis-para-dispositivos-usb-em-sistemas-off-grid/",
    "https://clikdin.com/checklist-de-manutencao-para-sistemas-off-grid-antes-de-uma-expedicao/",
    "https://clikdin.com/dicas-para-proteger-sistemas-off-grid-contra-umidade-e-corrosao/",
    "https://clikdin.com/resiliencia-energetica-como-sistemas-off-grid-ajudam-a-enfrentar-mudancas-climaticas/",
    "https://clikdin.com/baterias-portateis-de-ion-litio-vs-gel-qual-a-melhor-para-sistemas-off-grid/",
    "https://clikdin.com/solucoes-off-grid-e-economia-circular-reduzindo-residuos-e-promovendo-sustentabilidade/",
    "https://clikdin.com/paineis-solares-em-mochilas-off-grid/",
    "https://clikdin.com/os-7-melhores-controladores-de-carga-para-sistemas-off-grid-em-2025/",
    "https://clikdin.com/energia-solar-off-grid-a-chave-para-comunidades-sustentaveis-e-autossuficientes/",
    "https://clikdin.com/como-solucoes-off-grid-reduzem-a-pegada-de-carbono-em-areas-remotas/",
    "https://clikdin.com/como-identificar-e-resolver-problemas-em-controladores-de-carga-off-grid/",
    "https://clikdin.com/como-limpar-paineis-solares-portateis-para-garantir-maxima-eficiencia/",
    "https://clikdin.com/detectar-e-corrigir-microfissuras-em-paineis-solares-portateis/",
    "https://clikdin.com/como-usar-filtros-de-agua-portateis-alimentados-por-energia-solar/",
    "https://clikdin.com/como-escolher-inversores-de-energia-para-sistemas-solares-off-grid/",
    "https://clikdin.com/baterias-de-litio-ou-agm-como-escolher-a-melhor-opcao-para-sistemas-off-grid-sustentaveis/",
    "https://clikdin.com/lanternas-solares-para-acampamentos-off-grid/",
    "https://clikdin.com/impacto-ambiental-das-solucoes-off-grid-beneficios-na-preservacao-de-ecossistemas/",
    "https://clikdin.com/desafios-e-solucoes-na-implementacao-de-sistemas-off-grid-sustentaveis-na-america-latina/",
    "https://clikdin.com/category/dicas-de-manutencao/",
    "https://clikdin.com/category/sustentabilidade-e-impacto-ambiental/",
    "https://clikdin.com/category/acessorios/"
]

# Função para simular rolagem na página
def rolar_pagina(driver, vezes=3):
    for _ in range(vezes):
        scroll_pixels = random.randint(300, 800)
        driver.execute_script(f"window.scrollBy(0, {scroll_pixels});")
        time.sleep(random.uniform(1, 3))
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(2)

# Configura o sinal para Ctrl + C
signal.signal(signal.SIGINT, signal_handler)

# Loop infinito
while True:
    for url in URLS:
        print(f"Acessando: {url}")
        driver.get(url)
        time.sleep(3)

        # Simula a rolagem na página
        rolar_pagina(driver, vezes=5)

        # Tenta clicar em links internos da página
        links = driver.find_elements(By.TAG_NAME, "a")
        if links:
            primeiro_link = links[0].get_attribute("href")
            if primeiro_link:
                print(f"Seguindo para: {primeiro_link}")
                driver.get(primeiro_link)
                time.sleep(3)
                rolar_pagina(driver, vezes=3)

# Fecha o navegador
driver.quit()
print("Finalizado!")
