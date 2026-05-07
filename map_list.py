from guest import Guest
def map_raw_responce(x):
    guest_list = []
    for item in x:
        guest_name = item["name"]
        guest_email = item["email"]
        guest_diet = item["diet"]
        new_guest = Guest(guest_name, guest_email, guest_diet)
        guest_list.append(new_guest)
    return guest_list
def show_all_guest(i):
    for guest in i:
        print(f"Guest created {guest.name}, {guest.email}, {guest.diet}")