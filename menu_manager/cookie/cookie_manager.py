import os
import json

class CookieManager:
    def __init__(self):
        self.cookie_file = 'cookie.txt'

    def save_cookie(self, key, value):
        """쿠키 데이터를 저장"""
        try:
            # Load existing data if file exists
            data = {}
            if os.path.exists(self.cookie_file):
                with open(self.cookie_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            
            # Update or add new value
            data[key] = value
            
            # Save updated data
            with open(self.cookie_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Failed to save cookie: {e}")

    def save_file_location(self, location):
        """파일 위치를 cookie.txt에 저장"""
        self.save_cookie("latest_selected_order_file_location", location)

    def save_access_token(self, token):
        """액세스 토큰을 cookie.txt에 저장"""
        self.save_cookie("access_token", token)

    def load_last_file_location(self):
        """cookie.txt에서 마지막 파일 위치 로드"""
        try:
            if os.path.exists(self.cookie_file):
                with open(self.cookie_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get("latest_selected_order_file_location")
        except Exception as e:
            print(f"Failed to load location: {e}")
        return None

    def load_cookie(self, key):
        """쿠키 데이터를 불러옴"""
        try:
            if os.path.exists(self.cookie_file):
                with open(self.cookie_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get(key)
        except Exception as e:
            print(f"Failed to load cookie: {e}")
        return None