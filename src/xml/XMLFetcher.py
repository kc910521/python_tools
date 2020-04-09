#!/usr/bin/python3
# Author: Chunk

import xml.etree.ElementTree as ET

workBench_XML_path = "/home/caikun/PycharmProjects/codeExecutor/src/resource/connection.xml"


def fetch_from_work_bench(path):
    arr = []
    tree = ET.parse(path)
    root = tree.getroot()
    for v in root.iter('value'):
        if 'hostIdentifier' == v.attrib.get('key'):
            print(v.text.split('@', 1)[1])
            arr.append(v.text.split('@', 1)[1])
    return arr


if __name__ == '__main__':
    print("====over===========")
