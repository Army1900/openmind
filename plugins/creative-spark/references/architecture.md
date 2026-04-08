# Creative Spark - Architecture

## Design Philosophy

**Problem**: AI is constrained but lacks creativity. It excels at logic, reasoning, and pattern matching, but struggles with unconventional thinking.

**Solution**: Deliberately introduce "irrational" elements that force the AI out of established patterns.

**Principle**: Keep it small. Only include skills that are proven, practical, and not redundant with AI's built-in capabilities.

## The 3 Core Skills

### 1. cross-domain (跨域类比)
**Why included**: Most innovations are borrowings from other domains. This is a proven innovation pattern.

**Mechanism**: Abstract problem essence → Find in nature/art/other fields → Translate back

**Best for**: Problem-solving stuck, conventional approaches exhausted

### 2. constraint-flip (约束反转)
**Why included**: Practical reframing technique that genuinely works. Turns blockers into enablers.

**Mechanism**: Identify constraint → Invert framing → Extract hidden value → Embed as feature

**Best for**: "We can't because..." statements, resource scarcity

### 3. deep-dream (深度梦境)
**Why included**: Accesses insights that rational analysis can't reach. Dreams operate on different logic—jumps, contradictions, metaphors.

**Mechanism**: Absorb problem → Enter dream state → Generate surreal narrative → Wake with insight

**Best for**: Problem stuck after rational attempts, need unexpected perspective

## What We Excluded (And Why)

| Excluded | Why |
|----------|-----|
| random-seed | Effect varies, AI can simulate but not truly benefit |
| perspective-shift | Claude already has role-play capability built-in |
| forced-fusion | AI tends to generate meaningless combinations |
| anti-pattern | Hard to execute genuinely, easy to become contrarian for its own sake |
| what-if-extreme | Useful but niche, not core enough |

## Skill Combination

The 3 skills can be combined:

```
constraint-flip → cross-domain
"How does nature handle this constraint?"

cross-domain → deep-dream
Dream about the problem using borrowed domain's logic

deep-dream → constraint-flip
The dream might reveal how the constraint transforms
```

## File Structure

```
creative-spark/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── skills/
│   ├── cross-domain/
│   │   └── SKILL.md
│   ├── constraint-flip/
│   │   └── SKILL.md
│   └── deep-dream/
│       └── SKILL.md
├── agents/
│   ├── dream-weaver.md
│   ├── memory-keeper.md
│   └── session-trigger.md
├── scripts/
│   ├── cli.py
│   ├── dream_engine.py
│   └── extractor.py
└── references/
    └── architecture.md          # This file
```

## Trigger Detection

| Skill | Trigger Pattern |
|-------|-----------------|
| cross-domain | "stuck", "how would nature", "need fresh perspective" |
| constraint-flip | "can't because", "limited by", "blocked by" |
| deep-dream | "dream on this", "sleep on it", stuck after rational attempts |

## Output Format

All skills follow:
1. **Process visibility**: Show the algorithm in action
2. **Multiple angles**: Not just one answer
3. **Actionable sparks**: Specific, testable ideas
