from model.input_data import *
import shutil
from fixture.work_with_db import DbHelper

def test_delete_environment(fix):
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<IMAGE_EXPORT>,objid<"+objId+">").encode("utf-8"))
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<"+camId+">").encode("utf-8"))
    shutil.rmtree(str(dir))

def test_clean_db():
    db = DbHelper(host="localhost", dbname="image", user="postgres", password="postgres")
    db.clean_db()

