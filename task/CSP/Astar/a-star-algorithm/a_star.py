# a_star.py

import os
import sys
import time
import numpy as np
from matplotlib.patches import Rectangle

import point
import random_map

class AStar:
    def __init__(self, map,target_x,target_y):
        self.map=map
        self.open_set = []
        self.close_set = []
        self.target_x=target_x
        self.target_y=target_y

    # Distance to end point;it is evaluation;need negative number
    def HeuristicCost(self, p):
        x_dis = abs(self.target_x - p.x)
        y_dis = abs(self.target_y - p.y)
        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def NextCost(self,p,parent):
        nextcost=np.sqrt(2)
        if abs(parent.x-p.x)-abs(parent.y-p.y):
            nextcost=1
        return nextcost
    
    def IsValidPoint(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= self.map.size or y >= self.map.size:
            return False
        return not self.map.IsObstacle(x, y)

    def IsInPointList(self, p, point_list):
        for i,point in enumerate(point_list):
            if point.x == p.x and point.y == p.y:
                return i
        return -1

    def IsInOpenList(self, p):
        return self.IsInPointList(p, self.open_set)

    def IsInCloseList(self, p):
        return self.IsInPointList(p, self.close_set)

    def IsStartPoint(self, p):
        return p.x == 0 and p.y ==0

    def IsEndPoint(self, p):
        return p.x == self.target_x and p.y == self.target_y

    def SaveImage(self, plt):
        millis = int(round(time.time() * 1000))
        figure_save_path = "res_png"
        if not os.path.exists(figure_save_path):
            os.makedirs(figure_save_path)
        filename = './' + str(millis) + '.png'
        plt.savefig(os.path.join(figure_save_path , filename))

    def ProcessPoint(self, x, y,parent):
        # Do nothing for invalid point
        if not self.IsValidPoint(x, y): return
        p = point.Point(x, y)

        # Do nothing for visited point
        if self.IsInCloseList(p) != -1: return 

        if self.IsInOpenList(p) !=-1:
            index = self.IsInOpenList(p)
            p=self.open_set[index]
            newcost=parent.basecost+self.NextCost(p,parent)
            if(newcost<p.basecost):
                p.parent=parent
                p.basecost=newcost
                p.totalcost=p.basecost+p.heuristiccost
                print('Update Point [', p.x, ',', p.y, ']', ',Estimated Cost: ', p.totalcost)   
        else:
            p.parent = parent
            p.basecost=parent.basecost+self.NextCost(p,p.parent)
            p.heuristiccost=self.HeuristicCost(p)
            p.totalcost=p.basecost+p.heuristiccost
            self.open_set.append(p)
            

    def SelectPointInOpenList(self):
        index = 0
        selected_index = -1
        min_cost = sys.maxsize
        for p in self.open_set:
            if p.totalcost < min_cost:
                min_cost = p.totalcost
                selected_index = index
            index += 1
        return selected_index

    def BuildPath(self, p, ax, plt, start_time):
        path = []
        while True:
            path.insert(0, p) # Insert first
            if self.IsStartPoint(p):
                break
            else:
                p = p.parent
        for p in path:
            rec = Rectangle((p.x, p.y), 1, 1, color='g')
            ax.add_patch(rec)
            plt.draw()
            self.SaveImage(plt)
        end_time = time.time()
        print('===== Algorithm finish in', int(end_time-start_time), ' seconds')

    def RunAndSaveImage(self, ax, plt):
        start_time = time.time()

        start_point = point.Point(0, 0)
        start_parent = point.Point(-1, -1)
        start_point.basecost = 0
        start_point.heuristiccost = self.HeuristicCost(start_point)
        start_point.totalcost = start_point.basecost + start_point.heuristiccost
        start_point.parent = start_parent
        self.open_set.append(start_point)

        while True:
            index = self.SelectPointInOpenList()
            if index < 0:
                print('No path found, algorithm failed!!!')
                return
            p = self.open_set[index]
            rec = Rectangle((p.x, p.y), 1, 1, color='c')
            ax.add_patch(rec)
            self.SaveImage(plt)
            print('Expand Point [', p.x, ',', p.y, ']',',come from: [', p.parent.x, ',', p.parent.y, ']')
            if self.IsEndPoint(p):
                return self.BuildPath(p, ax, plt, start_time)

            del self.open_set[index]
            self.close_set.append(p)

            # Process all neighbors
            x = p.x
            y = p.y
            self.ProcessPoint(x-1, y+1, p)
            self.ProcessPoint(x-1, y, p)
            self.ProcessPoint(x-1, y-1, p)
            self.ProcessPoint(x, y-1, p)
            self.ProcessPoint(x+1, y-1, p)
            self.ProcessPoint(x+1, y, p)
            self.ProcessPoint(x+1, y+1, p)
            self.ProcessPoint(x, y+1, p)




