# OpenMind - 思维开拓工具箱

A Claude Plugin Marketplace that breaks AI's creative boundaries through unconventional thinking methods.

## Philosophy

**AI is constrained but lacks creativity.** These plugins deliberately introduce "irrational" elements to spark breakthrough thinking.

## Structure

```
openmind/
├── .claude-plugin/
│   └── marketplace.json          # Plugin marketplace manifest
├── plugins/
│   └── creative-spark/           # 奇思妙想 Plugin
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── skills/
│       │   ├── cross-domain/     # Cross-domain analogies
│       │   ├── constraint-flip/  # Constraint inversion
│       │   └── deep-dream/       # Dream logic for insights
│       ├── agents/
│       └── scripts/
└── templates/
```

## Installation

```bash
claude plugin install https://github.com/openmind/openmind
```

## Core Skills (3)

| Skill | Chinese | Trigger | What It Does |
|-------|---------|---------|--------------|
| **cross-domain** | 跨域类比 | Problem stuck | Borrows solutions from nature/art/other fields |
| **constraint-flip** | 约束反转 | "Can't because..." | Transforms limitations into features |
| **deep-dream** | 深度梦境 | Need insight | Uses dream logic to reframe problems |

## Usage Examples

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
into the same room I just left. I keep opening it, expecting somewhere new.
The doorknob is hot.*

Someone whispers: "The building isn't the problem. The ground is shifting."

*I wake up.*

**The insight**: What if the architecture isn't the problem? The dream kept
returning to the same room—circular dependency. But the whisper said the ground
is shifting. Maybe the underlying data model is unstable, and the API walls
are just reacting to that. Check the data model first.
```

## Why These 3?

- **cross-domain**: Proven innovation pattern - most breakthroughs are cross-domain borrowings
- **constraint-flip**: Practical reframing that genuinely works
- **deep-dream**: Accesses insights that rational analysis can't reach

## The Skills Complement Each Other

```
cross-domain     →  "How would nature solve this?"
constraint-flip  →  "What if the limitation is a feature?"
deep-dream       →  "Let me dream on this..."
```

## License

MIT License - see [LICENSE](LICENSE) for details.
