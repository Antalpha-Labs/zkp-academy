Plonk 學習 - 基礎認識

proof的目的很重要，要了解到底證明什麼。

ZKP有兩個角色, 一個是prover, 一個verifier, 
如果要編寫prover, 有兩點要留意，第一是要產生一個有效的proof, 第二是要注意在產生proof時，有沒有暴露了一些不想公開的訊息。
如果要編寫verifier，要關注檢查的proof是不是有效的，能否滿足成為有效證明的條件。
prover要用最少的資源去證明一件事，verifier要用最少的資源去驗證一件事。

當完成一組代碼後，就算順利完成編譯，也不算是完全沒有bug的。因為代碼的完整性是不能忽視，需要經過測試，不過惡意的prover有很多種，在測試上是存在很大難度，難以完全進行所有測試。畢竟技術也在進步，有時候新的技術可能會欺騙到verifier。
所以在設計上，最重要的要考慮到自己寫的verifier如何不被惡意prover欺騙。

一個協議需要關注以下三部分: 
1. 完整性(completeness)
能否驗證所有為真的證明

2. 可靠性(soundness)
當證明是真的，就會通過驗證

3. 零知識(Zero-knowledge)
保護個人隱私

在prover與verifier之間要有大量交互，在有足夠多的交互下，才可以進一步減低作弊的風險。
真的證明能通過驗證，是其中一項條件，不代表這就是完整的。
如果要是假的證明又能通過驗證，這就雖然通過完整性，但就欠缺可靠性。所以兩者需要同時
如果不能區分假的證明，這就雖然通過可靠性，但就欠缺完整性。
所以兩者需要同時為真，才可以做到有效的驗證。

基於Non-interactive zero-knowledge proof ，用戶可以直接生成proof，然後發送到區塊鏈上進行驗證。
從而加快驗證效率

透過Fiat-Shamir transformation，可以實現Non-interactive zero-knowledge proof，
令public coin protocol變成Non-interactive proof。
public coin protocol 可以讓誠實的驗證點發出隨機的coin(可以理解為隨機數)作為訊息，然後由prover產生一個proof。
不過發出隨機的coin的動作不一定由verifier負責，可以由其他人負責。
所以可以引入random oracle(例如是 cryptographic hash function)來生成隨機數，然後由prover產生一個proof，再直接發送給verifier(on-chain)。因此，也減少了verifier的工作量。
https://miro.medium.com/v2/resize:fit:1100/format:webp/0*KFAp0RYRk0cOVMqc.png

commitment 有以下特性: 
- O(1) size
- Binding, 當commitment出現，其數值就不能被修改。保證其他人拿到你的commitment也不可以再改它。
- Hiding, 當數值不公開，就不能被發現。不被人知道你的輸入資料, 每次生成的commitment都不同。

Plonk具有 commit-and-prove的特性，

commitment 有什麼種類?
1. hash
2. merkle-tree
3. pedersen commitment
還有其他的。

why zkSNARK?
1. 可以實現verifier on-chain
2. recursive proof: 可以做到計算的compression及可以做到不同組合的計算效果.

why Plonk?
1. 是一個universal trust setup (KZG10)
2. Proving O(nlogn), Verifier O(logn), Proof-size O(1)

Plonk 的組成部分是 arithematic +  polynomial IOP。

Circut:
門是屬於 Polynomial Gates。
當Circut經過計算之後會產出一堆polynomial。

polynomial會交給polynomial IOP

polynomial commitment
例子 : KZG10, IPM, FRI

參考:
1. Fiat-Shamir transformation 
https://www.zkdocs.com/docs/zkdocs/protocol-primitives/fiat-shamir/

2. zkSNARK是如何組成的 — 1
https://medium.com/swf-lab/zksnark%E6%98%AF%E5%A6%82%E4%BD%95%E7%B5%84%E6%88%90%E7%9A%84-1-2c6a474bcb06

3. Zero Knowledge Proofs: Example with Pedersen Commitments in Monero
https://medium.com/coinmonks/zero-knowledge-proofs-um-what-a092f0ee9f28

4. Understanding KZG10 Polynomial Commitments
https://taoa.io/posts/Understanding-KZG10-Polynomial-Commitments

5. Recursive zkSNARKs: Exploring New Territory
https://0xparc.org/blog/groth16-recursion
