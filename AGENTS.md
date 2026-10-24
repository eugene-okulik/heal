# AGENTS.md

Self-healing UI tests: Playwright page objects wrapped with an LLM "healer" (OpenRouter) that re-finds broken selectors.

## Setup
- Python project; use the local `venv/`. No requirements.txt — dependencies used: `pytest`, `pytest-playwright`, `openai`, `requests`, `playwright` (sync API).
- `OPENROUTER_API_KEY` env var is required for the healer (`utils/healer.py`) and `rag.py`. Without it, LLM calls silently fail/return nothing useful.

## Running tests
```sh
.venv/venv/bin/pytest          # or: python -m pytest
python -m pytest test_product.py            # single file
```
- Tests are E2E against a real site: `ProductPage.URL` is hardcoded to `http://testshop.qa-practice.com/...` — network access required.
- Playwright browser must be installed: `playwright install` (uses sync API, headed by default via pytest-playwright unless headless configured).

## Code hygiene
- No leftover code: remove unused imports, dead code, commented-out code before finishing. Keep only what the current code needs.

## Architecture
- `pages/base_page.py`: `BasePage` with a custom `@heal` decorator. On `PlaywrightTimeoutError`, it calls `utils/healer.py` `find_selector()` (LLM gets the page DOM + element `description=` kwarg) and retries with the returned XPath. Healing only works if the failing `find()` call passes a `description` kwarg — without it the original exception is re-raised.
- Always locate elements via `self.find(selector, description="...")`, never raw `page.locator(...).click()` — otherwise healing is bypassed.
- Locating an element inside another element must also go through the healing helpers: use `self.find_child(parent, selector, description="...")` or `self.find_child_by_role(parent, role, title, description="...")`. Never call `parent.locator(...)` / `parent.get_by_role(...)` directly — nested lookups bypass healing the same way raw page locators do.
- Page objects subclass `BasePage` and must set `URL` for `open()` to work.
- `rag.py`: standalone script (not pytest) — chunks `user_guide.md` by markdown headings, embeds via OpenRouter, answers a question from stdin. Key is hardcoded here; prefer env var.
- `old/`: dead code, ignore.
