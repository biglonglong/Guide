import random
import math
import numpy as np
import matplotlib.pyplot as plt


class GA(object):
    def __init__(self, num_city, num_chromosome, iteration, data):
        self.num_city = num_city             # 城市数量
        self.location = data                 # 城市坐标
        self.dis_matrix = self.compute_dis_matrix()     # 距离矩阵
        self.num_chromosome = num_chromosome           # 染色体数量
        self.chromosomes = self.greedy_init()       # 染色体初始化
        self.ga_choose_ratio = 0.2          # 成活率、复制、交叉
        self.mutate_ratio = 0.05            # 变异
        self.iteration = iteration           # 进化次数

        scores = self.compute_adp(self.chromosomes)    #初始染色体得分
        sort_index = np.argsort(-scores)               #初始染色体得分排序

        self.iter_x = [0]                              #迭代轮次
        self.iter_y = [1. / scores[sort_index[0]]]     #迭代轮次对应最佳得分
        self.best_record=[1. / scores[sort_index[0]]]  #收敛情况


    # 计算不同城市之间的距离
    def compute_dis_matrix(self):
        dis_mat = np.zeros((self.num_city, self.num_city))
        for i in range(self.num_city):
            for j in range(self.num_city):
                if i == j:
                    dis_mat[i][j] = np.inf
                else:
                    distance = np.sqrt(sum([(x[0] - x[1]) ** 2 for x in zip(self.location[i], self.location[j])]))
                    dis_mat[i][j] = distance
        return dis_mat

    # 距离city_from最近的一个城市序号
    def Closest_City(self,city_from,city_set):
        city_to=city_from
        for i in city_set:
            if self.dis_matrix[city_from][i]<self.dis_matrix[city_from][city_to]:
                city_to=i
        return city_to
        
    # 染色体的贪心初始化
    def greedy_init(self):
        chromosomes_init = []
        start_city = 0
        for i in range(self.num_chromosome):
            model_chromosome = [x for x in range(0, self.num_city)]
            # 染色体个数多于城市个数
            if start_city >= self.num_city:
                start_city = np.random.randint(0, self.num_city)
                chromosomes_init.append(chromosomes_init[start_city].copy())
            # 从start_city出发生成贪心路径
            current_city = start_city
            model_chromosome.remove(current_city)
            chromosome_one = [current_city]
            while len(model_chromosome):
                closest_city=self.Closest_City(current_city,model_chromosome)
                model_chromosome.remove(closest_city)
                chromosome_one.append(closest_city)
            chromosomes_init.append(chromosome_one)
            start_city += 1
        return chromosomes_init
    
    # 计算路径长度
    def compute_pathlen(self, path):
        path_len = 0
        for i in range(len(path)-1):
            path_len = path_len+ self.dis_matrix[path[i]][path[i+1]]
        path_len = path_len + self.dis_matrix[path[0]][path[len(path)-1]]
        return path_len

    # 计算种群适应度
    def compute_adp(self, chromosomes):
        adp = []
        for chromosome in chromosomes:
            length = self.compute_pathlen(chromosome)
            adp.append(1.0 / length)
        return np.array(adp)

    # 交叉（保证染色体正常）
    def ga_cross(self, chromosome1, chromosome2):
        # 交叉点
        cross_list = [t for t in range(len(chromosome1))]
        poses = list(random.sample(cross_list, 2))
        poses.sort()
        start, end = poses

        # 找到冲突
        tmp = chromosome1[start:end]
        chromosome1_conflict_index = []
        for sub in tmp:
            index = chromosome2.index(sub)
            if not (index >= start and index < end):
                chromosome1_conflict_index.append(index)
        chromosome2_confict_index = []
        tmp = chromosome2[start:end]
        for sub in tmp:
            index = chromosome1.index(sub)
            if not (index >= start and index < end):
                chromosome2_confict_index.append(index)
        assert len(chromosome1_conflict_index) == len(chromosome2_confict_index)

        # 交叉
        tmp = chromosome1[start:end].copy()
        chromosome1[start:end] = chromosome2[start:end]
        chromosome2[start:end] = tmp

        # 解决冲突
        for index in range(len(chromosome1_conflict_index)):
            i = chromosome1_conflict_index[index]
            j = chromosome2_confict_index[index]
            chromosome2[i], chromosome1[j] = chromosome1[j], chromosome2[i]

        return list(chromosome1), list(chromosome2)

    # 复制
    def Select_Parent(self, scores):
        sort_index = np.argsort(-scores).copy()
        sort_index = sort_index[0:int(self.ga_choose_ratio * len(sort_index))]
        parents = []
        parents_score = []
        for index in sort_index:
            parents.append(self.chromosomes[index])
            parents_score.append(scores[index])
        return parents, parents_score

    # 轮盘赌
    def Roulette(self, parents_score, parents):
        sum_score = sum(parents_score)
        score_ratio = [sub * 1.0 / sum_score for sub in parents_score]
        rand1 = np.random.rand()
        rand2 = np.random.rand()
        for i, sub in enumerate(score_ratio):
            if rand1 >= 0:
                rand1 -= sub
                if rand1 < 0:
                    index1 = i
            if rand2 >= 0:
                rand2 -= sub
                if rand2 < 0:
                    index2 = i
            if rand1 < 0 and rand2 < 0:
                break
        return list(parents[index1]), list(parents[index2])

    # 变异
    def ga_mutate(self, chromosome):
        path_list = [t for t in range(len(chromosome))]
        genes = list(random.sample(path_list, 2))
        start, end = min(genes), max(genes)
        tmp = chromosome[start:end]
        # np.random.shuffle(tmp)
        tmp = tmp[::-1]
        chromosome[start:end] = tmp

        return list(chromosome)

    def ga(self):
        # 获得父代适应度
        scores = self.compute_adp(self.chromosomes)
        # 选择部分优秀个体作为父代候选集合
        parents, parents_score = self.Select_Parent(scores)
        tmp_best_one = parents[0]
        tmp_best_score = parents_score[0]
        # 复制
        newchromosomes = parents.copy()
        # 交叉、变异
        while len(newchromosomes) < self.num_chromosome:
            # 轮盘赌方式对父代进行选择
            chromosome_x, chromosome_y = self.Roulette(parents_score, parents)
            # 交叉
            chromosome_x, chromosome_y = self.ga_cross(chromosome_x, chromosome_y)
            # 变异
            if np.random.rand() < self.mutate_ratio:
                chromosome_temp =chromosome_x
                before = self.compute_pathlen(chromosome_x)
                chromosome_x = self.ga_mutate(chromosome_x)
                after = self.compute_pathlen(chromosome_x)
                if after > before:
                    chromosome_x = chromosome_temp
            if np.random.rand() < self.mutate_ratio:
                chromosome_temp =chromosome_y
                before = self.compute_pathlen(chromosome_y)
                chromosome_y = self.ga_mutate(chromosome_y)
                after = self.compute_pathlen(chromosome_y)
                if after > before:
                    chromosome_y = chromosome_temp
            x_adp = 1. / self.compute_pathlen(chromosome_x)
            y_adp = 1. / self.compute_pathlen(chromosome_y)
            # 将适应度高的放入种群中
            if x_adp > y_adp and (not chromosome_x in newchromosomes):
                newchromosomes.append(chromosome_x)
            elif x_adp <= y_adp and (not chromosome_y in newchromosomes):
                newchromosomes.append(chromosome_y)

        #进化
        self.chromosomes = newchromosomes
        return tmp_best_one, tmp_best_score

    def run(self):
        BEST_LIST = None
        best_score = -math.inf
        for i in range(1, self.iteration + 1):
            tmp_best_one, tmp_best_score = self.ga()
            self.iter_x.append(i)
            self.iter_y.append(1. / tmp_best_score)
            if tmp_best_score > best_score:
                best_score = tmp_best_score
                BEST_LIST = tmp_best_one
            self.best_record.append(1./best_score)
            print('the ',i,' iteration: ',1./best_score)
        return self.location[BEST_LIST], 1. / best_score


# 读取数据
def read_tsp(path):
    lines = open(path, 'r').readlines()
    assert 'NODE_COORD_SECTION\n' in lines
    index = lines.index('NODE_COORD_SECTION\n')
    data = lines[index + 1:-1]
    tmp = []
    for line in data:
        line = line.strip().split(' ')
        if line[0] == 'EOF':
            continue
        tmpline = []
        for x in line:
            if x == '':
                continue
            else:
                tmpline.append(float(x))
        if tmpline == []:
            continue
        tmp.append(tmpline)
    data = tmp
    return data


if __name__ == '__main__':
    data = read_tsp('.\st70.tsp')
    data = np.array(data)
    data = data[:, 1:]
    
    model = GA(num_city=data.shape[0], num_chromosome=25, iteration=200, data=data.copy())
    Best_path, Best = model.run()
    print('---------- after iterations,final res: ',' ---------- ')
    print(Best_path, Best)

    fig, axs = plt.subplots(2, 1, sharex=False, sharey=False)
    axs[0].scatter(Best_path[:, 0], Best_path[:,1])
    Best_path = np.vstack([Best_path, Best_path[0]])
    axs[0].plot(Best_path[:, 0], Best_path[:, 1])
    axs[0].set_title('Iteration results')

    iterations = range(model.iteration+1)
    best_record = model.best_record
    axs[1].plot(iterations, best_record)
    axs[1].set_title('Convergence curve')

    plt.show()


