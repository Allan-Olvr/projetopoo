import pygame
import sys


pygame.init()


LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Spirit: Escape from the Castle")


COR_FUNDO = (20, 10, 35)        
COR_TEXTO_TITULO = (147, 112, 219) 
COR_BOTAO_NORMAL = (48, 25, 84)   
COR_BOTAO_HOVER = (75, 0, 130)    
COR_TEXTO_BOTAO = (240, 240, 255)


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
        
        tela.fill(COR_FUNDO)

        posicao_mouse = pygame.mouse.get_pos()

        desenhar_texto("SPIRIT: ESCAPE FROM THE CASTLE", fonte_titulo, COR_TEXTO_TITULO, tela, LARGURA // 2, 120)

        largura_botao, altura_botao = 250, 50
        x_botao = (LARGURA // 2) - (largura_botao // 2)
        
        btn_jogar = pygame.Rect(x_botao, 250, largura_botao, altura_botao)
        btn_creditos = pygame.Rect(x_botao, 330, largura_botao, altura_botao) 
        btn_sair = pygame.Rect(x_botao, 410, largura_botao, altura_botao)

      
        if btn_jogar.collidepoint(posicao_mouse):
            pygame.draw.rect(tela, COR_BOTAO_HOVER, btn_jogar, border_radius=10)
        else:
            pygame.draw.rect(tela, COR_BOTAO_NORMAL, btn_jogar, border_radius=10)

      
        if btn_creditos.collidepoint(posicao_mouse):
            pygame.draw.rect(tela, COR_BOTAO_HOVER, btn_creditos, border_radius=10)
        else:
            pygame.draw.rect(tela, COR_BOTAO_NORMAL, btn_creditos, border_radius=10)

      
        if btn_sair.collidepoint(posicao_mouse):
            pygame.draw.rect(tela, COR_BOTAO_HOVER, btn_sair, border_radius=10)
        else:
            pygame.draw.rect(tela, COR_BOTAO_NORMAL, btn_sair, border_radius=10)

       
        desenhar_texto("Jogar", fonte_botoes, COR_TEXTO_BOTAO, tela, LARGURA // 2, 275)
        desenhar_texto("Créditos", fonte_botoes, COR_TEXTO_BOTAO, tela, LARGURA // 2, 355)
        desenhar_texto("Sair", fonte_botoes, COR_TEXTO_BOTAO, tela, LARGURA // 2, 435)

       
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1: 
                    if btn_jogar.collidepoint(posicao_mouse):
                        print("Iniciar o Jogo!") 
                       
                    
                    elif btn_creditos.collidepoint(posicao_mouse):
                        print("Abrir Tela de Créditos!") 
                        
                        
                    elif btn_sair.collidepoint(posicao_mouse):
                        pygame.quit()
                        sys.exit()

       
        pygame.display.update()
        relogio.tick(60)


if __name__ == "__main__":
    menu_principal()

