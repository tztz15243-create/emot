import requests
from google_play_scraper import app
import json

def AuToUpDaTE():
    result = app('com.dts.freefireth', lang="fr", country='fr')
    version = result['version']
    
    # القيم الافتراضية الجديدة
    url = "https://loginbp.ggpolarbear.com/"
    ob = "OB53"
    
    try:
        # استخدام الـ API الجديد الموثوق
        r = requests.get('https://redzedupdater.vercel.app/', verify=True)
        if r.status_code == 200:
            data = r.json()
            url = data.get('server_url', url)
            ob = data.get('latest_release_version', ob)
            print(f"✅ Version fetched: {version}, OB={ob}, URL={url}")
        else:
            print(f"⚠️ API returned status {r.status_code}, using defaults")
    except requests.exceptions.JSONDecodeError:
        print("⚠️ API response is not JSON, using defaults")
    except Exception as e:
        print(f"⚠️ Failed to fetch from API: {e}, using defaults")
    
    return url, ob, version
