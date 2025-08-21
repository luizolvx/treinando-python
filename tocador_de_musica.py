import pygame

pygame.init()
pygame.mixer.music.load("C:\Users\oluiz\Downloads\ex01.mp3")
pygame.mixer.music.play()           # inicia a reprodução
pygame.event.wait()                 # mantém o programa aberto até um evento acontecer
