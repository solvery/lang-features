# -*- coding: utf-8 -*  
import serial  
import struct
import time  

config_head = [0x80, 0x81, 0x82, 0x83, 0x00]



#  COM3修改成您老的使用的串口 
ser = serial.Serial("COM3", 115200)  
def main():  
    int_num = 12
    osd_left    = 2
    osd_top     = 20
    osd_seg_height  = 400
    osd_seg_width   = 80 
    osd_alpha   = 0x80
    osd_num     = 0x27
    osd_r   = 0
    osd_g   = 0
    osd_b   = 0

    v1_clip_left      = 0
    v1_clip_top       = 0
    v1_clip_width     = 1920
    v1_clip_height    = 1080 
    v1_out_left       = 0
    v1_out_top        = 0
    v1_out_width      = 1920
    v1_out_height     = 1080
    v1_alpha          = 0xf0
    v1_scale_h        = 0x100
    v1_scale_v	      = 0x100

    v2_clip_left      = 0
    v2_clip_top       = 0
    v2_clip_width     = 1920
    v2_clip_height    = 1080 
    v2_out_left       = 0
    v2_out_top        = 0
    v2_out_width      = 1920
    v2_out_height     = 1080
    v2_alpha          = 0x80
    v2_scale_h        = 0x100
    v2_scale_v	      = 0x100

    background_r    = 0
    background_g    = 0
    background_b    = 0

    while True:  
        data_bin_array=''
        config_data = [\
            0x80, 0x81, 0x82, 0x83, 0x00, \
            osd_left/0x100, osd_left%0x100, \
            osd_top/0x100, osd_top%0x100, \
            osd_seg_height/0x100, osd_seg_height%0x100,\
            osd_seg_width/0x100, osd_seg_width%0x100,\
            osd_alpha,\
            int2bcd(int_num),\
            osd_r,\
            osd_g,\
            osd_b,\
            v1_clip_left/0x100, v1_clip_left%0x100,\
            v1_clip_top/0x100, v1_clip_top%0x100,\
            v1_clip_width/0x100, v1_clip_width%0x100,\
            v1_clip_height/0x100, v1_clip_height%0x100,\
            v1_out_left/0x100,   v1_out_left%0x100,\
            v1_out_top/0x100,    v1_out_top%0x100,\
            v1_out_width/0x100,  v1_out_width%0x100,\
            v1_out_height/0x100, v1_out_height%0x100,\
            v1_alpha,\
            v1_scale_h/0x100, v1_scale_h%0x100,\
            v1_scale_v/0x100, v1_scale_v%0x100,\
            v2_clip_left/0x100, v2_clip_left%0x100,\
            v2_clip_top/0x100, v2_clip_top%0x100,\
            v2_clip_width/0x100, v2_clip_width%0x100,\
            v2_clip_height/0x100, v2_clip_height%0x100,\
            v2_out_left/0x100,   v2_out_left%0x100,\
            v2_out_top/0x100,    v2_out_top%0x100,\
            v2_out_width/0x100,  v2_out_width%0x100,\
            v2_out_height/0x100, v2_out_height%0x100,\
            v2_alpha,\
            v2_scale_h/0x100, v2_scale_h%0x100,\
            v2_scale_v/0x100, v2_scale_v%0x100,\
            background_r,\
            background_g,\
            background_b\
        ]

        for data in config_data:
            data_bin = struct.pack('B', data) 
            data_bin_array = data_bin_array + data_bin[0]
        ser.write(data_bin_array)

        time.sleep(0.1)
        #raw_input()
        osd_left = osd_left + 1
        osd_top = osd_top + 1
        if (osd_left > 1200):
            osd_left = 0
        if (osd_top > 300):
            osd_top = 0
        if (osd_left%20 == 0):
            int_num =  int_num + 1


def int2bcd(a):
    return (a/10)*16+ (a%10 & 0x0f)
    pass
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


