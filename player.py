import pygame , math
import time

pygame.init()
class Player:
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)
		self.player_size = 50
		self.rect = pygame.Rect(self.x, self.y, self.player_size, self.player_size)
		self.image = pygame.image.load('img/delivery.png')
		self.rotated_image = self.image
		self.angle = 0
		self.velX = 0
		self.velY = 0
		self.left_pressed = False
		self.right_pressed = False
		self.up_pressed = False
		self.down_pressed = False
		self.speed = 4
		self.start_time = time.time()

	# get current cell position of the player
	def get_current_cell(self, x, y, grid_cells):
		for cell in grid_cells:
			if cell.x == x and cell.y == y:
				return cell

	# stops player to pass through walls
	def check_move(self, tile, grid_cells, thickness):
		current_cell_x, current_cell_y = self.x // tile, self.y // tile
		current_cell = self.get_current_cell(current_cell_x, current_cell_y, grid_cells)
		current_cell_abs_x, current_cell_abs_y = current_cell_x * tile, current_cell_y * tile
		if self.left_pressed:
			if current_cell.walls['left']:
				if self.x <= current_cell_abs_x + thickness:
					self.left_pressed = False
		if self.right_pressed:
			if current_cell.walls['right']:
				if self.x >= current_cell_abs_x + tile - (self.player_size + thickness):
					self.right_pressed = False
		if self.up_pressed:
			if current_cell.walls['top']:
				if self.y <= current_cell_abs_y + thickness:
					self.up_pressed = False
		if self.down_pressed:
			if current_cell.walls['bottom']:
				if self.y >= current_cell_abs_y + tile - (self.player_size + thickness):
					self.down_pressed = False

	# drawing player to the screen
	def draw(self, screen):
		screen.blit(self.rotated_image, self.rect)
		elapsed_time = time.time() - self.start_time  
		if elapsed_time > 5:  # Sửa dòng này
			#Che mê cung hiện chỗ vật di chuyển
			screen.fill(pygame.Color("silver"), (self.x, 0, 702-self.x, self.y)) # màn bên phải kéo tới ô vật thể
			if self.x > 602 :
				screen.fill(pygame.Color("silver"), (self.x, self.y + 100,100-(self.x-602), 602-(self.y+100))) #màn ở dưới
			else :
				screen.fill(pygame.Color("silver"), (self.x, self.y + 100, 100, 602-(self.y+100)))
			screen.fill(pygame.Color("silver"), (0, 0 ,self.x, 602)) #màn bên trái
			screen.fill(pygame.Color("silver"), (self.x + 100, self.y , 702-(self.x+100), 602-self.y)) 

	# updates player position while moving
	def update(self):
		self.rotated_image = pygame.transform.rotate(self.image, self.angle)
		self.rect = self.rotated_image.get_rect(center=self.rect.center)
		self.velX = 0
		self.velY = 0
		if self.left_pressed and not self.right_pressed:
			self.velX = -self.speed
			self.angle += 5
		if self.right_pressed and not self.left_pressed:
			self.velX = self.speed
			self.angle -= 5
		if self.up_pressed and not self.down_pressed:
			self.velY = -self.speed
		if self.down_pressed and not self.up_pressed:
			self.velY = self.speed
		self.x += self.velX
		self.y += self.velY

		self.rect = pygame.Rect(int(self.x), int(self.y), self.player_size, self.player_size)
