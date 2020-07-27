import time
from model.input_data import *
import datetime as dt
from fixture.load_dll import DllHelper


class ReactHelper:
    def __init__(self):
        self.self = self

    def create_record_and_timestamp(self, fix):
        time.sleep(1)
        fix.send_react(("CAM|" + camId + "|REC").encode("utf-8"))
        time.sleep(2)
        m = dt.datetime.now()
        tm = m.strftime("%Y%m%dT%H%M%S%Z")
        time.sleep(3)
        fix.send_react(("CAM|" + camId + "|REC_STOP").encode("utf-8"))
        time.sleep(10)
        return tm

    def send_user_react(self, caption_data="", export_image_data=None, fix_dll=None, process_data="", tick1="", tick="", tm_name="", tm="", export_engine="file", fn="filename$", file_name="", camId_n=camId, dir_n=";dir$", dir_d=dir):
        fix_dll.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick1 + ">,import<cam$" + camId + ";" + tm_name + tm + ">,export_engine<" + export_engine + ">,export<" + fn + file_name + tick + camId_n + dir_n + dir_d + ">,export_image<" + export_image_data + ">,process<" + process_data + ">,caption<" + caption_data + ">").encode("utf-8"))
        time.sleep(7)

    #def destroy(self):
    #    self.destroy()
