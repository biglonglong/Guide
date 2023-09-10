# point.py

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.basecost = None
        self.heuristiccost =None
        self.totalcost =None
        '''
        # self.totalcost = self.basecost+self.heuristiccost
        try to fix totalcost following basecost & heuristiccost
        but no function
        '''
        self.parent = None

