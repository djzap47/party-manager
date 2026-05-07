import requests
def get_n8n_data():
    url = "https://steve107-20107.mikrus.cloud/webhook/9d69b11a-dada-4477-b347-5c87b5f7dc36"
    x = requests.get(url)
    return x.json()
