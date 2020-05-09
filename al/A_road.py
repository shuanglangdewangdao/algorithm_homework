from random import randint
from matplotlib import pyplot as plt
import numpy as np
import math
import copy
#可行动的点
class SearchEntry():
	def __init__(self, x, y, g_cost, f_cost=0, pre_entry=None):
		self.x = x
		self.y = y
		self.g_cost = g_cost
		self.f_cost = f_cost
		self.pre_entry = pre_entry
	
	def getPos(self):
		return (self.x, self.y)
##地图类
class Map():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.map = [[0 for x in range(self.width)] for y in range(self.height)]
	##随机产生障碍
	def createBlock(self, block_num):
		for i in range(block_num):
			x, y = (randint(0, self.width-1), randint(0, self.height-1))
			self.map[x][y] = 4
		for i in range(block_num):
			x, y = (randint(0, self.width-1), randint(0, self.height-1))
			self.map[x][y] = 2
		for i in range(block_num):
			x, y = (randint(0, self.width-1), randint(0, self.height-1))
			self.map[x][y] = 100		
	#添加一个可移动的点用以随机设定入口出口
	def generatePos(self, rangeX, rangeY):
		x, y = (randint(rangeX[0], rangeX[1]), randint(rangeY[0], rangeY[1]))
		while self.map[x][y] == 100:
			x, y = (randint(rangeX[0], rangeX[1]), randint(rangeY[0], rangeY[1]))
		return (x , y)

	def showMapplot(self):
		fig=plt.figure(figsize=(16,16))
		vlines = np.linspace(0,self.width,num=self.width+1)
		hlines = np.linspace(0,self.height,num=self.height+1)
		plt.hlines(hlines,min(vlines),max(vlines))
		plt.vlines(vlines,min(hlines),max(hlines))
		for x in range(self.width):
			for y in range(self.height):
				if self.map[y][x]==4:
					# print(x,y)
					x1 = np.array([i for i in range(x,x+2,1)])
					plt.fill_between(x1,y+1,y,facecolor="yellow")
				elif self.map[y][x]==2:
					x1 = np.array([i for i in range(x,x+2,1)])
					plt.fill_between(x1,y+1,y,facecolor="blue")
				elif self.map[y][x]==1:
					x1 = np.array([i for i in range(x,x+2,1)])
					plt.fill_between(x1,y+1,y,facecolor="red")
				elif self.map[y][x]==3:
					x1 = np.array([i for i in range(x,x+2,1)])
					plt.fill_between(x1,y+1,y,facecolor="green")
				elif self.map[y][x]==100:
					x1 = np.array([i for i in range(x,x+2,1)])
					plt.fill_between(x1,y+1,y,facecolor="grey")
		plt.show()
def AStarSearch(map, source, dest, modle):

	##获取移动后位置
	def getNewPosition(map, location, offset):
		x,y = (location.x + offset[0], location.y + offset[1])
		if x < 0 or x >= map.width or y < 0 or y >= map.height or map.map[x][y] == 100:
			return None
		return (x, y)
	#获取的移动后位置能否加入列表中
	def getPositions(map, location):
		offsets = [(-1,0), (0, -1), (1, 0), (0, 1), (-1,-1), (1, -1), (-1, 1), (1, 1)]
		poslist = []
		for offset in offsets:
			pos = getNewPosition(map, location, offset)
			if pos is not None:
				poslist.append(pos)
		return poslist
	
	# 使用距离做估计
	def calHeuristic(pos, dest):
		return abs(dest.x - pos[0]) + abs(dest.y - pos[1])
	#移动消耗斜向为sqrt(2)其他为1
	def getMoveCost(location, pos):
		if location.x != pos[0] and location.y != pos[1]:
			return math.sqrt(2)
		else:
			return 1

	# 检查是否在列表中
	def isInList(list, pos):
		if pos in list:
			return list[pos]
		return None
	
	# 添加周围的可行点
	def addAdjacentPositions(map, location, dest, openlist, closedlist):
		poslist = getPositions(map, location)
		for pos in poslist:
			if isInList(closedlist, pos) is None:
				findEntry = isInList(openlist, pos)
				h_cost = calHeuristic(pos, dest)
				g_cost = location.g_cost + getMoveCost(location, pos) + map.map[location.y][location.x]
				if findEntry is None :
					openlist[pos] = SearchEntry(pos[0], pos[1], g_cost, g_cost+h_cost, location)
				elif findEntry.g_cost > g_cost:
					findEntry.g_cost = g_cost
					findEntry.f_cost = g_cost + h_cost
					findEntry.pre_entry = location
	
	# 寻找f最小的点
	def getFastPosition(openlist):
		fast = None
		for entry in openlist.values():
			if fast is None:
				fast = entry
			elif fast.f_cost > entry.f_cost:
				fast = entry
		return fast
	# def AStar2Search(map, source, dest):
	# 	sourceopenlist = {}
	# 	destopenlist = {}
	# 	sourceclosedlist = {}
	# 	destclosedlist = {}
	# 	sourcelocation = SearchEntry(source[0], source[1], map.map[source[1]][source[0]])
	# 	destlocation = SearchEntry(dest[0], dest[1], map.map[dest[1]][dest[0]])
	# 	sourceopenlist[source] = sourcelocation
	# 	destopenlist[dest] = destlocation
	# 	while True:
	# 		sourcelocation = getFastPosition(sourceopenlist)
	# 		if sourcelocation is None:
	# 			print("can't find valid path")
	# 			break
	# 		if sourcelocation.x == destlocation.x and sourcelocation.y == destlocation.y:
	# 			break
	# 		sourcelosedlist[sourcelocation.getPos()] = sourcelocation
	# 		sourceopenlist.pop(sourcelocation.getPos())
	# 		addAdjacentPositions(map, sourcelocation, destlocation, sourceopenlist, sourceclosedlist)
			
	# 		destlocation = getFastPosition(destopenlist)
	# 		if destlocation is None:
	# 			print("can't find valid path")
	# 			break
	# 		destlosedlist[destlocation.getPos()] = destlocation
	# 		destopenlist.pop(destlocation.getPos())
	# 		addAdjacentPositions(map, destlocation, sourcelocation, destopenlist, destclosedlist)


	# 	while True:
	# 		if sourcelocation is not None:
	# 			map.map[sourcelocation.y][sourcelocation.x] = 1
	# 			sourcelocation=sourcelocation.pre_entry
	# 			map.showMapplot()
	# 		if destlocation is not None:
	# 			map.map[destlocation.y][destlocation.x] = 1
	# 			destlocation=destlocation.pre_entry
	# 			map.showMapplot()
	# 		if sourcelocation is None & destlocation is None:
	# 			break
	#openlist是可以使用的,closedlist是用过的
	if modle == 1:
		openlist = {}
		closedlist = {}
		location = SearchEntry(source[0], source[1], map.map[source[1]][source[0]])
		dest = SearchEntry(dest[0], dest[1], 0.0)
		openlist[source] = location
		while True:
			location = getFastPosition(openlist)
			if location is None:
				print("can't find valid path")
				break
		
			if location.x == dest.x and location.y == dest.y:
				break
			closedlist[location.getPos()] = location
			openlist.pop(location.getPos())
			addAdjacentPositions(map, location, dest, openlist, closedlist)
		while location is not None:
			map.map[location.y][location.x] = 1
			location = location.pre_entry
	else:
		sourceopenlist = {}
		destopenlist = {}
		sourceclosedlist = {}
		destclosedlist = {}
		sourcelocation = SearchEntry(source[0], source[1], map.map[source[1]][source[0]])
		destlocation = SearchEntry(dest[0], dest[1], map.map[dest[1]][dest[0]])
		sourceopenlist[source] = sourcelocation
		destopenlist[dest] = destlocation
		while True:
			sourcelocation = getFastPosition(sourceopenlist)
			destlocation = getFastPosition(destopenlist)
			if sourcelocation.x == destlocation.x and sourcelocation.y == destlocation.y:
				break
			
			if sourcelocation is None:
				print("can't find valid path")
				break
			sourceclosedlist[sourcelocation.getPos()] = sourcelocation
			sourceopenlist.pop(sourcelocation.getPos())
			addAdjacentPositions(map, sourcelocation, destlocation, sourceopenlist, sourceclosedlist)
			
			# destlocation = getFastPosition(destopenlist)
			if destlocation is None:
				print("can't find valid path")
				break
			destclosedlist[destlocation.getPos()] = destlocation
			destopenlist.pop(destlocation.getPos())
			addAdjacentPositions(map, destlocation, sourcelocation, destopenlist, destclosedlist)
		sourceres = []
		while sourcelocation is not None:
			sourceres.append(sourcelocation)
			sourcelocation = sourcelocation.pre_entry
		destres = []
		while destlocation is not None:
			destres.append(destlocation)
			destlocation = destlocation.pre_entry
		length = len(sourceres)
		if len(destres) > length:
			length = len(destres)
		for i in  range(length):
			if sourceres:
				s=sourceres.pop()
				map.map[s.y][s.x] = 1
				map.showMapplot()
			if destres:
				d=destres.pop()
				map.map[d.y][d.x] = 3
				map.showMapplot()


	
WIDTH = 10
HEIGHT = 10
BLOCK_NUM = 20
map = Map(WIDTH, HEIGHT)
map.createBlock(BLOCK_NUM)
# map.showMap()
map.showMapplot()

# source = map.generatePos((0,WIDTH//3),(0,HEIGHT//3))
# dest = map.generatePos((WIDTH//2,WIDTH-1),(HEIGHT//2,HEIGHT-1))
source = (0,0)
dest = (9,9)
print("source:", source)
print("dest:", dest)
map1=Map(WIDTH, HEIGHT)
map1.map=copy.deepcopy(map.map)
AStarSearch(map1, source, dest,1)
# map1.showMap()
map1.showMapplot()
AStarSearch(map, source, dest,2)
# map.showMap()
map.showMapplot()
