# Story Encoding Instructions

**Core Principle:** Use **only** the predicates provided in the instructions file, and in the 
examples provided. Do **NOT** assume a predicate exists if it is not explicitly listed.

## Order Specifications
*   **Separate Food and Drink:** Drinks and food in a restaurant order must be encoded separately. They **cannot** be combined as a single food item/order.

## Inference Rules
*   **No Unmentioned Actions:** If a story does **not** explicitly mention actions (e.g., entering a restaurant, ordering, eating), do **not** infer them. Leave them out of the encoding. Inference is handled by the pre-existing ASP code.
*   **Negated Activities:** For negations in a story (e.g., "They did not eat the salad", "Sam forgot to pay"), use:
    *   `st_obs(Fluent, false, I)`
    *   `st_hpd(Action, false)`
    *   **For false actions specifically:** Do **not** include a timestep. Use only `st_hpd(Action, false).`

## Entity Representation
*   **Waiter Role:** If someone other than an explicitly named waiter (e.g., manager, owner, host) performs waiter duties (taking orders, serving, etc.), encode them as `waiter("the manager")`, `waiter("owner")`, etc.
    *   **Exception:** If the story *also* mentions a separate "waiter," then all other such people must be represented by the `person()` predicate instead.
*   **Unspecified Food Items:**
    *   If the story mentions a generic word like "food" or "meal" but no specific item name, encode as `food("food")`, `food("meal")`, etc.
    *   If even generic words are absent, do **not** encode `food("food")`. Use the constant **`'f'`** wherever necessary in the encodings.

## General Guidelines
*   **Inconsistencies:** If you find inconsistencies in the given examples, follow the encoding method that appears **most frequently**.
*   **Unnecessary Predicate:** The `story_step()` predicate is **not** necessary. Do not use it.