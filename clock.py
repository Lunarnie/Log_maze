import pygame, time, math

pygame.font.init()

class Clock:
	def __init__(self):
		self.start_time = None
		self.elapsed_time = 0
		self.font1 = pygame.font.SysFont("impact", 40)
		self.font2 = pygame.font.SysFont("Paytone One",27)
		self.message_color = pygame.Color("red")
		self.message_color2 = pygame.Color("White")
		self.limit = 30 #second limit time

	# Start the timer
	def start_timer(self):
		self.start_time = time.time()

	# Update the timer
	def update_timer(self):
		if self.start_time is not None:
			self.elapsed_time = time.time() - self.start_time

	# Display the timer
	def display_timer(self):
		secs = int((self.limit-self.elapsed_time % 60))
		mins = int((self.limit-self.elapsed_time) / 60)
		my_time = self.font1.render(f"{mins:02}:{secs:02}", True, self.message_color)
		return my_time
	
	#Money
	def loss_money(self):
		cost = 1000
		fee_money = 5
		if self.elapsed_time > self.limit : 
			total = cost - fee_money*(math.floor(self.elapsed_time-self.limit))
			return self.font2.render(f'You gain {total}$', True, self.message_color2)
		if self.elapsed_time < self.limit and self.elapsed_time > (self.limit - 5) :
			return self.font2.render(f'You gain {cost}$', True, self.message_color2)
		if (self.limit - 10 ) < self.elapsed_time and self.elapsed_time <= (self.limit - 5)  : 
			total = cost + 5
			return self.font2.render(f'You gain {total}$', True, self.message_color2)
		if self.elapsed_time <= (self.limit - 10)  : 
			total = cost + 15
			return self.font2.render(f'You gain {total}$', True, self.message_color2)
    
	# Stop the timer
	def stop_timer(self):
		self.start_time = None
