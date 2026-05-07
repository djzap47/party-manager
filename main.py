
from api_guest import get_n8n_data
from map_list import map_raw_responce, show_all_guest
raw_responce = get_n8n_data()
ready_guests = map_raw_responce(raw_responce)
show_all_guest(ready_guests)

