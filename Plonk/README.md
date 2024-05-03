
ZKP（零知识证明）技术为加密行业带来了新的叙事和活力，ZKP 和区块链的结合正在经历快速发展和广泛应用的过程，充满着巨大的想象和潜力， 而当下只有较少人踏足，这意味着 **ZK 领域仍是一片蓝海**。

**无论是从理论层面还是工程实践层面，想要高效学习 ZKP，PLONK 是绝佳之选。**

PLONK 理论基础扎实，它借鉴了很多经典 ZKP 技术的理论基础，如算术电路、查找表、内积证明等，很多后续的优化方案，包括 PlonkUp、UltraPlonk、Halo2 等，都是 PLONK 家族的一员。**随着对 ZKP 性能和可扩展性需求的不断提高，PLONK 家族方案已成为目前最受欢迎和应用最广泛的 ZKP 系统之一。**

除此以外，PLONK 工程价值极高，创新地使用了新的算术电路编码方案和新的开箱即用(out-of-the-box)证明系统，为构建高效、可扩展的通用零知识证明系统奠定了基础，包括 Starkware 和 zkSync 的以太坊二层网络，Filecoin 等分布式存储项目、Mina 和 Aleo 等隐私区块链，**众多热门项目都使用或基于 PLONK 实现**。

只有全面深入研习 PLONK 的理论基础、数学原理和工程实践，克服知识的"诅咒"，才能嗅得金蔷薇的纯粹芬芳。

围绕 PLONK，我们准备了系列课程，面向有一定 ZKP 相关的数学和理论基础者，**每节课程将结合具体的例子和代码，带你全面构建 PLONK 的认知框架**，帮你更好理解有关理论基础的实际运用，并带你深入 PLONK 的理论和工程代码实践。


本期课程内容参考郭宇老师的文章，以及 Harry 做的代码实现展开:

- [https://github.com/sec-bit/learning-zkp/tree/develop/plonk-intro-zh](https://github.com/sec-bit/learning-zkp/tree/develop/plonk-intro-zh)
- [https://github.com/Antalpha-Labs/plonk-intro-notebook](https://github.com/Antalpha-Labs/plonk-intro-notebook?tab=readme-ov-file)


## 详细安排 

⏰ **开营时间**：5月26日（周日）

🧩 **课程时间**: 每周二、四晚 8 点

⛲️ **课程阵地：**

- 微信群：开放给大家交流讨论，仅限课程报名者和导师，后续所有相关课程通知在群内发布
- Zoom：上课所用，每节课前都有相应的链接
- GitHub：本次课程核心协作平台，导师会在每节课前放置预习资料，学生在上面提交课程作业，相关的交流讨论也可以在其中完成


## 课程内容 

| 序号 | 课程题目 | 课程内容 | 讲师 | 助教 |
| --- | --- | --- | --- | --- |
| 第1周 | ZKP & Plonk overview | zkp overview; zkp & 复杂理论; zkp landscape | 郭宇老师 |  |
|  | Plonk 算术化 | 为什么需要算术化, 如何做算术化 | 郭燕老师 |  |
| 第2周 | Plonk 中的多项式 | 多项式概率检查, Lagrange 插值, 单位根 | Wangyao |  |
|  | 置换证明 | Grand product, Multiset 等价, 置换证明 | Wangyao |  |
| 第3周 | Plonk 中的约束 | 算术约束, 拷贝约束 | Jade |  |
|  | Plonk 中的多项式承诺 | 多项式基础, KZG 承诺 | Po |  |
| 第4周 | Lookup Gate | 讲解 Plonkup | yingfei |  |
|  | Custom Gate | 讲解 Custom Gate | yingfei |  |
| 第5周 | 代码实践 | 完成 Plonk 代码, 实现证明的完整流程 | harry |  |
|  |  |  |  |  |

以及最后的完结作业