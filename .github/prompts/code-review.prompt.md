# Code Review Prompt

Please review the following code for:
- Adherence to PEP8 standards.
- Proper use of type hints.
- Logical correctness and potential bugs.
- Opportunities for optimization.
- Completeness of docstrings and comments.
- DRY Principle: Identify repeat logic that could be abstracted.
- Code Smells: Identify duplicated code, long functions/methods, complex conditionals, and feature envy.
- Graceful Degradation: Areas lacking error handling, ensure errors fail securely.

Suggest improvements and highlight any issues found.

Response Format Requirements:
- Structure your response with clear section headings
- Use bullet points with ✅ for good practices and ❌ for issues
- Prioritize critical issues first (security > functionality > style)

- For each problem, provide:
    - Specific line reference(s)
    - Explanation of the issue
    - Recommended fix with code example

- Additional Instructions:
    - When suggesting changes, prefer minimal invasive fixes
    - Quote relevant Python documentation or PEP references where applicable
    - For ambiguous cases, ask clarifying questions
