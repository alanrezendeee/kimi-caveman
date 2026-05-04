# Contributing to kimi-caveman

Thank you for your interest in contributing! 🪨

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev]"
   ```

## Development Workflow

1. Create a feature branch: `git checkout -b feat/my-feature`
2. Make your changes
3. Run tests: `pytest`
4. Run linter: `ruff check .`
5. Commit with clear messages
6. Open a Pull Request

## Code Style

- We use `ruff` for linting and formatting
- Follow PEP 8 guidelines
- Keep functions focused and documented

## Reporting Issues

- Use the issue templates
- Provide reproduction steps
- Include environment details

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
