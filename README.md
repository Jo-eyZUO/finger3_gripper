[[IcETRAN] Application and Optimal Design of a Soft Robotic Gripper for Grasping Objects of Arbitrary Shape](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10645079)  
1. 评估具有四种不同手指(2,3,4,6只)配置的机器人手  与七种已知和规则形状物体(圆 三角 方形)一起运作的方法。
2. 使用七步评分系统进行了夹持的互动检查，检查了物体的质量、方向、位置和重心变化对夹持结果的影响。

[Explainable Grasping with Soft Grippers using Visual Quality Metrics](https://research.engr.oregonstate.edu/rdml/sites/research.engr.oregonstate.edu.rdml/files/explainability_of_soft_robotic_grippers_using_visual_quality_metrics_1.pdf)
1. 使用软手验证了 **仅使用视觉数据** 获得的**三个夹持质量度量的预测**准确性, 其中抓取规则性和距离指标有用。
2. The metrics used to predict the quality of a given grasp were selected based on analysis from Rupert, et al.  [Predicting grasp success in the real world - A study of quality metrics and human assessment] (https://www.sciencedirect.com/science/article/pii/S0921889019300247)  
3. In this paper we use a theory-based explanation system to provide transparency into the grasp classification [A Multidisciplinary Survey and Framework for Design and Evaluation of Explainable AI Systems](https://arxiv.org/abs/1811.11839)
4. Our experimental results indicate that the regularity and distance metrics are suitable to soft grippers

[Predicting grasp success in the real world - A study of quality metrics and human assessment] (https://www.sciencedirect.com/science/article/pii/S0921889019300247)  
1. 系统地研究了**七种常用的抓取质量指标**在预测真实机器人抓取执行结果时的表现。
2. 在仿真中产生数据集，并用指标给抓取姿势打分，在实际机器人上验证抓取的性能。
3. 鉴于所得到的数据集，我们训练了不同的分类器，仅使用抓取质量指标作为输入来预测抓取成功。
4. A physics metric in simulation & Human oracle 都不足以预测 real grasp， 所以用grasp quality metrics 七个指标组合去预测
5. 规定了Experimental protocol测量抓取稳定性的实验方案
6. 结果显示，**质量指标的组合**可实现对真实抓取高达 85% 的分类准确性。

[[RAL] A Three-Finger Adaptive Gripper With Finger-Embedded Suction Cups for Enhanced Object Grasping Mechanism](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10777060&tag=1) 
1. 结构创新，设计了一个具有5个自由度结构的夹持器，将**吸盘集成到指尖**，允许调节吸盘的角度，从而在各种环境中实现有效抓握。
2. 该夹持器的多功能性通过执行混合指吸式夹持以及传统指和吸盘夹持来进行测试。

[[RAL] Kinetostatics and Retention Force Analysis of Soft Robot Grippers with External Tendon Routing](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10803019)
1. 纯做手的结构以及建模分析。
2. 提出了一种基于应变能最小化的运动静力学建模方法，受力于力学和几何约束，用于估计具有**外部腱线布线(ETR)** 的软机器人夹持器的形状，包括具有复合结构的夹持器。
3. 此外，使用卡斯蒂利亚诺第一定理来估计夹持器的保持力。
![[Pasted image 20241227215057.png]]

[[TASE] AI Co-Pilot Object Recognition for Sensory Soft Robotic Grippers](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10792662)
1. **设计软传感器+识别算法**，建立了一种**仿生感知软夹爪系统**，能够在抓握任务过程中感知和生成目标物体信息。
2. 一种**应变/压力双模传感器**，模仿了人类皮肤的出色柔软性（杨氏模量<10 kPa）和高灵敏度（应变增益>2000），已经开发并无缝集成到一个三指软机械手夹爪中。
3. 开发了一种**Swin Transformer网络**，从传感器获取的双模数据中学习规则并生成抓取对象的类别信息。
4. 感知夹爪系统在**分类各种形状和大小的18个物体**时表现出优越的识别准确性，实现了惊人的94.9%准确率。

[[RAL] Rapidly Tunable Stiffness Soft Gripper for Multifunctional Grasping](https://ieeexplore.ieee.org/document/10766417)
1. **设计手指材料+结构**，多功能柔性夹持器，具有快速响应和高承载能力，通过热响应可变刚度手指和喷射冷却系统的结合实现。
2. 热响应可变刚度手指由液态金属颗粒和形状记忆聚合物复合材料组成的分层材料构成，刚度范围从3.56 MPa到4356 MPa，跨越三个数量级。
3. 最大承载能力可达∼13 N（单个手指在15 mm偏转时），最大弯曲角度约为∼82°，快速硬化速度约为∼2秒。

[[Access]PneuNet Based Hybrid Soft Gripper for Multi-Shape Object Handling](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10792893)
1. 结构上 **改进finger** 里加了一层 layer jamming element (LJE) 结构
2. gripper design 单个手指可以转动角度，具有 **三种抓取模式**
3. grasping mode selection
4. 提取contour 分类判断抓取模式
![[Pasted image 20241227180910.png]]

