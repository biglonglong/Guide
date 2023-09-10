> 变异、交叉、复制
>
> 自然选择，适者生存

## 遗传算法

**基因和染色体**：将问题形式化，得到由元素组成的可行解，抽象为一条基因组成的“染色体”

**适应度函数**：用一个函数来评判一个可行解的好坏，保留较好的解，即自然选择，适者生存，从而经过若干次迭代后染色体的质量将越来越优良

**交叉**：选取两个可行解作为父母，从两个可行解中各选取一部分组成新解，这条新染色体上即包含了一定数量的爸爸的基因，也包含了一定数量的妈妈的基因。

> 谁作为父母？  这不是随机选择的，一般是通过轮盘赌算法完成。
>
> 染色体i被选择的概率 = 染色体i的适应度 / 所有染色体的适应度之和

**变异**：交叉仅改变元素的组合顺序，经过N次进化后，计算结果更接近于局部最优解，引入变异对交叉生成的染色体随机选择若干个基因，随机修改基因的值

**复制**：每次进化中，为了保留上一代优良的染色体，将上一代中适应度最高的几条染色体直接原封不动地复制给下一代。



## 流程

- 随机生成一组可行解—第一代染色体。

- 采用适应度函数分别计算每一条染色体的适应程度，根据适应程度计算每一条染色体在下一次进化中被选中的概率

- 进化

  - 通过“交叉”，生成N-M条染色体；


  - 再对交叉后生成的N-M条染色体进行“变异”操作；


  - 然后使用“复制”的方式生成M条染色体；


到此为止，N条染色体生成完毕！紧接着分别计算N条染色体的适应度和下次被选中的概率。

这就是一次进化的过程，紧接着进行新一轮的进化。



## 究竟需要进化多少次？

每一次进化都会更优，因此理论上进化的次数越多越好，但在实际应用中往往会在==结果精确度==和==执行效率==之间寻找一个平衡点，一般有两种方式：

### 1. 限定进化次数

在一些实际应用中，可以事先统计出进化的次数。比如，你通过大量实验发现：不管输入的数据如何变化，算法在进化N次之后就能够得到最优解，那么你就可以将进化的次数设成N。

### 2. 限定允许范围

我们可以事先设定一个可以接收的结果范围，当算法进行X次进化后，一旦发现了当前的结果已经在误差范围之内了，那么就终止算法。







## 算法实现

[GA](GA.py)

- `compute_dis_matrix`：根据st70.tsp的坐标数据计算距离矩阵
- ==`greedy_init`==：初始化种群中的num_chromosome个染色体，注意每个染色体为0~num_city的一个排列，采用贪心算法，对任何一个染色体，当前城市基因最近的城市基因作为下一个城市基因
  - `Closest_City`：当前城市基因最近的城市基因，不允许与之前的基因冲突
- `compute_pathlen`：计算该染色体归约可行解的城市花费
- `compute_adp`：城市花费的倒数，花费越大，适应度越低
- `ga_cross`：交叉：对父母染色体，任取两个位置间的基因进行交换，检查父母染色体中存在两次的基因作为冲突点，将父母冲突点进行交换解决冲突
- `Select_Parent`：复制：选择种群中具有较好得分的染色体
- `Roulette`：得分归一化，采用两个随机数来对归一化得分进行选择
  - C++采用轮盘赌从全体个体中生成num_chromosome个新个体
  - python采用轮盘赌从较好个体中选择父母进行交叉、随机变异并择优选择后代，不断生成保证种群大小不变。较好个体直接遗传给后代，占ga_choose_ratio
- `ga_mutate`：变异有很多种，可以是基因交换，也可以是基因块倒转，也可以定向变异









## C++实现

```C++
#include "stdio.h"
#include "stdlib.h"
#include "time.h"
#define cityNum 10				
#define popSize 10
#define croRate 0.85				
#define mutRate 0.1				
#define MAX 999					

//定义染色体的结构
struct Chrom
{
	int cityArr[cityNum];		
	char name;				
	float adapt;				
	int dis;					
};
struct Chrom genes[popSize];	
struct Chrom genesNew[popSize]; 
struct Chrom temp;			


char names[cityNum] = {'A','B','C','D','E','F','G','H','I','J'};		

int distance[cityNum][cityNum] = {{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9  },	  
							 {  1, 0, 1, 2, 3, 4, 5, 6, 7, 8  },
							 {  2, 1, 0, 1, 2, 3, 4, 5, 6, 7  },
							 {  3, 2, 1, 0, 1, 2, 3, 4, 5, 6  },
							 {  4, 3, 2, 1, 0, 1, 2, 3, 4, 5  },
							 {  5, 4, 3, 2, 1, 0, 1, 2, 3, 4  },
							 {  6, 5, 4, 3, 2, 1, 0, 1, 2, 3  },
							 {  7, 6, 5, 4, 3, 2, 1, 0, 1, 2  },
							 {  8, 7, 6, 5, 4, 3, 2, 1, 0, 1  },
							 {  9, 8, 7, 6, 5, 4, 3, 2, 1, 0  }};	

void initGroup()
{
	int i,j,k;
	int t = 0;
	int flag = 0;
	srand(time(NULL));//产生随机种子
	for(i = 0; i < popSize; i ++)
	{
		
	    temp.name = names[i];
		temp.adapt = 0.0f;
		temp.dis = 0;
		
		for(j = 0; j < cityNum;)
		{
			t = rand()%cityNum;	
			flag = 1;//用于标志之前是否已经访问过该city
			for(k = 0; k < j; k ++)
			{
				if(genes[i].cityArr[k] == t)
				{
					flag = 0;
					break;//表示已经访问过了，重复
				}
			}
			if(flag)//flag没有置0，将该city加入
			{
				temp.cityArr[j] = t;
				genes[i] = temp;
				j++;
			}
		}
	}
}

void popFitness()
{
	int i,n1,n2;
	for(i = 0; i < popSize; i ++)
	{
		genes[i].dis = 0;
		for(int j = 1;j < cityNum; j ++)
		{
			n1 = genes[i].cityArr[j-1];
			n2 = genes[i].cityArr[j];
			genes[i].dis += distance[n1][n2];
		}
		genes[i].dis += distance[genes[i].cityArr[0]][genes[i].cityArr[cityNum-1]];
        //循环结束再加上首尾
		genes[i].adapt = (float)1/genes[i].dis;	
        //genes[i]的适应度，路线长度越短该值越大
	}
}

int chooseBest()
//选择出适应度最大的基因
{
	int choose = 0;
	float best = 0.0f;
	best = genes[0].adapt;
	for(int i = 0; i < popSize; i ++)
	{
		if(genes[i].adapt < best)
		{
			best = genes[i].adapt;
			choose = i;
		}
	}
	return choose;
}

void select()
/*轮盘赌方法*/
{
	float biggestSum = 0.0f;
	float adapt_pro[popSize];
	float pick = 0.0f;
	int i;
	for(i = 0; i < popSize; i ++)
	{
		 biggestSum += genes[i].adapt; 
	}
	for(i = 0; i < popSize; i ++)
	{
		 adapt_pro[i] = genes[i].adapt / biggestSum; 
	}
	
    for(i = 0;i < popSize; i ++)
    {
        pick = (float)rand()/RAND_MAX;//每次随机生成0~1之间的一个随机数 
	    /********** Begin **********/
        float m=0;//m接收累积概率的值
        for(int k=0;k<popSize;k++)
        {
            if(pick<=m+adapt_pro[k])
              /*如果随机数 pick≤adapt_pro[1]
                genes1被选中
                如果随机数 adapt_pro[k−1]<pick≤adapt_pro[k](2≤k≤N)
                则genesk被选中*/
            {
                genesNew[i]=genes[k];
                break;
            }
            m+=adapt_pro[k];//累积概率
        }
        
        
	    /********** End **********/
    }
    for(i = 0;i < popSize; i++)
    {
	    genes[i] = genesNew[i];
    }
}

void cross()
{
    float pick;
    int choice1,choice2;
    int pos1,pos2;
    int temp;
    int conflict1[popSize];	
    int conflict2[popSize];
    int num1;
    int num2;
    int index1,index2;
    int move = 0;				
    while(move < popSize-1)
    {
        pick = (float)rand()/RAND_MAX; 
        if(pick > croRate)		
        {
            move += 2;
            continue;			
        }
        choice1 = move;			
        choice2 = move+1;		
        pos1 = rand()%popSize;
        pos2 = rand()%popSize;
        while(pos1 > popSize -2 || pos1 < 1)
        {
            pos1 = rand()%popSize;
        }
        while(pos2 > popSize -2 || pos2 < 1)
        {
            pos2 = rand()%popSize;
        }

        if(pos1 > pos2)
        {
            temp = pos1;
            pos1 = pos2;
            pos2 = temp; 
        }

        for(int j = pos1;j <= pos2; j++)
        {
            temp = genes[choice1].cityArr[j];
            genes[choice1].cityArr[j] = genes[choice2].cityArr[j];
            genes[choice2].cityArr[j] = temp;
        }

        num1 = 0;
        num2 = 0;

        if(pos1 > 0 && pos2 < popSize - 1)
        {
            /********** Begin **********/
           //如果交叉过程中选择到的部分交叉后会冲突，首先进行记录
          /*会冲突的情况
            12|3456|789
            46|2738|159
            此时如果交换则得到12|2738|789，46|3456|159很明显重复了，不是我们需要的，需要先将其位置             记录下来  
            */
                
            for(int j=0;j<pos1;j++)
            {
                for(int k=pos1;k<=pos2;k++)
                {
                    if(genes[choice1].cityArr[j]==genes[choice1].cityArr[k])
                        conflict1[num1++]=j;
                    if(genes[choice2].cityArr[j]==genes[choice2].cityArr[k])
                        conflict2[num2++]=j;
                }
            }
          
	        /********** End **********/
            

            for(int j = pos2 + 1;j < popSize;j++)
            {
                for(int k = pos1; k <= pos2; k ++)
                {
                    /********** Begin **********/
                    if(genes[choice1].cityArr[j]==genes[choice1].cityArr[k])
                        conflict1[num1++]=j;
                    if(genes[choice2].cityArr[j]==genes[choice2].cityArr[k])
                        conflict2[num2++]=j;
                    
                    
                    /********** End **********/
                }
            }
        }
        if((num1 == num2) && num1 > 0)
        {
            /*
            这一步的操作就是将记录的自己冲突的值与对方冲突的值进行调换，如上面的例子得到的实际上应该是
            14|2738|659
            27|3456|189
            */
            for(int j = 0;j < num1; j ++)
            {
                index1 = conflict1[j];
                index2 = conflict2[j];
                temp = genes[choice1].cityArr[index1]; 
                genes[choice1].cityArr[index1] = genes[choice2].cityArr[index2];
                genes[choice2].cityArr[index2] = temp;
            }
        }
        move += 2;
    }
}

void mutation()
{
    //突变
	double pick;
    int pos1,pos2,temp;
    for(int i = 0;i < popSize; i ++)
    {
        pick = (float)rand()/RAND_MAX; 
        if(pick > mutRate)
		{
            continue;
		}
        pos1 = rand()%popSize;
        pos2 = rand()%popSize;
        while(pos1 > popSize - 1)
        {
           pos1 = rand()%popSize;
        }
        while(pos2 > popSize - 1)
        {
           pos2 = rand()%popSize;
        }

	   int a = genes[i].dis;
        temp = genes[i].cityArr[pos1];
        genes[i].cityArr[pos1] = genes[i].cityArr[pos2];
        genes[i].cityArr[pos2] = temp;

		popFitness();
		if(genes[i].dis > a)
		{
			temp = genes[i].cityArr[pos1];
			genes[i].cityArr[pos1] = genes[i].cityArr[pos2];
			genes[i].cityArr[pos2] = temp;
		}
    }
}

```





