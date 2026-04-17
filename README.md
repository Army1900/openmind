# OpenMind - 思维开拓工具箱

A Claude Plugin Marketplace that breaks AI's creative boundaries through unconventional thinking methods.

## Philosophy

**AI is constrained but lacks creativity.** These plugins deliberately introduce "irrational" elements to spark breakthrough thinking.

## Structure

```
openmind/
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   ├── creative-spark/           # 奇思妙想 - Innovation breakthrough
│   │   └── skills/
│   │       ├── cross-domain/     # 跨域类比
│   │       ├── constraint-flip/  # 约束反转
│   │       └── deep-dream/       # 深度梦境
│   │
│   └── poetic-spotlight/         # 诗意点睛 - Essence crystallization
│       └── skills/
│           └── poetic-essence/   # 诗意本质
│
│   └── know-act-unity/           # 知行合一 - Goal achievement
│       └── skills/
│           ├── clarify-intent/   # 明心定向
│           ├── act-on-ground/    # 事上练
│           └── reflect-anchor/   # 知行复盘
└── templates/
```

## Installation

```bash
claude plugin install https://github.com/openmind/openmind
```

---

## Plugin 1: creative-spark (奇思妙想)

**3 skills for innovation breakthrough**

| Skill | Chinese | Trigger | What It Does |
|-------|---------|---------|--------------|
| **cross-domain** | 跨域类比 | Problem stuck | Borrows solutions from nature/art/other fields |
| **constraint-flip** | 约束反转 | "Can't because..." | Transforms limitations into features |
| **deep-dream** | 深度梦境 | Need insight | Uses dream logic to reframe problems |

### cross-domain
```
User: How can I optimize database queries?

[cross-domain triggers]

AI: In nature, pitcher plants don't chase prey - they create irresistible traps.
What if data "flowed" toward where it's needed, instead of being queried?
This suggests a "data gravity" model...
```

### constraint-flip
```
User: We have zero marketing budget.

[constraint-flip triggers]

AI: Because you have zero budget, your product MUST be remarkable.
Every user must want to tell three friends. This isn't a limitation -
it's a quality bar that funded competitors don't have.
```

### deep-dream
```
User: Our architecture has circular dependencies. We've refactored three times.

[deep-dream triggers]

AI: Let me dream on this...

*I'm in a building where walls are API calls. There's a door that opens
into the same room. Someone whispers: "The building isn't the problem.
The ground is shifting."*

**The insight**: Maybe the architecture isn't the problem—the underlying
data model is unstable. Check the data model first.
```

---

## Plugin 2: poetic-spotlight (诗意点睛)

**Crystallize project essence with classical Chinese poetry**

| Skill | Chinese | Trigger | What It Does |
|-------|---------|---------|--------------|
| **poetic-essence** | 诗意本质 | Project milestone | Quotes/adapts poetry to crystallize the moment |

### Three Modes

| Mode | Trigger | Action |
|------|---------|--------|
| **WRITE** | Milestone reached | Quote classical poetry (or adapt if no exact match) |
| **READ** | "What poem fits this situation?" | Find matching poem + interpret for project |
| **INTERPRET** | User shares a poem | Deep reading + actionable insights |

### WRITE mode (at milestones)
```
[After completing a major feature]

AI: 这个里程碑要不要用诗定个调？

User: 好啊

AI: **"山重水复疑无路，柳暗花明又一村"**
——陆游《游山西村》

**解读**：
"山重水复"——四个方向，四堵墙。
但"又一村"——不是找到原来的路，是进入新的世界。

**对项目的启示**：
四次改方向不是迷路——是你在用排除法。
现在的"重新开始"，带着四次排除后的清晰。
```

### READ mode
```
User: 增长到了平台期，有什么古诗能解读一下？

[poetic-essence READ]

AI: **"不识庐山真面目，只缘身在此山中"**
——苏轼《题西林壁》

**解读**：
你卡住了，是因为你还在"山"里——现有的用户群、渠道、假设。

**对项目的启示**：
增长停滞不是"推不动"——是"走不出"。
找3个完全不同于现有用户的人聊聊，他们告诉你山的另一面。
```

### INTERPRET mode
```
User: 团队寄语是"长风破浪会有时"，帮我品品

[poetic-essence INTERPRET]

AI: 这是李白《行路难》——写于他很迷茫的时候。

**深层解**：
"会有时"不是"现在"，是"终会"。
这不是胜利宣言——是低谷期的信念。

**对团队的启示**：
真正的力量不是"破浪"，而是"等风来"时的准备。
与其急着破浪，不如先挂好帆。
```

---

## Plugin 3: know-act-unity (知行合一)

**3 goal-achievement skills grounded in Wang Yangming's philosophy**

> "知而不行只是未知" — Knowing without acting is not truly knowing.

| Skill | Chinese | Trigger | What It Does |
|-------|---------|---------|--------------|
| **clarify-intent** | 明心定向 | Vague goal stated | Distills to one actionable first step |
| **act-on-ground** | 事上练 | Over-planning, no action | Minimum verifiable action, execute now |
| **reflect-anchor** | 知行复盘 | Phase complete or failed | Confront false assumptions, recalibrate |

### The Cycle

```
clarify-intent (定向) → act-on-ground (事上练) → reflect-anchor (复盘) → loop
```

### clarify-intent
```
User: Our auth system is a mess, we need to refactor it.

[clarify-intent triggers]

AI: "A mess" — what specifically? Code structure? Security? Speed?
What hurts the most when you try to add auth features?

User: Adding OAuth takes 3 days and touches 7 files.

AI: The real intent isn't "refactor auth" — that's the method.
You want: adding auth features in 1-2 files, done in 1 day.

First action: "Find all files that reference auth, map the call graph."

✅ Gate passed — one sentence, actionable, has a deliverable.
```

### act-on-ground
```
User: [direction clear, but hasn't started]

[act-on-ground triggers]

AI: Don't refactor yet. Minimum step: grep all auth references.

Result: 17 files reference auth (not 7 as expected).
11 are indirect dependencies, 8 pierce through encapsulation.

What this reveals: This isn't a refactoring problem — it's an architecture
problem. The scope is 2.4x larger than perceived.

Next step: Test if the 8 encapsulation-piercing deps actually break on change.
```

### reflect-anchor
```
[After 3 action steps on auth refactoring]

[reflect-anchor triggers]

AI: Original goal: "Add auth features in 1-2 files, 1 day."
Where are we now?

What action proved wrong:
- Assumed "refactoring" would solve it → Wrong. It's an architecture problem.
- Assumed 7 files → Actually 17. Scope was underestimated.

What I thought I knew but didn't:
"I assumed this was a code quality issue. It's actually an abstraction
boundary issue — auth internals are exposed, not encapsulated."

Calibrated direction: Build an abstraction layer first, then refactor.
```

---

## Why These Plugins?

| Plugin | Solves What |
|--------|-------------|
| **creative-spark** | Rational approaches exhausted, need breakthrough |
| **poetic-spotlight** | Direction fuzzy, need to crystallize essence |
| **know-act-unity** | Knowing what to do but not doing it, or doing without verifying |

## License

MIT License - see [LICENSE](LICENSE) for details.
# openmind
