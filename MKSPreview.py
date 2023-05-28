# Copyright (c) 2021
# MKS Plugin is released under the terms of the AGPLv3 or higher.
from UM.Application import Application
from cura.Snapshot import Snapshot
from PyQt6 import QtCore
from UM.Logger import Logger

from . import Constants

def add_leading_zeros(rgb):
    str_hex = "%x" % rgb
    str_hex_len = len(str_hex)
    if str_hex_len == 3:
        str_hex = '0' + str_hex[0:3]
    elif str_hex_len == 2:
        str_hex = '00' + str_hex[0:2]
    elif str_hex_len == 1:
        str_hex = '000' + str_hex[0:1]
    return str_hex

import os
from array import array
from ctypes import *
from UM.Platform import Platform
def add_screenshot_str(img, width, height, img_type):
    with open(r'D:\Desktop\N3\bin\new_size.txt', 'w') as f:
        f.write(f'w: {width}, h: {height}')
    if Platform.isOSX():
        pDll = CDLL(os.path.join(os.path.dirname(__file__), "libColPic.dylib"))
    elif Platform.isLinux():
        pDll = CDLL(os.path.join(os.path.dirname(__file__), "libColPic.so"))
    else:
        pDll = CDLL(os.path.join(os.path.dirname(__file__), "ColPic_X64.dll"))

    result = ""
    b_image = img.scaled(width, height, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
    img_size = b_image.size()
    color16 = array('H')
    try:
        # Logger.log("d", "try == ")
        for i in range(img_size.height()):
            for j in range(img_size.width()):
                pixel_color = b_image.pixelColor(j, i)
                r = pixel_color.red() >> 3
                g = pixel_color.green() >> 2
                b = pixel_color.blue() >> 3
                rgb = (r << 11) | (g << 5) | b
                color16.append(rgb)

        # int ColPic_EncodeStr(U16* fromcolor16, int picw, int pich, U8* outputdata, int outputmaxtsize, int colorsmax);
        fromcolor16 = color16.tobytes()
        outputdata = array('B',[0]*img_size.height()*img_size.width()).tobytes()
        resultInt = pDll.ColPic_EncodeStr(fromcolor16, img_size.height(), img_size.width(), outputdata, img_size.height()*img_size.width(), 1024)

        data0 = str(outputdata).replace('\\x00', '')
        data1 = data0[2:len(data0) - 2]
        eachMax = 1024 - 8 - 1
        maxline = int(len(data1)/eachMax)
        appendlen = eachMax - 3 - int(len(data1)%eachMax)

        for i in range(len(data1)):
            if i == maxline*eachMax:
                result += '\r;' + img_type + data1[i]
            elif i == 0:
                result += img_type + data1[i]
            elif i%eachMax == 0:
                result += '\r' + img_type + data1[i]
            else:
                result += data1[i]
        result += '\r;'
        for j in range(appendlen):
            result += '0'

    except Exception as e:
        Logger.log("d", "Exception == " + str(e))
    return result

def take_screenshot():
    cut_image = Snapshot.snapshot(width = 900, height = 900)
    return cut_image

def add_preview(self):
    application = Application.getInstance()

    scene = application.getController().getScene()

    global_container_stack = application.getGlobalContainerStack()
    if not global_container_stack:
        return

    # If the scene does not have a gcode, do nothing
    gcode_dict = getattr(scene, "gcode_dict", {})
    if not gcode_dict:  # this also checks for an empty dict
        Logger.log("w", "Scene has no gcode to process")
        return

    dict_changed = False

    processed_marker = ";MKSPREVIEWPROCESSED\n"

    image = take_screenshot()
    screenshot_string = ""
    simage = 0
    gimage = 0

    if image:
        meta_data = global_container_stack.getMetaData()
        Logger.log("d", "Get current preview settings.")
        if Constants.SIMAGE in meta_data:
            simage = int(global_container_stack.getMetaDataEntry(Constants.SIMAGE))
            Logger.log("d", "mks_simage value: " + str(simage))
            screenshot_string += add_screenshot_str(image, simage, simage, ";simage:")
        if Constants.GIMAGE in meta_data:
            gimage = int(global_container_stack.getMetaDataEntry(Constants.GIMAGE))
            Logger.log("d", "mks_gimage value: " + str(gimage))
            # ;; - needed for correct colors. do not remove them.
            screenshot_string += add_screenshot_str(image, gimage, gimage, ";;gimage:")
        screenshot_string += "\r"
    else:
        Logger.log("d", "Skipping adding screenshot")
        return
    
    for plate_id in gcode_dict:
        gcode_list = gcode_dict[plate_id]
        if len(gcode_list) < 2:
            Logger.log("w", "Plate %s does not contain any layers", plate_id)
            continue

        if processed_marker in gcode_list[0]:
            Logger.log("d", "Plate %s has already been processed", plate_id)
            continue

        # adding to header
        gcode_list[0] += processed_marker
        gcode_list[0] += "; Postprocessed by [MKS WiFi plugin](https://github.com/Jeredian/mks-wifi-plugin)\n"
        gcode_list[0] += "; simage=%d\n" % simage
        gcode_list[0] += "; gimage=%d\n" % gimage
        gcode_list[0] = screenshot_string + gcode_list[0]
        gcode_dict[plate_id] = gcode_list
        dict_changed = True

    if dict_changed:
        setattr(scene, "gcode_dict", gcode_dict)
