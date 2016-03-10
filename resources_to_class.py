# -*- coding: utf-8 -*-
"""
    resources_to_class.py
    ~~~~~~~~~

    把项目中的图片资源生成一个 Objective-C 语言的 class,
    类中的方法名称会根据图片命名来定义 @2X 和 @3x 会同一个方法名.

    :copyright: (c) 2016 - 3 - 8 by taffy.
"""
import os


__RESOURCES_DIR__ =  '/Users/taffy/Project/Moblie/homura/homura/v3/v3Resources/'
__CLASS_DIR__ = '/Users/taffy/Project/Moblie/homura/homura/v3/V3Common/ScriptGenerating/'
__CLASS_NAME_H__ = 'HMRV3ResourceManager.h'
__CLASS_HEADER_H__ = '//\n//  HMRV3ResourceManager.h\n//  daily\n//\n//  Created by taffy on 16/3/8.\n//  Copyright © 2016年 Zhihu. All rights reserved.\n//\n\n'
__SUFIXX_FILE__ = '_Night'

def __write_to_class_interface(filename):
    __method_interface(filename)

def __filter_filename(name):

    # 过滤掉非图片的
    if name.endswith('png') == False and name.endswith('jpg') == False:
        return None

    # 过滤掉 @3x 的
    if '@3x' in name:
        return None

    # 过滤掉后缀是 __SUFIXX_FILE__ 的
    if __SUFIXX_FILE__ in name:
        return None


    str = name[:-4]

    if '@2x' in str:
        str = str[:-3]

    return str

def __method_interface(name):
    file_h.write('#define resource_' + name + ' GET_IMAGE('+ name +')\n')

def walk_dir(dir, file_h, topdown = True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            str = __filter_filename(name)
            if str != None:
                # 打印出没有夜间的图片
                if not (str + __SUFIXX_FILE__ + '@2x.png') in files or not (str + __SUFIXX_FILE__ + '.png') in files:
                    print(name)

                __write_to_class_interface(str)

file_h = open(__CLASS_DIR__ + __CLASS_NAME_H__, 'w')

file_h.write(__CLASS_HEADER_H__)
print('没有夜间的资源有:\n')
walk_dir(__RESOURCES_DIR__, file_h)
file_h.close()





