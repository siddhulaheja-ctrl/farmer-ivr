from vonage import Vonage, Auth
from vonage_voice import CreateCallRequest, Talk, Phone, ToPhone

APP_ID = "fb926ccb-0da7-4d10-814f-9a3ae05428e3"

client = Vonage(Auth(application_id=APP_ID, private_key="private.key"))

# fake data — this becomes a database lookup later
farmer = {
    "name": "Ramesh Kumar",
    "phone": "919179615394",     # your own number, no + sign
    "slot_date": "March fifteenth",
    "centre": "Karnal"
}

message = (
    f"Namaste {farmer['name']}. "
    f"Your procurement slot is booked for {farmer['slot_date']} "
    f"at {farmer['centre']} centre. Thank you."
)

response = client.voice.create_call(CreateCallRequest(
        to=[ToPhone(number=farmer["phone"])],
    from_=Phone(number="12345678901"),
    ncco=[Talk(text=message)]
))

print(response)