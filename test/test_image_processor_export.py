from model.input_data import *
import time


def test1_image_export_process_test(fix_dll, fix_react):
    tick = "process_test_"
    tm = fix_react.create_record_and_timestamp(fix_dll)
    fix_react.send_user_react(caption_data="15:ahaha test blabla \n phah testtest bla 123123111!!!", export_image_data="format$png;quality$85", process_data="color:200,50,150;penwidth:10;rect:10,20,25,15;crop:0,0,95,95;font:20;polygon:15,15,20,20,25,20,20,90,70,25,40,40,55,55;polyline:90,85,80,81,75,90,50,50;text:15,75,blabla test", tick=tick, tick1=tick, tm_name="time$", tm=tm, fix_dll=fix_dll, file_name="test1_")
    fix_dll.search_in_callback(par="request_id")
    time.sleep(7)
    assert fix_dll.p == tick


def test2_image_export_jpg_quality_low_test(fix_dll, fix_react):
    tick = "low_jpg_test_"
    tm = fix_react.create_record_and_timestamp(fix_dll)
    fix_react.send_user_react(caption_data="25:low jpg", export_image_data="format$jpg;quality$1", fix_dll=fix_dll, tick=tick, tick1=tick, tm_name="time$", tm=tm, file_name="test2_")
    time.sleep(5)
    fix_dll.search_in_callback(par="request_id")
    assert fix_dll.p == tick


def test3_image_export_jpg_quality_high_test(fix_dll, fix_react):
    tick = "high_jpg_test_"
    tm = fix_react.create_record_and_timestamp(fix_dll)
    fix_react.send_user_react(caption_data="25:high jpg", export_image_data="format$jpg;quality$100", fix_dll=fix_dll, tick=tick, tick1=tick, tm_name="time$", tm=tm, file_name="test3_")
    time.sleep(5)
    fix_dll.search_in_callback(par="request_id")
    assert fix_dll.p == tick
    time.sleep(2)

def test4_image_export_live_image(fix_dll, fix_react):
    time.sleep(2)
    tick = "liveImage_"
    fix_react.send_user_react(caption_data="25:live with twodim scale", export_image_data="format$jpg;quality$100", fix_dll=fix_dll, tick=tick, tick1=tick, tm_name="time$live", file_name="test4_", process_data="scale:400,400")
    time.sleep(5)
    fix_dll.search_in_callback(par="request_id")
    assert fix_dll.p == tick
    time.sleep(2)

def test5_image_export_arhive_and_live_image_task_in_a_row(fix_dll, fix_react):
    tick = "archive_"
    tick1 = "live_"
    tm = fix_react.create_record_and_timestamp(fix_dll)
    fix_react.send_user_react(caption_data="25:live", export_image_data="format$jpg;quality$100", fix_dll=fix_dll, tick=tick, tick1=tick,  tm_name="time$", tm=tm, file_name="test5_")
    time.sleep(2)
    fix_react.send_user_react(caption_data="25:live", export_image_data="format$jpg;quality$100", fix_dll=fix_dll, tick=tick1, tick1=tick1, tm_name="time$live", file_name="test5_")
    time.sleep(3)
    fix_react.send_user_react(caption_data="25:live2", export_image_data="format$jpg;quality$100", fix_dll=fix_dll, tick=tick1+"1", tick1=tick1+"1", tm_name="time$live", file_name="test5_")
    time.sleep(3)
    fix_react.send_user_react(caption_data="25:live3", export_image_data="format$jpg;quality$100", fix_dll=fix_dll, tick=tick1+"2", tick1=tick1+"2", tm_name="time$live", file_name="test5_")
    time.sleep(3)

    fix_dll.search_all_in_callback(par="request_id")
    assert fix_dll.l[0] == tick
    assert fix_dll.l[1] == tick1
    assert fix_dll.l[2] == tick1 + "1"
    assert fix_dll.l[3] == tick1 + "2"
    #print(fix.l[0])


def test6_ImageExport_DBImage(fix_dll, fix_react, fix_db):
    tick1 = "DBImage"
    db_str = IdDB + ":INSERT INTO public.image(image, tid) VALUES(?, '" + tid + "')"
    tm = fix_react.create_record_and_timestamp(fix_dll)
    fix_react.send_user_react(export_image_data="format$png;quality$85", fix_dll=fix_dll, tick1=tick1, tm_name="time$", tm=tm, fn=db_str, export_engine="sql", process_data="color:200,50,150;penwidth:10;rect:10,20,25,15;font:20;polygon:15,15,20,20", camId_n="", dir_n="", dir_d="")

    #fix_dll.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick + ">,import<cam$" + camId + ";time$" + tm + ">,export_engine<sql>,export<" + db_str + ">,export_image<format$png;quality$85>,process<color:200,50,150;penwidth:10;rect:10,20,25,15;font:20;polygon:15,15,20,20>").encode("utf-8"))
    time.sleep(3)
    fix_dll.search_in_callback(par="request_id")
    assert fix_dll.p == tick1
    fix_db.check_db()
    time.sleep(1)
    assert fix_db.records != [] and fix_db.records is not None
    time.sleep(1)


# оставлю как пример
# fix_dll.send_react(("IMAGE_EXPORT|" + objId + "|EXPORT|request_id<" + tick1 + "3>,import<cam$" + camId + ";time$live>,export_engine<file>,export<filename$test5_export_" + tick + "3_on_cam" + camId + ";dir$" + dir + ">,export_image<format$jpg;quality$100>,caption<25:live3>").encode("utf-8"))





