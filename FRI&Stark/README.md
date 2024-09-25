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


### 前置知识

对 ZKP 有一定的了解，了解 ZKP 中的基本概念。如果不了解也没关系，推荐同时学习这门 MOOC [Zero Knowledge Proofs](https://zk-learning.org/) 以及我们的往期课程 [Plonk一期](https://www.youtube.com/playlist?list=PLbQFt1T_44DwN1zWl-KWhkp3s0LAkF2a8) [Plonk二期](https://www.youtube.com/playlist?list=PLbQFt1T_44Dy2FQU5oSbIdtfw2S64L72y)

+ **线上答疑：** [Github Discussion](https://github.com/Antalpha-Labs/zkp-academy/discussions/categories/q-a)

### 开营AMA

+ 视频回放：[Youtube 链接](https://www.youtube.com/watch?v=mXHaBqJ0aYI)

## 课程表

### Part 1: STARK101【8月12日 - 8月25日】

通过 STARK101 课程入门，了解 STARKs 中各个组件的功能，以及这些功能在 ZKP 中起到了什么作用。
在 Part1 中我们将布置下我们需要完成的第一个作业 [(discussion链接)](https://github.com/Antalpha-Labs/zkp-academy/discussions/35)

【第一周课程安排】
- 第一节课：Overview of FRI.
  - 预习材料：有时间的可以看一下上一期 Plonk 的内容，领航员: Guoyu，时间：星期二，晚上8点
  - 课程回放：[Youtube 链接](https://youtu.be/VUjiC5Qwdmo)
  - PPT [链接](https://github.com/Antalpha-Labs/zkp-academy/blob/main/FRI%26Stark/lesson%201/FRI%20overview%202024-08-13%2019-54-37.pdf)
- 第二节课：How to do Low Degree Extension and constrain our LDE.
  - 预习材料：STARK101 第一及第二个视频，领航员: Tim，时间：星期四，晚上8点
  - 课程回放：[Youtube 链接](https://youtu.be/HLgiprbnsBA)
  - Note [链接](./stark101/stark101_arithmetization.md)
- 答疑：周六晚上时间 8 点

【第二周课程安排】
- 第三节课：What does FRI actually do?
  - 预习材料：STARK101 第三个视频，领航员: Dream，时间：星期二，晚上8点
  - 课程回放：[Youtube 链接](https://www.youtube.com/watch?v=dfUQaLOeHFc)
- 第四节课：How to convince the verifier by FRI?
  - 预习材料：STARK101 第四个视频，领航员: Harold, 时间：星期四，晚上8点
  - 课程回放：[Youtube 链接](https://youtu.be/FigtQ5C6G5s)
- 答疑：周六晚上时间 8 点
  - 答疑回放：[YouTube 链接](https://www.youtube.com/watch?v=65-PcleywRg)

共学资料：[STARK101](https://starkware.co/stark-101/)


**第一 part 作业**：[Arithmetization in STARKs](https://github.com/Antalpha-Labs/zkp-academy/discussions/35)

### Part 2: zk-learning.org Lecture 8【8月26日 - 9月8日】

通过 zk-learning 的第八讲及其它辅助材料，深入理解 zk-STARKs 的工作原理和技术细节。

讲师：backdoor、Kyrin、0xhhh、Yingfei

【第一周课程安排】
- 第一节课：FRI by Hand.
  - 课程内容：FRI的例子及协议细节，讲师：backdoor，时间：星期二晚上8点
  - 课程回放：[Youtube 链接](https://www.youtube.com/watch?v=W5dXnaSwrQw)
- 第二节课：Attack Cases in FRI & Comparison of PCSs(KZG, IPA).
  - 课程内容：LDT的安全分析及PCS对比，讲师：Kyrin，时间：星期四晚上8点
  - 课程回放：[Youtube 链接](https://youtu.be/_0aMoAZ1L7k)
- 答疑：周六晚上时间 8 点
  - 答疑回放：[Youtube 链接](https://youtu.be/unvwDkqpbpA)

【第二周课程安排】
- 第三节课：Stark by Hand (PCS with FRI).
  - 课程内容：FRI的多项式承诺，讲师：0xhhh，时间：星期二晚上8点
  - 课程回放：[Youtube 链接](https://youtu.be/ak1wGXfGlyc)
- 第四节课：Soundness of STARK.
  - 课程内容：STARK的形式化流程及安全性分析，讲师：Yingfei，时间：星期四晚上8点
  - 课程回放：[Youtube 链接](https://youtu.be/p3zxhnSDqFM)
- 第五节课：Soundness of FRI.
  - 课程内容：FRI协议的安全性分析，讲师：Yingfei，时间：星期六晚上8点
  - 课程回放：[Youtube 链接](https://youtu.be/Sfm5GjI69fc)


共学资料：[zk-learning.org](https://zk-learning.org/)

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

【第一周课程安排】
- 第一节课：lambda class版zk-stark实现
  - 预习材料： 阅读lambda class版zk-stark的[理论和实现流程](https://lambdaclass.github.io/lambdaworks/starks/recap.html)，有余力的可以看看[代码实现](https://github.com/lambdaclass/lambdaworks/tree/main/provers/stark)，领航员: 饭卡，时间：星期二，晚上8点
  - 课程回放：[Youtube 链接](https://youtu.be/wEIiSuaMH4o)
- 第二节课：Plonky3 two_adic_pcs概述
  - 预习材料：
    - [Plonky3](https://github.com/Plonky3/Plonky3)fri文件夹内的代码，
    - two_adic_pcs运行流程图：https://miro.com/app/board/uXjVNbLn8WU=/?share_link_id=878894620109
  - 领航员: 阳小雪，时间：星期四，晚上8点
  - 课程回放：[Youtube 链接](https://youtu.be/swCjt9YibyE)

【第二周课程安排】
- 第三节课：
  - Plonky3/fri/src/two_adic_pcs.rs
  - 预习材料：[Plonky3](https://github.com/Plonky3/Plonky3)fri文件夹内的代码，领航员: 阳小雪，时间：星期四，晚上8点
  - 课程回放：[Youtube 链接](https://youtu.be/rUQK6j3Bhsk)
- 第四节课：
  - uni-stark of plonky3
  - 预习材料：[Plonky3](https://github.com/Plonky3/Plonky3)uni-stark 文件夹内的代码，领航员: hhh，时间：星期六，晚上8点
  - 代码注释： https://github.com/cyl19970726/Plonky3/tree/main_comment
  - 课程回放：[Youtube 链接](https://youtu.be/UHfP-1Pm1Ak)


共学资料：
  - [Plonky3](https://github.com/Plonky3/Plonky3)

+ 辅助学习：
  1. [Winterfell - FRI](https://github.com/facebook/winterfell)
  2. [RiscZero - FRI](https://github.com/risc0/risc0/blob/main/risc0/zkp/src/prove/fri.rs)
  3. [how to code fri from scratch](https://blog.lambdaclass.com/how-to-code-fri-from-scratch/)
  4. lambda class版zk-stark （[理论](https://lambdaclass.github.io/lambdaworks/starks/recap.html), [代码](https://github.com/lambdaclass/lambdaworks/tree/main/provers/stark)）

**第三 part 作业**：[Plonky3-fri](https://github.com/Antalpha-Labs/zkp-academy/discussions/58)


### Part 4: Circle STARKs 【时间10月13日至10月19日，地点 清迈,泰国，参与此课程须完成线上课程，提前报名】

+ 讲师：Kurt Pan、小熊、wangyao
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
第一 part 作业：[Arithmetization in STARKs](https://github.com/Antalpha-Labs/zkp-academy/discussions/35)

第三 part 作业：[Plonky3-fri](https://github.com/Antalpha-Labs/zkp-academy/discussions/58)

### 老师介绍

  + Dream：Scroll Core Engineer，Blocksight 作者。数学&密码学持续学习者，前爱立信，微软高级工程师，区块链与隐私计算一线工程研发。
  + wangyao：数学博士（未完成）研究 ZK，学习 FHE，探索代数学和密码学的相交地带。
  + Kurt Pan：学院派新密码朋克，郭宇老师的好学生
  + Tim：Tim，北京邮电大学硕士，密码学爱好者，CTFer，热衷ZK安全。
  + 小熊：pku 物理本科，法国 AI 硕士，现正专注密码学，做 ZK 相关科研
  + Harold：研究 zk 协议 todolist 望不到头的人，偶尔会做一些技术分享，欢迎大家来一起讨论～
  + Kyrin：区块链方向博士生，zkp 技术爱好者，与大佬们学习最新技术。
  + 0xhhh： 正在学习 binuis，circle stark，zk 爱好者
  + backdoor：OKX ZK Dev，代码和理论两手抓，希望跟大家多交流学习～
  + Po：EthStorage ZK Researcher, 半路出家区块链，持续学习 DA 和 ZK 前沿研究。
  + 阳小雪：安比实验室 ZK Researcher, 最近在学习 Plonky3 的代码
  + Yingfei：密码学博士生，interested in lattice-based zero-knowledge proofs and signatures。
  + 饭卡：电子科技大学硕士，持续学习 zk ing


## Co-learn notes bounty

为鼓励学员学习与分享，本课程推出 Co-learn notes bounty 活动，学员可以将学习中的内容整理成个人笔记提交到 co-learn notes 目录下，收录后每篇笔记给出 200CNY 的 bounty，并发布在 Antalpha-Labs 公众号上。笔记主题围绕 ZKP 相关技术，不局限于 FRI or Stark 协议。

**联系方式**：添加小助手微信 AntalphaLabs
**备注**：不要吝啬给我们一个 star 哦～

## Sponsor

<img src="assets/SN-Linear-Flat colour.png" width="75%;"/>
