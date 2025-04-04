import nfc

def select_reader():
    """This function return a NFC reader if it's connected."""
    reader = nfc.ContactlessFrontend("usb")

    if reader is None:
        print("No NFC reader detected through USB port.")
        exit()

    return reader

def wait_and_read_uid(reader):
    """Waits for an NFC card and returns its UID as a list of hex strings."""
    uid_in_array = []

    def on_connect(tag):
        for byte in tag.identifier:
            hex_value = f"{byte:02X}"
            uid_in_array.append(hex_value)
        return False

    reader.connect(rdwr={'on-connect': on_connect})

    return uid_in_array

def formated_uid(unformatted_uid):
    """Formats a UID list into a colon-separated string with two-digit hex values."""
    formated = []

    for hex in unformatted_uid:
        if len(hex) == 1:
            formated.append("0" + hex)
        else:
            formated.append(hex)

    return ":".join(formated)

