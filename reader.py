from smartcard.System import readers
GET_UID_COMMAND = [0xFF, 0xCA, 0x00, 0x00, 0x00]


def select_reader():
    """Returns an NFC reader if it's connected via USB."""
    reader = readers()

    if len(reader) == 0:
        print("No NFC reader detected through USB port.")
        exit()
    else:
        nfc_reader = reader[0].createConnection()
        return nfc_reader


def wait_and_read_uid(reader):
    """Sends APDU command to retrieve the UID from the NFC card."""
    try:
        reader.connect()

        response, sw1, sw2 = reader.transmit(GET_UID_COMMAND)

        # Check if the status words indicate a successful response (0x90 means successful operation) (0x00 means without errors)
        if [sw1, sw2] == [0x90, 0x00]:
            uid_array = [f"{byte:02X}" for byte in response]
            return uid_array

        else:
            print("Failed to read UID.")
            return []
    except Exception as e:
        return []

def formated_uid(unformatted_uid):
    """Formats a UID list into a colon-separated string with two-digit hex values."""
    return ":".join(unformatted_uid)

