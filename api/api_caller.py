import requests
import json

class ApiCaller:
    def __init__(self, base_url):
        self.base_url = base_url
        self.access_token = None
        
    def login(self, username, password, otp):
        url = f"{self.base_url}/api/v1/users/signin"
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        payload = {
            'userId': username,
            'password': password,
            'otp': otp
        }
        
        response = requests.post(
            url,
            headers=headers,
            json=payload
        )
        
        result = response.json()
        self.access_token = result['result']['accessJwt']
        return result
    
    def create_menu(self, menu_name, description, items):
        if not self.access_token:
            raise ValueError("Not logged in. Please login first.")
            
        url = f"{self.base_url}/api/v1/menus"
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }
        
        payload = {
            'menuName': menu_name,
            'description': description,
            'items': items
        }
        
        response = requests.post(
            url,
            headers=headers,
            json=payload
        )
        
        return response.json()

    def update_menu(self, menu_id, name, items):
        if not self.access_token:
            raise ValueError("Not logged in. Please login first.")
            
        url = f"{self.base_url}/api/v1/menus"
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }
        
        payload = {
            'id': menu_id,
            'name': name,
            'items': items
        }
        
        response = requests.put(
            url,
            headers=headers,
            json=payload
        )
        
        return response.json()

    def delete_menu(self, menu_id):
        if not self.access_token:
            raise ValueError("Not logged in. Please login first.")
            
        url = f"{self.base_url}/api/v1/menus/{menu_id}"
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }
        
        response = requests.delete(
            url,
            headers=headers
        )
        print(response)
        
        return response.json()

if __name__ == "__main__":
    # Configuration
    BASE_URL = "http://localhost:8080"
    
    api = ApiCaller(BASE_URL)
    
    # Login
    api.login(
        username="krksuperadmin",
        password="ab"
    )
    
    # Menu data
    menu_data = {
        "name": "MV, MachineY, PLC, 분전반 메뉴",
        "description": "MV, MachineY, PLC, 분전반 메뉴",
        "items": []  # Add your menu items here
    }
    
    # Create menu
    result = api.create_menu(
        menu_data["name"],
        menu_data["description"],
        menu_data["items"]
    )
    
    print(json.dumps(result, indent=2, ensure_ascii=False))