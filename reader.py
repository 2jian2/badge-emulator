import nfc

def select_reader():
    """This function return a NFC reader if it's connected."""
    reader = nfc.ContactlessFrontend("usb")

    if reader is None:
        print("No NFC reader detected through USB port.")
        exit()

    return reader

def wait_and_read_uid(reader):


    uid_in_array = []

    def on_connect(tag):
        for byte in tag.identifier:
            hex_value = hex(byte)[2:].upper() # convert each byte to a 2-digit uppercase hex string without '0x'
            hex_value = f"{byte:02X}"
            uid_in_array.append(hex_value)
        return False

    reader.connect(rdwr={'on-connect': on_connect})

    return uid_in_array
