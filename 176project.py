import speedtest
import matplotlib .pyplot as plt
import time

list_download_speed=[]
list_upload_speed=[]

for i in range(5):
    st= speedtest.Speedtest()
    download_speed= round(st.download()/1000000,2)
    label_download_speed.append(download_speed)
    upload_speed = round(st.upload()/1000000,2)
    label_upload_speed.append(upload_speed)
    time.sleep(60)
    
print(list_download_speed)
print(list_upload_speed)    
    
plt.plot(x, list_download_speed, label = "download speed")  
plt.plot(x, list_upload_speed, label="upload speed")

title("Speed")
plt.legend()

  
    
    
    