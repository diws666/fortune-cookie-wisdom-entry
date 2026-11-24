import os

# 89-character fortune-cookie wisdom for a software developer (voice: short, balanced, plain truth).
FORTUNE = "Your code will outlive your comments. Write both like a stranger must read them at 3 a.m."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(FORTUNE)
