# Plonk学习笔记分享
## 前言
学习完郭老师的Plonk系列，并且跟着各位老师在本期共学社学习了一遍，对Plonk有一些基本的认识，于是想对本次学习内容做个整理。  

因为自己是从初学小白（在本次学习之前完全零基础，亦非Web3背景）开始，学习Plonk经历过从0开始的阶段。因此，在整理笔记，想可以对同样零基础的同学有所帮助。也在写的过程中将内容重新做了梳理、调整或扩充。可能对于已经熟悉的同学而言，内容及行文略显啰嗦。<br> 

另外，Github对于数学公式渲染显示的支持有限，部分内容显示效果不佳。本文可另详[hackmd版本链接](https://hackmd.io/@Dt_nNFZZRDmdFriUTBb_gw/Skd5EsouR)（显示效果更好）。

## 一、问题场景
Prover要向Verify证明，自己知道一个输入（此处采用向量表达） $\vec x=(x1,x2,x3,x4)$ ，可以使得 $(x1+x2) \cdot x3\cdot x4=out$ 。例如：Prover知道 $\vec x=(1,2,4,5)$ ，由这个输入可以得到 $out=60$ 的输出。  

当我把这个场景向原来的同事分享时，对方表示出难以置信的大笑：“这个还要证明？把它的输入给计算机，让程序算一遍不就知道了吗？”OK，在我自己完全不了解ZKP的背景前，我也是这样的反应：感觉是一个很瓜、很奇怪的问题。

重点来了！这里的任务是：需要将Prover知道的输入 $\vec x$ （视为一个知识）向Verifer保密，使得在Verifer不知道输入具体是什么的情况，仍然相应这个输入满足 $(x1+x2) \cdot x3\cdot x4=out$ 的关系。 $out$ 是共知的，但 $\vec x$ 是秘密的。

这样就顺手引出了ZKP协议之Plonk协议的目标之一：如何实现Prover不透露输入（这里术语用witness，即对应于 $x$ ）的情况下，仍然可以给出可信的证明，使得Verifer相信Prover真的知道witness（或输入 $\vec x$ ），使得 $f(\vec x)=out$ 。

这里有几点需要备注一下：
1. 这里可以看作输入与输出是一个函数关系，输入为 $\vec x$ ，输出为 $out=f(\vec x)$ ，可将这个输入与输出的关系称为约束（可视作为函数 $f$ ）。
2. 约束关系 $f$ 与输出 $out$ 为双方共知的，输入 $\vec x$ 为Prover的秘密知识。
3. 使用“电路”的形式，来表达这种约束关系。这个电路可以理解成，使用最基础的约束（即简单的加法乘法门），进行不断叠加，来表达整个的函数关系。或者反过来说，我们把复合函数不断拆解，形成一组离散的门，这些离散的门约束即为算术约束，同时各个离散门之间具有的约束关系为复制约束。<br> 例如 $f=(x1+x2)\cdot x3\cdot x4$ ，可以表示为一个加法门约束与两个乘法门约束的叠加，同时加法门与两个乘法门之间存在一种约束关系。如下图：

<div align="center">
 <img src="https://hackmd.io/_uploads/HJirzJhdA.png=100*100" width="300"/>
</div>


## 二、相关背景知识
在正式进入Plonk的内容之前，还需要先了解关于多项式编码的知识。  
设有一个向量 $\vec v=(1,2,5,6)$ ，我们将其编码在 $H=(1,2,3,4)$ ，即为将其转化为一个 $d<4$ 的多项式 $f(x)$ ，取多项式的根为 $H=(1,2,3,4)$ ，即 $v(1)=1,v(2)=2,v(3)=5,v(4)=6$ ，这里使用拉格朗日插值法，可以得到：

$$f_v(x)= -\frac{2}{3}x^3+5x^2-\frac{28}{3}x+6$$

这个过程可以理解为将 $N$ 个离散点编码为一个 $N-1$ 阶的多项式。那做多项编码有什么好处呢？  

例如，有两个向量， $\vec v=(1,2,5,6)$ ,  $\vec t=(1,2,5,7)$ ，如果直接验证向量 $v$ 是否等于 $t$ ，如果直接判断相当于做四次计算，判断 $v[i] \stackrel{?}{=}t[i],\  \forall i \in[0,|v|]$ 。

如果先将两个向量对应编码成多项式 $f_v(x)\ 与\ f_t(x)$ 。我们显然知道，当且仅当向量 $v$ 等于向量 $t$ 时，则两个多项式才完全相等，即 $f_v(x)=f_t(x)$ 。除了验算 $v[i] \stackrel{?}{=}t[i]$ ,有没有更简洁的方法？

**关键点来了**：针对这两个多项式是否相等，只需要选取一个随机点，即可以大概率地进行验证了。过程是这样的。例如，上面所举的例子中，拉格朗日插值法得到两个项式：

$$f_v(x)= -\frac{2}{3}x^3+5x^2-\frac{28}{3}x+6$$

$$f_t(x)= -\frac{1}{2}x^3+4x^2-\frac{15}{2}x+5$$

令 

$$f_s(x)=f_t(x)-f_v(x)=\frac{1}{6}x^3-x^2+\frac{11}{6}x-1$$  

 $f_s(x)$ 是一个 $degree=3$ 的多项式，那么 $f_s(x)=0$ 最多仅有3个解，即意味着， $f_v(x)$ 与 $f_t(x)$ 最多仅有3个交点。用这个小示例可知：两个 $d$ 阶的多项式，至多只有 $d$ 个点会相交。

这个小示例因为次数比较低，我们用肉眼当然可以判断二者的系数不等，但协议中并不是通过逐项比较各个系数，而是使用 Schwartz-Zippel 定理的结论进行随机挑战来判断：
>Schwartz-Zippel 定理:  <br>
如果有两个多项式 f(x) 和 g(x) 同为两个次数不超过 d 的多项式。那么 Verifier 只需要给出一个随机挑战值 ζ∈F ，计算 f(ζ) 是否等于 g(ζ) 即可大概率得知 f(x)=g(x) ，其中出错的概率 ≤d/|F| 。只要保证 F 足够大，那么检查出错的概率就可以忽略不计。

那么在上述例子中，最多只可能有3个交点，假设 $x$ 的取值范围扩大为  $F$ ， $|F|=2^{254}$ ,则单次挑战出错的概率 $≤3/2^{254}$ 。

在后续的整个体系，都建立在此定理及其多项式编码的应用的基础上。

我的理解是，所有与验证离散点的关系的问题，（比如后面我们要证明的置换关系，或是Lookup中的查询关系）都可以用类似的思路转化为多项式关系，通过随机数挑战来验证。可以近似看为，将原本需要N次的验证计算，压缩到一次（极大概率正确）的验证。

## 三、Plonk原理及流程
### 1、概述 
有了以上基础后，就可以进入Plonk原理了！
在理解了郭老师的对Plonk讲解文章后，我对于阐述Plonk协议中流程的次序做了小小的调整，概括如下。\
（1）算术化：先通过Plonkish，将输入输出约束关系转化为Plonk能接受的约束表达式。不论这个约束是门电路的算术约束、还是暗含的拷贝约束。这个过程一并归入到算术化之中。这个部分可对应于Plonkathon（Plonkathon的python版代码中的Program这个部分。）\
（2）将约束关系，通过向量化的等式表达出来。这里尤其是如何将置换约束表达出来，Plonk协议可谓颇有些技巧。向量可近似理解为离散化的原始信息点。\
（3）有了向量化的等式表达，就可以通过多项式编码，将各约束式表达并压缩为单个多项式等式的约束关系，进而可以随机数挑战验证了！当然，整个过程中，需要用到好些方法技巧，使约束关系式的计算量缩减。\
（4）最后，使用多项式承诺，来验证约束式。由于本文篇幅有限，这部分暂且不做阐述，将于另外笔记中做总结整理。
### 2、算术化
在Plonk中的算术化称为Plonkish，即把一系列约束（或者说，一个函数关系），转化为一个Plonk协议能处理的数学形式。而任意一个复杂的计算过程（函数）、都可以最小化地拆解成多个加法门与乘法门关系的组合，（类似于计算机内部最底层操作都是加法计算，由加法运算组合起来构成更复杂的运算。）每一个加法或乘法门称为一个门约束的组合。\
这部分的详细阐述过程可以看[郭老师的原文](https://learn.z2o-k7e.world/plonk-intro-cn/plonk-arithmetization.html)，这里仅做个简单阐述。  

- 算术约束\
对于 $(x1+x2)\cdot x3\cdot x4=out$ 的示例，可拆解为三个算术约束：<br>
 $x1+x2=x6$ <br>
 $x3\cdot x4=x5$ <br>
 $x6\cdot x5=out$ <br>
我们的目标是，针对任意一个约束门，都能使用一个统一形式的数学等式进行表达。那么，我们就可以使用 $W$ 矩阵来表达约束： $\vec w_{a}$ 表示左输入， $\vec w_{b}$ 表示右输入， $\vec w_{c}$ 表示输出。同时，我们用 $Q$ 矩阵来表示单个约束的运算。\
最终，所有的算术约束可以统一化地转化为：\
 $\vec q_{L}\circ \vec w_{a}+\vec q_{R}\circ \vec w_{b}+\vec q_{M}\circ (\vec w_{a}\circ \vec w_{b})+\vec q_{c}-\vec q_{o}\circ \vec w_{c}=0。$ \
这里形成的 $Q$ 矩阵，是对于算术约束关系的描述，属于公开的公共知识。而作为输入的 $W$ 矩阵 $(W=[\vec w_{a},\vec w_{b},\vec w_{c}])$ ，则是仅Prover知道的秘密知识。\
现在，这个式子已经是一个关于向量运算的表达，基于前面的背景我们知道它已经具备多项式编码的条件了！

- 置换约束
如下图所示的两个电路，其 $Q$ 矩阵虽然完全相同，但这两个电路却完全不同。
<div align="center">
 <img src="https://hackmd.io/_uploads/rkgoZxnd0.png" width="700"/>
</div>

这是由于我们将计算过程拆解成了一步一步的加法或乘法计算，那么在每步计算之间都有关联关系。例如,第一个加法门:  
$x1+x2=out1$ \
 第二个乘法门：\
  $x6*x5=out2$  
这里第一个加法门的输出 $out1$ ，作为了第二个乘法门的左输入 $x6$ ，其实暗含了 $out1=x6$ 。
因此，这里两个有关联的约束门之间，二者还必须需要有关联约束。\
在Plonk中使用一种置换关系矩阵 $σ$ ，来表达这种关联约束，如下表:
<div align="center">
 <img src="https://hackmd.io/_uploads/SJUEQx3_C.png" width="250"/>
</div>

表中，相同颜色字母的变量为置换约束关系。例如，在第一个约束中的左输入 $w_{a1}=x_{6}$ ，须要求 $w_{a1}=w_{c2} (x_{6}与x_{6}置换)$ ，因此第二个约束中的输出 $w_{c2}$ 必须等于 $x_{6}$ 。

但是这种形式的表达仅能让我们知道，谁和谁置换（相等），却没有转化为类似算术约束的等式表达，无法进行多项式编码！因此，我们需要对约束关系进行深度挖掘，以便将其转化为向量式的数学等式表达。
### 3、置换关系转化为向量表达
整个过程需要用到一系列的方法：Grand Product—Multiset—Permuta—Copy Constraints，都是为了通过数学上的变换，将这种置换约束表达出来。（在后续的lookup之亦是类似的过程。）\
这里仅对这个过程作一个简述，详细过程参[郭老师原文章](https://learn.z2o-k7e.world/plonk-intro-cn/plonk-permutation.html)。

#### (1)Grand Product
证明一个连乘关系：

$$P=q_{0}* q_{1}*q_{2}.....q_{n-2}$$ 

我们通过引入一个中间的辅助向量 $r$ ，使得：<br>

$$r_{0}=1$$

$$r_{k+1}=q_{k}*r_{k}$$ 

那么，整个连乘过程，可以由以下步骤形成：
<div align="center">
 <img src="https://hackmd.io/_uploads/HkfU4xhdA.png" width="300"/>
</div>

这里只要我们可以转换为向{ $q_{i}$ }与{ $r_{i}$ }的形式，我们就可以进行多项式编码了。\
比如：由<br>

$$r_{0}=1$$

可得到:<br>

$$L_{0}(x)*(r(x)-1)=0$$

由

$$r_{k+1}=q_{k}*r_{k}$$

可得到： $q(x) * r(x) = r(w*x)$ <br>  

#### (2)Multiset
怎么证明，两个集合{ $p_{i}$ }与 { $q_{i}$ }，其中一个集合是另一个集合的乱序重排？\
如果直接将两个集合中的元素连乘然后判断相等，这种方法是无法证明的。比如反例:{3,6}不等于{9,2}）。\
这里只需要略作调整。针对将 { $q_{i}$ }集合的元素，看作一个多项式 $q(x)$ 的根。\
对于集合{ $q_{i}$ }，每个元素作为多项式的根可确定一个多项式，因此有惟一的多项式 $q(x)$ 与之对应:

$$q(x)=(X-q_{0})(X-q_{1})(X-q_{2})...(X-q_{n-1})$$ 

 因此，{ $p_{i}$ }与{ $q_{i}$ }是置换关系，可等价于<br>
 
 $$\prod(X-q_{i})=q(X)=p(X)=\prod(X-p_{i})$$

 进一步可等价于：<br>
 
 $$\prod\frac{X-q_{i}}{X-p_{i}}=1$$

到了这一步，我们已经将它变换为连乘的形式，于是可以使用上一节中的Grand Product了！\
**这里仍是应用了多项式编码的思想，可见多项式编码的思想贯穿始终！**

#### (3)置换证明
有了以上两步的基础，现在可以继续往更深的步骤进行推进了！

Multiset 等价可以被看作是一类特殊的置换证明、或者更准确的说，应是未知位置的置换。若要证明“公开而特定的位置置换”，我们还需要再对位置进行编码，然后再使用上面步骤中的。

先使用两个向量举例，假设对其进行奇偶换位（这里简化举例，设 $n$ 为偶数）\
原始向量：<br>

$$\vec a=(a_{0},a_{1},a_{2}.....a_{n-1},a_{n})$$

 换位后的向量：<br>

$$\vec b=(a_{1},a_{0},a_{3},a_{2}....a_{n},a_{n-1})$$

我们需要对向量中的元素的位置进行编码，来标识其换位的情况。\
换位前的位置:<br>
 
$$\vec i=(0,1,2.....n-1,n)$$

换位后的位置：<br>

$$\vec σ=(2,1,4,3.....n,n-1)$$

再将表达信息的向量与其位置的向量，合并在一起，进而可以得到换位前与换位后的合并向量 $a’$ 与 $b’$ ，如下：

<div align="center">
 <img src="https://hackmd.io/_uploads/H1Uktgh_A.png" width="350"/>
</div>

这里需要再使用一个随机数 $\beta$ （在协议中应在Verifer给出），从而可以将向量的二元素的元组折叠成一个元素。\
**这里再次看到使用随机数的神奇功效！使用随机数，将两个信息，可以压缩成一个！**
折叠后的两个向量组如下：

<div align="center">
 <img src="https://hackmd.io/_uploads/HJIDFg3dA.png" width="350"/>
</div>

这里的核心insight是：表达信息的元素的变换，是跟随着其位置变换而变换的，因此可以将对应的信息与其位置编码压缩成一个向量。\
例如：将 $a_{1}$ 从1号位置变换到 $σ(0)$ 号位置，成了 $b_{0}$ 。那么显然有:<br>

 a1 + 1*β = b0 + σ(0)*β = b0 + 1*β
 
 那么这样，我们就把位置信息也整合进了向量之中。这样就可以使用上一步中的Multiset的方法、最终转化为一个连乘证明了！

#### (4)置换矩阵的位置编码及向量化
有了以上步骤的基础，现在我们可以回到表达置换关系的 $σ$ 矩阵中进行观察。

<div align="center">
 <img src="https://hackmd.io/_uploads/H1qPBw3O0.png" width="250"/>
</div>

针对这个置换关系，我们对其进行位置编码。（郭老师原文里，置换关系矩阵σ中，对位置的编号为1、2、3、4，而后位置矩阵编号为0、1、2、3。我们这里暂改为采用0、1、2、3）
置换前的位置编码{ $i_{d}$ }：

<div align="center">
 <img src="https://hackmd.io/_uploads/HkZbUP3_C.png" width="235"/>
</div>

置换后的位置编码{ $σ$ }：

<div align="center">
 <img src="https://hackmd.io/_uploads/S1kNUwnuA.png" width="250"/>
</div>

根据我们在前面获得的**insight**，即**原始信息（W矩阵）与对应的位置信息，不论怎么变换，二者都是相对应的**。那么，我们就可以直接使用两个随机数，将位置与信息两个元素组合起来，然后再将三个向量相乘、从而压缩成一个向量。压缩后向量的连乘，必然满足置换关系。
置换前向量 $f$ 与置换后向量 $g$ 表达如下：<br>
 
<div align="center">
 <img src="https://hackmd.io/_uploads/BJJrr1MYR.png" width="550"/>
</div>
 
 不妨对于上述示例做个验证。置换前为：
 
<div align="center">
 <img src="https://hackmd.io/_uploads/SkurByfKA.png" width="550"/>
</div>

我们可以简单验算一下：<br>

<div align="center">
 <img src="https://hackmd.io/_uploads/B1yLSyMtC.png" width="550"/>
</div>

由此可知在连乘中，对应的项均可以消去。因此，构造的向量{ $f_{i}$ }与置换后的向量{ $g_{i}$ }，必然须满足：

$$\prod f_{i}=\prod g_{i}$$

等价于：

$$\prod \frac{f_{i}}{g_{i}}=1$$

由此，完全满足进行多项式编码的条件了。


## 四、多项式编码及约束式计算
### 约束式表达
现在，我们终于把电路的约束关系，都用向量的形式，进行了表达！再总结一下：Plonk中电路的约束包含算术约束与置换约束。
#### 算术约束
表达为：

$$\vec q_{L}\circ \vec w_{a}+\vec q_{R}\circ \vec w_{b}+\vec q_{M}\circ \vec w_{a}\circ \vec w_{b}+\vec w_{c}+\vec q_{o}\circ w_{c}=0$$

同时对各个向量在定义域H上进行多项式编码、转化为多项式，约束可表达为：

$$q_{L}(X)\cdot w_{a}(X)+q_{R}(X)\cdot w_{b}(X)+q_{M}(X)\cdot w_{a}(X)\cdot w_{b}(X)+q_{c}(X)+q_{o}(X)\cdot w_{c}(X)=0$$

#### 置换约束
表达为：

$$z_{0}=1$$ $$z_{i+1}=z_{i}\cdot\frac{f_{i}}{g_{i}}$$ 

可编码为：

$$z(w^0)=1$$ $$z(wX)\cdot g(X)=z(X)\cdot f(X)$$

其中：

$$f(X)=(w_{a}(X)+\beta\cdot id_{a}(X)+\gamma)(w_{b}(X)+\beta\cdot id_{b}(X)+\gamma)(w_{c}(X)+\beta\cdot id_{c}(X)+\gamma)$$ 

$$g(X)=(w_{a}(X)+\beta\cdot \sigma_{a}(X)+\gamma)(w{b}(X)+\beta\cdot \sigma_{b}(X)+\gamma)(w_{c}(X)+\beta\cdot \sigma_{c}(X)+\gamma)$$

### 简化计算的技巧方法
这里为了使运算更简化，整个过程中还用到了几个常用的技巧或方法。
1. 存放公开参数\
这就需要再引入一个新的列，专门存放公开参数，记为 φ。这样，就不必将公开值( $out$ )固定为常数。这样，改变一个输出值，也不会使得多项式  $q_{c}(X)$ 重新计算。然后，将算术约束式表示为：

$$q_{L}(X)\cdot w_{a}(X)+q_{R}(X)\cdot w_{b}(X)+q_{M}(X)\cdot w_{a}(X)\cdot w_{b}(X)+q_{c}(X)-q_{o}(X)\cdot w_{c}(X)+φ(X)=0$$

2. 编码时，多项式根的选取\
最开始多项式编码的示例，随意取多项式根 $H=[1,2,3,4]$ 。在协议中，实际上为针对有限域 $F_{p}$ ，选取其乘法子群 $H={1,w^1, w^2,... w^{n-1}}$ , 且 $n=2^k$ ,
如此可以满足在多项式编码的计算过程中，可简化计算，如下式所示:

$$\prod_{i=0}^{n-1}(X-w^i)=X^n-1$$ 

3. 置换关系中，位置编码的选取\
我们在前面示例中，置换关系的位置编码是随意选择自然数（0,1,2...）作为位置编码。而实际上，巧妙地选择位置编码，可以进一步减少工作量。按如下方法选择：

$${id_{a}}=(1,w,w^2,w^3)$$

$${id_{b}}=(k_1,k_1w,k_1w^2,k_1w^3)$$

$${id_{c}}=(k_2,k_2w,k_2w^2,k_2w^3)$$ 

由此，对这些向量进行多项式编码时，就可以轻松的得到：

$$id_{a}(X)=X$$ 

$$id_{b}(X)=k_1X$$ 

$$id_{c}(X)=k_2X$$ 

其中：k1、k2为互相不等的要·二次非剩余。

### 约束多项式的聚合
终于！有了上述内容，我们可以将上述约束的多项式，做一个聚合了！（本文于第五部分中附上Demo级的代码示例，以下的公式与代码示例中一致.）

针对以下三个式子作聚合：

$$q_{L}(X)\cdot w_{a}(X)+q_{R}(X)\cdot w_{b}(X)+q_{M}(X)\cdot w_{a}(X)\cdot w_{b}(X)+q_{c}(X)-q_{o}(X)\cdot w_{c}(X)+φ(X)=0$$ 

$$z(w^0)=1$$

$$z(wX)\cdot g(X)=z(X)\cdot f(X)$$

我们用 $C_{1}(X)、C_{2}(X)、C_{3}(X)$ 来表达以下三个式子：<br>
 
$$C_{1}(X)=q_{L}(X)\cdot w_{a}(X)+q_{R}(X)\cdot w_{b}(X)+q_{M}(X)\cdot w_{a}(X)\cdot w_{b}(X)+q_{c}(X)-q_{o}(X)\cdot w_{c}(X)+φ(X)$$


$$C_{2}(X)=z(wX)\cdot g(X)-z(X)\cdot f(X)$$ 

$$C_{3}(X)=L_{0}(X)\cdot (z(X)-1)$$ 

 然后计算：<br>
 
$$z_{H}(X)=X^n-1$$ 

最后，使用随机数α聚合，即可得到：

$$C_{Combine}(X)=C_{1}(X)+\alpha \cdot C_{2}(X)+\alpha^2 \cdot C_{3}(X)$$ 

而商多项式：

$$t(X)=\frac{C_{Combine}(X)}{z_{H}(X)}$$

### 随机挑战验证
Verifier通过发送随机挑战数 ζ，来检查的各个多项式的打开值，对结果进行验证。这个部分可详[郭老师的文章](https://learn.z2o-k7e.world/plonk-intro-cn/plonk-constraints.html)，本文仅侧重于整个流程的演进，此处不再叙述这部分。

## 五、简化代码示例
最后，对上述内容附上对应的零基础入门级Demo代码示例，针对以上流程所述及的部分作个示例解释。示例说明如下：
1. 示例中不包括Plonkish部分，而是直接将已经算术化的电路 $W$ 矩阵与 $σ$ 矩阵直接作为输入。可参考Plonkathon代码中的Program模块，作为实际项目中的一种算术化过程。
2. 示例中不包含多项式承诺及最后的随机数挑战验证环节。本示例仅对多项式计算进行验证。
3. 示例中，选取一个较小的域 $F101$ 来进行演示，整个过程可以跟踪得更直观。

### 导入库、初始定义
~~~python
import numpy as np
import galois
field_order = 101 #取一个较小的域，来进行计算
prim_g = 2 # primitive generator for F(101),取生成元为2
GF101 = galois.GF(field_order)

# Given two 1-D arrays x and y
# Returns the Lagrange interpolating polynomial through the points (x, y).
def lagrange_poly_in_finite_field(x, y):
    return galois.lagrange_poly(GF101(x), GF101(y))
def get_div_num(a, b):
    return GF101(a) / GF101(b)
# roots of unity for subgroup H
roots_of_unity = GF101([1, 10, 100, 91]) #使用生成元w=10

k1 = prim_g  #取k1=生成元g=2
k2 = prim_g * prim_g #取k2=生成元g^2=4,以使k1 k2二次非剩余
~~~

### 直接输入电路矩阵
~~~python
#Q 矩阵：以下再把q矩阵直接放进去。因为只有三个约束，最后一位补0
ql=GF101([0,0,0,0]) 
qr=GF101([0,0,0,0]) 
qm=GF101([1,1,0,0]) 
qc=GF101([0,0,60,0]) 
qo=GF101([1,1,0,0])  #注意：如果是加上-ϕx这一项的话，那么对于out的约束项，qo这里就取0。
ϕx=GF101([0,0,60,0]) 

#构造idx矩阵
id_vec_1 = GF101([1, 10, 100, 91]) # same as subgroup H,即id1=[w^0,w^1,w^2,w^3]，即为ida
id_vec_2 = []
id_vec_3 = []
for i in range(len(roots_of_unity)):
    id_vec_2.append(GF101(k1) * id_vec_1[i])  #即为idb
    id_vec_3.append(GF101(k2) * id_vec_1[i])  #即为idc
print("id_vec_1: ", id_vec_1)
print("id_vec_2: ", id_vec_2)
print("id_vec_3: ", id_vec_3)

#构造σ矩阵。
sigma_vec_1 = [id_vec_1[0], id_vec_3[0], id_vec_1[2], id_vec_1[3]] #即为σa
sigma_vec_2 = [id_vec_2[0], id_vec_2[1], id_vec_2[2], id_vec_2[3]] #即为σb
sigma_vec_3 = [id_vec_1[1], id_vec_3[2], id_vec_3[1], id_vec_3[3]] #即为σc
print("sigma_vec_1: ", sigma_vec_1)
print("sigma_vec_2: ", sigma_vec_2)
print("sigma_vec_3: ", sigma_vec_3)

# Witness Prover的秘密输入
w_a = GF101([3, 12, 0, 0]) 
w_b = GF101([4, 5, 0, 0])
w_c = GF101([12, 60, 60, 0])
# 先行验证一下，约束式是否成立
for i in range(len(roots_of_unity)):
    assert ql[i]*w_a[i]+qr[i]*w_b[i]+qm[i]*w_a[i]*w_b[i]-qo[i]*w_c[i]+qc[i]-ϕx[i]==0  #-ϕx[i] 
~~~

### 计算算术约束式C1(x)
~~~python
w_a_poly = lagrange_poly_in_finite_field(roots_of_unity, w_a)
w_b_poly = lagrange_poly_in_finite_field(roots_of_unity, w_b)
w_c_poly = lagrange_poly_in_finite_field(roots_of_unity, w_c)
ql_poly = lagrange_poly_in_finite_field(roots_of_unity, ql)
qr_poly = lagrange_poly_in_finite_field(roots_of_unity, qr)
qm_poly = lagrange_poly_in_finite_field(roots_of_unity, qm)
qo_poly = lagrange_poly_in_finite_field(roots_of_unity, qo)
qc_poly = lagrange_poly_in_finite_field(roots_of_unity, qc)
ϕx_poly = lagrange_poly_in_finite_field(roots_of_unity, ϕx)
C1_poly=ql_poly*w_a_poly+qr_poly*w_b_poly+qm_poly*w_a_poly*w_b_poly-qo_poly*w_c_poly+qc_poly-ϕx_poly

print("Output:")
print("w_a(X): ", w_a_poly)
print("w_b(X): ", w_b_poly)
print("w_c(X): ", w_c_poly)
print("ql(X): ", ql_poly)
print("qr(X): ", qr_poly)
print("qm(X): ", qm_poly)
print("qo(X): ", qo_poly)
print("qc(X): ", qc_poly)
print("ϕ(X): ", ϕx_poly)
print("计算约束式C1(X): ", C1_poly)
~~~


### 计算置换约束式C2(x)与C3(x)
~~~python
beta = GF101(2) #随机数β、γ，用于聚合出f(x)与g(x)
gamma = GF101(3)
f_values = []
g_values = []
q_values = []
for i in range(len(roots_of_unity)):
  f_acc_num_1 = w_a[i] + beta * id_vec_1[i] + gamma
  f_acc_num_2 = w_b[i] + beta * id_vec_2[i] + gamma
  f_acc_num_3 = w_c[i] + beta * id_vec_3[i] + gamma
  g_acc_num_1 = w_a[i] + beta * sigma_vec_1[i] + gamma
  g_acc_num_2 = w_b[i] + beta * sigma_vec_2[i] + gamma
  g_acc_num_3 = w_c[i] + beta * sigma_vec_3[i] + gamma
  f_acc_num = f_acc_num_1 * f_acc_num_2 * f_acc_num_3
  g_acc_num = g_acc_num_1 * g_acc_num_2 * g_acc_num_3
  f_values.append(f_acc_num) #对应于fx
  g_values.append(g_acc_num) #对应于gx
  q_values.append(get_div_num(f_acc_num, g_acc_num))

# Calculate accumulator values z_values
z_values = [1]
for i in range(len(roots_of_unity) - 1):
    z_values.append(z_values[-1] * get_div_num(f_values[i], g_values[i]))
# Calculate z_w_values by shift z_values, the last value is 1
z_w_values = z_values[1:] + z_values[:1]
print("f_values: ", f_values)
print("g_values: ", g_values)
print("q_values: ", q_values)
print("z_values: ", z_values)
print("z_w_values: ", z_w_values)
L_0_values = GF101([1, 0, 0, 0])

# Do the interpolation, return polynomial
L_0_poly = lagrange_poly_in_finite_field(roots_of_unity, L_0_values)
f_poly = lagrange_poly_in_finite_field(roots_of_unity, f_values)
g_poly = lagrange_poly_in_finite_field(roots_of_unity, g_values)
z_poly = lagrange_poly_in_finite_field(roots_of_unity, z_values)
z_w_poly = lagrange_poly_in_finite_field(roots_of_unity, z_w_values)
print("Output:")
print("L_0(X): ", L_0_poly)
print("f(X) = ", f_poly)
print("g(X) = ", g_poly)
print("z(X) = ", z_poly)
print("z_w(X) = ", z_w_poly)
C2_poly=g_poly * z_w_poly - f_poly * z_poly  # z(wx)*g(x)-z(x)*f(x)
print("C2(X) = ", C2_poly)

#针对z1=1的约束，按下式，构造C3
C3_poly=L_0_poly * (z_poly - GF101(1)) # L0(x)*(Z(x)-1)
~~~

### 随机数聚合
~~~python
#用随机数α将C1、C2、C3进行聚合，计算商多项式q(x)
# Vanishing polynomial: (X - 1)(X - 10)(X - 100)(X - 91)
z_H_poly = galois.Poly([1, 1], field = GF101) * galois.Poly([1, 10], field = GF101) * galois.Poly([1, 100], field = GF101) * galois.Poly([1, 91], field = GF101)
print("Vanishing polynomial z_H_poly: ", z_H_poly)

#这里对C1 C2 C3都检查一下
quot_poly2=C2_poly//z_H_poly
assert C2_poly == quot_poly2 * z_H_poly, "C2_poly wrong"
quot_poly3=C3_poly//z_H_poly
assert C3_poly == quot_poly3 * z_H_poly, "C3_poly wrong"
quot_poly1 = C1_poly//z_H_poly
assert C1_poly == quot_poly1 * z_H_poly, "C1_poly wrong"
alpha = GF101(23) #用α来聚合多个式子。
combined_poly=C1_poly + alpha*C2_poly + alpha*alpha*C3_poly
print("Combined polynomial combined_poly: ", combined_poly)
quot_poly = combined_poly // z_H_poly #计算商多项式
print("Quotient polynomial quot_poly: ", quot_poly)
assert combined_poly == quot_poly * z_H_poly, "Division has a remainder(should not have)"
~~~

### 作最后的验证
~~~python
# This number should be be a random number
zeta = GF101(4) # zeta应是随机取
y_1 = combined_poly(zeta)
print("y_1: ", y_1)
y_2_poly = quot_poly * z_H_poly
y_2 = y_2_poly(zeta)
print("y_2: ", y_2)
# Final step: Verify by verifier
assert y_1 == y_2, "Check failed"
~~~

本文可另详[hackmd版本链接](https://hackmd.io/@Dt_nNFZZRDmdFriUTBb_gw/Skd5EsouR)（显示效果更好）
