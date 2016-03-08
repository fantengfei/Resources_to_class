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
__CLASS_DIR__ = '/Users/taffy/Project/Moblie/homura/homura/v3/V3Common/Utility/'

__CLASS_NAME_M__ = 'HMRV3ResourceManager.m'
__CLASS_NAME_H__ = 'HMRV3ResourceManager.h'

__CLASS_HEADER_M__ = '//\n//  HMRV3ResourceManager.m\n//  daily\n//\n//  Created by taffy on 16/3/8.\n//  Copyright © 2016年 Zhihu. All rights reserved.\n//\n\n#import "HMRV3ResourceManager.h"\n\n@implementation HMRV3ResourceManager\n\n'
__CLASS_HEADER_H__ = '//\n//  HMRV3ResourceManager.h\n//  daily\n//\n//  Created by taffy on 16/3/8.\n//  Copyright © 2016年 Zhihu. All rights reserved.\n//\n\n#import <Foundation/Foundation.h>\n\n@interface HMRV3ResourceManager : NSObject\n\n'
__CLASS_END__ = '\n\n@end'

__SUFIXX_FILE__ = '_Night'

# + (NSString *)test;
# + (NSString *)test {
#   return @"xxxxxx";
# }

def __write_to_class_interface(filename):
    __method_interface(filename)

def __write_to_class_implementation(filename):
    __method_implementation(filename)

def __filter_filename(name):

    # 过滤掉非图片的
    if name.endswith('png') == False:
        return None

    # 过滤掉 @3x 的
    if '@3x' in name:
        return None

    # 过滤掉后缀是 __SUFIXX_FILE__ 的
    if __SUFIXX_FILE__ in name:
        return None

    # 把开头字母是数字的添加 '_'
    if name[0:1].isdigit():
        name = '_' + name

    str = name[:-4]

    if '@2x' in str:
        str = str[:-3]

    return str

def __method_interface(name):
    file_h.write('+ (UIImage *)' + name + ';\n')

def __method_implementation(name):
    file_m.write('+ (UIImage *)'+ name + ' {\n   return GET_IMAGE('+name+');\n}\n\n')


def walk_dir(dir, file_m, file_h, topdown = True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            str = __filter_filename(name)
            if str != None:
                # 打印出没有夜间的图片
                if not (str + __SUFIXX_FILE__ + '@2x.png') in files or not (str + __SUFIXX_FILE__ + '.png') in files:
                    print(name)

                __write_to_class_interface(str)
                __write_to_class_implementation(str)

file_m = open(__CLASS_DIR__ + __CLASS_NAME_M__,'w')
file_h = open(__CLASS_DIR__ + __CLASS_NAME_H__, 'w')

file_m.write(__CLASS_HEADER_M__)
file_h.write(__CLASS_HEADER_H__)

print('没有夜间的资源有:\n')
walk_dir(__RESOURCES_DIR__, file_m, file_h)

file_m.write(__CLASS_END__)
file_h.write(__CLASS_END__)

file_m.close()
file_h.close()





