#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from acrosure_sdk import AcrosureClient

client = AcrosureClient("token1", "app1", "product1")
client.verify_signature('f84c04fbe06d1d1bd96cf99a00a3e304ae5185097be1c5a949587ed3a131814f', 'data ป')
import pdb; pdb.set_trace()
# client.application.call_api("fail")
# import pdb; pdb.set_trace()

print("END")
print("END")
print("END")
