# FRI & Stark Course

## 基本信息

FRI（Fast Reed-Solomon Interactive Oracle Proof of Proximity）是 STARKs（Scalable Transparent ARguments of Knowledge）的核心组成部分。

作为一种重要的证明系统，FRI 正迅速崭露头角。

FRI 是一种基于 Reed-Solomon 码的交互式证明系统，能为零知识证明提供高效的低复杂度验证，提升验证效率并显著降低验证成本。具体来说，它允许证明者（Prover）向验证者（Verifier）证明某个多项式的评估值确实具有低度性，而不需要验证者重新计算这个多项式。

值得一提的是，FRI 在后量子时代拥有独特的优势。

一方面，FRI 依赖于信息论的安全性和哈希函数的抗碰撞特性，而不是传统的基于数学难题的密码系统。这意味着即使面对能够高效解决整数分解和离散对数问题的量子计算机，FRI 仍然能够保持其安全性。这种设计使得 FRI 能够在量子计算环境下依然可靠，提供高强度的防护。

另一方面，FRI 使用 Merkle Tree 进行数据承诺和验证，通过哈希函数的抗碰撞性确保数据完整性和真实性。Merkle Tree 的安全性依赖于选定哈希函数的抗碰撞性，如 SHA-256、Blake3 等，这些哈希函数在量子计算时代依然具有较高的安全性。通过 Merkle Tree，FRI 能够高效地验证多项式评估值，从而减少计算开销和验证时间。

总而言之，FRI 及其在 STARKs 中的应用，凭借其独特的设计和依赖于信息论的安全性，使得 FRI 不仅是未来密码学中不可或缺的关键技术，也将在 Crypto 领域成为保障系统安全和隐私的重要工具。

当我们站在历史的风陵渡，用未来的眼光审视当下，FRI 显然是一片充满可能性的土壤。

### 课程安排

【**基础-线上**】

+ **课程形式**：线上视频直播课程 + 代码实践
+ **开营时间**：8月12日
+ **课程时间**：6周（8月12日-9月22日）
+ **课程目标**：通过本期共学，参与学员将深入地理解 FRI 协议的底层原理、安全分析及其在STARK证明系统中的作用，研读实际证明系统中FRI部分的源码，并有能力用代码实现FRI的流程。
+ **线上答疑：** [Github Discussion](https://github.com/Antalpha-Labs/zkp-academy/discussions/categories/q-a)

【**进阶-线下**】
*进阶课程须完成线上课程才可参与*
+ **课程形式**：线下论文通读
+ **课程时间**：待定，预计两周
+ **课程地点**：待定
+ **课程目标**：深入理解 Circle STARKs 的原理与最新进展

### 前置知识

对 ZKP 有一定的了解，了解 ZKP 中的基本概念。如果不了解也没关系，推荐同时学习这门 MOOC [Zero Knowledge Proofs](https://zk-learning.org/) 以及我们的往期课程 [Plonk一期](https://www.youtube.com/playlist?list=PLbQFt1T_44DwN1zWl-KWhkp3s0LAkF2a8) [Plonk二期](https://www.youtube.com/playlist?list=PLbQFt1T_44Dy2FQU5oSbIdtfw2S64L72y)

### 开营AMA

+ 视频回放：

## 课程表

### Part 1: STARK101【8月12日 - 8月25日】

通过 STARK101 课程入门，了解 STARKs 的基本概念和应用场景。

+ 讲师：Harold、Tim、Dream
+ 课程回放：
+ 共学资料：[STARK101](https://starkware.co/stark-101/)

### Part 2: zk-learning.org Lecture 8【8月26日 - 9月8日】

通过 zk-learning 的第八讲及其它辅助材料，深入理解 zk-STARKs 的工作原理和技术细节。

+ 讲师：0xhhh、Yingfei、Kyrin、backdoor
+ 课程回放：
+ 共学资料：[zk-learning.org](https://zk-learning.org/)

【辅助教程】

+ [STARK Anatomy](https://aszepieniec.github.io/stark-anatomy/)
+ [Vitalik Blogs Part 1](https://vitalik.eth.limo/general/2017/11/09/starks_part_1.html) [Part 2](https://vitalik.eth.limo/general/2017/11/22/starks_part_2.html) [Part 3](https://vitalik.eth.limo/general/2018/07/21/starks_part_3.html)

【安全分析】

+ [SNARK Security and Performance](https://a16zcrypto.com/posts/article/snark-security-and-performance/)
+ [Safe and Sound – A Deep Dive into STARK Security](https://starkware.co/safe-and-sound-a-deep-dive-into-stark-security)

+ [ethSTARK Documentation – Version 1.2](https://eprint.iacr.org/2021/582.pdf)

+ [Fiat-Shamir Security of FRI and Related SNARKs](https://eprint.iacr.org/2023/1071.pdf)

+ [Proximity Gaps for Reed-Solomon Codes](https://eprint.iacr.org/2020/654.pdf)

+ https://snargsbook.org/

### Part 3: FRI 代码【9月9日 - 9月22日】

学习和实现 FRI 代码，通过 Plonky3 和 lambda class团队的 zk-stark，掌握 FRI 的实际编程技巧。

+ 讲师：阳小雪、饭卡、Po
+ 课程回放：
+ 共学资料：[Plonky3 - FRI](https://github.com/Plonky3/Plonky3)

+ 辅助学习：
  1. [Winterfell - FRI](https://github.com/facebook/winterfell)
  2. [RiscZero - FRI](https://github.com/risc0/risc0/blob/main/risc0/zkp/src/prove/fri.rs)
  3. [how to code fri from scratch](https://blog.lambdaclass.com/how-to-code-fri-from-scratch/)
  4. lambda class版zk-stark （[理论](https://lambdaclass.github.io/lambdaworks/starks/recap.html), [代码](https://github.com/lambdaclass/lambdaworks/tree/main/provers/stark)）


### Part 4: Circle STARKs 【时间地点待定，参与此课程须完成线上课程】

+ 讲师：Kurt Pan、白菜、小熊、wangyao
+ 课程回放：
+ 共学资料：
  1. [Vitalik Blog](https://vitalik.eth.limo/general/2024/07/23/circlestarks.html)
  2. [Kurt Pan 译](https://mp.weixin.qq.com/s/g6hcok1tJVIIOSoz3dxRFQ)
  3. [David Wong Post](https://www.zksecurity.xyz/blog/posts/circle-starks-1/)
  4. [circle stark and stwo](https://elibensasson.blog/why-im-excited-by-circle-stark-and-stwo/)
  5. [Paper](https://eprint.iacr.org/2024/278.pdf)



【**课程其他补充学习资料**】

+ [Cairo 推荐](https://github.com/lambdaclass/cairo-vm?tab=readme-ov-file#starks)

+ [RiscZero 推荐](https://dev.risczero.com/reference-docs/about-fri)

+ [RiscZero Introduction to FRI](https://www.youtube.com/playlist?list=PLcPzhUaCxlCi6rRRiIlkzJ_YELUlKO4Mz)

+ [Fast Reed-Solomon IOP (FRI) Proximity Test](https://rot256.dev/post/fri/)

+ [(综述) A summary on the FRI low degree test](https://eprint.iacr.org/2022/1216.pdf)

+ [(DAS应用) FRIDA: Data Availability Sampling from FRI](https://eprint.iacr.org/2024/248.pdf)

+ [(算术化) Study of Arithmetization Methods for STARKs](https://eprint.iacr.org/2023/661.pdf)

## 作业



### 老师介绍

  + Dream：Scroll Core Engineer，Blocksight 作者。数学&密码学持续学习者，前爱立信，微软高级工程师，区块链与隐私计算一线工程研发。
  + wangyao：数学博士（未完成）研究 ZK，学习 FHE，探索代数学和密码学的相交地带。
  + Kurt Pan：学院派新密码朋克，郭宇老师的好学生
  + 白菜 cstark：多年 ML 从业者，ZKP 研究者，关注ZKML，撰写分享了多篇 ZKP 文章
  + Tim：Tim，北京邮电大学硕士，密码学爱好者，CTFer，热衷ZK安全。
  + 小熊：pku 物理本科，法国 AI 硕士，现正专注密码学，做 ZK 相关科研
  + Harold：研究 zk 协议 todolist 望不到头的人，偶尔会做一些技术分享，欢迎大家来一起讨论～
  + Kyrin：区块链方向博士生，zkp 技术爱好者，与大佬们学习最新技术。
  + 0xhhh：bitlayer 工程师，zk 爱好者
  + backdoor：OKX ZK Dev，代码和理论两手抓，希望跟大家多交流学习～
  + Po：EthStorage ZK Researcher, 半路出家区块链，持续学习 DA 和 ZK 前沿研究。
  + 阳小雪：安比实验室 ZK Researcher, 最近在学习 Plonky3 的代码
  + Yingfei：密码学博士生，interested in lattice-based zero-knowledge proofs and signatures。
  + 饭卡：电子科技大学硕士，持续学习 zk ing


## Co-learn notes bounty

为鼓励学员学习与分享，本课程推出 Co-learn notes bounty 活动，学员可以将学习中的内容整理成个人笔记提交到 co-learn notes 目录下，收录后每篇笔记给出 200CNY 的 bounty，并发布在 Antalpha-Labs 公众号上。笔记主题围绕 ZKP 相关技术，不局限于 FRI or Stark 协议。



**联系方式**：添加小助手微信 AntalphaLabs
