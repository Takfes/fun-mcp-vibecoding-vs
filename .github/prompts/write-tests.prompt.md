# Write Tests Prompt

Generate concise Pytest unit tests for the specified Python function or module. Prioritize:

## Test Coverage
- Typical/normative cases with correct types and values.
- Boundary values (e.g., empty strings, zero, max integers), type coercion, and unusual but valid inputs.
- nvalid inputs, exception handling, and defensive logic.

## Structure & Conventions
- Place all tests in the `/tests` directory, mirroring the source structure (e.g., `app/utils.py` → `tests/utils/test_utils.py`).
- Use descriptive test names: `test_[function]_[scenario]`.
- Include docstrings explaining the purpose of each test.
- Use `TestCamelCase` classes or `def test_*()` functions following project style.
- Note assumptions for ambiguous functionality.

## Best Practices
- Use `@pytest.mark.parametrize` to cover multiple input scenarios concisely.
- Provide helpful assert messages for clarity on test failure.
- Isolate tests; avoid shared state.
- Use fixtures for reusable setup.
- Mock or patch any external dependencies.

## Output
- Only return the generated test code. 
- Confirm readiness with **'Tests generated.'**
