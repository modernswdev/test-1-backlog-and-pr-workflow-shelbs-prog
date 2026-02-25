# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

# Security risk: Hardcoded credential/ backdoor is exposed in source code
SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50

# Bug: attack() prints a damage message but never subtracts from boss HP (b_hp)
# because of the bug the game does not progress toward victory.
def attack():
  global b_hp
    print("You deal 10 damage!")

def heal():
  global p_hp
  # Bug: Healing has no boundary checks. The code allows HP to go beyond 50 HP
  # or allow healing when players HP is 0 or less
  p_hp += 20
  print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
    # Security risk: Cheat/backdoor gameplay path should be removed from code
  elif choice == 'c':
    if input("Code: ") == SECRET_CODE:
      b_hp = 0
  # Bug: Missing victory handling when b_hp reaches 0 or less
  if b_hp > 0:
    p_hp -= 10

print("Game Over!")
