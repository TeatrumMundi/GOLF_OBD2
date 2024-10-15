import obd

try:
    connection = obd.OBD(fast=False, timeout=30)  # auto-connects to USB or RF port

    if connection.status() == obd.OBDStatus.NOT_CONNECTED:
        print("Nie można połączyć się z urządzeniem OBD.")
    else:
        cmd = obd.commands.SPEED  # wybierz komendę OBD (sensor)

        response = connection.query(cmd)  # wyślij komendę i przetwórz odpowiedź

        if response.is_null():
            print("Brak odpowiedzi od urządzenia OBD.")
        else:
            print(response.value)  # zwraca wartości z jednostkami (Pint)
            print(response.value.to("mph"))  # przyjazna konwersja jednostek
except Exception as e:
    print(f"Wystąpił błąd: {e}")
