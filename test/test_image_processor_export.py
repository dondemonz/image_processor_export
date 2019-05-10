from model.input_data import *
import time
import datetime as dt

def test_image_export_procces_test(fix):
    tick = "procces_test"
    time.sleep(1)
    fix.send_react(("CAM|" + camId + "|REC").encode("utf-8"))
    time.sleep(2)
    m = dt.datetime.now()
    tm = m.strftime("%Y%m%dT%H%M%S%Z")
    time.sleep(3)
    fix.send_react(("CAM|" + camId + "|REC_STOP").encode("utf-8"))
    time.sleep(7)
    fix.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$"+tm+">,export_engine<file>,export<filename$test1_export_" + tick + "_on_cam" + camId + ";dir$" + dir + ">,export_image<format$png;quality$85>,process<color:200,50,150;penwidth:10;rect:10,20,25,15;crop:0,0,95,95;font:20;polygon:15,15,20,20,25,20,20,90,70,25,40,40,55,55;polyline:90,85,80,81,75,90,50,50;text:15,75,blabla test>,caption<15:ahaha test blabla \n phah testtest bla 123123111!!!>").encode("utf-8"))
    time.sleep(2)
    fix.search_in_callback(par="request_id")
    assert fix.p == tick


def test_image_export_jpg_quality_low_test(fix):
    tick = "low_jpg_test"
    time.sleep(1)
    fix.send_react(("CAM|" + camId + "|REC").encode("utf-8"))
    time.sleep(2)
    m = dt.datetime.now()
    tm = m.strftime("%Y%m%dT%H%M%S%Z")
    time.sleep(3)
    fix.send_react(("CAM|" + camId + "|REC_STOP").encode("utf-8"))
    time.sleep(7)
    fix.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$"+tm+">,export_engine<file>,export<filename$test2_export_" + tick + "_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$1>,caption<25:low jpg>").encode("utf-8"))
    time.sleep(1)
    fix.search_in_callback(par="request_id")
    assert fix.p == tick


def test_image_export_jpg_quality_high_test(fix):
    tick = "high_jpg_test"
    time.sleep(1)
    fix.send_react(("CAM|" + camId + "|REC").encode("utf-8"))
    time.sleep(2)
    m = dt.datetime.now()
    tm = m.strftime("%Y%m%dT%H%M%S%Z")
    time.sleep(3)
    fix.send_react(("CAM|" + camId + "|REC_STOP").encode("utf-8"))
    time.sleep(7)
    fix.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$"+tm+">,export_engine<file>,export<filename$test3_export_" + tick + "_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:high jpg>").encode("utf-8"))
    time.sleep(1)
    fix.search_in_callback(par="request_id")
    assert fix.p == tick


