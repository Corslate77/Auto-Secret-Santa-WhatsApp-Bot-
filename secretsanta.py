import random
import pywhatkit
import time

# Replace these with real names and phone numbers.
# Ensure numbers include the country code (e.g., +1, +44, +90).
participants = {
    "Bahar": "+905551112233",
    "Ahsen": "+905551112234",
    "Melek": "+905551112235",
    "Ahmet": "+905551112236",
    "Efe": "+905551112237",
    "Eray": "+905551112238",
    "Eren": "+905551112239",
    "Kagan": "+905551112240",
    "Musa": "+905551112241",
    "Aylin": "+905551112242",
    "Kadirhan": "+905551112243"
}


def run_secret_santa():
    # Extract names and shuffle them randomly
    names = list(participants.keys())
    random.shuffle(names)

    # The "Circle Method": Each person buys a gift for the next person in the list.
    # The last person buys for the first person. This prevents anyone from drawing themselves.
    for i in range(len(names)):
        giver = names[i]
        receiver = names[(i + 1) % len(names)]
        giver_phone = participants[giver]

        # Secret Santa WhatsApp Message
        message = (
            "🎄 Happy New Year! 🎅\n\n"
            "The Secret Santa draw is finally complete!\n"
            f"You are the Secret Santa for: *{receiver}* 🎁\n\n"
            "Keep it a secret and let's make this year unforgettable. Happy holidays!"
        )

        print(f"Sending message to {giver}... (Their assignment: {receiver})")

        try:
            # Send the message instantly and close the WhatsApp Web tab afterwards
            pywhatkit.sendwhatmsg_instantly(
                phone_no=giver_phone,
                message=message,
                wait_time=15,
                tab_close=True,
                close_time=3
            )
            # Small delay to prevent browser tab conflicts
            time.sleep(2)

        except Exception as e:
            print(f"Error! Could not send message to {giver}. Reason: {e}")


# Run the script
if __name__ == "__main__":
    run_secret_santa()