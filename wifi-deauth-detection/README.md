# 🛡️ WiFi Deauthentication Attack Detection System

A Python-based cybersecurity application that **detects WiFi Deauthentication (Deauth) attacks in real time** using **Scapy** and dynamically informs the user via a **GUI**, enhanced with **Gemini AI analysis** for attack type and prevention techniques.

---

## 📌 Project Overview

WiFi Deauthentication attacks are commonly used to forcibly disconnect users from wireless networks. This project continuously monitors **802.11 management frames** and detects deauth attacks in real time.

Once an attack is detected:

* The GUI updates dynamically
* Gemini AI analyzes the attack
* User is informed about:

  * Attack type
  * Risk level
  * Explanation
  * Prevention steps

---

## 🚀 Key Features

* 🔍 Real-time WiFi Deauth attack detection
* 📡 Uses **Scapy only** (no pywifi)
* 🖥️ Python GUI with live updates (Tkinter)
* 🧠 AI-powered analysis using **Google Gemini API**
* 📝 Attack logging with timestamp
* 🔐 Cybersecurity & academic project friendly

---

## 🧠 Technologies Used

| Component       | Technology            |
| --------------- | --------------------- |
| Language        | Python 3              |
| Packet Analysis | Scapy                 |
| GUI             | Tkinter               |
| AI              | Google Gemini API     |
| OS              | Linux (Kali / Ubuntu) |

---

## 🗂️ Project Structure

```
wifi-deauth-detection/
│
├── app.py               # Main application entry point
├── detector.py          # Deauth detection logic (Scapy)
├── gui.py               # GUI + live updates
├── gemini_ai.py         # Gemini API integration
├── config.py            # API configuration
├── logger.py            # Attack logging
│
├── requirements.txt
├── .env.example
├── README.md
└── assets/
```

---

## ⚙️ System Requirements

* Linux OS (Kali Linux recommended)
* Monitor mode supported WiFi adapter
* Python 3.8+
* Root privileges

> ❗ Windows does **not** support monitor mode and raw 802.11 frame sniffing.

---

## 📥 Installation Steps

### 1️⃣ Enable Monitor Mode

```bash
sudo airmon-ng start wlan0
```

### 2️⃣ Clone Repository

```bash
git clone https://github.com/cyber-abhi01/Project.git
cd Project/wifi-deauth-detection

```

### 3️⃣ Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 4️⃣ Configure Gemini API

* Rename `.env.example` to `.env`
* Add your API key:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

```bash
sudo python3 app.py
```

The GUI will start and begin monitoring WiFi deauthentication attacks.

---

## 🧪 How It Works (Workflow)

```
Monitor Mode Interface
        ↓
Scapy Packet Sniffing
        ↓
Detect Dot11Deauth Frames
        ↓
Send Data to Gemini AI
        ↓
Live GUI Update
        ↓
Attack Log Saved
```

---

## 🖥️ Sample Output (GUI)

```
🚨 WiFi Deauthentication Attack Detected 🚨

Attack Type:
WiFi Deauthentication Flood Attack

Risk Level:
High

Explanation:
This attack repeatedly disconnects users from the network.

Prevention:
- Enable WPA3
- Use 802.11w Management Frame Protection
- Monitor abnormal deauth traffic
```

---

## 🔐 Security & Ethical Note

This tool is designed **only for educational and defensive security purposes**.
Do not use it for unauthorized network monitoring.

---

## 🎓 Academic Use

Perfect for:

* Final Year Project
* Cyber Security Lab
* Network Security Demonstration
* Viva & Practical Exams

---

## 🔮 Future Enhancements

* Attack rate thresholding
* Multiple attacker detection
* Graphical attack statistics
* Windows demo (simulation mode)
* Web-based dashboard

---

## 👨‍💻 Author

**Abhishek**
Cybersecurity & Python Dev.

---


