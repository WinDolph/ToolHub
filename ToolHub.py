import os

categories = {
    "Brute-Force & Password Cracking": [
        {"name": "Hydra", "link": "https://github.com/vanhauser-thc/thc-hydra", "desc": "SSH, FTP, HTTP gibi servislerde brute-force saldırısı yapar."},
        {"name": "IGHack", "link": "https://github.com/noob-hackers/ighack", "desc": "Instagram hesaplarına brute-force saldırısı yapar."},
        {"name": "SocialBox", "link": "https://github.com/samsesh/SocialBox-Termux", "desc": "Facebook, Gmail, Instagram için brute-force aracı."},
        {"name": "Hash-Id", "link": "https://github.com/blackploit/hash-identifier", "desc": "Hash türünü tespit eder."},
        {"name": "JohnTheRipper", "link": "https://github.com/magnumripper/JohnTheRipper", "desc": "Popüler parola kırma aracı."},
        {"name": "Patator", "link": "https://github.com/lanjelot/patator", "desc": "Modüler brute-force framework."},
        {"name": "Crowbar", "link": "https://github.com/galkan/crowbar", "desc": "SSH, RDP brute-force aracı."},
        {"name": "CeWL", "link": "https://github.com/digininja/CeWL", "desc": "Özel wordlist oluşturur."},
        {"name": "Medusa", "link": "https://github.com/jmk-foofus/medusa", "desc": "Paralel, hızlı brute-force."},
        {"name": "Aircrack-ng", "link": "https://github.com/aircrack-ng/aircrack-ng", "desc": "Wi-Fi parola kırma aracı."},
    ],

    "Phishing & Social Engineering": [
        {"name": "Zphisher", "link": "https://github.com/htr-tech/zphisher", "desc": "30+ sosyal medya için phishing aracı."},
        {"name": "BlackEye", "link": "https://github.com/An0nUD4Y/blackeye", "desc": "Phishing sayfaları ile kimlik bilgisi toplama."},
        {"name": "EvilPhisher", "link": "https://github.com/evildevill/evilphisher", "desc": "Phishing kampanyaları oluşturur."},
        {"name": "Shellphish", "link": "https://github.com/thelinuxchoice/shellphish", "desc": "Sosyal medya phishing aracı."},
        {"name": "PhishX", "link": "https://github.com/khrsh17/PhishX", "desc": "Phishing sayfa oluşturucu."},
        {"name": "SocialBox", "link": "https://github.com/samsesh/SocialBox-Termux", "desc": "Brute-force ve phishing aracı."},
        {"name": "Modlishka", "link": "https://github.com/drk1wi/Modlishka", "desc": "Modern phishing proxy aracı."},
        {"name": "Gophish", "link": "https://github.com/gophish/gophish", "desc": "Phishing kampanya aracı."},
        {"name": "KingPhisher", "link": "https://github.com/securestate/king-phisher", "desc": "Phishing simülasyon aracı."},
        {"name": "CredSniper", "link": "https://github.com/UndeadSec/CredSniper", "desc": "Gelişmiş phishing framework."},
    ],

    "OSINT & Info Gathering": [
        {"name": "theHarvester", "link": "https://github.com/laramies/theHarvester", "desc": "E-posta ve domain bilgisi toplar."},
        {"name": "Recon-ng", "link": "https://github.com/lanmaster53/recon-ng", "desc": "Modüler OSINT framework."},
        {"name": "Sublist3r", "link": "https://github.com/aboul3la/Sublist3r", "desc": "Alt domain keşif aracı."},
        {"name": "IP-Tracer", "link": "https://github.com/rajkumardusad/IP-Tracer", "desc": "IP konum bilgisi bulur."},
        {"name": "InstaHack", "link": "https://github.com/evildevill/instahack", "desc": "Instagram bilgi toplama aracı."},
        {"name": "Sherlock", "link": "https://github.com/sherlock-project/sherlock", "desc": "Sosyal medya hesap bulucu."},
        {"name": "Metagoofil", "link": "https://github.com/laramies/metagoofil", "desc": "Metadata toplama aracı."},
        {"name": "Dnsenum", "link": "https://github.com/fwaeytens/dnsenum", "desc": "DNS bilgi toplama."},
        {"name": "Maltego", "link": "https://www.paterva.com/web7/", "desc": "Grafik tabanlı bilgi toplama."},
        {"name": "OSINT Framework", "link": "https://osintframework.com/", "desc": "Online OSINT kaynakları."},
    ],

    "Network Scanning & Penetration": [
        {"name": "Nmap", "link": "https://github.com/nmap/nmap", "desc": "Port ve servis tarama aracı."},
        {"name": "BetterCAP", "link": "https://github.com/bettercap/bettercap", "desc": "Network MITM saldırıları."},
        {"name": "Sn1per", "link": "https://github.com/1N3/Sn1per", "desc": "Pentest otomasyon aracı."},
        {"name": "SQLmap", "link": "https://github.com/sqlmapproject/sqlmap", "desc": "Otomatik SQL injection aracı."},
        {"name": "Dirb", "link": "https://github.com/v0re/dirb", "desc": "Dizin tarama aracı."},
        {"name": "WhatWeb", "link": "https://github.com/urbanadventurer/WhatWeb", "desc": "Web uygulama fingerprinting."},
        {"name": "Netcat", "link": "https://github.com/diegocr/netcat", "desc": "Ağ bağlantı ve dinleme aracı."},
        {"name": "Masscan", "link": "https://github.com/robertdavidgraham/masscan", "desc": "Süper hızlı port tarayıcı."},
        {"name": "Recon-ng", "link": "https://github.com/lanmaster53/recon-ng", "desc": "Modüler bilgi toplama."},
        {"name": "Fierce", "link": "https://github.com/mschwager/fierce", "desc": "Domain ve IP tarayıcı."},
    ],

    "Exploitation & Vulnerability": [
        {"name": "Metasploit Framework", "link": "https://github.com/rapid7/metasploit-framework", "desc": "Güçlü exploit framework."},
        {"name": "BeEF", "link": "https://github.com/beefproject/beef", "desc": "Browser exploit framework."},
        {"name": "wpsploit", "link": "https://github.com/Dionach/WPSploit", "desc": "WordPress güvenlik testi."},
        {"name": "Impacket", "link": "https://github.com/SecureAuthCorp/impacket", "desc": "Network protokol exploit araçları."},
        {"name": "CrackMapExec", "link": "https://github.com/byt3bl33d3r/CrackMapExec", "desc": "Windows ağ exploit aracı."},
        {"name": "Sqlmap", "link": "https://github.com/sqlmapproject/sqlmap", "desc": "SQL injection açığı arama."},
        {"name": "Searchsploit", "link": "https://github.com/offensive-security/exploitdb", "desc": "Exploit veri tabanı aracı."},
        {"name": "RouterSploit", "link": "https://github.com/threat9/routersploit", "desc": "Router exploit framework."},
        {"name": "Commix", "link": "https://github.com/commixproject/commix", "desc": "Komut enjeksiyonu testi."},
        {"name": "XSStrike", "link": "https://github.com/s0md3v/XSStrike", "desc": "XSS açığı tespit aracı."},
    ],

    "Wi-Fi & Wireless Attacks": [
        {"name": "Aircrack-ng", "link": "https://github.com/aircrack-ng/aircrack-ng", "desc": "Wi-Fi parola kırma."},
        {"name": "Reaver", "link": "https://github.com/t6x/reaver-wps-fork-t6x", "desc": "WPS PIN kırma."},
        {"name": "Wifite", "link": "https://github.com/derv82/wifite2", "desc": "Otomatik Wi-Fi saldırıları."},
        {"name": "Fern Wifi Cracker", "link": "https://github.com/savio-code/fern-wifi-cracker", "desc": "GUI destekli Wi-Fi saldırı."},
        {"name": "MDK3", "link": "https://github.com/wi-fi-analyzer/mdk3-master", "desc": "Wi-Fi DoS saldırısı."},
        {"name": "Kismet", "link": "https://github.com/kismetwireless/kismet", "desc": "Kablosuz ağ tespiti."},
        {"name": "BlueMaho", "link": "https://github.com/BlueMaho/BlueMaho", "desc": "Bluetooth saldırı aracı."},
        {"name": "Wifiphisher", "link": "https://github.com/wifiphisher/wifiphisher", "desc": "Phishing tabanlı Wi-Fi saldırısı."},
        {"name": "Airgeddon", "link": "https://github.com/v1s1t0r1sh3r3/airgeddon", "desc": "Kablosuz saldırı scripti."},
        {"name": "Pixiewps", "link": "https://github.com/wi-fi-analyzer/pixiewps", "desc": "WPS Pixie Dust saldırısı."},
    ],

    "Cryptography & Steganography": [
        {"name": "Steghide", "link": "https://github.com/StefanoDeVuono/steghide", "desc": "Dosya içine gizleme aracı."},
        {"name": "Stegcloak", "link": "https://github.com/kurolabs/stegcloak", "desc": "Gizli metin saklama aracı."},
        {"name": "OpenStego", "link": "https://www.openstego.com/", "desc": "Görsel steganografi."},
        {"name": "Cryptool", "link": "https://www.cryptool.org/en/", "desc": "Kriptografi eğitim aracı."},
        {"name": "GPG", "link": "https://gnupg.org/", "desc": "Dosya şifreleme."},
        {"name": "Hashcat", "link": "https://hashcat.net/hashcat/", "desc": "Hash kırma aracı."},
        {"name": "TrueCrypt", "link": "https://www.grc.com/misc/truecrypt/truecrypt.htm", "desc": "Disk şifreleme."},
        {"name": "VeraCrypt", "link": "https://www.veracrypt.fr/en/Home.html", "desc": "Disk şifreleme."},
        {"name": "Cryptcat", "link": "https://sourceforge.net/projects/cryptcat/", "desc": "Şifreli netcat."},
        {"name": "ZBar", "link": "https://github.com/mchehab/zbar", "desc": "QR barkod okuyucu."},
    ],

    "Keyloggers & System Monitoring": [
        {"name": "Termux Keylogger", "link": "https://github.com/junegunn/keylogger", "desc": "Terminal tuş kaydedici."},
        {"name": "Spycam", "link": "https://github.com/thelinuxchoice/spycam", "desc": "Kamera casusluğu."},
        {"name": "WhatsApp Spy", "link": "https://github.com/ebrahim3/whatsapp-spy", "desc": "WhatsApp izleme."},
        {"name": "Termux API", "link": "https://github.com/termux/termux-api", "desc": "Termux için API araçları."},
       {"name": "Termux Monitor", "link": "https://github.com/Techriz/Termux", "desc": "Sistem kaynakları izleme."},
        {"name": "ADB Toolkit", "link": "https://github.com/SecWiki/android-malware", "desc": "Android Debug Bridge araçları."},
        {"name": "LogKali", "link": "https://github.com/rajkumardusad/logkali", "desc": "Sistem logları toplama."},
        {"name": "Termux Screenshot", "link": "https://github.com/termux/termux-api", "desc": "Ekran görüntüsü alma."},
        {"name": "Process Watcher", "link": "https://github.com/duangle/process-watcher", "desc": "Süreç izleme aracı."},
        {"name": "Infection Tracker", "link": "https://github.com/infectiontracker/infectiontracker", "desc": "Kötü amaçlı yazılım izleme."},
    ],

    "DDoS & Network Attacks": [
        {"name": "LOIC", "link": "https://github.com/NewEraCracker/LOIC", "desc": "Basit HTTP DDoS saldırısı."},
        {"name": "HOIC", "link": "https://github.com/galkan/hoic", "desc": "Yüksek etkili DDoS saldırısı."},
        {"name": "GoldenEye", "link": "https://github.com/jseidl/GoldenEye", "desc": "Python tabanlı HTTP DoS."},
        {"name": "Slowloris", "link": "https://github.com/gkbrk/slowloris", "desc": "HTTP Slow DoS saldırısı."},
        {"name": "Xerxes", "link": "https://github.com/XerxesX10/Xerxes", "desc": "Yüksek hızlı HTTP saldırısı."},
        {"name": "UFONet", "link": "https://github.com/epsylon/ufonet", "desc": "Web site DDoS aracı."},
        {"name": "Torshammer", "link": "https://github.com/dotfighter/torshammer", "desc": "Tor tabanlı DoS saldırısı."},
        {"name": "Hping3", "link": "https://github.com/antirez/hping", "desc": "TCP/IP paket oluşturucu."},
        {"name": "DDoS Script", "link": "https://github.com/Anonyfox007/DDoS-Script", "desc": "Çeşitli DDoS yöntemleri."},
        {"name": "Xbomb", "link": "https://github.com/Xeonx/XBomb", "desc": "SMS & Network bombalama."},
    ],
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = r"""
 _______          _ _    _       _     
|__   __|        | | |  | |     | |    
   | | ___   ___ | | |__| |_   _| |__  
   | |/ _ \ / _ \| |  __  | | | | '_ \ 
   | | (_) | (_) | | |  | | |_| | |_) |
   |_|\___/ \___/|_|_|  |_|\__,_|_.__/ 
"""
    print(banner)
    print("         from WinDolph (hacktivizm)\n")
def show_main_menu():
    clear()
    print_banner()
    print("🛠️ Hoşgeldin kankam, ne istersin?\n")
    for i, cat in enumerate(categories.keys(), 1):
        print(f"{i}. {cat}")
    print("X. Çıkmak için")

def show_tools(category):
    clear()
    print(f"🔎 {category} Araçları:\n")
    tools = categories[category]
    for i, tool in enumerate(tools, 1):
        print(f"{i}. {tool['name']}")
    print("G. Geri dön")

def show_tool_details(category, index):
    clear()
    tool = categories[category][index]
    print(f"📦 {tool['name']}")
    print(f"🔗 GitHub Linki: {tool['link']}")
    print(f"📄 Açıklama: {tool['desc']}")
    print(f"📥 İndirme Kodu:\n\n  git clone {tool['link']}")
    print("\nG. Geri dön")

def main():
    while True:
        show_main_menu()
        choice = input("\nBir kategori seçin: ").strip().lower()
        if choice == 'x':
            print("Çıkılıyor kankam...")
            break
        try:
            category = list(categories.keys())[int(choice) - 1]
        except (ValueError, IndexError):
            continue

        while True:
            show_tools(category)
            tool_choice = input("\nBir aracı seçin: ").strip().lower()
            if tool_choice == 'g':
                break
            try:
                tool_index = int(tool_choice) - 1
                if tool_index < 0 or tool_index >= len(categories[category]):
                    continue
            except ValueError:
                continue

            while True:
                show_tool_details(category, tool_index)
                back = input("\nSeçiminiz (G): ").strip().lower()
                if back == 'g':
                    break

if __name__ == "__main__":
    main()