from model.input_data import *
import time
#import datetime as dt
from fixture.work_with_db import DbHelper
#from fixture.react import ReactHelper

def test1_image_export_process_test(fix_dll, fix_react):
    tick = "process_test"
    tm = fix_react.create_record_and_timestamp(fix_dll)
    fix_dll.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$" + tm + ">,export_engine<file>,export<filename$test1_export_" + tick + "_on_cam" + camId + ";dir$" + dir + ">,export_image<format$png;quality$85>,process<color:200,50,150;penwidth:10;rect:10,20,25,15;crop:0,0,95,95;font:20;polygon:15,15,20,20,25,20,20,90,70,25,40,40,55,55;polyline:90,85,80,81,75,90,50,50;text:15,75,blabla test>,caption<15:ahaha test blabla \n phah testtest bla 123123111!!!>").encode("utf-8"))
    time.sleep(7)
    fix_dll.search_in_callback(par="request_id")
    time.sleep(7)
    assert fix_dll.p == tick




def test2_image_export_jpg_quality_low_test(fix_dll, fix_react):
    tick = "low_jpg_test"
    tm = fix_react.create_record_and_timestamp(fix_dll)
    fix_dll.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$" + tm + ">,export_engine<file>,export<filename$test2_export_" + tick + "_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$1>,caption<25:low jpg>").encode("utf-8"))
    time.sleep(5)
    fix_dll.search_in_callback(par="request_id")
    assert fix_dll.p == tick


def test3_image_export_jpg_quality_high_test(fix_dll, fix_react):
    tick = "high_jpg_test"
    tm = fix_react.create_record_and_timestamp(fix_dll)
    fix_dll.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$" + tm + ">,export_engine<file>,export<filename$test3_export_" + tick + "_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:high jpg>").encode("utf-8"))
    time.sleep(5)
    fix_dll.search_in_callback(par="request_id")
    assert fix_dll.p == tick
    time.sleep(2)

def test4_image_export_live_image(fix_dll):
    tick = "liveImage"
    fix_dll.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$live>,export_engine<file>,export<filename$test4_export_" + tick + "_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:live with twodim scale>,process<scale:400,400>").encode("utf-8"))
    time.sleep(2)
    fix_dll.search_in_callback(par="request_id")
    assert fix_dll.p == tick
    time.sleep(2)

def test5_image_export_arhive_and_live_image_task_in_a_row(fix_dll, fix_react):
    tick = "archive"
    tick1 = "live"
    tm = fix_react.create_record_and_timestamp(fix_dll)
    fix_dll.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$" + tm + ">,export_engine<file>,export<filename$test5_export_" + tick + "_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:live>").encode("utf-8"))
    time.sleep(2)
    fix_dll.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick1 + ">,import<cam$" + camId + ";time$live>,export_engine<file>,export<filename$test5_export_" + tick + "_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:live>").encode("utf-8"))
    time.sleep(3)
    fix_dll.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick1 + "2>,import<cam$" + camId + ";time$live>,export_engine<file>,export<filename$test5_export_" + tick + "2_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:live2>").encode("utf-8"))
    time.sleep(3)
    fix_dll.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick1 + "3>,import<cam$" + camId + ";time$live>,export_engine<file>,export<filename$test5_export_" + tick + "3_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:live3>").encode("utf-8"))
    time.sleep(3)

    fix_dll.search_all_in_callback(par="request_id")
    assert fix_dll.l[0] == tick
    assert fix_dll.l[1] == tick1
    assert fix_dll.l[2] == tick1 + "2"
    assert fix_dll.l[3] == tick1 + "3"
    #print(fix.l[0])


def test6_ImageExport_DBImage(fix_dll, fix_react, fix_db):
    tick = "DBImage"
    fix_db.create_db_and_tables()
    tm = fix_react.create_record_and_timestamp(fix_dll)
    DBstr = IdDB+":INSERT INTO public.image(image, tid) VALUES(?, '"+tid+"')"
    fix_dll.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$" + tm + ">,export_engine<sql>,export<" + DBstr + ">,export_image<format$png;quality$85>,process<color:200,50,150;penwidth:10;rect:10,20,25,15;font:20;polygon:15,15,20,20>").encode("utf-8"))
    time.sleep(3)
    fix_dll.search_in_callback(par="request_id")
    assert fix_dll.p == tick
    fix_db.check_db()
    time.sleep(1)
    assert fix_db.records != []






