import os, time, requests

NOTION_KEY = os.getenv("NOTION_KEY", "")
NOTION_DB = os.getenv("NOTION_DB", "")
headers = {"Authorization": f"Bearer {NOTION_KEY}", "Notion-Version": "2022-06-28"}

def loop():
    while True:
        try:
            res = requests.post(f"https://api.notion.com/v1/databases/{NOTION_DB}/query", headers=headers)
            if res.status_code == 200:
                print("[Notion] OK", len(res.json().get("results", [])), "items")
            else:
                print("[Notion] Error", res.status_code, res.text)
        except Exception as e:
            print("[Notion] Exception:", e)
        time.sleep(60)

if __name__ == "__main__":
    print("[Runner] Notion sync starting…")
    loop()
