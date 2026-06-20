# Security Best Practices for AI Cable Diagnostic Device

## 1. Network Security
- **Firewall**: Use `ufw` to block all incoming ports except 5000 (API) and 22 (SSH).
- **VPN**: Access the device dashboard only via a secure VPN (e.g., WireGuard).
- **API Tokens**: The API is protected by an `X-API-Token` header. Change the default token in `src/api.py` before deployment.

## 2. Auditing
- All sensitive access (history, AR data) is logged in `logs/audit.log`.
- Unauthorized attempts are automatically flagged with the requester's IP address.

## 3. Physical Security
- Ensure the Raspberry Pi is in a locked, weather-resistant enclosure.
- Disable USB boot and set a BIOS/Firmware password if supported.

## 4. Updates
- Run `sudo apt update && sudo apt upgrade` regularly.
- Keep Python dependencies updated using `pip install --upgrade -r requirements.txt`.

## 5. Data Encryption
- For high-security environments, consider encrypting the `data/diagnostics.db` SQLite database using `SQLCipher`.
