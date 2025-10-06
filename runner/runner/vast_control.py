import os, time, requests
VAST_KEY = os.getenv("VAST_KEY","")
headers={"Authorization":f"Bearer {VAST_KEY}"}

def get_info():
    try:
        r=requests.get("https://api.vast.ai/user/info/",headers=headers)
        if r.ok:
            bal=r.json().get("results",{}).get("balance_usd","?")
            print(f"[Vast] Kredit: {bal} USD")
        else:
            print("[Vast] Error",r.status_code,r.text)
    except Exception as e:
        print("[Vast] Exception:",e)

if __name__=="__main__":
    print("[Runner] Vast kontrola běží…")
    while True:
        get_info(); time.sleep(600)
