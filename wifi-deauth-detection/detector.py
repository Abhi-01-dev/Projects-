from scapy.all import sniff, Dot11, Dot11Deauth
from gui import gui_queue
from gemini_ai import analyze_attack
from logger import log_attack

INTERFACE = "wlan0mon"

def packet_handler(packet):
    if packet.haslayer(Dot11Deauth):
        attacker = packet[Dot11].addr2
        target = packet[Dot11].addr1
        bssid = packet[Dot11].addr3
        reason = packet[Dot11Deauth].reason

        attack_data = f"""
Attacker MAC : {attacker}
Target MAC  : {target}
BSSID       : {bssid}
Reason Code : {reason}
"""

        log_attack(attack_data)

        ai_response = analyze_attack(attack_data)

        final_text = (
            "🚨 WiFi Deauthentication Attack Detected 🚨\n\n"
            "📡 Attack Details:\n"
            f"{attack_data}\n"
            "🧠 Gemini AI Analysis:\n"
            f"{ai_response}"
        )

        gui_queue.put(final_text)

def start_detection():
    sniff(
        iface=INTERFACE,
        prn=packet_handler,
        store=False
    )
