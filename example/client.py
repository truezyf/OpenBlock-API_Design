import requests

# Base URL of your Flask server
BASE_URL = "http://localhost:5000"


def login(username, password):
    response = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password})
    if response.status_code == 200:
        access_token = response.json()["access_token"]
        print("Login successful!")
        return access_token
    else:
        print("Failed to log in")
        return None


def get_points(access_token, wallet_address, from_date, to_date):
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"wallet_address": wallet_address, "from_date": from_date, "to_date": to_date}
    response = requests.get(f"{BASE_URL}/points", headers=headers, params=params)
    if response.status_code == 200:
        print("Points data:", response.json())
    else:
        print("Failed to fetch points data")


if __name__ == "__main__":
    username = "admin"
    password = "password"

    token = login(username, password)

    if token:
        wallet_address = "0x1155b614971f16758c92c4890ed338c9e3ede6b7"
        from_date = "2024-01-01"
        to_date = "2024-01-31"

        get_points(token, wallet_address, from_date, to_date)
