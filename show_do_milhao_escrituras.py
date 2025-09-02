#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Show do Milhão — Ediçao Escrituras (Bíblia + Livro de Mórmon + D&C)
Dois jogadores no terminal, com rodadas por nível (Fácil, Médio, Difícil),
ajudas (50/50, Pular, Perguntar ao Cônjuge) e placar final.
"""

import random
import sys
import pygame
from time import sleep
from colorama import init, Fore, Back, Style
from tqdm import tqdm
import os
import time

# Limpa o terminal no Windows
os.system('cls')

# Inicializa o colorama
init()

# -------------------------------
# Banco de perguntas
# nivel: "facil" | "medio" | "dificil"
# correta: "A" | "B" | "C" | "D"
# -------------------------------

PERGUNTAS = [
    # ----------------- FACIL (15) -----------------
    {
        "nivel": "facil",
        "pergunta": "Quem construiu uma arca para sobreviver ao dilúvio?",
        "alternativas": ["Abraão", "Noé", "Moisés", "Elias"],
        "correta": "B",
    },
    {
        "nivel": "facil",
        "pergunta": "Quem foi jogado na cova dos leões?",
        "alternativas": ["Davi", "Jonas", "Daniel", "José"],
        "correta": "C",
    },
    {
        "nivel": "facil",
        "pergunta": "Quem foi a mãe de Jesus Cristo?",
        "alternativas": ["Maria", "Isabel", "Marta", "Sara"],
        "correta": "A",
    },
    {
        "nivel": "facil",
        "pergunta": "Qual apóstolo negou Jesus três vezes?",
        "alternativas": ["João", "Pedro", "Tiago", "André"],
        "correta": "B",
    },
    {
        "nivel": "facil",
        "pergunta": "Quem guiou o povo de Israel na saída do Egito?",
        "alternativas": ["Moisés", "Josué", "Arão", "Gideão"],
        "correta": "A",
    },
    {
        "nivel": "facil",
        "pergunta": "Quem foi o irmão de Néfi?",
        "alternativas": ["Mórmon", "Morôni", "Lamã", "Enoque"],
        "correta": "C",
    },
    {
        "nivel": "facil",
        "pergunta": "Quem foi o profeta que batizou Jesus Cristo?",
        "alternativas": ["João Batista", "Isaías", "Elias", "Jeremias"],
        "correta": "A",
    },
    {
        "nivel": "facil",
        "pergunta": "Quem foi o primeiro homem criado por Deus?",
        "alternativas": ["Adão", "Sete", "Abel", "Caim"],
        "correta": "A",
    },
    {
        "nivel": "facil",
        "pergunta": "Quem escreveu a maioria das cartas do Novo Testamento?",
        "alternativas": ["Paulo", "João", "Pedro", "Lucas"],
        "correta": "A",
    },
    {
        "nivel": "facil",
        "pergunta": "Quem viu a visão da “árvore da vida” no Livro de Mórmon?",
        "alternativas": ["Néfi", "Leí", "Alma", "Mórmon"],
        "correta": "B",
    },
    {
        "nivel": "facil",
        "pergunta": "Em qual livro encontramos os Dez Mandamentos?",
        "alternativas": ["Gênesis", "Êxodo", "Levítico", "Números"],
        "correta": "B",
    },
    {
        "nivel": "facil",
        "pergunta": "Quem foi o pai de Lamã e Lemuel?",
        "alternativas": ["Alma", "Mórmon", "Leí", "Amuleque"],
        "correta": "C",
    },
    {
        "nivel": "facil",
        "pergunta": "Qual apóstolo andou sobre as águas junto com Jesus?",
        "alternativas": ["Tiago", "Pedro", "João", "Tomé"],
        "correta": "B",
    },
    {
        "nivel": "facil",
        "pergunta": "Quem interpretou o sonho do faraó no Egito?",
        "alternativas": ["José", "Moisés", "Daniel", "Salomão"],
        "correta": "A",
    },
    {
        "nivel": "facil",
        "pergunta": "Quem foi o profeta que recebeu as placas de ouro do anjo Morôni?",
        "alternativas": ["Joseph Smith", "Brigham Young", "Oliver Cowdery", "Sidney Rigdon"],
        "correta": "A",
    },

    # ----------------- MEDIO (15) -----------------
    {
        "nivel": "medio",
        "pergunta": "Qual foi o profeta que sucedeu Moisés como líder de Israel?",
        "alternativas": ["Gideão", "Josué", "Samuel", "Davi"],
        "correta": "B",
    },
    {
        "nivel": "medio",
        "pergunta": "Qual foi o primeiro rei de Israel?",
        "alternativas": ["Saul", "Davi", "Salomão", "Roboão"],
        "correta": "A",
    },
    {
        "nivel": "medio",
        "pergunta": "Quem foi o último profeta a escrever no Livro de Mórmon?",
        "alternativas": ["Alma", "Néfi", "Morôni", "Helamã"],
        "correta": "C",
    },
    {
        "nivel": "medio",
        "pergunta": "Onde Jesus Cristo realizou seu primeiro milagre?",
        "alternativas": ["Jerusalém", "Caná da Galileia", "Belém", "Nazaré"],
        "correta": "B",
    },
    {
        "nivel": "medio",
        "pergunta": "Quem foi a esposa de Adão?",
        "alternativas": ["Sara", "Eva", "Rebeca", "Raquel"],
        "correta": "B",
    },
    {
        "nivel": "medio",
        "pergunta": "Em Doutrina e Convênios, qual revelação fala sobre a Palavra de Sabedoria?",
        "alternativas": ["42", "76", "89", "121"],
        "correta": "C",
    },
    {
        "nivel": "medio",
        "pergunta": "Quem escreveu o livro de Apocalipse?",
        "alternativas": ["João", "Pedro", "Paulo", "Lucas"],
        "correta": "A",
    },
    {
        "nivel": "medio",
        "pergunta": "Quem traduziu o Livro de Mórmon?",
        "alternativas": ["Brigham Young", "Joseph Smith", "Oliver Cowdery", "Sidney Rigdon"],
        "correta": "B",
    },
    {
        "nivel": "medio",
        "pergunta": "Quem recebeu a revelação da Primeira Visão?",
        "alternativas": ["Brigham Young", "Joseph Smith", "Morôni", "Samuel Smith"],
        "correta": "B",
    },
    {
        "nivel": "medio",
        "pergunta": "Qual foi a cidade onde nasceu Jesus Cristo?",
        "alternativas": ["Nazaré", "Jerusalém", "Belém", "Cafarnaum"],
        "correta": "C",
    },
    {
        "nivel": "medio",
        "pergunta": "Qual profeta enfrentou os sacerdotes de Baal no Monte Carmelo?",
        "alternativas": ["Isaías", "Elias", "Jeremias", "Eliseu"],
        "correta": "B",
    },
    {
        "nivel": "medio",
        "pergunta": "Quem foi levado ao céu em um carro de fogo?",
        "alternativas": ["Moisés", "Elias", "Enoque", "Eliseu"],
        "correta": "B",
    },
    {
        "nivel": "medio",
        "pergunta": "Em qual rio Jesus foi batizado?",
        "alternativas": ["Jordão", "Tigre", "Nilo", "Eufrates"],
        "correta": "A",
    },
    {
        "nivel": "medio",
        "pergunta": "Quem foi o rei que construiu o templo em Jerusalém?",
        "alternativas": ["Saul", "Davi", "Salomão", "Ezequias"],
        "correta": "C",
    },
    {
        "nivel": "medio",
        "pergunta": "Quem foi o profeta que viu os últimos dias e escreveu sobre guerras, pestes e terremotos?",
        "alternativas": ["Isaías", "Jeremias", "Ezequiel", "Amós"],
        "correta": "C",
    },

    # ----------------- DIFICIL (15) -----------------
    {
        "nivel": "dificil",
        "pergunta": "Em Doutrina e Convênios, qual seção fala sobre o sacerdócio de Melquisedeque?",
        "alternativas": ["84", "107", "121", "132"],
        "correta": "B",
    },
    {
        "nivel": "dificil",
        "pergunta": "Quem foi o profeta que viu o Senhor no templo e disse: “Aqui estou, envia-me”?",
        "alternativas": ["Isaías", "Jeremias", "Ezequiel", "Amós"],
        "correta": "A",
    },
    {
        "nivel": "dificil",
        "pergunta": "Qual o nome da esposa de Alma, o filho?",
        "alternativas": ["Isabel", "Sara", "Não é mencionado", "Míriam"],
        "correta": "C",
    },
    {
        "nivel": "dificil",
        "pergunta": "Quem foi o profeta que recebeu a revelação conhecida como “A Visão” (Seção 76 de D&C)?",
        "alternativas": ["Sidney Rigdon", "Joseph Smith", "Oliver Cowdery", "Brigham Young"],
        "correta": "B",
    },
    {
        "nivel": "dificil",
        "pergunta": "Qual foi o rei que jogou três jovens hebreus na fornalha ardente?",
        "alternativas": ["Dario", "Nabucodonosor", "Ciro", "Artaxerxes"],
        "correta": "B",
    },
    {
        "nivel": "dificil",
        "pergunta": "Quem foi o profeta que escreveu as placas pequenas no Livro de Mórmon?",
        "alternativas": ["Néfi", "Morôni", "Mórmon", "Alma"],
        "correta": "A",
    },
    {
        "nivel": "dificil",
        "pergunta": "Qual o nome da montanha onde Moisés recebeu os Dez Mandamentos?",
        "alternativas": ["Sinai", "Horebe", "Nebo", "Carmelo"],
        "correta": "A",
    },
    {
        "nivel": "dificil",
        "pergunta": "Quem foi o profeta que viu a visão do vale de ossos secos?",
        "alternativas": ["Isaías", "Jeremias", "Ezequiel", "Daniel"],
        "correta": "C",
    },
    {
        "nivel": "dificil",
        "pergunta": "Em qual cidade Joseph Smith foi martirizado?",
        "alternativas": ["Kirtland", "Nauvoo", "Carthage", "Palmyra"],
        "correta": "C",
    },
    {
        "nivel": "dificil",
        "pergunta": "Qual profeta escreveu sobre a vinda de Cristo cinco séculos antes de Seu nascimento, mencionando Maria pelo nome?",
        "alternativas": ["Néfi", "Alma", "Isaías", "Rei Benjamim"],
        "correta": "A",
    },
    {
        "nivel": "dificil",
        "pergunta": "Quem foi o apóstolo que teve a revelação de levar o evangelho aos gentios?",
        "alternativas": ["Pedro", "Paulo", "Tiago", "João"],
        "correta": "A",
    },
    {
        "nivel": "dificil",
        "pergunta": "Em qual ano foi organizada oficialmente a Igreja de Jesus Cristo dos Santos dos Últimos Dias?",
        "alternativas": ["1820", "1829", "1830", "1836"],
        "correta": "C",
    },
    {
        "nivel": "dificil",
        "pergunta": "Quem foi o profeta que profetizou a vinda dos Jareditas?",
        "alternativas": ["Enoque", "Morôni", "Éter", "Mósiá"],
        "correta": "C",
    },
    {
        "nivel": "dificil",
        "pergunta": "Quem escreveu as últimas palavras no Livro de Mórmon?",
        "alternativas": ["Mórmon", "Morôni", "Alma", "Helamã"],
        "correta": "B",
    },
    {
        "nivel": "dificil",
        "pergunta": "Qual é o nome do lugar onde Adão reuniu seus descendentes antes de morrer, segundo Doutrina e Convênios?",
        "alternativas": ["Sião", "Adão-ondi-Amã", "Monte Moriá", "Vale de Josafá"],
        "correta": "B",
    },
]

PONTOS = {"facil": 100, "medio": 300, "dificil": 600}

AJUDAS_POR_JOGADOR = {
    "5050": 4,       # elimina 2 alternativas erradas
    "pular": 2,      # pula a pergunta sem pontuar
    "perguntar": 0,  # o outro jogador pode dar um palpite antes da resposta final
}

BANNER = r"""
====================================================
        S H O W   D O   M I L H Ã O — Escrituras
====================================================
Regras rápidas:
- 3 rodadas: Fácil (100 pts), Médio (300 pts), Difícil (600 pts).
- Ajudas (1x por jogador): [50/50], [PULAR], [PERGUNTAR].
- Alternem turnos; vence quem somar mais pontos.
- Digite A, B, C ou D para responder. Digite AJUDA para usar.
Boa sorte!
"""

def input_nao_vazio(msg: str) -> str:
    while True:
        s = input(msg).strip()
        if s:
            return s

def escolher_ordem_jogadores(j1, j2):
    ordem = [j1, j2]
    random.shuffle(ordem)
    return ordem

def listar_ajudas(estado):
    disponiveis = []
    for k, v in estado.items():
        if v > 0:
            disponiveis.append(k)
    return ", ".join(disponiveis) if disponiveis else "Nenhuma"

def aplicar_5050(alternativas, correta_letra):
    # Retorna um conjunto de letras que permanecerão após 50/50
    letras = ["A", "B", "C", "D"]
    erradas = [l for l in letras if l != correta_letra]
    remover = random.sample(erradas, 2)
    restantes = [l for l in letras if l not in remover]
    return restantes

def perguntar_conjuge(nome_conjuge, alternativas):
    print(f"\n{nome_conjuge}, qual seu palpite? (A/B/C/D) — isso NÃO fixa a resposta do outro.")
    while True:
        palpite = input("Palpite do cônjuge: ").strip().upper()
        if palpite in ["A", "B", "C", "D"]:
            print(f"{nome_conjuge} palpita: {palpite}")
            return palpite
        print("Entrada inválida. Tente A, B, C ou D.")

def loading_animation(text, duration=2):
    for _ in tqdm(range(100), desc=text, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
        sleep(duration/100)

def print_banner():
    print(Fore.YELLOW + Style.BRIGHT + BANNER + Style.RESET_ALL)

def print_question(nivel, pontos, pergunta):
    nivel_cores = {
        "facil": Fore.GREEN,
        "medio": Fore.YELLOW,
        "dificil": Fore.RED
    }
    print("\n" + "="*60)
    print(nivel_cores[nivel] + f"NÍVEL: {nivel.upper()} - Vale {pontos} pontos" + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + pergunta + Style.RESET_ALL)

def print_alternativa(letra, texto, letras_visiveis=None):
    if letras_visiveis and letra not in letras_visiveis:
        return
    print(Fore.WHITE + f"  {letra}) " + Style.RESET_ALL + texto)

def print_resultado(correto, pontos=0):
    if correto:
        print(Fore.GREEN + Style.BRIGHT + f"✅ CORRETO! +{pontos} pontos!" + Style.RESET_ALL)
    else:
        print(Fore.RED + Style.BRIGHT + "❌ INCORRETO!" + Style.RESET_ALL)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, speed=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def loading_question():
    clear_terminal()
    print("\nCarregando próxima pergunta:")
    width = 40
    for i in range(width + 1):
        progress = "█" * i + "▒" * (width - i)
        percentage = (i / width) * 100
        print(f"\r[{progress}] {percentage:.1f}%", end='', flush=True)
        time.sleep(0.03)
    print("\n")

def apresentar_pergunta(item, nome_jogador, estado_ajudas, nome_conjuge):
    loading_question()  # Nova animação de carregamento
    
    print("\n" + "="*60)
    print(Fore.CYAN + f"Jogador: {nome_jogador}" + Style.RESET_ALL)
    
    # Efeito de digitação para a pergunta
    print_question(item["nivel"], PONTOS[item["nivel"]], "")
    typing_effect(item["pergunta"])
    
    letras = ["A", "B", "C", "D"]
    alternativas = dict(zip(letras, item["alternativas"]))
    letras_visiveis = letras[:]

    while True:
        for l in letras_visiveis:
            print_alternativa(l, alternativas[l], letras_visiveis)
            time.sleep(0.3)  # Pequena pausa entre alternativas
        
        print(Fore.YELLOW + f"\nAjudas: {listar_ajudas(estado_ajudas)}" + Style.RESET_ALL)
        resp = input(Fore.WHITE + "Sua resposta (A/B/C/D) ou AJUDA: " + Style.RESET_ALL).strip().upper()

        if resp in letras_visiveis:
            return resp  # resposta final
        if resp == "AJUDA":
            if all(v == 0 for v in estado_ajudas.values()):
                print("Você não tem mais ajudas.")
                continue
            print("Ajudas: [50/50] [PULAR] [PERGUNTAR]")
            escolha = input("Qual ajuda deseja usar? ").strip().lower()

            if escolha in ("50/50", "5050", "50"):
                if estado_ajudas["5050"] <= 0:
                    print("50/50 já foi utilizada.")
                    continue
                estado_ajudas["5050"] -= 1
                letras_visiveis = aplicar_5050(alternativas, item["correta"])
                print("50/50 aplicado! Restaram: " + ", ".join(letras_visiveis))
                continue

            elif escolha in ("pular", "pula", "skip"):
                if estado_ajudas["pular"] <= 0:
                    print("Pular já foi utilizado.")
                    continue
                estado_ajudas["pular"] -= 1
                print("Pergunta pulada. Sem pontos nesta vez.")
                return None  # pulou

            elif escolha in ("perguntar", "conjuge", "ajuda"):
                if estado_ajudas["perguntar"] <= 0:
                    print("Perguntar ao cônjuge já foi utilizada.")
                    continue
                estado_ajudas["perguntar"] -= 1
                perguntar_conjuge(nome_conjuge, alternativas)
                # volta para escolher resposta
                continue
            else:
                print("Ajuda inválida.")
                continue
        else:
            print("Entrada inválida. Tente A, B, C, D ou AJUDA.")

def jogar_rodada(perguntas_nivel, jogadores, placar, ajudas_por_jogador):
    # Alterna entre jogadores para as perguntas deste nível
    idx_jogador = 0
    for item in perguntas_nivel:
        nome = jogadores[idx_jogador]
        outro = jogadores[(idx_jogador + 1) % 2]

        resp = apresentar_pergunta(item, nome, ajudas_por_jogador[nome], outro)
        if resp is None:
            # pulou
            sleep(2)  # Espera 2 segundos antes da próxima pergunta
        else:
            if resp == item["correta"]:
                pontos = PONTOS[item["nivel"]]
                placar[nome] += pontos
                print(f"✅ Resposta correta! +{pontos} pontos.")
                try:
                    pygame.init()
                    pygame.mixer.init()
                    pygame.mixer.music.load("acertou.mp3")
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.5)
                    # Espera a música tocar
                    while pygame.mixer.music.get_busy():
                        pygame.time.Clock().tick(10)
                    sleep(1)  # Espera adicional após a música
                except Exception as e:
                    print(f"Erro ao tocar música: {e}")
                    sleep(2)  # Se não tocar música, espera 2 segundos
            else:
                # Mostra apenas uma vez a resposta incorreta
                print(Fore.RED + Style.BRIGHT + "❌ INCORRETO!" + Style.RESET_ALL)
                try:
                    pygame.init()
                    pygame.mixer.init()
                    pygame.mixer.music.load("errou.mp3")
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.5)
                    while pygame.mixer.music.get_busy():
                        pygame.time.Clock().tick(10)
                except Exception as e:
                    print(f"Erro ao tocar música: {e}")
                
                # Mostra a resposta correta formatada
                print(Fore.GREEN + Style.BRIGHT + f"\nA resposta correta era a alternativa {item['correta']}:" + Style.RESET_ALL)
                print(Fore.GREEN + f"  {item['correta']}) {item['alternativas'][ord(item['correta'])-ord('A')]}" + Style.RESET_ALL)
                sleep(3)  # Espera para ler a resposta
        
        # Animação de transição antes da próxima pergunta
        print("\nPróxima pergunta em...")
        for i in range(3, 0, -1):
            print(f"{i}...")
            sleep(1)
        
        # troca jogador
        idx_jogador = (idx_jogador + 1) % 2

def main():
    print_banner()
    loading_animation("Carregando o jogo", 2)
    try:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("intro.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)  # Ajusta volume para 50%
    except Exception as e:
        print(f"Erro ao tocar música: {e}")
        print("Verifique se o arquivo intro.mp3 está na pasta do jogo")

    j1 = input_nao_vazio(Fore.CYAN + "Nome do(a) Jogador(a) 1: " + Style.RESET_ALL)
    j2 = input_nao_vazio(Fore.CYAN + "Nome do(a) Jogador(a) 2: " + Style.RESET_ALL)
    
    loading_animation("Sorteando ordem dos jogadores", 1)
    jogadores = escolher_ordem_jogadores(j1, j2)
    print(Fore.GREEN + f"\nOrdem sorteada: {jogadores[0]} começa, depois {jogadores[1]}.\n" + Style.RESET_ALL)

    # separa perguntas por nível e embaralha
    faciles = [p for p in PERGUNTAS if p["nivel"] == "facil"]
    medios  = [p for p in PERGUNTAS if p["nivel"] == "medio"]
    dificeis= [p for p in PERGUNTAS if p["nivel"] == "dificil"]
    random.shuffle(faciles)
    random.shuffle(medios)
    random.shuffle(dificeis)

    # quantas por nível? padrão: todas (15 cada)
    print("Configuração rápida (pressione Enter para usar o padrão).")
    print("Se for para reunião familiar considere 8/8/8")
    try:
        qtd_f = input("Quantas perguntas FÁCEIS (1-15, padrão 15)? ").strip()
        qtd_m = input("Quantas perguntas MÉDIAS (1-15, padrão 15)? ").strip()
        qtd_d = input("Quantas perguntas DIFÍCEIS (1-15, padrão 15)? ").strip()
        qtd_f = 15 if qtd_f == "" else max(1, min(15, int(qtd_f)))
        qtd_m = 15 if qtd_m == "" else max(1, min(15, int(qtd_m)))
        qtd_d = 15 if qtd_d == "" else max(1, min(15, int(qtd_d)))
    except ValueError:
        print("Entrada inválida. Usando padrão 15/15/15.")
        qtd_f = qtd_m = qtd_d = 15

    faciles = faciles[:qtd_f]
    medios  = medios[:qtd_m]
    dificeis= dificeis[:qtd_d]

    placar = {jogadores[0]: 0, jogadores[1]: 0}
    ajudas_por_jogador = {
        jogadores[0]: dict(AJUDAS_POR_JOGADOR),
        jogadores[1]: dict(AJUDAS_POR_JOGADOR),
    }

    try:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("boasorte.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)  # Ajusta volume para 50%
    except Exception as e:
        print(f"Erro ao tocar música: {e}")
        print("Verifique se o arquivo boasorte.mp3 está na pasta do jogo")

    print("\n===== RODADA FÁCIL =====")
    jogar_rodada(faciles, jogadores, placar, ajudas_por_jogador)

    print("\n===== RODADA MÉDIA =====")
    jogar_rodada(medios, jogadores, placar, ajudas_por_jogador)

    print("\n===== RODADA DIFÍCIL =====")
    jogar_rodada(dificeis, jogadores, placar, ajudas_por_jogador)

    clear_terminal()

    print("\n" + "="*60)
    print(Fore.YELLOW + Style.BRIGHT + "F I M   D O   J O G O" + Style.RESET_ALL)
    print("="*60)
    print(Fore.CYAN + "Placar final:" + Style.RESET_ALL)
    print(f" - {jogadores[0]}: {Fore.GREEN}{placar[jogadores[0]]} pontos{Style.RESET_ALL}")
    print(f" - {jogadores[1]}: {Fore.GREEN}{placar[jogadores[1]]} pontos{Style.RESET_ALL}")

    if placar[jogadores[0]] > placar[jogadores[1]]:
        print(Fore.YELLOW + Style.BRIGHT + f"\n🏆 Campeão(ã): {jogadores[0]}! Parabéns!" + Style.RESET_ALL)
        try:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("final.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.5)
            # Espera a música terminar
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except Exception as e:
            print(f"Erro ao tocar música: {e}")
            print("Verifique se o arquivo final.mp3 está na pasta do jogo")

    elif placar[jogadores[1]] > placar[jogadores[0]]:
        print(Fore.YELLOW + Style.BRIGHT + f"\n🏆 Campeão(ã): {jogadores[1]}! Parabéns!" + Style.RESET_ALL)
        try:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("final.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.5)
            # Espera a música terminar
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except Exception as e:
            print(f"Erro ao tocar música: {e}")
            print("Verifique se o arquivo final.mp3 está na pasta do jogo")

    else:
        print(Fore.YELLOW + Style.BRIGHT + "\n🤝 Empate! Que casal entrosado!" + Style.RESET_ALL)
        try:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("final.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.5)
            # Espera a música terminar
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except Exception as e:
            print(f"Erro ao tocar música: {e}")
            print("Verifique se o arquivo final.mp3 está na pasta do jogo")

    print("\nDica: Quer revisar respostas? Façam juntos com as escrituras abertas. 😉")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSaindo... Até a próxima!")
        sys.exit(0)
