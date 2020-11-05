
import cv2
import numpy as np


class VideoPlayer():
	def __init__(self,video_name):
		self.video_name = video_name
		self.max_video_steps = 6
		self.sim_steps = 0

	def sim(self):
		if(self.sim_steps > self.max_video_steps):
			self.sim_steps = 0
		self.sim_steps+=1

	def draw(self):
		print(self.sim_steps)
		folder_name,sep,ext = self.video_name.partition('.')		
		image = cv2.imread(f"{folder_name}/{self.sim_steps}.png")
		cv2.imwrite("current_image.png",image)
		return image

	#writing video images out first makes retrieving them easier
	def video_write(self):
		vidcap = cv2.VideoCapture(self.video_name)
		success,image = vidcap.read()
		count = 0
		while success:
			success,image = vidcap.read()
			folder_name,sep,ext = self.video_name.partition('.')		
			resized = cv2.resize(image, (32,32), interpolation = cv2.INTER_AREA)
			cv2.imwrite(f"{folder_name}/{count}.png",resized)
			count += 1
