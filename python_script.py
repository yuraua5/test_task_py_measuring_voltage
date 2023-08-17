import serial
import time

ser = serial.Serial("COM3", 9600)


def read_voltage() -> int:
    ser.write(f"READ_VOLTAGE\n".encode())
    data = ser.readline().decode().strip()
    return int(data)


def set_nplc(nplc: int) -> None:
    ser.write(f"SET_NPLC {nplc}\n".encode())
    time.sleep(0.1)


def convert_to_voltage(value: int) -> float:
    return value * (3.3 / 1023)


if __name__ == "__main__":
    try:
        set_nplc(1)
        raw_value = read_voltage()
        voltage = convert_to_voltage(raw_value)
        print(f"Measured voltage: {voltage:.2f} V")

    except Exception as e:
        print("Error:", e)
    finally:
        ser.close()
