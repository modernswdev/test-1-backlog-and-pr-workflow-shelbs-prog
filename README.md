[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/4rFBy60P)
# Practical Exam: GitHub Workflow & Security Audit (Boss Mini)

**Objective:** Demonstrate mastery of the GitHub process by performing a security audit and technical repair on a prototype combat script.

## The Scenario
You are a Junior Software Engineer at a gaming firm. You have inherited the `boss_mini.py` script. Your manager (the Instructor) has flagged this code as "Not Production Ready." You must bring this code up to industry standards using a strict Agile/GitHub Workflow.

---

## Phase 1 — Setup & Traceability — Create Backlog (GitHub Issue) (20 points)

1. Fork the instructor's repository to your own account by accepting the GitHub Classroom assignment. Check your email after you accept if you don't see the assignment.
2. Open an Issue titled **"Security & Logic Audit: boss_mini.py"**.
3. In the Issue description identify (developer perspective only):
   - Exactly which line contains the hardcoded credential (the "Security Backdoor").
   - Why the current `attack` function fails to progress the game. (Hint: what should happen if you deal damage? Consider the `heal` function.)
   - The danger of the current `heal` function regarding player state (hint: over-healing — what happens if you're already at 0 or 50? What could you add to protect against this?)

---

## Phase 2 — Technical Implementation & Documentation (40 points)

- Create a branch named `fix/boss-combat-logic`.
- In this phase you are *documenting* the repair (you do not have to implement fixes unless you want bonus points).
- For each identified bug, add a detailed Python comment (`#`) directly above the problematic line explaining:
  - The specific error occurring.
  - BONUS: the logic required to fix it.

Tasks to identify and comment:
- **Attack Logic:** Locate the `attack` function. Add a comment explaining that the math to subtract 10 health from the Boss (`b_hp`) is missing and must be added.
- **Healing Guardrails:** Locate the `heal` function. Add a comment explaining the need for boundary checks to prevent a player from healing past `50` HP or healing when their health is `0` (or less).
- **Security Audit:** Locate the `SECRET_CODE`. Add a comment stating that this variable and the cheat logic must be removed to close the backdoor vulnerability.
- **Win Condition:** Locate the game loop. Add a comment explaining how to trigger a "Victory" message and terminate the loop when the Boss health reaches `0`.

---

## Phase 3 — Pull Request & Peer Review (40 points)

1. Push your branch and open a Pull Request (PR) to your own `main` branch.
2. Traceability: In your PR description use the keyword **"Closes #1"** to link your issue.
3. Collaborative Review:
   - Add a classmate as a Collaborator to your repo.
   - Review their PR: leave one meaningful technical comment (e.g., "Did you consider using a constant for `MAX_HP`?", "Good catch — this is a security risk", etc.).
   - Address any feedback from your peer and merge the code into your `main` branch.

**Submission:** Submit the URL of your GitHub repository. Grading is based on Commit History, Issue documentation, and the PR conversation — not just the final code.

---

## Bonus Points — Technical Implementation (20 points)

On branch `fix/boss-combat-logic`, implement these fixes:
- **Attack Logic:** Modify the `attack` function so it actually subtracts `10` health from the Boss (`b_hp`) each time it is called.
- **Healing Guardrails:** Implement boundary checks to ensure a player cannot heal past `50` HP and cannot heal if their health is already `0` or less.
- **Security Audit:** Remove the `SECRET_CODE` variable and the associated cheat logic block entirely to close the security vulnerability.
- **Win Condition:** Ensure the game loop terminates with a **"Victory"** message if the Boss health reaches `0`.
