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
        time.sleep(7)
        return tm

    #def destroy(self):
    #    self.destroy()
