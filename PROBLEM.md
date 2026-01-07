## Problem: Validation of Optional Nested Models

When a Pydantic model includes an optional nested model, validation behavior
should be consistent when the nested model is provided with missing required fields.

Expected Behavior:
- If a nested model is present in the input data, all required fields
  inside that nested model must be validated.
- Missing required fields inside the nested model must raise a ValidationError.
- Error messages must include the exact nested field path.

Current Behavior:
- When an optional nested model is provided with missing required fields,
  validation may not consistently raise a ValidationError.
- This results in incomplete or misleading validation feedback.

Success Criteria:
- ValidationError is raised whenever required fields are missing
  inside a provided nested model.
- Errors are deterministic and include correct field paths.
