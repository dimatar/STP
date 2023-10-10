import requests


def fetch_response_from_api(url, headers=None, params=None, method="GET"):
    """
    Fetches a response from the given API URL.

    Args:
        url (str): The API endpoint URL.
        headers (dict, optional): Headers to send with the request.
        params (dict, optional): Parameters to send with the request.
        method (str, optional): HTTP method to use. Default is "GET".

    Returns:
        dict: Parsed JSON response from the API.
    """
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, params=params)
        # Add other HTTP methods as needed...
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code

        if response.headers.get("content-type") == "application/json":
            return response.json()  # If response is in JSON format, parse it and return a dictionary
        else:
            return response.text  # Else, return raw text content
    except requests.RequestException as e:
        print(f"Error fetching response from API: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    URL = "https://a.liveuamap.com/api"
    API_KEY = "your_api_key_here"
    headers = {
        "Authorization": f"Bearer {API_KEY}",  # Or "X-API-Key": API_KEY, depending on the API's documentation
    }
    response_data = fetch_response_from_api(URL, headers=headers)
    if response_data:
        print(response_data)
