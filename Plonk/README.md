# Plonk Course

## 基本信息

ZKP（零知识证明）技术为加密行业带来了新的叙事和活力，ZKP 和区块链的结合正在经历快速发展和广泛应用的过程，充满着巨大的想象和潜力， 而当下只有较少人踏足，这意味着 **ZK 领域仍是一片蓝海**。

**无论是从理论层面还是工程实践层面，想要高效学习 ZKP，PLONK 是绝佳之选。**

PLONK 理论基础扎实，它借鉴了很多经典 ZKP 技术的理论基础，如算术电路、查找表、内积证明等，很多后续的优化方案，包括 PlonkUp、UltraPlonk、Halo2 等，都是 PLONK 家族的一员。**随着对 ZKP 性能和可扩展性需求的不断提高，PLONK 家族方案已成为目前最受欢迎和应用最广泛的 ZKP 系统之一。**

除此以外，PLONK 工程价值极高，创新地使用了新的算术电路编码方案和新的开箱即用(out-of-the-box)证明系统，为构建高效、可扩展的通用零知识证明系统奠定了基础，包括 Starkware 和 zkSync 的以太坊二层网络，Filecoin 等分布式存储项目、Mina 和 Aleo 等隐私区块链，**众多热门项目都使用或基于 PLONK 实现**。

只有全面深入研习 PLONK 的理论基础、数学原理和工程实践，克服知识的"诅咒"，才能嗅得金蔷薇的纯粹芬芳。

围绕 PLONK，我们准备了系列课程，面向有一定 ZKP 相关的数学和理论基础者，**每节课程将结合具体的例子和代码，带你全面构建 PLONK 的认知框架**，帮你更好理解有关理论基础的实际运用，并带你深入 PLONK 的理论和工程代码实践。

### 课程安排

* **课程形式：** 线上视频直播课程 + 代码实践
* **开营时间：** 5月26日
* **课程时间：** 共计5周，每周二、周四20:00~21:30上课。
* **线上答疑：** [Github Discussion](https://github.com/Antalpha-Labs/zkp-academy/discussions/categories/q-a)
* **课程目标：** 通过本课程的学习，学习者将更加深入地理解 Plonk 协议的底层原理，如 Plonk 算术化、置换证明、算术约束、多项式承诺、Lookup等，并有能力用代码实现一个完整的 Plonk 证明流程。

### 前置知识

对 ZKP 有一定的了解，了解 ZKP 中的基本概念。如果不了解也没关系，推荐同时学习这门课程[Zero Knowledge Proofs](https://zk-learning.org/)。

### 工作人员

* 👨‍🏫 讲师：
  * 郭宇：SECBIT Labs （安比实验室）创始人，曾经高校教育从业者，关注领域为零知识证明，智能合约安全，程序语言理论。
  * Yan：中科大本硕博，科大软件学院网安方向教师，当前兴趣包括AI和区块链，持续学习中。
  * Wangyao：数学博士（未完成）研究 ZK，学习 FHE，探索代数学和密码学的相交地带。
  * Jade：ZK 开发者@安比实验室。电子科技大学数学硕士，热爱数学与密码学，致力于将理论知识转化为实际应用。
  * Po：EthStorage ZK Researcher, 半路出家区块链，持续学习 DA 和 ZK 前沿研究。
  * Yingfei：密码学博士生， interested in lattice-based zero-knowledge proofs and signatures。
  * Harry Liu：零知识证明(ZKP)技术爱好者, 在个人学习的同时, 也积极在社区进行分享和组织各种 ZKP 相关的活动。
* 👨‍🎓 助教：
  * Harold：“zkp 真的是太好玩啦！”，喜欢开源。
  * Purple：文转码，zkp 学习ing。
  * Jade：ZK 开发者@安比实验室。电子科技大学数学硕士，热爱数学与密码学，致力于将理论知识转化为实际应用。
  
### 开营 AMA
 * 视频回放 [开营 AMA](https://www.youtube.com/watch?v=3h972SlVsoI)
   
## 课程表

### Lesson 1【5月28日周二】 ZKP & Plonk overivew

在第一次课程中，我们将对 ZKP 和 Plonk 有个整体的认识，知道 Plonk 在 ZKP 发展中的位置，并认识到其重要性。

* 主讲老师：郭宇
* 课程回放：[YouTube 链接](https://youtu.be/OOBD7cnR1J4)
* 补充材料：[课程笔记](https://github.com/Antalpha-Labs/zkp-academy/blob/main/Plonk/lesson%201/whyplonk%202024-05-28.pdf)

### Lesson 2【5月30日周四】 Plonk 算术化

我们将理解引入 Plonkish 算术化的优点，清楚它与 R1CS 的区别，并掌握 Plonkish 算术化的具体过程。

* 主讲老师：Yan
* 课程回放：[Youtube 链接](https://youtu.be/L3qMBzPgfWY)
* 课程笔记：[链接](https://github.com/sec-bit/learning-zkp/blob/master/plonk-intro-notebook-zh/1-plonk-arithmetization.ipynb)
* 补充材料：[理解 PLONK（一）：Plonkish Arithmetization](https://github.com/sec-bit/learning-zkp/blob/master/plonk-intro-zh/1-plonk-arithmetization.md)
* 补充材料：[分享理解 PLONK 原理 一](https://www.youtube.com/watch?v=HtKmRcSJUG4&list=PLbQFt1T_44DwN1zWl-KWhkp3s0LAkF2a8&index=5&t=376s)

### Lesson 3【6月4日周二】 Plonk 中的多项式

我们将深入多项式编码的细节，掌握多项式编码将多个约束压缩成一个约束的具体过程。

* 主讲老师：Wangyao
* 课程回放：[Youtube 链接](https://youtu.be/bNGac1CJEKM)
* 课程幻灯片
* 补充材料：[理解 PLONK（二）：多项式编码](https://github.com/sec-bit/learning-zkp/blob/master/plonk-intro-zh/2-plonk-lagrange-basis.md)
* 补充材料：[分享 PLONK 原理 二](https://www.youtube.com/watch?v=O5HGp3EHDI0&list=PLbQFt1T_44DwN1zWl-KWhkp3s0LAkF2a8&index=4)

### Lesson 4【6月6日周四】 置换证明

我们将深入理解置换证明底层原理。

* 主讲老师：Wangyao
* 课程回放：[Youtube 链接](https://youtu.be/B7ubzpXSpqI)
* 课程幻灯片
* 补充材料：[理解 PLONK（三）：置换证明](https://github.com/sec-bit/learning-zkp/blob/master/plonk-intro-zh/3-plonk-permutation.md)

### 2nd Office Hour 【6月8日周六】

* 答疑老师：郭宇、Wangyao、Harry、Keep...
* 答疑回放：[Youtube 链接](https://youtu.be/SkTmEwbBx-I)

### Lesson 5【6月11日周二】 Plonk中的约束

我们将掌握算术约束与拷贝约束的底层原理。

* 主讲老师：Jade
* 课程回放：[Youtube 链接](https://youtu.be/J1P60urkGwc)
* 课程幻灯片: [链接](/Plonk/lesson%205/PLONK%20-%20Lecture%205%20-%20算术约束与拷贝约束.pdf)
* 课程代码: [链接](/Plonk/lesson%205/plonk-lecture5-constraints.ipynb)
* 补充材料：[理解 PLONK（四）：算术约束与拷贝约束](https://github.com/sec-bit/learning-zkp/blob/master/plonk-intro-zh/4-plonk-constraints.md)

### Lesson 6【6月13日周四】 Plonk中的多项式承诺

我们将明白什么是多项式承诺，掌握 KZG10 的多项式承诺构造。

* 主讲老师：Po
* 课程回放：[Youtube 链接](https://youtu.be/yEH23SwxCG0)
* 课程幻灯片
* 补充材料：[理解 Plonk（五）：多项式承诺](https://github.com/sec-bit/learning-zkp/blob/master/plonk-intro-zh/5-plonk-polycom.md)

### 3rd Office Hour 【6月15日周六】

* 答疑老师：郭宇、Harry、Kurt Pan...
* 答疑回放：[Youtube 链接](https://youtu.be/qagV_-Sqb9o)

### Lesson 7【6月18日周二】 Lookup Gate

我们将深入 Lookup 的细节，学习 Lookup Gate 不同方案以及优化。

* 主讲老师：Yingfei
* 课程回放：[Youtube 链接](https://youtu.be/pmO6p9Q-x6g)
* 课程幻灯片：[链接](/Plonk/lesson%207/Plonk.pdf)
* 补充材料：[理解 PLONK（七）：Lookup Gate](https://github.com/sec-bit/learning-zkp/blob/master/plonk-intro-zh/7-plonk-lookup.md)
* 补充材料：[分享理解 PLONK 原理 三 Lookup argument](https://www.youtube.com/watch?v=StvnHnC4Dk4&list=PLbQFt1T_44DwN1zWl-KWhkp3s0LAkF2a8&index=3)

### Lesson 8【6月20日周四】 Custom Gate & Lookup Gate

我们将明白 Custom Gate 的底层原理。

* 主讲老师：Yingfei
* 课程回放：[Youtube 链接](https://youtu.be/I6asKtO8Q8E)
* 课程幻灯片：[链接](/Plonk/lesson%208/plookup%20and%20custom%20gates.pdf)
* 补充材料：

### 4th Office Hour 【6月22日周六】

* 答疑老师：Harry...
* 答疑回放：[Youtube 链接](https://youtu.be/DRfMGSvaluQ)

### Lesson 9【6月25日周二】 代码实践

我们将从代码入手，实现一个完整的 Plonk 协议。

* 主讲老师：Harry Liu
* 课程回放：[Youtube 链接](https://youtu.be/lHEJuYYk3VU)
* 课程幻灯片
* 补充材料：[Baby Plonk](https://github.com/Antalpha-Labs/baby-plonk)

## 作业

## Co-learn notes bounty

为鼓励学员学习与分享，本课程推出 Co-learn notes bounty 活动，学员可以将学习中的内容整理成个人笔记提交到 Plonk/co-learn notes 目录下，收录后每篇笔记给出 200CNY 的 bounty，并发布在 Antalpha-Labs 公众号上。笔记主题围绕 ZKP 相关技术，不局限于 Plonk 协议。

## References

* [理解 Plonk 协议](https://github.com/sec-bit/learning-zkp/tree/master/plonk-intro-cn)
* [Plonk intro notebook](https://github.com/Antalpha-Labs/plonk-intro-notebook?tab=readme-ov-file)

**联系方式**：添加小助手微信 AntalphaLabs
