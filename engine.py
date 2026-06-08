import pygame
import sys

# Inicialização do Pygame
pygame.init()

# 1. Configurações da Janela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Spirit: Escape from the Castle")

# 2. Definição de Cores (Paleta baseada no seu README: masmorra azulada/roxa)
COR_FUNDO = (20, 10, 35)        # Roxo bem escuro/sombrio
COR_TEXTO_TITULO = (147, 112, 219) # Roxo médio (Purple)
COR_BOTAO_NORMAL = (48, 25, 84)   # Roxo escuro para os botões
COR_BOTAO_HOVER = (75, 0, 130)    # Índigo (brilha ao passar o mouse)
COR_TEXTO_BOTAO = (240, 240, 255) # Branco azulado

# 3. Fontes
fonte_titulo = pygame.font.SysFont("impact", 50)
fonte_botoes = pygame.font.SysFont("arial", 30)

def desenhar_texto(texto, fonte, cor, superficie, x, y):
    """Função auxiliar para desenhar texto centralizado"""
    objeto_texto = fonte.render(texto, True, cor)
    retangulo_texto = objeto_texto.get_rect()
    retangulo_texto.center = (x, y)
    superficie.blit(objeto_texto, retangulo_texto)

def menu_principal():
    relogio = pygame.time.Clock()

    while True:
        # Define a cor de fundo do castelo sombrio
        tela.fill(COR_FUNDO)

        # Captura a posição atual do mouse
        posicao_mouse = pygame.mouse.get_pos()

        # Desenha o Título do Jogo
        desenhar_texto("SPIRIT: ESCAPE FROM THE CASTLE", fonte_titulo, COR_TEXTO_TITULO, tela, LARGURA // 2, 120)

        # 4. Criação dos Retângulos dos Botões (Centralizados)
        largura_botao, altura_botao = 250, 50
        x_botao = (LARGURA // 2) - (largura_botao // 2)
        
        btn_jogar = pygame.Rect(x_botao, 250, largura_botao, altura_botao)
        btn_creditos = pygame.Rect(x_botao, 330, largura_botao, altura_botao) # Nome da variável atualizado para clareza
        btn_sair = pygame.Rect(x_botao, 410, largura_botao, altura_botao)

        # 5. Lógica de Interação (Hover - Mudar de cor ao passar o mouse)
        # Botão Jogar
        if btn_jogar.collidepoint(posicao_mouse):
            pygame.draw.rect(tela, COR_BOTAO_HOVER, btn_jogar, border_radius=10)
        else:
            pygame.draw.rect(tela, COR_BOTAO_NORMAL, btn_jogar, border_radius=10)

        # Botão Créditos
        if btn_creditos.collidepoint(posicao_mouse):
            pygame.draw.rect(tela, COR_BOTAO_HOVER, btn_creditos, border_radius=10)
        else:
            pygame.draw.rect(tela, COR_BOTAO_NORMAL, btn_creditos, border_radius=10)

        # Botão Sair
        if btn_sair.collidepoint(posicao_mouse):
            pygame.draw.rect(tela, COR_BOTAO_HOVER, btn_sair, border_radius=10)
        else:
            pygame.draw.rect(tela, COR_BOTAO_NORMAL, btn_sair, border_radius=10)

        # 6. Desenhar o texto por cima dos botões (Nome alterado para "Créditos")
        desenhar_texto("Jogar", fonte_botoes, COR_TEXTO_BOTAO, tela, LARGURA // 2, 275)
        desenhar_texto("Créditos", fonte_botoes, COR_TEXTO_BOTAO, tela, LARGURA // 2, 355)
        desenhar_texto("Sair", fonte_botoes, COR_TEXTO_BOTAO, tela, LARGURA // 2, 435)

        # 7. Monitoramento de Eventos (Cliques e Fechamento)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1: # Clique com o botão esquerdo do mouse
                    if btn_jogar.collidepoint(posicao_mouse):
                        print("Iniciar o Jogo!") 
                        # loop_jogo()
                    
                    elif btn_creditos.collidepoint(posicao_mouse):
                        print("Abrir Tela de Créditos!") # Print atualizado
                        # Aqui você criará a tela de créditos futuramente
                        
                    elif btn_sair.collidepoint(posicao_mouse):
                        pygame.quit()
                        sys.exit()

        # Atualiza a tela a 60 Frames Por Segundo
        pygame.display.update()
        relogio.tick(60)

# Para rodar o menu se o script for executado diretamente
if __name__ == "__main__":
    menu_principal()

