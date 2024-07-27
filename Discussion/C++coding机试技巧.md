# C++coding机试技巧



## 一、代码规范

### 变量命名

统一为**小驼峰命名法**：第一个单词首字母小写，其他单词首字母大写

```C++
int myAge;
```

### 代码空格

- [x] 分隔符（`,` 、`;`）后空格;算术表达式紧贴


```C++
int i, j;
for(int fastIndex=0; fastIndex<nums.size(); fastIndex++)
```

- [x] 大括号和函数保持同一行，与控制语句（while，if，for）前空格


```C++
while(n) {
    n--;
}
```



## 二、常用头

### 头文件

#### 标准c库

| 头文件       | 说明         | 头文件           | 说明             | 头文件          | 说明         |
| ------------ | ------------ | ---------------- | ---------------- | --------------- | ------------ |
| assert.h     | 断言相关     | ctype.h          | 字符类型判断     | errno.h         | 标准错误机制 |
| float.h      | 浮点限制     | limits.h         | 整形限制         | locale.h        | 本地化接口   |
| math.h/cmath | 数学函数     | setjmp.h         | 非本地跳转       | signal.h        | 信号相关     |
| stdarg.h     | 可变参数处理 | stddef.h         | 宏和类型定义     | stdio.h/cstdlib | 标准I/O      |
| stdlib.h     | 标准工具库   | string.h/cstring | 字符串和内存处理 | time.h          | 时间相关     |
| cstdio       | c标准IO      |                  |                  |                 |              |

#### STL库

| using namespace std; |           |            |               |            |              |
| -------------------- | --------- | ---------- | ------------- | ---------- | ------------ |
| **头文件**           | **说明**  | **头文件** | **说明**      | **头文件** | **说明**     |
| algorithm            | 通用算法  | deque      | 双端队列      | vector     | 向量         |
| iterator             | 迭代器    | stack      | 栈            | map        | 图（键值对） |
| list                 | 列表      | string     | 字符串        | set        | 集合         |
| queue                | 队列      | bitset     | bit类         | numeric    | 数值算法     |
| iostream             | C++标准IO | bitset     | C++标准位序列 |            |              |

### 宏定义

```C++
//求最大值和最小值
#define  MAX(x,y) (((x)>(y)) ? (x) : (y))
#define  MIN(x,y) (((x) < (y)) ? (x) : (y))
```

```C++
//取余
#define  mod(x) ((x)%MOD)
```

```C++
//for循环
#define  FOR(i,f_start,f_end) for(int i=f_start;i<=f_end;++i) 
```

```C++
//返回数组元素的个数
#define  ARR_SIZE(a)  (sizeof((a))/sizeof((a[0])))
```

```C++
//初始化数组
#define MT(x,i) memset(x,i,sizeof(x))
```

```C++
//符号重定义
#define LL long long
#define ull unsigned long long
#define pii pair<int,int>
```

```C++
//常见常数
#define PI acos(-1.0)
#define eps 1e-12
#define INF 0x3f3f3f3f //int最大值
const int INF_INT = 2147483647;
const ll INF_LL = 9223372036854775807LL;
const ull INF_ULL = 18446744073709551615Ull;
const ll P = 92540646808111039LL;
const ll maxn = 1e5 + 10, MOD = 1e9 + 7;
const int Move[4][2] = {-1,0,1,0,0,1,0,-1};
const int Move_[8][2] = {-1,-1,-1,0,-1,1,0,-1,0,1,1,-1,1,0,1,1};
```

### 函数

#### atoi()

```C++
#include <stdlib.h>
#include <cstring>
int atoi(const char *str)
//把参数 str 所指向的字符串转换为一个整数（类型为 int 型）,如果没有执行有效的转换，则返回零

int num = atoi(<string>.c_str());
```

#### memset()

```C++
#include <cstring>
void *memset(void *str, int c, size_t n)
//复制字符 c（一个无符号字符）到参数 str 所指向的字符串的前 n 个字符
    
memset(arr, -1, sizeof(arr));
memset(arr, 0, sizeof(arr));
```

#### to_string()

```C++
#include<string>
string to_string (auto num)
//将数字转换为字符串
    
string pi=to_string(3.1415926);
```



## 三、new堆区使用

### 常规

```c++
int *x = new int;       		//开辟一个存放整数的存储空间，返回一个指向该空间的地址(即指针)
int *a = new int(100);  		//开辟一个存放整数的空间，指定初值为100，返回一个指向该空间的地址
char *b = new char[10]; 		//开辟一个存放字符的10字符大小的数组空间，返回首元素的地址
```

### 固定二维数组

```c++
const int MAXCOL = 3;			//固定列值
cin>>row;
//申请一维数据并将其转成二维数组指针
int *pp_arr = new int[nRow * MAXCOL];
int (*p)[MAXCOL] = (int(*)[MAXCOL])pp_arr;
//此时p[i][j]就可正常使用
```


### 不固定二维数组

```c++
cin>>row>>col;
int **p = new int*[row];
for (int i = 0; i < row; i ++) {
    p[i] = new int[col];
}
```



## 四、结构体

### 定义

```c++
struct InitMember {
    int first;
    double second;
    char* third;
    float four;
};
```

### 初始化

```c++
struct InitMember test1 = {-10,3.141590，"method one"，0.25};

struct InitMember test2;
test2.first = -10;
test2.second = 3.141590;
test2.third = "method two";
test2.four = 0.25;
```

### 构造函数

```c++
//定义图的定点
typedef struct Vertex {
    int id,inDegree,outDegree;
    vector<int> connectors;    //存储节点的后续连接顶点编号
    Vertex() : id(-1),inDegree(0),outDegree(0) {}
    Vertex(int nid) : id(nid),inDegree(0),outDegree(0) {}
} Vertex;

Vertex v(8);
```

### 运算符重载

```c++
typedef struct node{int id;int h;} node;
bool operator <(const node& a,const node & b) {return (a.h)<(b.h);}
```



## 五、常用STL

### container

> 2.list            底层数据结构为双向链表，支持快速增删
>
> 3.deque      deque是一个双端队列(double-ended queue)，也是在堆中保存内容的.它的保存形式如下:
>[堆1] --> [堆2] -->[堆3] --> ...每个堆保存好几个元素,然后堆和堆之间有指针指向,看起来像是list和vector的结合品. 底层数据结构为一个中央控制器和多个缓冲区，支持首尾（中间不能）快速增删，也支持随机访问
> 
> 11.hash_set     底层数据结构为hash表，无序，不重复
>
> 12.hash_multiset 底层数据结构为hash表，无序，可重复 
>
> 13.hash_map    底层数据结构为hash表，无序，不重复
>
> 14.hash_multimap 底层数据结构为hash表，无序，可重复 

#### string

```c++
/*
封装 char* 字符串指针的类，管理 char* 所分配内存，不用考虑内存释放和越界，但内部字符串不以空字符结尾*/

string s											//	生成一个空字符串
s=str,s.assign(str)			     		   			//  赋值
string s(str)										//	生成str复制品s
string s(str,idx)									//	以str始于idx的部分初始化s
string s(str,idx,len)								//	以str始于idx且不超过len长的部分初始化s
string s(cstr)										//	以cstr初始化s
string s(cstr,len)								    //	以cstr前不超过len长的部分初始化s
string s(n,ch)									    //	以n个字符ch初始化s
string s(beg,end)								    //	以由迭代器begin和end指定字符串[begin, end)初始化s

s[i],s.at(i)	             						//  访问下标对应字符元素
s.begin()											//  返回指向首元素的正向迭代器
s.end()												//  返回指向尾元素的下一个位置的正向迭代器
s.rbegin()											//  返回指向尾元素的逆向迭代器
s.rend()											//  返回指向首元素的上一个位置的逆向迭代器

+=,s.append(str),s.push_back(ch)					//	拼接s和str/ch
s.insert(idx,str)									//	在s的idx处插入str
s.erase(idx,len)									//  删除s从idx开始的len个字符
s.replace(idx,len,str)								//	将s从idx开始的len个字符替换为str
s.substr(idx,len)									//	返回s从idx开始的len个字符子串
>、<、>=、<=、==、!=、s.compare(str)  				//	按照字典序比较两个字符串

s.c_str()											//	返回一个指向C字符串的指针常量,指向字符数组以空字符结尾    
s.data()											//	返回一个指向C字符串的指针常量,不以空字符结尾
s.copy(p,len,idx)									//	将s从idx开始的len个字符复制到数组指针p，不以空字符结尾
>>													//	从stream中读取字符串
<<													//	将值写入stream
    
s.size(),s.length()            						//  返回串长
s.capacity()										//	s已分配容量
s.reserve(len)        								//  预分配缓冲空间，使存储空间可容纳len个字符
s.resize(len)										//  扩展字符串，或者截断字符串为len长
s.max_size()										//	string类型结构最多包含的字符数

s.empty()           								//  检查串空
s.clear()											//  删除容器中的所有内容
s.swap(v)           								//  将s与另一个string对象v内容进行交换
```

#### vector

```C++
/*
顺序结构线性表,支持快速随机访问，在使用过程中动态地增长存储空间,底层数据结构为数组*/

vector<type> v      								//  生成一个type类型空序列
vector<type> v(n)  									//  生成一个含有n个type类型元素的空序列
vector<type> v(first,last)，v.assign(first,last)    //  以指定序列[first, last)初始化v
vector<vector<int> >res(m,vector<int>(n,0));        //   生成一个m*n的置0数组
	
v[i]                								//  访问下标对应序列元素
v.front()           								//  返回首元素
v.back()            								//  返回尾元素
v.begin()           								//  返回指向首元素的正向迭代器
v.end()             								//  返回指向尾元素的正向迭代器

v.push_back(val)      								//  向序列尾插入元素val
v.pop_back()        								//  删除尾元素
v.insert(it,val)   								    //  向迭代器it指向的元素前插入新元素val
v.insert(it,n,val)								    //  向迭代器it指向的元素前插入n个新元素val
v.insert(it,first,last)     						//  向迭代器it指向的元素前插入指定序列[first, last)

v.erase(it)											//  删除迭代器it指向元素
v.erase(first,last)								    //  删除指定序列[first, last)

>、<、>=、<=、==、!=   								//	按照字典序比较两个序列  

v.size()            								//  返回序列长
v.reserve(len)        								//  预分配缓冲空间，使存储空间可容纳len个元素
v.resize(len)										//  扩展序列，或者截断序列为len长
v.resize(len,val)    								//  扩展序列并以val值填充，或者截断序列为len长
    
v.empty()           								//  检查序列空
v.clear()											//  删除容器中的所有内容
v.swap(s)           								//  将v与另一个vector对象s进行交换
```

#### stack

```c++
/*
底层用list或deque实现，先进后出*/

stack<type> s										//	生成一个type类型空栈	

s.push(val)  										//  入栈
s.pop()    											//  出栈
s.top()    											//  访问栈顶

s.empty()  											//  检查栈空
s.size()  											//  返回栈大小
```

#### queue

```c++
/*
底层用list或deque实现，先进先出*/

queue<int> q										//	生成一个type类型空队列	

q.push(val)  										//  入队
q.pop()    											//  出队
q.front()  											//  访问队首元素
q.back()   											//  访问队尾元素

q.empty()  											//  检查队空
q.size()	   										//  返回队长
```

#### set

```C++
/*
set去重,multiset可以存在相同元素,unordered_set查询更快*/

set<type> s											//	生成一个type类型空集合
multiset<type> s									//	生成一个type类型空可重集合
unordered_set<type> s(first,last)     				//	以指定序列[first, last)初始化s

s.begin()       									//  返回指向首元素的正向迭代器
s.end()         									//  返回指向尾元素的下一个位置的正向迭代器
s.rbegin()											//  返回指向尾元素的逆向迭代器
s.rend()											//  返回指向首元素的上一个位置的逆向迭代器

s.insert(val)      									//  插入元素val
s.erase(val)       									//  删除集合s中元素val
s.find(val)        									//  返回一个指向被查元素val的迭代器,无则返回s.end()

s.size()        									//  返回集合长
s.count(val)       									//  返回集合中val的个数

s.empty()      										//  检查集合空
s.clear()											//  删除容器中的所有内容
s.swap(v)											//  将s与另一个set对象v进行交换
    
s.max_size()    									//  返回set类型对象能容纳的元素的最大限值
s.get_allocator()   								//  返回集合s的分配器
s.equal_range(val) 									//  返回集合s中与给定值val相等的上下限迭代器
s.lower_bound() 									//  返回指向第一个大于或等于指定键的元素迭代器
s.upper_bound() 									//  返回指向第一个大于指定键的元素迭代器
s.key_comp()    									//  用于比较两个键的大小关系，它返回一个用于键比较的函数对象
s.value_comp()  									//  用于比较两个值的大小关系，它返回一个用于值比较的函数对象
```

#### pair

```C++
/*
#include <utility>,pair二元组或元素对*/

pair<type1,type2> p          						//	生成一个<type1,type2>类型空二元组
p.first												//	定义/返回二元组p的第一个元素
p.second											//	定义/返回二元组p的第二个元素
make_pair(val1,val2)								//  以val1为键,val2为值初始化p
    
<、>、<=、>=、==、!=								 	//  按照字典序比较，先比较first，first相等时再比较second
```

#### map

```C++
/*
存储pair序列,所有元素的Key值必须是唯一的,multiset可以存在相同键值,unordered_map查询更快*/
map<type1,type2> m								//	生成一个<type1,type2>类型空字典

m[key] = value									//  修改/插入pair<key,value>，返回m[key]的value值
m.insert(make_pair(key,value)) 					//  插入pair<key,value>，insert操作会返回一个pair,当map中没有与key相匹配的键值时,其first是指向插入元素对的迭代器,其second为true;若map中已经存在与key相等的键值时,其first是指向该元素对的迭代器,second为false

int value = m[key]              				//  查找字典中键为key的value值，无则创建m[key]=0且返回0
it = m.find(key)			    				//  查找字典中键为key对应迭代器，无则返回m.end()

m.erase(key)									//  删除指定key键值相匹配的元素对,并返回被删除的元素的个数
m.erase(it)										//  删除由迭代器it所指定的元素对,并返回指向下一个元素对的迭代器
    
m.size();       								//  返回字典长
m.empty();      								//  检查字典空
m.clear();      								//  删除容器中的所有内容
```

#### list


下面给出几个常用的定义list对象的方法示例：

```c++
list<int>a{1,2,3}
list<int>a(n)    //声明一个n个元素的列表，每个元素都是0
list<int>a(n, m)  //声明一个n个元素的列表，每个元素都是m
list<int>a(first, last)  //声明一个列表，其元素的初始值来源于由区间所指定的序列中的元素，first和last是迭代器

```

list的基本操作：

```c++
a.begin()           //  返回指向首元素的随机存取迭代器
a.end()             //  返回指向尾元素的下一个位置的随机存取迭代器
a.push_front(x)     //  向表头插入元素x
a.push_back(x)      //  向表尾插入元素x
a.pop_back()        //  删除表尾元素
a.pop_front()       //  删除表头元素
a.size()            //  返回表长
a.empty()           //  表为空时，返回真，否则返回假
a.resize(n)         //  改变序列长度，超出的元素将会全部被删除，如果序列需要扩展（原空间小于n），元素默认值将填满扩展出的空间
a.resize(n, val)    //  改变序列长度，超出的元素将会全部被删除，如果序列需要扩展（原空间小于n），val将填满扩展出的空间
a.clear()           //  删除容器中的所有元素
a.front()           //  返回首元素
a.back()            //  返回尾元素
a.swap(v)           //  将a与另一个list对象进行交换
a.merge(b)          //  调用结束后b变为空，a中元素包含原来a和b的元素
a.insert(it, val)   //  向迭代器it指向的元素前插入新元素val
a.insert(it, n, val)//  向迭代器it指向的元素前插入n个新元素val
a.insert(it, first, last)   
//  将由迭代器first和last所指定的序列[first, last)插入到迭代器it指向的元素前面
a.erase(it)         //  删除由迭代器it所指向的元素
a.erase(first, last)//  删除由迭代器first和last所指定的序列[first, last)
a.remove(x)         //  删除了a中所有值为x的元素
a.assign(n, val)    // 将a中的所有元素替换成n个val元素
a.assign(b.begin(), b.end())
//将a变成b

```

#### bitset

在 STLSTL 的头文件中 bitset中定义了模版类 bitsetbitset，用来方便地管理一系列的 bitbit 位的类。bitsetbitset 除了可以访问指定下标的 bitbit 位以外，还可以把它们作为一个整数来进行某些统计。

bitsetbitset 模板类需要一个模版参数，用来明确指定含有多少位。

定义 bitsetbitset 对象的示例代码：

```c++
const int MAXN = 32;
bitset<MAXN> bt;            //  bt 包括 MAXN 位，下标 0 ~ MAXN - 1，默认初始化为 0
bitset<MAXN> bt1(0xf);      //  0xf 表示十六进制数 f，对应二进制 1111，将 bt1 低 4 位初始化为 1
bitset<MAXN> bt2(012);      //  012 表示八进制数 12，对应二进制 1010，即将 bt2 低 4 位初始化为 1010
bitset<MAXN> bt3("1010");   //  将 bt3 低 4 位初始化为 1010
bitset<MAXN> bt4(s, pos, n);//  将 01 字符串 s 的 pos 位开始的 n 位初始化 bt4
```

bitsetbitset 基本操作：

```c++
bt.any()        //  bt 中是否存在置为 1 的二进制位？
bt.none()       //  bt 中不存在置为 1 的二进制位吗？
bt.count()      //  bt 中置为 1 的二进制位的个数
bt.size()       //  bt 中二进制位的个数
bt[pos]         //  访问 bt 中在 pos 处的二进制位
bt.test(pos)    //  bt 中在 pos 处的二进制位是否为 1
bt.set()        //  把 bt 中所有二进制位都置为 1
bt.set(pos)     //  把 bt 中在 pos 处的二进制位置为 1
bt.reset()      //  把 bt 中所有二进制位都置为 0
bt.reset(pos)   //  把 bt 中在pos处的二进制位置为0
bt.flip()       //  把 bt 中所有二进制位逐位取反
bt.flip(pos)    //  把 bt 中在 pos 处的二进制位取反
bt[pos].flip()  //  同上
bt.to_ulong()   //  用 bt 中同样的二进制位返回一个 unsigned long 值
os << bt        //  把 bt 中的位集输出到 os 流
```



### algorithm

#### 不修改内容的序列操作

|函数|说明|
| -------------------------------------------------------- | ------------------------------------------------------------ |
| adjacent_find| 查找两个相邻（Adjacent）的等价（Identical）元素              |
| all_ofC++11                                              | 检测在给定范围中是否所有元素都满足给定的条件                 |
| any_ofC++11                                              | 检测在给定范围中是否存在元素满足给定条件                     |
| count         | 返回值等价于给定值的元素的个数                               |
| count_if      | 返回值满足给定条件的元素的个数                               |
| equal         | 返回两个范围是否相等                                         |
| find           | 返回第一个值等价于给定值的元素                               |
| find_end                                                 | 查找范围*A*中与范围*B*等价的子范围最后出现的位置             |
| find_first_of | 查找范围*A*中第一个与范围*B*中任一元素等价的元素的位置       |
| find_if                                                  | 返回第一个值满足给定条件的元素                               |
| find_if_notC++11                                         | 返回第一个值不满足给定条件的元素                             |
| for_each                                                 | 对范围中的每个元素调用指定函数                               |
| mismatch                                                 | 返回两个范围中第一个元素不等价的位置                         |
| none_ofC++11                                             | 检测在给定范围中是否不存在元素满足给定的条件                 |
| search          | 在范围*A*中查找第一个与范围*B*等价的子范围的位置             |
| search_n                                                 | 在给定范围中查找第一个连续*n*个元素都等价于给定值的子范围的位置 |

#### 修改内容的序列操作

|函数|说明|
| -------------------------------------------------------- | ------------------------------------------------------------ |
| copy         | 将一个范围中的元素拷贝到新的位置处                           |
| copy_backward                                          | 将一个范围中的元素按逆序拷贝到新的位置处                     |
| copy_ifC++11                                           | 将一个范围中满足给定条件的元素拷贝到新的位置处               |
| copy_nC++11                                            | 拷贝 n 个元素到新的位置处                                    |
| fill         | 将一个范围的元素赋值为给定值                                 |
| fill_n                                                 | 将某个位置开始的 n 个元素赋值为给定值                        |
| generate                                               | 将一个函数的执行结果保存到指定范围的元素中，用于批量赋值范围中的元素 |
| generate_n                                             | 将一个函数的执行结果保存到指定位置开始的 n 个元素中          |
| iter_swap                                              | 交换两个迭代器（Iterator）指向的元素                         |
| moveC++11     | 将一个范围中的元素移动到新的位置处                           |
| move_backwardC++11                                     | 将一个范围中的元素按逆序移动到新的位置处                     |
| random_shuffle                                         | 随机打乱指定范围中的元素的位置                               |
| remove       | 将一个范围中值等价于给定值的元素删除                         |
| remove_if                                              | 将一个范围中值满足给定条件的元素删除                         |
| remove_copy                                            | 拷贝一个范围的元素，将其中值等价于给定值的元素删除           |
| remove_copy_if                                         | 拷贝一个范围的元素，将其中值满足给定条件的元素删除           |
| replace      | 将一个范围中值等价于给定值的元素赋值为新的值                 |
| replace_copy                                           | 拷贝一个范围的元素，将其中值等价于给定值的元素赋值为新的值   |
| replace_copy_if                                        | 拷贝一个范围的元素，将其中值满足给定条件的元素赋值为新的值   |
| replace_if                                             | 将一个范围中值满足给定条件的元素赋值为新的值                 |
| **reverse(first, last)** | 反转指定序列[first, last)                   |
| **reverse_copy(first, last, begin)**                   | 将指定序列[first, last)对应反转序列，拷贝到以begin开始的序列内 |
| rotate      | 循环移动指定范围中的元素                                     |
| rotate_copy                                            | 拷贝指定范围的循环移动结果                                   |
| shuffleC++11 | 用指定的随机数引擎随机打乱指定范围中的元素的位置             |
| swap        | 交换两个对象的值                                             |
| swap_ranges | 交换两个范围的元素                                           |
| transform   | 对指定范围中的每个元素调用某个函数以改变元素的值             |
| unique                                                 | 删除指定范围中的所有连续重复元素，仅仅留下每组等值元素中的第一个元素。 |
| unique_copy                                            | 拷贝指定范围的唯一化（参考上述的 unique）结果                |

#### 划分操作
|函数|说明|
| -------------------------------------------------------- | ------------------------------------------------------------ |
|is_partitionedC++11| 检测某个范围是否按指定谓词（Predicate）划分过|
|partition  | 将某个范围划分为两组|
|partition_copyC++11 | 拷贝指定范围的划分结果|
|partition_pointC++11  |  返回被划分范围的划分点|
|stable_partition   | 稳定划分，两组元素各维持相对顺序|

#### 排序操作

|函数|说明|
| -------------------------------------------------------- | ------------------------------------------------------------ |
|is_sortedC++11 | 检测指定范围是否已排序|
|is_sorted_untilC++11    |返回最大已排序子范围|
|nth_element|部份排序指定范围中的元素，使得范围按给定位置处的元素划分|
|partial_sort   | 部份排序|
|partial_sort_copy  | 拷贝部分排序的结果|
|**sort(begin, end, cmp)**  | 将序列[begin, end)以cmp的方式排序，cmp返回为序列元素间比较提供布尔值 |
|stable_sort |稳定排序|

#### 二分法查找操作


|函数|说明|
| -------------------------------------------------------- | ------------------------------------------------------------ |
|binary_search |  判断范围中是否存在值等价于给定值的元素|
|equal_range |返回范围中值等于给定值的元素组成的子范围|
|lower_bound |返回指向范围中第一个值大于或等于给定值的元素的迭代器|
|upper_bound |返回指向范围中第一个值大于给定值的元素的迭代器|


#### 集合操作

|函数|说明|
| -------------------------------------------------------- | ------------------------------------------------------------ |
|includes  |  判断一个集合是否是另一个集合的子集|
|inplace_merge  | 就绪合并|
|merge   合并|
|set_difference | 获得两个集合的差集|
|set_intersection |   获得两个集合的交集|
|set_symmetric_difference  |  获得两个集合的对称差|
|set_union  | 获得两个集合的并集|


#### 堆操作

|函数|说明|
| -------------------------------------------------------- | ------------------------------------------------------------ |
|is_heap |检测给定范围是否满足堆结构|
|is_heap_untilC++11  |检测给定范围中满足堆结构的最大子范围|
|make_heap |  用给定范围构造出一个堆|
|pop_heap   | 从一个堆中删除最大的元素|
|push_heap |  向堆中增加一个元素|
|sort_heap  | 将满足堆结构的范围排序|

#### 最大/最小操作

|函数|说明|
| -------------------------------------------------------- | ------------------------------------------------------------ |
|is_permutationC++11 |判断一个序列是否是另一个序列的一种排序|
|lexicographical_compare |比较两个序列的字典序|
|max |返回两个元素中值最大的元素|
|max_element |返回给定范围中值最大的元素|
|min |返回两个元素中值最小的元素|
|min_element |返回给定范围中值最小的元素|
|minmaxC++11 |返回两个元素中值最大及最小的元素|
|minmax_elementC++11|返回给定范围中值最大及最小的元素|
|next_permutation  |  返回给定范围中的元素组成的下一个按字典序的排列|
|prev_permutation  |  返回给定范围中的元素组成的上一个按字典序的排列|



## 六、编程模板

### 二分法

#### 无重复插入

```C++
int binarySearch(vector<int>& nums, int target) {
    int middle,left=0,right=nums.size()-1;
    while(left<=right){
        middle = left+(right-left)/2;
        if(nums[middle]<target) left=middle+1 ;
        else if(nums[middle]>target) right=middle-1;
        else return middle;
    }
    return left/return right+1;
}
```

#### 区间查找

```C++
//使得区间在[left,right]区间内，单独探讨边界是否正常，注意while不包括left==right的情况以防死循环
//利用二分法最终归于某个元素的核对这一性质
int findLeft(vector<int>& nums, int target){
    int middle,left=0,right=nums.size()-1;
    while(left<right){
        middle=(left+right)/2;
        if(nums[middle]<target) left=middle+1;
        else if(nums[middle]>target) right=middle-1;
        else right=middle;
    }
    if(nums[left]==target) return left;
    else return -1;
}
int findRight(vector<int>& nums, int target){
    int middle,left=0,right=nums.size()-1;
    while(left<right){
        middle=(left+right)/2+(left+right)%2;
        if(nums[middle]<target) left=middle+1;
        else if(nums[middle]>target) right=middle-1;
        else left=middle;
    }
    if(nums[right]==target) return right;
    else return -1;
}

//lower为true分nums[mid]>=target和nums[mid]<target,为false分nums[mid]<=target和nums[mid]>target
int binarySearch(vector<int>& nums,int target,bool lower){
    int left=0,right=nums.size()-1, ans=nums.size();
    while (left <= right){
        int mid=(left+right)/2;
        if (nums[mid]>target||(lower&&nums[mid]>=target)){
            right=mid-1;
            ans=mid;
        }
        else left=mid+1;        
    }
    return ans;
}
int leftIdx=binarySearch(nums,target,true);
int rightIdx=binarySearch(nums,target,false) - 1;
```



### 双指针

> 注意for循环存在末尾指针自变

#### 快慢指针

```C++
int slowFast(vector<int>& nums, int val) {
    int slow=0;
    for(int fast=0;fast<nums.size();fast++){
        if(condition(nums[fast],val))
            action(slow++,fast);
    }
    return slow;
}
```

#### 双头指针

```C++
int leftRight(vector<int>& nums){
    int left=0,right=nums.size()-1;
    while(left<=right){
        if(condition(left,right)) select(left++,right--);
        else select(left++,right--);
    }
}
```

#### 滑动窗口

```C++
//先找到合法的窗口，再对窗口内进行优化
int startEnd(int target, vector<int>& nums) {
    int start=0;
    int res=INT32_MAX;
    for(int end=0;end<nums.size();end++){
        while(check(start,end,target)){
            for(start++)//for(start--)
            	deal(res，end-start+1);
        }
    }
    return res;
}
//unordered_map<char,int> ori,cnt合法检查与记录
unordered_map <char, int> ori, cnt;
bool check() {
    for (const auto &p: ori) {
        if (cnt[p.first] < p.second) {
            return false;
        }
    }
    return true;
}
for (const auto &c: t) {
    ++ori[c];
}
if (ori.find(s[end]) != ori.end()) {
    ++cnt[s[end]];
}
```

#### 四之和组合与去重

```C++
vector<vector<int>> fourSum(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());      		//需要排序、不可返回索引

    vector<vector<int>> res;
    for(int i=0; i<nums.size(); i++) {
        if(i>0 && nums[i]==nums[i-1]) {			//a去重
            continue;
        }
        for(int j=i+1; j<nums.size(); j++) {
            if(j>i+1 && nums[j]==nums[j-1]) {		//b去重
                continue;
            }

            int left=j+1,right=nums.size()-1;
            while(left<right) {
                long val = (long)nums[i]+nums[j]+nums[left]+nums[right];
                if(val>target) {
                    right--;
                }
                else if(val<target) {
                    left++;
                }
                else{
                    while(right-1>left && nums[right]==nums[right - 1]) right--;
                    while(right>left+1 && nums[left]==nums[left + 1]) left++;			//c、d去重
                    
                    res.push_back({nums[i], nums[j], nums[left], nums[right]});
                    right--;
                    left++;
                }
            }
        } 
    }
    return res;
}
```

#### 螺旋矩阵

```C++
vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> res(n,vector<int>(n,0));
    int x1=0,y1=0,x2=n-1,y2=n-1;
    int num=1;
    while(x1<x2&&y1<y2){
        for(int i=y1;i<y2;i++) res[x1][i]=num++;
        for(int i=x1;i<x2;i++) res[i][y2]=num++;
        for(int i=y2;i>y1;i--) res[x2][i]=num++;
        for(int i=x2;i>x1;i--) res[i][y1]=num++;
        x1++;y1++;x2--;y2--;
    }
    if(x1==x2)
        for(int i=y1;i<=y2;i++) res[x1][i]=num++;
    else if(y1==y2)
        for(int i=x1;i<=x2;i++) res[i][y1]=num++;
    return res;
}
```



### 链表

> 注意虚拟节点dummyHead

#### 定义

```C++
//合法检查，执行操作，修改属性
// 定义链表节点结构体
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// 初始化链表  int _size = 0;
ListNode* _dummyHead= new ListNode(0,head);
ListNode* cur = _dummyHead->next;  //_dummyHead;
while(index--){   //while(cur->next != nullptr)
    cur = cur->next;
}
```

#### 反转链表

```C++
//遍历
ListNode* reverseList(ListNode* head) {
    ListNode *tmp;
    ListNode *curr=head;
    ListNode *pre=NULL;
    while(curr!=NULL){
        tmp=curr->next;
        curr->next=pre;
        pre=curr;
        curr=tmp;
    }
    return pre;
}
------------------------------------------------------------------------------
//递归：记录尾节点，逆向反转
ListNode* reverseList(ListNode* head) {
    if(head==NULL || head->next==NULL) return head;
    ListNode *last=reverseList(head->next);
    head->next->next=head;
    head->next=NULL;
    return last;
}
```

#### 环入口

```C++
//slow:x+y   fast:x+n*(y+z)  --->   x=n(y+z)+z
ListNode *detectCycle(ListNode *head) {
    if(head==NULL) return NULL;

    ListNode* slow=head;
    ListNode* fast=head;
    while(fast->next!=NULL && fast->next->next!=NULL) {
        slow=slow->next;
        fast=fast->next->next;
        if(slow==fast) {
            ListNode* meet=slow;
            ListNode* entry=head;
            while(meet!=entry) {
                meet=meet->next;
                entry=entry->next;
            }
            return entry;
        }
    } 
    return NULL;;
}
```



### 字符串

> C语言字符串以‘\0’结尾，C++ string没有

#### 字符串反转

```C++
void reverse(vector<char>& s,int start,int end){
    for(int i=start;i<=(start+end)/2;i++){
        swap(s[i],s[end+start-i]);
    }
}
----------------swap--------------------------------
int temp = s[i];
s[i] = s[j];
s[j] = temp;

a[i] = a[i] ^ a[j]; 
a[j] = a[i] ^ a[j]; // a[j] = a[i] ^ a[j] ^ a[j] = a[i]
a[i] = a[i] ^ a[j]; // a[i] = a[i] ^ a[j] ^ a[i] = a[j]

a[i] = a[i] + a[j];
a[j] = a[i] - a[j]; // a[j] = a[i] + a[j] - a[j]
a[i] = a[i] - a[j]; // a[i] = a[i] + a[j] - a[i]
```

#### 朴素模式匹配

```C++
int i=0,m=text.size(),n=model.size();
while(i+n<=m){
    if(model.compare(m.substr(i,n))!=0) ++i;
    else return i;
}
return 0;
```

#### Sunday匹配

```C++
int i=0, j=0, m=text.size(), n=model.size();

# define MAXCH 256
int* offset=new int[MAXCH];
for(int k=0; k<MAXCH; k++) {
    offset[k]=n+1;
}
for(int k=0; k<n; k++) {
    offset[model[k]]=n-k;
}

while(i+n<=m) {
    while(text[i+j]==model[j]) {
        ++j;
        if(j>=n) return i;
    }
    i+=offset[text[i+n]];
    j=0
}
return 0;
```

#### KMP

```C++
// j point to prefix end, i point to suffix end +1
void getNext(int* next, const string& s) {
    int j=-1;
    next[0]=-1;
    for(int i=1; i<s.size(); i++) {
        while(j>=0 && s[i]!=s[j+1]) {
            j=next[j];
        }
        if(s[i]==s[j+1]) {
            j++;
        }
        next[i]=j;
    }
}

int strStr(string haystack, string needle) {
    if(needle.size()==0) return -1;
    int next[needle.size()];
    getNext(next, needle);
    
    int j=-1;
    for(int i=0; i<haystack.size(); i++) {
        while(j>=0 && haystack[i]!=needle[j+1]) {
            j=next[j];
        }
        if(haystack[i]==needle[j+1]) {
            j++;
        }
        if(j==needle.size()-1) {
            return i-needle.size()+1;
        }
    }
    return -1;
}
```



### 哈希表

>  **快速判断一个元素是否出现过的场景**（紧凑数据用数组，分散数据用集合，对应关系用字典）
>
>  | 集合               | 底层实现   | 是否有序 | 数值是否可以重复 | 能否更改数值 | 查询效率 | 增删效率 |
>| ------------------ | ---------- | -------- | ---------------- | ------------ | -------- | -------- |
>  | std::set           | 红黑树     | **有序** | 否               | 否           | O(log n) | O(log n) |
>  | std::multiset      | 红黑树     | 有序     | **是**           | 否           | O(logn)  | O(logn)  |
>  | std::unordered_set | **哈希表** | 无序     | 否               | 否           | O(1)     | O(1)     |
>  
>  | 映射               | 底层实现   | 是否有序    | 数值是否可以重复 | 能否更改数值 | 查询效率 | 增删效率 |
>| ------------------ | ---------- | ----------- | ---------------- | ------------ | -------- | -------- |
>  | std::map           | 红黑树     | **key有序** | key不可重复      | key不可修改  | O(logn)  | O(logn)  |
>  | std::multimap      | 红黑树     | key有序     | **key可重复**    | key不可修改  | O(log n) | O(log n) |
>  | std::unordered_map | **哈希表** | key无序     | key不可重复      | key不可修改  | O(1)     | O(1)     |

#### 两三数之和组合与去重

```C++
//a = nums[i], b = nums[j], c = -(a + b), a + b + c = 0, 三数之和是在确定第一个数的情况下求两数之和并去重
vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());			//需要排序、不可返回索引
    
    vector<vector<int>> res;
    for(int i=0; i<nums.size(); i++) {
        if(nums[i]>0) {
            break;
        }
        if(i>0 && nums[i]==nums[i-1]) {		//三元组元素a去重
            continue;
        }
        unordered_set<int> s;
        for(int j=i+1; j<nums.size(); j++) {
            if(j>i+2 && nums[j]==nums[j-1]  && nums[j-1]==nums[j-2]) {		//三元组元素b去重
                continue;
            }
            int c=-(nums[i]+nums[j]);
            if(s.find(c)!=s.end()) {
                res.push_back({nums[i],nums[j],c});
                s.erase(c);		//三元组元素c去重
            }else{
                s.insert(nums[j]);
            }
        }
    }
    return res;
}
```



### 栈

> 注意st.empty()再确定st.pop() 或者 st.top()

#### 匹配括号

```C++
bool isValid(string s) {
    stack<char> st;
    for(int i=0; i<s.size(); i++) {
        if(s[i]=='(') st.push(')');
        else if(s[i]=='{') st.push('}');
        else if(s[i]=='[') st.push(']');
        else if(!st.empty() && st.top()==s[i]) st.pop();
        else return false;
    }
    return st.empty();
}
```

#### 计算逆波兰式

```C++
int evalRPN(vector<string>& tokens) {
    stack<int> st;
    for(int i=0;i<tokens.size();i++){
        if(tokens[i]=="+"){
            int num2=st.top();
            st.pop();
            int num1=st.top();
            st.pop();
            int res=num1+num2;
            st.push(res);
        }
        else if(tokens[i]=="-"){
            int num2=st.top();
            st.pop();
            int num1=st.top();
            st.pop();
            int res=num1-num2;
            st.push(res);
        }
        else if(tokens[i]=="*"){
            int num2=st.top();
            st.pop();
            int num1=st.top();
            st.pop();
            int res=num1*num2;
            st.push(res);
        }
        else if(tokens[i]=="/"){
            int num2=st.top();
            st.pop();
            int num1=st.top();
            st.pop();
            int res=num1/num2;
            st.push(res);
        }
        else st.push(atoi(tokens[i].c_str()));
    }
    return st.top();
}
```

#### 栈->队列

```C++
class MyQueue {
public:
    MyQueue() {

    }
    
    void push(int x) {
        stIn.push(x);
    }
    
    int pop() {
        if(stOut.empty()) {
            while(!stIn.empty()) {
                stOut.push(stIn.top());
                stIn.pop();
            }
        }
        int res=stOut.top();
        stOut.pop();
        return res;
    }
    
    int peek() {
        int res=this->pop();
        stOut.push(res);
        return res;
    }
    
    bool empty() {
        return stIn.empty() && stOut.empty();
    }
private:
    stack<int> stIn;
    stack<int> stOut;
};
```



### 队列

> 注意que.empty()再确定que.pop() 或者 que.front()、que.back()

#### 队列->栈

```C++
class MyStack {
public:
    MyStack() {

    }
    
    void push(int x) {
        que.push(x);
    }
    
    int pop() {
        int size=que.size();;
        size--;
        while(size--) {
            que.push(que.front());
            que.pop();
        }
        int res=que.front();
        que.pop();
        return res;
    }
    
    int top() {
        return que.back();
    }
    
    bool empty() {
        return que.empty();
    }
private:
    queue<int> que;
};
```

#### 单调队列(滑动窗口最值)

```C++
class MyQueue { 
public:
    void pop(int value) {
        if (!que.empty() && value == que.front()) {
            que.pop_front();
        }
    }
    
    void push(int value) {
        while (!que.empty() && value > que.back()) {
            que.pop_back();
        }
        que.push_back(value);

    }

    int front() {
        return que.front();
    }
private:
    deque<int> que; 
};
```

#### 优先队列(TOPK)

```C++
#include <queue>
priority_queue<Type, Container, Functional>
//将Type类型数据以Container存储，并以Functional的方式排序优先级,其中Container可以是vector或者deque,Functional可自定义优先级
//底层为vector，堆heap为处理规则来管理底层容器实现
    
class cmp {
public:
    bool operator()(const pair<int, int>& lhs, const pair<int, int>& rhs) {
        return lhs.second > rhs.second;
    }      
}; //小顶堆

priority_queue<pair<int,int>, vector<pair<int,int>>, cmp> pri_que;
pri_que.top();  
pri_que.pop();
pri_que.push(val);				//产生一个val副本，再插入队列
pri_que.emplace(num1,num2);   		//直接传入构造对象需要的元素，内部自动构造一个元素并插入队列
pri_que.empty();
pri_que.size();      
```



### 二叉树

> - **满二叉树：**深度为k时，2^k^-1个节点；若最后一层按序未填满，则为**完全二叉树**
> - **二叉搜索树**：左子树都小于根节点，右子树都大于根节点；左右子树高度差不超过1，则为**平衡二叉搜索树**
>
> 1. 链式存储：构建结构体指针
> 2. 顺序存储：对父节点下标`i`，左孩子下标为`2i+1`，右孩子下标为`2i+2`

#### 定义

```C++
struct treeNode {
    int val;
    treeNode* left;
    treeNode* right;
    treeNode(int x):val(x), left(NULL), right(NULL) {}
}
```

#### 遍历

```C++
void preOrder(treeNode* cur, vector<int>& res) {
    if(cur==NULL) {
        return;
    }
    res.push_back(cur->val);
    preOrder(cur->left, res);
    preOrder(cur->right, res);
}
------------------------------------------------------------------------------
void inOrder(treeNode* cur, vector<int>& res) {
    if(cur==NULL) {
        return;
    }
    inOrder(cur->left, res);
    res.push_back(cur->val);
    inOrder(cur->right, res);
}
------------------------------------------------------------------------------
void postOrder(treeNode* cur, vector<int>& res) {		// **递归模板**
    if(cur==NULL) {
        return;
    }
    postOrder(cur->left, res);
    postOrder(cur->right, res);
    res.push_back(cur->val);
}
```

```C++
//任何操作附属着栈操作即可
vector<int> preorderTraversal(TreeNode* root) {		//遍历顺序和二叉树访问顺序一致，顺序衍生
    vector<int> res;
    stack<TreeNode*> st;
    if(root!=NULL) {
        st.push(root);
    }
    
    while(!st.empty()) {
        TreeNode* cur=st.top();
        st.pop();

        res.push_back(cur->val);
        if(cur->right) {
            st.push(cur->right);
        }  
        if(cur->left) {
            st.push(cur->left);
        }
    }

    return res;
}
------------------------------------------------------------------------------
vector<int> inorderTraversal(TreeNode* root) {		//用栈保存中间节点，逆向回退
    vector<int> res;
    stack<TreeNode*> st;
    TreeNode* cur=root;
    
    while(cur!=NULL || !st.empty()) {
        if(cur!=NULL) {
            st.push(cur);
            cur=cur->left;
        }
        else {
            cur=st.top();
            st.pop();

            res.push_back(cur->val);
            cur=cur->right;
        }
    }
    
    return res;
}
------------------------------------------------------------------------------
vector<int> postorderTraversal(TreeNode* root) {
    vector<int> res;
    stack<TreeNode*> st;
    if(root!=NULL) {
        st.push(root);
    }

    while(!st.empty()) {
        TreeNode* cur=st.top();
        st.pop();

        res.push_back(cur->val);
        if(cur->left) {
            st.push(cur->left);
        }
        if(cur->right) {
            st.push(cur->right);
        }
    }

    reverse(res.begin(), res.end());
    return res;
}
------------------------------------------------------------------------------
vector<int> traversal(TreeNode* root) {				
    vector<int> res;
    stack<TreeNode*> st;
    if(root!=NULL) {
        st.push(root);
    }
    
    while (!st.empty()) {
        TreeNode* cur = st.top();
        st.pop();
        if (cur != NULL) {
            if (cur->right) st.push(cur->right);
            st.push(cur);                          
            st.push(NULL);			//空节点标记
            if (cur->left) st.push(cur->left);    
        } 
        else { 
            cur = st.top();    
            st.pop();
            res.push_back(cur->val); 
        }
    }
    return res;
}
```

```C++
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> res;
    queue<TreeNode*> que;
    if(root!=NULL) {
        que.push(root);
    }

    while(!que.empty()) {
        vector<int> vec;
        int size=que.size();

        for(int i=0; i<size; i++) {
            TreeNode* cur=que.front();
            que.pop();
            vec.push_back(cur->val);

            if(cur->left) {
                que.push(cur->left);
            }
            if(cur->right) {
                que.push(cur->right);
            }
        }
        res.push_back(vec);
    }

    return res;
}
```

```C++
vector<int> morrisInorderTraversal(TreeNode* root) {
    vector<int> res;
    TreeNode* cur=root;
    while(cur!=NULL) {
        if(cur->left==NULL) {
            res.push_back(cur->val);
            cur=cur->right;
        }
        else {
            TreeNode* pre=cur->left;
            while(pre->right!=NULL && pre->right!=cur) {
                pre=pre->right;
            }
            if(pre->right==cur) {	//已有线索，已探索
                pre->right=NULL;
                cur=cur->right;
            }
            else {				//设置线索
                pre->right=cur;
                cur=cur->left;
            }
        }
    }
}
```

#### 翻转

```C++
TreeNode* invertTree(TreeNode* root) {
        if (root == NULL) return root;
        invertTree(root->left);         
        swap(root->left, root->right); 
        invertTree(root->left);         // 注意 这里依然要遍历左孩子，因为中间节点已经翻转了
        return root;
}
```

#### 构造

```C++
TreeNode* traversal(vector<int>& inorder,int inorderBegin, int inorderEnd, vector<int>& postorder, int postorderBegin, int postorderEnd) {
    if(postorderBegin==postorderEnd) return NULL;

    int rootVal=postorder[postorderEnd-1];
    TreeNode* root=new TreeNode(rootVal);
    
    if(postorderBegin==postorderEnd-1) return root;		//减少可省略

    int rootPos;
    for(rootPos=0; rootPos<inorderEnd; rootPos++) {
        if(inorder[rootPos]==rootVal) {
            break;
        }
    }

    root->left=traversal(inorder, inorderBegin, rootPos, postorder, postorderBegin, postorderBegin+rootPos-inorderBegin);
    root->right=traversal(inorder, rootPos+1, inorderEnd, postorder, postorderBegin+rootPos-inorderBegin, postorderEnd-1);

    return root;
}
------------------------------------------------------------------------------
TreeNode* traversal(vector<int>& inorder,int inorderBegin, int inorderEnd, vector<int>& preorder, int preorderBegin, int preorderEnd) {
    if(preorderBegin==preorderEnd) return NULL;

    int rootVal=preorder[preorderBegin];
    TreeNode* root=new TreeNode(rootVal);

    if(preorderBegin==preorderEnd-1) return root;

    int rootPos;
    for(rootPos=0; rootPos<inorderEnd; rootPos++) {
        if(inorder[rootPos]==rootVal) {
            break;
        }
    }

    root->left=traversal(inorder, inorderBegin, rootPos, preorder, preorderBegin+1, preorderBegin+1+rootPos-inorderBegin);
    root->right=traversal(inorder, rootPos+1, inorderEnd, preorder, preorderBegin+1+rootPos-inorderBegin, preorderEnd);

    return root;
}
```

#### 合并

```C++
TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
    if(root1==NULL) return root2;
    if(root2==NULL) return root1;

    root1->val+=root2->val;
    root1->left=mergeTrees(root1->left, root2->left);
    root1->right=mergeTrees(root1->right, root2->right);
    return root1;

```

#### 公共祖先

```C++
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if(root==p || root==q || root==NULL) return root;

    TreeNode* leftPointer = lowestCommonAncestor(root->left, p , q);
    TreeNode* rightPointer = lowestCommonAncestor(root->right, p , q);

    if(leftPointer!=NULL && rightPointer!=NULL)  return root;
    else if(leftPointer==NULL && rightPointer!=NULL) return rightPointer;
    else if(leftPointer!=NULL && rightPointer==NULL) return leftPointer;
    else return NULL;
}
```

#### 二叉搜索树

##### 查找

```C++
TreeNode* searchBST(TreeNode* root, int val) {
    if (root == NULL || root->val == val) return root;
    if (root->val > val) return searchBST(root->left, val);
    if (root->val < val) return searchBST(root->right, val);
    return NULL;
}
------------------------------------------------------------------------------
TreeNode* searchBST(TreeNode* root, int val) {
    while (root!=NULL) {
        if (root->val>val) root=root->left;
        else if (root->val<val) root=root->right;
        else return root;
    }
    return NULL;
}
```

##### 验证

```C++
vector<int> vec;	//二叉搜索树中序遍历对应数组升序
void traversal(TreeNode* cur) {
    if(cur==NULL) return;

    traversal(cur->left);
    vec.push_back(cur->val);
    traversal(cur->right);
}
------------------------------------------------------------------------------
long long maxVal = LONG_MIN; 	//后台测试数据中有int最小值
bool isValidBST(TreeNode* root) {
    if (root==NULL) return true;

    bool left=isValidBST(root->left);
    
    if (maxVal < root->val) maxVal=root->val;
    else return false;
    
    bool right = isValidBST(root->right);
    return left && right;
}
------------------------------------------------------------------------------
TreeNode* pre = NULL; 		// 用来记录前一个节点
bool isValidBST(TreeNode* root) { 
    if (root == NULL) return true;
    bool left = isValidBST(root->left);

    if (pre!=NULL) {
        if(pre->val >= root->val) return false;
    }
    pre = root; 

    bool right = isValidBST(root->right);
    return left && right;
}
```

##### 插入

```c++
TreeNode* insertIntoBST(TreeNode* root, int val) {
    if (root == NULL) {
        TreeNode* node = new TreeNode(val);
        return node;
    }
    if (root->val > val) root->left = insertIntoBST(root->left, val);
    if (root->val < val) root->right = insertIntoBST(root->right, val);
    return root;
}
```

##### 删除

```C++
TreeNode* deleteNode(TreeNode* root, int key) {
    if(root==NULL) return NULL;

    else if(root->val==key) {
        if(root->left==NULL && root->right==NULL) {
            delete root;
            return NULL;
        }
        else if(root->left!=NULL && root->right==NULL) {
            TreeNode* retNode=root->left;
            delete root;
            return retNode;
        }
        else if(root->left==NULL && root->right!=NULL) {
            TreeNode* retNode=root->right;
            delete root;
            return retNode;
        }
        else {
            TreeNode* cur=root->right;
            while(cur->left!=NULL) {
                cur=cur->left;
            }
            cur->left=root->left;

            TreeNode* tmp=root;
            root=root->right;
            delete tmp;
            return root;
        }
    }

    else if(root->val>key){
        root->left=deleteNode(root->left, key);
    }
    else {
        root->right=deleteNode(root->right, key);
    }
    return root;
}
------------------------------------------------------------------------------

TreeNode* deleteNode(TreeNode* root, int key) {
    if (root == nullptr) return root;
    if (root->val == key) {
        if (root->right == nullptr) { // 这里第二次操作目标值：最终删除的作用
            return root->left;
        }
        TreeNode *cur = root->right;
        while (cur->left) {
            cur = cur->left;
        }
        swap(root->val, cur->val); // 这里第一次操作目标值：交换目标值其右子树最左面节点。
    }
    root->left = deleteNode(root->left, key);
    root->right = deleteNode(root->right, key);
    return root;
}

```

##### 修剪

```C++
TreeNode* trimBST(TreeNode* root, int low, int high) {
    if(root==NULL) return NULL;
    else if(root->val<low) return trimBST(root->right, low, high);
    else if(root->val>high) return trimBST(root->left, low, high);
    else {
        root->left=trimBST(root->left, low, high);
        root->right=trimBST(root->right, low, high);
        return root;
    }
}
```

##### 平衡构造

```C++
TreeNode* traversal(vector<int>& nums, int left, int right) {		//自然平衡
    if (left > right) return nullptr;
    int mid = left + ((right - left) / 2);
    TreeNode* root = new TreeNode(nums[mid]);
    root->left = traversal(nums, left, mid - 1);
    root->right = traversal(nums, mid + 1, right);
    return root;
}
```

##### 公共祖先

```C++
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {   	//二叉搜索树版
    if(root==NULL) return NULL;
    else if(p->val<root->val && q->val<root->val) return lowestCommonAncestor(root->left, p, q);
    else if(p->val>root->val && q->val>root->val) return lowestCommonAncestor(root->right, p, q);
    else return root;
}
```

##### 累加树

```C++
void traversal(TreeNode* cur, int& sum) {
    if(cur==NULL) return;

    if(cur->right) traversal(cur->right, sum);
    sum+=cur->val;
    cur->val=sum;
    if(cur->left) traversal(cur->left, sum);
}
```



### 回溯

> 递归：
>
> 1. 形成最优子结构性质：原问题和若干**相同独立**子问题之间的**关系**
> 2. 确定函数参数和返回值
> 3. 确定递归终止条件：
> 4. 根据最优子结构确定递归逻辑
>
> 回溯：
>
> 1. 将组合/切割/子集/排列问题抽象为**树形结构**
>
> 2. ```C++
>    vector<vector<type>> res;
>    vector<type> path;
>    void backtracking(参数) {
>        //子集：存放结果
>        if (终止条件) {		//组合：到达数量、切割：到达串底部、子集：剩余集合空
>            //组合、切割：存放结果;
>            return;
>        }
>                                                                         
>        for (选择：startIndex树本层集合中元素) {		//排列：使用used从0开始尝试
>            处理节点;
>            backtracking(路径，选择列表); // 递归到树下一层
>            回溯，撤销处理结果;
>        }
>    }
>    ```
>    
> 3. 剪枝

#### 递归

##### 模板

```C++
//所有路径 、 路径和
void traversal(TreeNode* cur, vector<int>& path, vector<string>& result) {
    path.push_back(cur->val);							//最后一个节点也要加入到path中 
    if (cur->left == NULL && cur->right == NULL) {
        string sPath;
        for (int i = 0; i < path.size() - 1; i++) {
            sPath += to_string(path[i]);
            sPath += "->";
        }
        sPath += to_string(path[path.size() - 1]);
        result.push_back(sPath);
        return;
    }
    
    if (cur->left) {
        traversal(cur->left, path, result);
        path.pop_back(); 
    }
    if (cur->right) {
        traversal(cur->right, path, result);
        path.pop_back(); 
    }
}

void traversal(TreeNode* cur, string path, vector<string>& result) {
    path += to_string(cur->val);
    if (cur->left == NULL && cur->right == NULL) {
        result.push_back(path);
        return;
    }
    if (cur->left) traversal(cur->left, path + "->", result); 
    if (cur->right) traversal(cur->right, path + "->", result); 
}
1.全局变量或者引用函参用于存储全局参与参数
2.局部变量仅作用于当前递归层次
3.直接函参与回溯处理有相同的效果，但回溯处理更好理解。
    
bool traversal(TreeNode* cur, int targetSum) {
    sum+=cur->val;
    if(cur->left==NULL && cur->right==NULL) {
        if(sum==targetSum) {
        	return true;
        }
        sum-=cur->val;		//补充回溯,可省略
        return false;		//补充回溯,可省略
    }

    if(cur->left) {
        if(trackbacking(cur->left, targetSum)) return true;
    }
    if(cur->right) {
        if(trackbacking(cur->right, targetSum)) return true;
    }
    sum-=cur->val;		//每出现一次符合条件路径，就少一次回溯
    return false;
}
1.递归过程需要返回值的递归函数非void
2.寻找某一符合条件路径的递归函数非void
3.注意回溯必须是对当前轮次值的回溯
    
void backtracking(TreeNode* cur, int targetSum){
    sum+=cur->val;
    path.push_back(cur->val);
    if(cur->left==NULL && cur->right==NULL) {
        if(sum==targetSum){
            res.push_back(path);
        }
        sum-=cur->val;			//补充回溯,不可省略
        path.pop_back(); 		//补充回溯,不可省略
        return;
    }  

    if(cur->left) {
        backtracking(cur->left, targetSum);
    }
    if(cur->right) {
        backtracking(cur->right, targetSum);
    }

    sum-=cur->val;
    path.pop_back();
}
1.寻找所有符合条件路径的递归函数不可省略出口回溯
    
void backtracking(TreeNode* cur, int targetSum) {
    if (cur->left==NULL && cur->right==NULL && sum==targetSum) {
        res.push_back(path);
        return;
    }

    if (cur->left) {
        sum += cur->left->val;
        path.push_back(cur->left->val);
        backtracking(cur->left, targetSum);    
        sum -= cur->left->val;       
        path.pop_back();                
    }
    if (cur->right) { 
        sum += cur->right->val;
        path.push_back(cur->right->val);
        backtracking(cur->right, targetSum);   
        sum -= cur->right->val;      
        path.pop_back();               
    }
    return;
}

vector<vector<int>> pathsum(treenode* root, int targetSum) {
    if (root != NULL) {
        path.push_back(root->val); 
    	backtracking(root, targetSum-root->val);
    }
    return res;
}
1.关于路径缺头少尾的问题，可用上述模板
```

##### 二维递归（解数独）

```C++
bool backtracking(vector<vector<char>>& board) {
    for (int i = 0; i < board.size(); i++) {        // 遍历行
        for (int j = 0; j < board[0].size(); j++) { // 遍历列
            if (board[i][j] != '.') continue;
            for (char k = '1'; k <= '9'; k++) {     // (i, j) 这个位置放k是否合适
                if (isValid(i, j, k, board)) {
                    board[i][j] = k;                
                    if (backtracking(board)) return true; // 如果找到合适一组立刻返回
                    board[i][j] = '.';             
                }
            }
            return false;                           
        }
    }
    return true; 
}

bool isValid(int row, int col, char val, vector<vector<char>>& board) {
    for (int i = 0; i < 9; i++) { 
        if (board[row][i] == val) {
            return false;
        }
    }
    for (int j = 0; j < 9; j++) { 
        if (board[j][col] == val) {
            return false;
        }
    }
    int startRow = (row / 3) * 3;
    int startCol = (col / 3) * 3;
    for (int i = startRow; i < startRow + 3; i++) {
        for (int j = startCol; j < startCol + 3; j++) {
            if (board[i][j] == val ) {
                return false;
            }
        }
    }
    return true;
}
```

####  回溯

```C++
vector<vector<int>> res;
vector<int> path;
void backtracking(vector<int>& nums,int startIndex, vector<bool>& used) {
    if(startIndex==nums.size()) {
        res.push_back(path);
        return;
    }
    for(int i=startIndex||0; i<nums.size(); i++) {
        if(!used[i]){
            path.push_back(nums[i]);
            used[i]=true;
            backtracking(nums, i+1, used);
            path.pop_back();
            used[i]=false;
        }
    }
}
```

```C++
//去重版（以组合总和为例）
...
int sum=0;
void backtracking(int target, vector<int>& candidates, int startIndex, vector<bool>& used) {
    if(sum==target) {
        res.push_back(path);
        return;
    }
    for(int i=startIndex; i<candidates.size() && sum+candidates[i]<=target; i++) {
        if(i>0 && candidates[i]==candidates[i-1] && used[i-1]==false) {
            continue;
        }
        sum+=candidates[i];
        path.push_back(candidates[i]);
        used[i]=true;
        backtracking(target, candidates, i+1, used);
        sum-=candidates[i];
        path.pop_back();
        used[i]=false;
    }
}

void backtracking(int target, vector<int>& candidates, int startIndex) {
    ...
    for(int i=startIndex; i<candidates.size() && sum+candidates[i]<=target; i++) {
        if(i>startIndex && candidates[i]==candidates[i-1]) {
            continue;
        }
        sum+=candidates[i];
        path.push_back(candidates[i]);
        backtracking(target, candidates, i+1);
        sum-=candidates[i];
        path.pop_back();
    }
}

void backtracking(int target, vector<int>& candidates, int startIndex) {
    ...
    unordered_set<int> uset;
    for(int i=startIndex; i<candidates.size() && sum+candidates[i]<=target; i++) {
        if(uset.find(candidates[i])==uset.end()){
            uset.insert(candidates[i]);
            sum+=candidates[i];
            path.push_back(candidates[i]);
            backtracking(target, candidates, i+1);
            sum-=candidates[i];
            path.pop_back();
        }
    }
}  		//对于具有顺序关系的序列题目（排列、递增子序列），使用uset可不sort，

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    vector<bool> used(candidates.size(), false);
    sort(candidates.begin(), candidates.end());
    backtracking(target, candidates, 0, used);
    return res;
}
```

#### 重新安排行程

```C++
unordered_map<string, map<string, int>> targets;
bool backtracking(int ticketNum, vector<string>& plan) {
    if(plan.size()==ticketNum+1) {
        return true;
    }

    for(pair<const string, int>& target : targets[plan[plan.size()-1]]) {
        if(target.second>0) {
            plan.push_back(target.first);
            target.second--;
            if(backtracking(ticketNum, plan)) return true;
            plan.pop_back();
            target.second++;
        }   
    }
    return false;
}

vector<string> findItinerary(vector<vector<string>>& tickets) {
    for(const vector<string> ticket : tickets) {
        targets[ticket[0]][ticket[1]]++;
    }

    vector<string> plan;
    plan.push_back("JFK");
    backtracking(tickets.size(), plan);
    return plan;
}  
```



### 贪心

> 模拟尝试：选择**每个子问题的局部最优**，将局部最优堆叠成全局最优，否则dp

#### 分发饼干

```C++
int findContentChildren(vector<int>& g, vector<int>& s) {
    sort(g.begin(),g.end());
    sort(s.begin(),s.end());
    int index = 0;
    for(int i = 0; i < s.size(); i++) { // 饼干
        if(index < g.size() && g[index] <= s[i]){ // 胃口
            index++;
        }
    }
    return index;
}
```

#### 摆动序列

```C++
int wiggleMaxLength(vector<int>& nums) {
    if(nums.size()<=1) return nums.size();

    int res=1;
    int preDiff=0;
    int curDiff;
    for(int i=1; i<nums.size(); i++) {
        curDiff=nums[i]-nums[i-1];
        if((preDiff>=0 && curDiff<0) || (preDiff<=0 && curDiff>0)) {
            res++;
            preDiff=curDiff;
        }
    }
    
    return res;
}
```

#### 跳跃游戏

```C++
int jump(vector<int>& nums) {
    if(nums.size()==1) return 0;

    int curCover=0;
    int step=0;
    int nextCover=0;
    for (int i=0; i<=nextCover; i++) {
        nextCover=max(nextCover, i+nums[i]);
        if(i==curCover) {
            if(curCover>=nums.size()-1) return step;
            curCover=nextCover;
            step++;
            if(curCover>=nums.size()-1) return step; 
        }
    }
    return -1;
}
```

#### 加油站

```C++
int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    int curSum=0;       //为正，则为正作用起点，可为后续积攒力量
    int totalSum=0;     //totalSum>=0那一定可以跑完一圈
    int start=0;

    for(int i=0; i<gas.size(); i++) {
        curSum+=(gas[i]-cost[i]);
        totalSum+=(gas[i]-cost[i]);
        if(curSum<0) {
            start=i+1;
            curSum=0;
        }
    }
    if(totalSum>=0) return start;
    return -1;
}
```

#### 分发糖果

```C++
int candy(vector<int>& ratings) {
    int size=ratings.size();
    vector<int> candies(size, 1);

    for(int i=1; i<size; i++) {
        if(ratings[i]>ratings[i-1])
            candies[i]=candies[i-1]+1;
    }
    for(int i=size-1; i>0; i--) {
        if(ratings[i-1]>ratings[i]) {
            candies[i-1]=max(candies[i-1], candies[i]+1);
        }
    }

    int candySum=0;
    for(int i=0; i<size; i++) candySum+=candies[i];
    return candySum;
}
```

#### 身高重建队列

```C++
static bool cmp(vector<int>& a, vector<int>& b) {
        if(a[0]==b[0]) return a[1]<b[1];
        return a[0]>b[0];
    }
vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
    sort(people.begin(), people.end(), cmp);

    vector<vector<int>> que;
    for(int i=0; i<people.size(); i++) {
        int pos=people[i][1];
        que.insert(que.begin()+pos, people[i]);
    }
    return que;
}
```

#### 重叠区间

```C++
static bool cmp(const vector<int>& a, const vector<int>& b) {
    return a[0]<b[0]; //左边界排序
}
int OverlapIntervals(vector<vector<int>>& intervals) {
    if(intervals.size()==0) return 0;
    
    sort(intervals.begin(), intervals.end(), cmp);
    int res=0;
    for (int i=1; i<intervals.size(); i++) {
        if (intervals[i][0]<intervals[i-1][1]) { //重叠情况
            intervals[i][1]=min(intervals[i-1][1], intervals[i][1]);
            res++;
        }
    }
    return res;
}
```

#### 非重叠区间

```C++
static bool cmp (const vector<int>& a, const vector<int>& b) {
    return a[1]<b[1]; // 右边界排序
}
int nonOverlapIntervals(vector<vector<int>>& intervals) {
    if (intervals.size()==0) return 0;
    
    sort(intervals.begin(), intervals.end(), cmp);
    int res=1;
    int end=intervals[0][1];
    for (int i=1; i<intervals.size(); i++) {
        if (end<=intervals[i][0]) {
            end=intervals[i][1];
            res++;
        }
    }
    return res;
}
```

#### 划分字母区间

```C++
vector<int> partitionLabels(string s) {
    int hash[26]={0};
    for(int i=0; i<s.size(); i++) {
        hash[s[i]-'a']=i;
    }

    vector<int> res;
    int left=0, right=0;
    for(int i=0; i<s.size(); i++) {
        right=max(right, hash[s[i]-'a']);
        if(i==right) {
            res.push_back(right-left+1);
            left=right+1;
        }
    }
    return res;
}
```

#### 单调递增数字

```C++
int monotoneIncreasingDigits(int n) {
    string strNum=to_string(n);
    int flag=strNum.size();
    for(int i=strNum.size()-1; i>0; i--) {
        if(strNum[i-1]>strNum[i]) {
            strNum[i-1]--;
            flag=i;
        }
    }
    for(int i=flag; i<strNum.size(); i++) {strNum[i]='9';
    return stoi(strNum);
}
```

#### 监控二叉树

```c++
int res=0;
int traversal(TreeNode* cur) {
    if(cur==NULL) return 2;       
    int left=traversal(cur->left);
    int right=traversal(cur->right);
    if(left==0 || right==0) {
        res++;
        return 1;   
    }
    else if(left==1 || right==1) return 2;
    else return 0;
}

int minCameraCover(TreeNode* root) {
    if(traversal(root)==0) res++;
    return res;
}
```



### 动态规划

> 拆分==子问题==（**确定dp数组下标含义**），==记住==过往，状态dp推导（**确定递推公式**），**初始化和dp数组遍历顺序**，**打印dp数组debug**

#### 最大子数组和

```C++
int maxSubArray(vector<int>& nums) {
    int res=INT_MIN;
    int sum=0;

    for(int i=0; i<nums.size(); i++) {
        sum+=nums[i];
        if(sum>res) {
            res=sum;
        }

        if(sum<0) sum=0;
    }

    return res;
}
```

#### 买卖股票的最佳时机II

```C++
int maxProfit(vector<int>& prices) {
    int res=0;
    for(int i=1; i<prices.size(); i++) {
        res+=max(prices[i]-prices[i-1], 0);
    }
    return res;
}
```

```C++
int maxProfit(vector<int>& prices, int fee) {
    int res=0;
    int minPrice=prices[0];

    for(int i=1; i<prices.size(); i++) {
        if(prices[i]<minPrice) {
            minPrice=prices[i];
        }
        else if(prices[i]>minPrice+fee) {
            res+=(prices[i]-minPrice-fee);
            minPrice=prices[i]-fee;
        }
        else continue;
    }
    return res;
}
```



## 七、时间复杂度

### 超时

- 算法死循环\栈溢出，debug算法
- 问题需要更低的时间复杂度算法，采用更多的空间或者简便的算法补齐
- 提高机器、语言、编译器的强度

### 复杂度计算

- 大O表示法：算法复杂度是关于问题规模n的运行单元数/内存空间的渐进
- 复杂度计算会**忽略低阶项和常数项**，但实际由于问题规模和忽略项的大小会存在很大的差异
- O(1)常数阶 < O(logn)对数阶 < O(n)线性阶 < O(n^2)平方阶 < O(n^3)立方阶 < O(2^n)指数阶
- 递归算法复杂度=递归的次数 * 每次递归中的操作次数/内存要求，一般可以通过树形结构计算
- 空间复杂度S(n)一般不包括程序本身，仅考虑程序运行时占用内存的大小，注意**传参形式**：传值调用、指针调用、引用调用



## 八、VScode快捷键

```txt
crtl + / 							# 注释
```



## 九、常见错误

1. 几个常见但不容易被发现的bug。

- 注意`++a`和`a++`  产生边界问题
- 注意**数据类型**溢出  导致结果出错
- **for循环末尾**对变量的变换  没有被考虑
- 多运行而不是大脑模拟



2. CCF 编译出错原因： 不允许C++STL容器嵌套。

```C++
map<string,list<string> > user;
```

就是要在后面的“>”之间，必须得有一个空格，如果有多层，那每层都得有一个空格。
