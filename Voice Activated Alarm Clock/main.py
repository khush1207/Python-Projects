import time
import speech_recognition as sr
import winsound

alarm_time = None


def listen_for_voice_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for voice command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Voice command received: {command}")
        handle_voice_command(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        start_voice_recognition()
    except sr.RequestError:
        print("Sorry, there was an error with the speech service.")
        start_voice_recognition()


def handle_voice_command(command):
    global alarm_time
    command = command.lower()

    if "set alarm" in command:
        time_str = command.replace("set alarm to", "").strip()
        try:
            alarm_time = time.strptime(time_str, "%H:%M")
            print(f"Alarm set for {time_str}")
            check_alarm()
        except ValueError:
            print("Sorry, I couldn't understand the time. Please use the 24-hour format HH:MM")
            start_voice_recognition()

    elif "turn off alarm" in command:
        alarm_off()
    elif "yes" in command:
        print("Say 'set alarm to HH:MM' to set an alarm, or 'turn off alarm' to stop it. "
              "For setting alarm use the 24-hour format")
        start_voice_recognition()
    elif "no" in command:
        alarm_off()
    else:
        print("Sorry, I didn't get that. Please try again.")
        start_voice_recognition()


def check_alarm():
    global alarm_time
    print("Waiting for the alarm time...")

    while True:
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min

        if current_hour == alarm_time.tm_hour and current_minute == alarm_time.tm_min:
            trigger_alarm()
            break

        time.sleep(1)


def trigger_alarm():
    print("It's time!")
    winsound.Beep(500, 2500 )
    print("Alarm stopped.")
    print("Do you want to set another alarm?")
    start_voice_recognition()


def alarm_off():
    print("Alarm turned off.")


def start_voice_recognition():
    listen_for_voice_command()


def main():
    global alarm_time
    print("Voice Activated Alarm Clock")
    print("Say 'set alarm to HH:MM' to set an alarm, or 'turn off alarm' to stop it. "
          "For setting alarm use the 24-hour format")
    start_voice_recognition()


if __name__ == "__main__":
    main()
