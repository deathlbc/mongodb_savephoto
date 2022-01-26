from pymongo import MongoClient
import gridfs

# 連接到server
connection = MongoClient("localhost", 27017)
# 要儲存圖片的資料庫名稱
db = connection["dbname_photo"]

# 創建一個gridFs物件
fs = gridfs.GridFS(db)

# 要存的圖片路徑、檔名
file2 = r".\p123.jpg"

# 打開圖檔並存入
with open(file2, "rb") as f:
    contents = f.read()

#把圖檔放入GridFs物件
fs.put(contents, filename = "file")
