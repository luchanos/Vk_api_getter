from db_dao import DbDao
from vk_dao import VkDao, ErrorInVKResponse
import requests

db = DbDao()
db.db_tab_creation()
vk = VkDao()
vk.json_loader()

try:
    db.save(vk.get_data())
    db.data_select()
    # db.cleaner()
except ErrorInVKResponse:
    print("Check request properties")
except requests.exceptions.ConnectionError:
    print('NO CONNECTION')