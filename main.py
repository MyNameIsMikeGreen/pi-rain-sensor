from time import sleep
from gpiozero import Buzzer, InputDevice

GPIO_BUZZER = 13    # Pin of buzzer
GPIO_SENSOR = 18    # Pin of sensor

POLL_TIME_SECONDS = 1                   # Seconds between subsequent polls of sensor state
BUZZER_SUSPENSION_TIME_SECONDS = 10     # Seconds after sounding buzzer to suspend further activity
BUZZER_SOUND_TIME_SECONDS = 1           # Seconds to sound buzzer for when activated


def main():
    buzzer = Buzzer(GPIO_BUZZER)
    rain_sensor = InputDevice(GPIO_SENSOR)

    while True:
        if rain_detected(rain_sensor):
            sound_buzzer(buzzer, BUZZER_SOUND_TIME_SECONDS)
            sleep(BUZZER_SUSPENSION_TIME_SECONDS)
        sleep(POLL_TIME_SECONDS)


def sound_buzzer(buzzer, seconds):
    buzzer.on()
    sleep(seconds)
    buzzer.off()


def rain_detected(rain_sensor):
    return False if rain_sensor.is_active else True     # Active input device indicates dry sensor


if __name__ == '__main__':
    main()
