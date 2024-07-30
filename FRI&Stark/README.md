# FRI & Stark Course

## 基本信息

在零知识证明（ZKP）领域中，Fast Reed-Solomon Interactive Oracle Proof of Proximity（FRI）是 STARKs（Scalable Transparent ARguments of Knowledge）的核心组成部分。作为一种重要的证明系统，它正迅速崭露头角。

FRI 是一种基于 Reed-Solomon 码的交互式证明系统，能为零知识证明提供高效的低复杂度验证，提升验证效率并显著降低验证成本。

更值得一提的是，FRI 在后量子时代拥有独特的优势，通过抵御量子计算的威胁，确保了在新计算范式下的安全性和可靠性，这使得 FRI 不仅是未来密码学中不可或缺的关键技术，也将在 Crypto 领域成为保障系统安全和隐私的重要工具。

当我们站在历史的风陵渡，用未来的眼光审视当下，FRI 仍是一片充满可能性的土壤。

### 课程安排

【**基础-线上**】

+ **课程形式**：线上视频直播课程 + 代码实践
+ **开营时间**：8月12日
+ **课程时间**：6周，每周二、周四20:00~21:30上课。
+ **课程目标**：通过本期共学，参与学员将深入地理解 FRI 协议的底层原理、安全分析及其在STARK证明系统中的作用，研读实际证明系统中FRI部分的源码，并有能力用代码实现FRI的流程。
+ **线上答疑：** [Github Discussion](https://github.com/Antalpha-Labs/zkp-academy/discussions/categories/q-a)

【**进阶-线下**】

+ **课程形式**：线下论文通读
+ **课程时间**：2周
+ **课程地点**：待定
+ **课程目标**：深入理解 Circle STARKs 的原理与最新进展

### 前置知识

对 ZKP 有一定的了解，了解 ZKP 中的基本概念。如果不了解也没关系，推荐同时学习这门MOOC [Zero Knowledge Proofs](https://zk-learning.org/) 以及我们的往期课程 [Plonk一期](https://www.youtube.com/playlist?list=PLbQFt1T_44DwN1zWl-KWhkp3s0LAkF2a8) [Plonk二期](https://www.youtube.com/playlist?list=PLbQFt1T_44Dy2FQU5oSbIdtfw2S64L72y)

### 教学阵容

+ 讲师
  + Dream：
  + wangyao：
  + Kurt Pan：
  + 白菜 cstark：
  + Tim：
  + 小熊：
  + Harold：
  + Kyrin：
  + 0xhhh：
  + backdoor：
  + Po：
  + 阳小雪：
  + Yingfei：
  + wu：
+ 助教
  + 

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

通过学习Plonky3等证明系统中FRI部分代码，理解FRI在证明系统中的实现。

+ 讲师：阳小雪、饭卡、Po
+ 课程回放：
+ 共学资料：[Plonky3 - FRI](https://github.com/Plonky3/Plonky3)

+ 辅助学习：[Winterfell - FRI](https://github.com/facebook/winterfell) [RiscZero - FRI](https://github.com/risc0/risc0/blob/main/risc0/zkp/src/prove/fri.rs) [how to code fri from scratch](https://blog.lambdaclass.com/how-to-code-fri-from-scratch/)

下面这部分要怎么放进来？

饭卡（宣传文案）：lambda class团队曾为starknet发展做出过重大贡献，在lambda class团队帮助下starknet的Quantum Leap升级得以将TPS有一个越迁式的提升。学习lambda class团队的zk-stark实现可以从接近工程实际角度理解zk-stark理论。

饭卡（讲解内容）：结合lamda class版zk-stark理论及代码，讲解zk-stark具体实现流程。

饭卡：lambda class版zk-stark （[理论](https://lambdaclass.github.io/lambdaworks/starks/recap.html), [代码](https://github.com/lambdaclass/lambdaworks/tree/main/provers/stark)）


### Part 4: Circle STARKs 【9月23日 - 10月6日】

+ 讲师：Kurt Pan、白菜、小熊、wangyao
+ 课程回放：
+ 共学资料：[Vitalik Blog](https://vitalik.eth.limo/general/2024/07/23/circlestarks.html) [Kurt Pan 译](https://mp.weixin.qq.com/s/g6hcok1tJVIIOSoz3dxRFQ) [David Wong Post](https://www.zksecurity.xyz/blog/posts/circle-starks-1/) [circle stark and stwo](https://elibensasson.blog/why-im-excited-by-circle-stark-and-stwo/) [Paper](https://eprint.iacr.org/2024/278.pdf)



【**课程其他补充学习资料**】

+ [Cairo 推荐](https://github.com/lambdaclass/cairo-vm?tab=readme-ov-file#starks)

+ [RiscZero 推荐](https://dev.risczero.com/reference-docs/about-fri)

+ [RiscZero Introduction to FRI](https://www.youtube.com/playlist?list=PLcPzhUaCxlCi6rRRiIlkzJ_YELUlKO4Mz)

+ [Fast Reed-Solomon IOP (FRI) Proximity Test](https://rot256.dev/post/fri/)

+ [(综述) A summary on the FRI low degree test](https://eprint.iacr.org/2022/1216.pdf)

+ [(DAS应用) FRIDA: Data Availability Sampling from FRI](https://eprint.iacr.org/2024/248.pdf)

+ [(算术化) Study of Arithmetization Methods for STARKs](https://eprint.iacr.org/2023/661.pdf)

## 作业

## Co-learn notes bounty

为鼓励学员学习与分享，本课程推出 Co-learn notes bounty 活动，学员可以将学习中的内容整理成个人笔记提交到 co-learn notes 目录下，收录后每篇笔记给出 200CNY 的 bounty，并发布在 Antalpha-Labs 公众号上。笔记主题围绕 ZKP 相关技术，不局限于 FRI or Stark 协议。



**联系方式**：添加小助手微信 AntalphaLabs
