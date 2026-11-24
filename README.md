# Basic Reconnaissance FTP Anonymous Check

This Python script performs basic network reconnaissance by checking common ports on a target IP address. It specifically attempts an anonymous FTP login if port 21 is found open, demonstrating a common initial vulnerability check in penetration testing, similar to steps taken on machines like Hack The Box's "Lame".

## Language

`python`

## How to Run

1. Save the code as `recon_scanner.py`.
2. Run from your terminal: `python recon_scanner.py <TARGET_IP>`
   (Replace `<TARGET_IP>` with an actual IP address, e.g., `127.0.0.1` or a vulnerable lab machine.)

## Original Article

This example accompanies the Turkish article: [Hack The Box Lame: Sızma Testi Raporu ve Güvenlik Değerlendirmesi](https://fatihsoysal.com/blog/hack-the-box-lame-sizma-testi-raporu-ve-guvenlik-degerlendirmesi/).

## License

MIT — see [LICENSE](LICENSE).
