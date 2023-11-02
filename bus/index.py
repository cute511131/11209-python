import requests
import folium
import tkinter as tk
from tkinter import ttk

# 函數來取得台北市公車即時資訊
def get_bus_data():
    api_url = "https://tcgbusfs.blob.core.windows.net/blobbus/GetBusData.gz"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()  # 解析JSON資料
        # 在這裡你可以處理資料，例如擷取公車位置和資訊

        # 創建一個Folium地圖
        m = folium.Map(location=[25.032969, 121.565418], zoom_start=15)

        # 在地圖上加上公車位置標記
        for bus in data:
            latitude = bus["BusPosition"]["PositionLat"]
            longitude = bus["BusPosition"]["PositionLon"]
            bus_number = bus["PlateNumb"]
            folium.Marker([latitude, longitude], tooltip=bus_number).add_to(m)

        # 儲存地圖在HTML檔案中
        m.save('bus_map.html')

        # 使用Web瀏覽器打開地圖
        import webbrowser
        webbrowser.open('bus_map.html')
    else:
        result_label.config(text="無法取得資料。HTTP狀態碼: " + str(response.status_code))

root = tk.Tk()
root.title("台北市公車即時地圖")

# 創建一個按鈕來觸發資料檢索
button = ttk.Button(root, text="取得公車資訊並顯示在地圖上", command=get_bus_data)
button.pack()

# 用來顯示錯誤訊息的標籤
result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
