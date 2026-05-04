# 🪨 kimi-caveman

[![PyPI](https://img.shields.io/pypi/v/kimi-caveman)](https://pypi.org/project/kimi-caveman/)
[![Python](https://img.shields.io/pypi/pyversions/kimi-caveman)](https://pypi.org/project/kimi-caveman/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

> **Why use many token when few do trick.**

A Kimi Code CLI skill that makes your agent talk like caveman — cutting **~60-75% of output tokens** while keeping full technical accuracy.

Based on the viral observation that terse, telegraphic communication dramatically reduces LLM token usage without losing substance.

---

## ✨ Features

- 🪶 **Lite / 🪨 Full / 🔥 Ultra / 📜 文言文** — pick your grunt level
- 🎯 **Same accuracy** — all technical info kept, only fluff dropped
- ⚡ **Faster responses** — less tokens to generate = speed go brrr
- 🗜️ **caveman-compress** — rewrite markdown/memory files into caveman-speak (~46% input token savings)
- 💬 **caveman-commit** — terse commit messages (≤50 chars)
- 🔍 **caveman-review** — one-line code review comments
- 📊 **Stats tracking** — token savings estimation

---

## 📦 Installation

### As a Kimi Skill (recommended)

```bash
# Clone to your skills directory
git clone https://github.com/theretech/kimi-caveman.git ~/.kimi/skills/caveman-mode
```

Or install via pip:

```bash
pip install kimi-caveman
```

---

## 🚀 Usage

### Activate caveman mode

Just say to Kimi:
- "caveman mode"
- "talk like caveman"
- "less tokens please"
- "modo caveman"

Deactivate with: "stop caveman" or "normal mode"

### Intensity Levels

| Level | Trigger | Style |
|-------|---------|-------|
| 🪶 Lite | `caveman lite` | Drop filler, keep grammar |
| 🪨 Full | `caveman full` | Default caveman. No articles, fragments |
| 🔥 Ultra | `caveman ultra` | Maximum compression, telegraphic |
| 📜 文言文 | `caveman wenyan` | Classical Chinese literary compression |

### Examples

**Normal Kimi (69 tokens):**
> "The reason your React component is re-rendering is likely because you're creating a new object reference on each render cycle. I'd recommend using useMemo to memoize the object."

**🪨 Caveman Kimi (19 tokens):**
> "New object ref each render. Inline object prop = new ref = re-render. Wrap in `useMemo`."

**🔥 Ultra (12 tokens):**
> "Inline obj prop → new ref → re-render. `useMemo`."

---

## 🗜️ caveman-compress

Compress markdown/memory files into caveman-speak. Preserves code blocks, URLs, and paths byte-for-byte.

```bash
# Compress a file
caveman-compress my-notes.md

# Output: my-notes.caveman.md (backup saved as .original.md)
```

| File | Original | Compressed | Saved |
|------|----------|------------|-------|
| `claude-md-preferences.md` | 706 | 285 | **59.6%** |
| `project-notes.md` | 1145 | 535 | **53.3%** |
| **Average** | **898** | **481** | **46%** |

---

## 🏗️ Architecture

```
kimi-caveman/
├── caveman_mode/
│   ├── SKILL.md              # Skill instructions for Kimi
│   ├── scripts/
│   │   └── compress.py       # Markdown compression tool
│   └── references/
│       └── modes.md          # Mode reference card
├── tests/
├── README.md
└── pyproject.toml
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Run tests: `pytest`
5. Run linter: `ruff check .`
6. Submit a PR

---

## ☕ Support

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/alanrezendeee)

**PIX (Brazil):**  
`54802231000148` — THE RETECH LTDA - EPP

---

## 📄 License

MIT — see [LICENSE](LICENSE) for details.

## 🏢 About

**kimi-caveman** is a token-efficient communication skill for [Kimi Code CLI](https://github.com/MoonshotAI/kimi-cli). It reduces agent output verbosity by 60-75% while maintaining 100% technical accuracy, making sessions faster, cheaper, and more readable.

Part of the **caveman ecosystem**: less tokens, same brain.

---

Built with 🪨 by [The Retech](https://github.com/theretech) and friends.
