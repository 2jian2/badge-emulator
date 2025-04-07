from smartcard.Exceptions import NoCardException
from smartcard.System import readers
from smartcard.scard import SCARD_SHARE_SHARED

GET_UID_COMMAND = [0xFF, 0xCA, 0x00, 0x00, 0x00]

class SmartCardReader:

    def __init__(self):
        self.reader = None
        self.connection = None


    def select_reader(self):
        """Returns an NFC reader if it's connected via USB. Else it returns None"""
        available_readers = readers()

        if not available_readers:
            print("No NFC reader detected through USB port.")
            self.reader = None
            return False

        self.reader = available_readers[0].createConnection() # Get the first reader available
        return True


    def read_uid(self):
        """Return the UID read from the NFC card."""

        if not self.reader:
            print("Reader not initialized.")
            return None

        try:
            try:
                self.connection = self.reader.connect() # Establish the connection wit the NFC reader
            except NoCardException:
                return None


            response, sw1, sw2 = self.reader.transmit(GET_UID_COMMAND)
            # Check if the status words indicate a successful response (0x90 means successful operation) (0x00 means without errors)
            if [sw1, sw2] == [0x90, 0x00]:
                uid_array = [f"{byte:02X}" for byte in response]
                return self._formatted_uid(uid_array)

            else:
                print("Invalid response from NFC card")
                return []

        except Exception as e:
            print(f"Exception while reading the NFC card {e}")
            return False



    def _formatted_uid(self, unformatted_uid):
        """Formats a UID list into a colon-separated string with two-digit hex values."""
        return ":".join(unformatted_uid)

