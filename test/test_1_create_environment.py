# Должен быть создан интерфейс iidk
# Должен быть пользователь с полными правами

from model.input_data import *
import os
import time
import winreg


def test_create_environment(fix):
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<IMAGE_EXPORT>,objid<"+objId+">,parent_id<"+slave+">,name<Test_Image_Processor>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + camId + ">,parent_id<" + slave + ">,name<" + camName + ">,type<Virtual>,chan<01>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + camId + ">,parent_id<" + camId + ">,name<" + camName + ">").encode("utf-8"))
    #fix.send_event(message=("CORE||CREATE_OBJECT|objtype<DATABASE>,objid<" + IdDB + ">,parent_id<" + camId + ">,name<" + camName + ">").encode("utf-8"))
    #fix.send_event(message=("CORE||CREATE_OBJECT|objtype<DATABASE>,objid<1>,parent_id<1>,name<1>").encode("utf-8"))

    #создание папки для экспорта тестов cam_get_cam_image
    if not os.path.exists("C:\\TEST\\"):
        os.mkdir("C:\\TEST\\")
        print("Directory ", "C:\\TEST\\", " Created ")
    else:
        print("Directory ", "C:\\TEST\\", " already exists")
    time.sleep(5)

def test_create_key_and_pareams():   # изменяет параемтр в реестре, после теста в restapi. на downloadTImeout 5 т.к. с 2 иногда не проходит тест
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, registrpath)
    winreg.SetValueEx(key, 'downloadTimeout', 0, winreg.REG_SZ, '4')

