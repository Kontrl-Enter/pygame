from pip import main

def install(mname):
    main(["install", mname])

#install("pygame")

import pygame

pygame.init()

pygame.display.set_caption('my game')
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.clock()

while True:
	for event in pygmae.event.get():
		if event.type == pygame.QUIT:
			pygmae.quit()
			sys.exit()

	pygame.display.update()
	clock.tick(60)

