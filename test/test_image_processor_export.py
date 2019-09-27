from model.input_data import *
import time
import datetime as dt
import winreg
from fixture.work_with_db import DbHelper

def test_create_key_and_pareams():   # изменяет параемтр в реестре, после теста в restapi. на downloadTImeout 5 т.к. с 2 иногда не проходит тест
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\WOW6432Node\\ISS\\SecurOS\\Niss400\\ImageProcessor")
    winreg.SetValueEx(key, 'downloadTimeout', 0, winreg.REG_SZ, '7')

def test1_image_export_procces_test(fix):
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
    time.sleep(3)
    fix.search_in_callback(par="request_id")
    time.sleep(3)
    assert fix.p == tick


def test2_image_export_jpg_quality_low_test(fix):
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


def test3_image_export_jpg_quality_high_test(fix):
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
    time.sleep(2)

def test4_image_export_live_image(fix):
    tick = "liveImage"
    fix.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$live>,export_engine<file>,export<filename$test4_export_" + tick + "_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:live with twodim scale>,process<scale:400,400>").encode("utf-8"))
    time.sleep(2)
    fix.search_in_callback(par="request_id")
    assert fix.p == tick
    time.sleep(2)

def test5_image_export_arhive_and_live_image_task_in_a_row(fix):
    tick = "archive"
    time.sleep(1)
    fix.send_react(("CAM|" + camId + "|REC").encode("utf-8"))
    time.sleep(2)
    m = dt.datetime.now()
    tm = m.strftime("%Y%m%dT%H%M%S%Z")
    time.sleep(3)
    fix.send_react(("CAM|" + camId + "|REC_STOP").encode("utf-8"))
    time.sleep(7)
    fix.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$"+tm+">,export_engine<file>,export<filename$test5_export_" + tick + "_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:live>").encode("utf-8"))
    time.sleep(2)
    #fix.search_in_callback(par="request_id")
    #assert fix.p == tick


    tick1 = "live"
    fix.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick1 + ">,import<cam$" + camId + ";time$live>,export_engine<file>,export<filename$test5_export_" + tick + "_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:live>").encode("utf-8"))
    time.sleep(3)
    #fix.search_all_in_callback(par="request_id")
    #assert fix.p == tick1


    fix.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick1 + "2>,import<cam$" + camId + ";time$live>,export_engine<file>,export<filename$test5_export_" + tick + "2_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:live2>").encode("utf-8"))
    time.sleep(3)
    #fix.search_in_callback(par="request_id")
    #assert fix.p == tick1+"2"


    fix.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick1 + "3>,import<cam$" + camId + ";time$live>,export_engine<file>,export<filename$test5_export_" + tick + "3_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:live3>").encode("utf-8"))
    time.sleep(3)
    #fix.search_in_callback(par="request_id")
    #assert fix.p == tick1+"3"
    fix.search_all_in_callback(par="request_id")
    assert fix.l[0] == tick
    assert fix.l[1] == tick1
    assert fix.l[2] == tick1 + "2"
    assert fix.l[3] == tick1 + "3"
    #print(fix.l[0])
    #print(fix.l[1])
    #print(fix.l[2])
    #print(fix.l[3])


def test6_ImageExport_DBImage(fix):
    tick = "DBImage"
    fix.send_react(("CAM|" + camId + "|REC").encode("utf-8"))
    time.sleep(2)
    m = dt.datetime.now()
    tm = m.strftime("%Y%m%dT%H%M%S%Z")
    time.sleep(2)
    fix.send_react(("CAM|" + camId + "|REC_STOP").encode("utf-8"))
    time.sleep(3)

    DBstr = IdDB+":INSERT INTO public.image(image, tid) VALUES(?, '"+tid+"')"
    fix.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$"+tm+">,export_engine<sql>,export<"+DBstr+">,export_image<format$png;quality$85>,process<color:200,50,150;penwidth:10;rect:10,20,25,15;font:20;polygon:15,15,20,20>").encode("utf-8"))
    time.sleep(3)
    fix.search_in_callback(par="request_id")
    assert fix.p == tick
    fix.search_all_in_callback(par="objaction")
    assert fix.l[2] == "EXPORT_DONE"

    db = DbHelper(host="localhost", dbname="image", user="postgres", password="postgres")
    db.check_db()
    time.sleep(1)
    assert db.records != []
    time.sleep(1)
