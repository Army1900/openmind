---
name: cross-domain
description: Use when problem-solving is stuck, when conventional approaches fail, or when seeking novel solutions through analogical thinking. TRIGGERS: "stuck", "need fresh perspective", "how does nature solve this", "analogical thinking", "cross-domain".
---

# Cross-Domain - 跨域类比

## Overview
Borrows solutions from biology, art, nature, and unrelated fields to inspire breakthrough thinking. The core insight: most problems have already been solved somewhere else, in a different form.

## The Core Pattern

**WITHOUT this skill**:
```
Problem → Try known solutions → Fail → Try harder → Give up
```

**WITH this skill**:
```
Problem → Identify core mechanism → Find in nature/art/other field → Translate back → Novel solution
```

## Trigger Conditions

- Problem-solving stuck after multiple attempts
- User asks "how would nature solve this?"
- Conventional approaches exhausted
- Seeking breakthrough innovation

## The Cross-Domain Algorithm

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. ABSTRACT - Extract the core mechanism                        │
│    "What is the ESSENCE of this problem?"                       │
│    e.g., "optimizing for limited resources under uncertainty"   │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. SEARCH - Find analogous solutions in other domains           │
│    Domain Pool:                                                 │
│    • Biology (evolution, organisms, ecosystems)                 │
│    • Physics (forces, energy, matter)                           │
│    • Art/Music (composition, harmony, contrast)                 │
│    • History (patterns, revolutions, discoveries)               │
│    • Sports/Games (strategy, competition, teamwork)             │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. TRANSLATE - Map the analogy back to the original problem     │
│    "How would [analogy] work in [our context]?"                 │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. SPARK - Generate concrete, actionable insights               │
│    "This suggests we could..."                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Example Output

```markdown
# Cross-Domain Insight: Database Query Optimization

## Problem Essence
"Efficiently finding what you need in a vast, changing landscape"

## Analogies Found

### 🌿 Nature: The Pitcher Plant
The pitcher plant doesn't chase prey - it creates an irresistible trap and waits.
**Translation**: Instead of actively querying, what if data "flowed" toward where it's needed?

### 🎵 Music: Jazz Improvisation
Jazz musicians follow a structure but improvise within it. The "changes" guide but don't restrict.
**Translation**: Pre-compute common query paths, but allow dynamic variations for edge cases.

### ⚽ Sports: Basketball Zone Defense
Players guard areas, not individual opponents. This is more efficient than man-to-man.
**Translation**: Partition queries by data "zones" rather than optimizing each query independently.

## Actionable Sparks
1. Consider a "data gravity" model - let frequently-joined data cluster together
2. Build "query compositions" with standard patterns + improvisation
3. Implement zone-based caching instead of query-specific caching
```

## Domain Reference Cards

| Domain | Key Patterns | Best For |
|--------|--------------|----------|
| **Biology** | Evolution, symbiosis, camouflage, migration | Adaptation, optimization, survival |
| **Physics** | Gravity, friction, resonance, entropy | Forces, constraints, efficiency |
| **Art** | Contrast, rhythm, negative space | Aesthetics, communication, perception |
| **Architecture** | Load-bearing, flow, modularity | Structure, scalability, organization |
| **Cooking** | Layering, reduction, fermentation | Transformation, combination, patience |
| **Games** | Strategy, bluffing, resource management | Competition, uncertainty, decision-making |

## Usage

```
User: How can I reduce churn in my SaaS product?

[Trigger cross-domain]

AI: Let me think about this through different lenses...

In nature, ecosystems with diversity are more resilient. Monocultures collapse.
In music, listeners stay engaged when there's tension AND resolution - predictability is boring.
In games, players quit when the "cost of switching" is low AND the "investment" feels wasted.

**Spark**: Churn might not be about adding features - it's about increasing "ecosystem investment".
What if users could see their accumulated value? Their unique data? Their learned preferences?
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Forcing weak analogies | Only use if the "aha" moment is genuine |
| Getting lost in the metaphor | Always translate back to concrete actions |
| Using only one domain | Pull from 2-3 domains for richer insights |
| Being too abstract | End with specific, testable ideas |

## Integration Notes

This skill works well combined with:
- **random-seed**: Use random stimulus to select which domain to explore
- **perspective-shift**: Adopt the perspective of someone FROM that domain
- **forced-fusion**: Combine multiple domain insights into one solution
