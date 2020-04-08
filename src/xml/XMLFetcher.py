#!/usr/bin/python3
# Author: Chunk

from xml.dom.minidom import parse
import xml.dom.minidom

workBench_XML_path = ""

if __name__ == '__main__':
    DOMTree = xml.dom.minidom.parse("/home/caikun/PycharmProjects/codeExecutor/src/resource/connection.xml")
    collection = DOMTree.documentElement
    if collection.hasAttribute("grt_format"):
        print("Root element : %s" % collection.getAttribute("grt_format"))
        movies = collection.getElementsBy
    print("====over===========")
