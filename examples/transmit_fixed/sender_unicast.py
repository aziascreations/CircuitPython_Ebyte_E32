# SPDX-FileCopyrightText: 2023 Herwin Bozet
#
# SPDX-License-Identifier: Unlicense

import board
import time

import ebyte_e32

PIN_M0 = board.IO13
PIN_M1 = board.IO12
PIN_RXD = board.IO11  # Pin marked as RX on the module
PIN_TXD = board.IO10  # Pin marked as TX on the module
PIN_AUX = board.IO9

e32 = ebyte_e32.E32Device(PIN_M0, PIN_M1, PIN_AUX, PIN_TXD, PIN_RXD, address=0xBEEF, channel=4)

# Switching to fixed transmission mode.
e32.tx_mode = ebyte_e32.TransmissionMode.TRANSMISSION_FIXED

# Switching to mode 0.  (Normal mode)
e32.mode = ebyte_e32.Modes.MODE_NORMAL

# Message content:
#  * Receiver's address: 0x1337  (b'\x13\x37')
#  * Receiver's channel: 4  (b'\x04')
#  * Message: b'Hello World !'
message = b'\x13\x37\x04Hello World !'

e32.uart.write(message)

# The message may be truncated at specific lengths depending on the frequencies used.
# Please check the documentation for more information !
