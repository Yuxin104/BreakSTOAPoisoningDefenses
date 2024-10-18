# Breaking State-of-the-Art Poisoning Defenses to Federated Learning: An Optimization-Based Attack Framework

This is the official implementation of "Breaking State-of-the-Art Poisoning Defenses to Federated Learning: An Optimization-Based Attack Framework"


## Introduction
Federated Learning (FL) is a novel client-server distributed learning framework that can protect data privacy. However, recent works show that FL is vulnerable to poisoning attacks. Many defenses with robust aggregators (AGRs) are proposed to mitigate the issue, but they are all broken by advanced attacks. Very recently, some renewed robust AGRs are designed, typically with novel clipping or/and filtering strategies, and they show promising defense performance against the advanced poisoning attacks. In this paper, we show that these novel robust AGRs are also vulnerable to carefully designed poisoning attacks. Specifically, we observe that breaking these robust AGRs reduces to bypassing the clipping or/and filtering of malicious clients, and propose an optimization-based attack framework to leverage this observation. Under the framework, we then design the customized attack against each robust AGR. Extensive experiments on multiple datasets and threat models verify our proposed optimization-based attack can break the SOTA AGRs. We hence call for novel defenses against poisoning attacks to FL.

## Cite
```python
@misc{yang2024learningbasedattackframeworkbreak,
      title={A Learning-Based Attack Framework to Break SOTA Poisoning Defenses in Federated Learning}, 
      author={Yuxin Yang and Qiang Li and Chenfei Nie and Yuan Hong and Meng Pang and Binghui Wang},
      year={2024},
      eprint={2407.15267},
      archivePrefix={arXiv},
      primaryClass={cs.CR},
      url={https://arxiv.org/abs/2407.15267}, 
}
```
