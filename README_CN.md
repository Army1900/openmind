# OpenMind - 思维开拓工具箱

一个 Claude 插件市场，通过非传统思维方法突破 AI 的创造力边界。

## 理念

**AI 约束强但创新不足。** 这些插件刻意引入"非理性"元素，激发突破性思维。

## 结构

```
openmind/
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   └── creative-spark/           # 奇思妙想
│       ├── skills/
│       │   ├── cross-domain/     # 跨域类比
│       │   ├── constraint-flip/  # 约束反转
│       │   └── deep-dream/       # 深度梦境
│       ├── agents/
│       └── scripts/
└── templates/
```

## 安装

```bash
claude plugin install https://github.com/openmind/openmind
```

## 核心技能 (3个)

| 技能 | 触发条件 | 作用 |
|------|----------|------|
| **cross-domain** | 问题卡住 | 从自然/艺术/其他领域借用解决方案 |
| **constraint-flip** | "因为X所以不能" | 把限制转化为特性 |
| **deep-dream** | 需要洞察 | 用梦境逻辑重构问题 |

## 使用示例

### cross-domain (跨域类比)
```
用户：如何优化数据库查询？

[cross-domain 触发]

AI：自然界中，猪笼草不追逐猎物——它创造不可抗拒的陷阱等待。
如果数据也这样，不是被查询，而是"流向"需要它的地方？
这提示了一种"数据引力"模型...
```

### constraint-flip (约束反转)
```
用户：我们没有营销预算。

[constraint-flip 触发]

AI：正因为没有预算，你的产品必须令人惊叹。
每个用户都必须想告诉三个朋友。这不是限制——
这是有资金支持的竞争对手没有的质量门槛。
```

### deep-dream (深度梦境)
```
用户：我们的架构有循环依赖，重构了三次还是有问题。

[deep-dream 触发]

AI：让我做个梦...

*我在一栋建筑里，墙壁是 API 调用。有扇门打开后还是同一个房间。
我不断开门，期待去新地方。门把手是热的。*

有人低语："问题不在建筑，是地在动。"

*醒来*

**洞察**：梦境一直回到同一个房间——循环依赖。但低语说地在动。
也许问题不在架构，而是底层数据模型不稳定？
先检查数据模型，而不是继续重构 API。
```

## 为什么这3个？

- **cross-domain**：已验证的创新模式——大多数突破都是跨域借用
- **constraint-flip**：实用的重构技巧，确实有效
- **deep-dream**：触及理性分析无法到达的洞察

## 技能互补

```
cross-domain     →  "自然界会怎么解决这个问题？"
constraint-flip  →  "如果限制是特性会怎样？"
deep-dream       →  "让我做个梦看看..."
```

## 许可证

MIT License - 详见 [LICENSE](LICENSE)
