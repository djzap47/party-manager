from guest import Guest
import requests
x = requests.get("https://steve107-20107.mikrus.cloud/webhook/9d69b11a-dada-4477-b347-5c87b5f7dc36")
raw_responce = x.json()
guest_list = []
for item in raw_responce:
    guest_name = item["name"]
    guest_email = item["email"]
    guest_diet = item["diet"]
    new_guest = Guest(guest_name, guest_email, guest_diet)
    guest_list.append(new_guest)

for guest in guest_list:
    print(f"Guest created {guest.name}, {guest.email}, {guest.diet}")

