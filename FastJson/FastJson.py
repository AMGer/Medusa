#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#改漏洞无特定的URL位置，可能是不通主键不同的URL
#里面的URL应该改为不处理，传入什么就打，或者跑全目录打
from FastJson import FastjsonDeserializationRemoteCodeExecutionVulnerability
from FastJson import FastjsonDeserializationRemoteCodeExecutionVulnerability2
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(FastjsonDeserializationRemoteCodeExecutionVulnerability.medusa, Url, Values, UnixTimestamp)
    ThreadPool.Append(FastjsonDeserializationRemoteCodeExecutionVulnerability2.medusa, Url, Values, UnixTimestamp)
    Prompt("FastJson")

