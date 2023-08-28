import serial
import time

uno = serial.Serial(port='COM6',   baudrate=9600, timeout=.1)

# while True:
#     line = uno.read(1)
#     decoded_line = line.decode('utf-8').strip()
#     print(f"Received line: {decoded_line}")
#     time.sleep(0.1)
#
while True:
    line = uno.readline()
    decoded_line = line.strip()
    print(f"Received data from Arduino: {decoded_line}")

# import serial
#
# def main():
#     try:
#         ser = serial.Serial('COM6', baudrate=115200, timeout=0.1)
#         print(f"Connected to {ser.name}")
#
#         while True:
#             line = ser.readline()
#             if line:
#                 decoded_line = line.decode().strip()
#                 print(f"Received data from Arduino: {decoded_line}")
#
#     except serial.SerialException as e:
#         print(f"Error: {e}")
#     except KeyboardInterrupt:
#         print("Exiting...")
#     finally:
#         if 'ser' in locals():
#             ser.close()
#
#
# if __name__ == "__main__":
#     main()

