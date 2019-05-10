from model.input_data import *

def test_delete_environment(fix):
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<IMAGE_EXPORT>,objid<"+objId+">").encode("utf-8"))
    fix.send_event(message=("CORE||DELETE_OBJECT|objtype<GRABBER>,objid<"+camId+">").encode("utf-8"))
