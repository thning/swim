# %%
import requests
from datetime import datetime  
import csv
import os

try:
    # 取得時間
    time = datetime.now()
    weekday, hr = time.strftime("%A"), time.strftime("%H")

    # 抓 API
    res = requests.get('https://lkcsc.cyc.org.tw/api') 
    current = res.json()['swim'][0]

    # 寫入 CSV
    with open('data.csv', 'a+', newline='') as csvfile:
        write = csv.writer(csvfile)
        if os.stat('data.csv').st_size == 0:
            write.writerow(["weekday", "hr", "current"])
        write.writerow([weekday, hr, current])

except Exception as e:
    # 錯誤時間
    error_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 建立 TXT 檔案，檔名包含時間 + "error"
    filename = f"{error_time}_error.txt"
    
    # 寫入錯誤訊息
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Error occurred at {error_time}\n")
        f.write(str(e))


# %%



