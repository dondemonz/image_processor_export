from fixture.load_dll import DllHelper
from fixture.work_with_db import DbHelper
from fixture.react import ReactHelper
from model.input_data import *
import pytest
import os
import time
import winreg
import shutil


@pytest.fixture(scope="session", autouse=True)
def fix_dll(request):
    fixture = DllHelper()
    # функция disconnect передается в качестве параметра
    request.addfinalizer(fixture.disconnect)
    return fixture

@pytest.fixture(scope="session")
def file_name():
    return file_name


@pytest.fixture(scope="session")
def fix_react():
    fixture = ReactHelper()
    #request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture(scope="session")
def fix_db(request):
    fixture = DbHelper(host="localhost", user="postgres", password="postgres")
    def fin():
        fixture.drop_db()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture(scope="session", autouse=True)
def fix2(request):
    # Должен быть создан интерфейс iidk
    # Должен быть пользователь с полными правами
    fix = DllHelper()
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<IMAGE_EXPORT>,objid<" + objId + ">,parent_id<" + slave + ">,name<Test_Image_Processor>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<GRABBER>,objid<" + camId + ">,parent_id<" + slave + ">,name<" + camName + ">,type<Virtual>,chan<01>").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<CAM>,objid<" + camId + ">,parent_id<" + camId + ">,name<" + camName + ">").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<DATABASE>,objid<" + IdDB + ">,name<" + IdDB + ">").encode("utf-8"))
    fix.send_event(message=("CORE||CREATE_OBJECT|objtype<DATABASE>,objid<1>,parent_id<1>,name<1>,dbname<image>,user<postgres>,pass<@iss	EDJPCALGCEPGMCDJAFCEEHIJDDFANJGE>").encode("utf-8"))


    # создание папки для экспорта тестов cam_get_cam_image
    if not os.path.exists("C:\\TEST\\"):
        os.mkdir("C:\\TEST\\")
        print("Directory ", "C:\\TEST\\", " Created ")
    else:
        print("Directory ", "C:\\TEST\\", " already exists")
    time.sleep(5)
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, registrpath)
    winreg.SetValueEx(key, 'downloadTimeout', 0, winreg.REG_SZ, '6')
    print('\nSome recource')

    def fin():
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<IMAGE_EXPORT>,objid<" + objId + ">").encode("utf-8"))
        fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<" + camId + ">").encode("utf-8"))
        shutil.rmtree(str(dir))
        #db = DbHelper(host="localhost", dbname="image", user="postgres", password="postgres")
        #db.clean_db()
        print('\nSome resource fin')
        fix.disconnect()
    request.addfinalizer(fin)
    return request