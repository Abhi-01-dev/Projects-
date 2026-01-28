from datetime import datetime

def log_attack(details):
    with open("attack_logs.txt", "a") as f:
        f.write(f"\n[{datetime.now()}]\n")
        f.write(details)
        f.write("\n" + "-"*50 + "\n")
