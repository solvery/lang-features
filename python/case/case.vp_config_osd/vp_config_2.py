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
        config_data = [osd_left/0x100, osd_left%0x100]
        for data in config_head:
            data_bin = struct.pack('B', data) 
            data_bin_array = data_bin_array + data_bin[0]
        data_bin_array = data_bin_array + struct.pack('BB', osd_left/0x100, osd_left%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', osd_top/0x100, osd_top%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', osd_seg_height/0x100, osd_seg_height%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', osd_seg_width/0x100, osd_seg_width%0x100)
        data_bin_array = data_bin_array + struct.pack('B', osd_alpha)
        data_bin_array = data_bin_array + struct.pack('B', int2bcd(int_num))
        data_bin_array = data_bin_array + struct.pack('B', osd_r)
        data_bin_array = data_bin_array + struct.pack('B', osd_g)
        data_bin_array = data_bin_array + struct.pack('B', osd_b)

        data_bin_array = data_bin_array + struct.pack('BB', v1_clip_left/0x100, v1_clip_left%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v1_clip_top/0x100, v1_clip_top%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v1_clip_width/0x100, v1_clip_width%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v1_clip_height/0x100, v1_clip_height%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v1_out_left/0x100,   v1_out_left%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v1_out_top/0x100,    v1_out_top%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v1_out_width/0x100,  v1_out_width%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v1_out_height/0x100, v1_out_height%0x100)
        data_bin_array = data_bin_array + struct.pack('B', v1_alpha)
        data_bin_array = data_bin_array + struct.pack('BB', v1_scale_h/0x100, v1_scale_h%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v1_scale_v/0x100, v1_scale_v%0x100)

        data_bin_array = data_bin_array + struct.pack('BB', v2_clip_left/0x100, v2_clip_left%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v2_clip_top/0x100, v2_clip_top%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v2_clip_width/0x100, v2_clip_width%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v2_clip_height/0x100, v2_clip_height%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v2_out_left/0x100,   v2_out_left%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v2_out_top/0x100,    v2_out_top%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v2_out_width/0x100,  v2_out_width%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v2_out_height/0x100, v2_out_height%0x100)
        data_bin_array = data_bin_array + struct.pack('B', v2_alpha)
        data_bin_array = data_bin_array + struct.pack('BB', v2_scale_h/0x100, v2_scale_h%0x100)
        data_bin_array = data_bin_array + struct.pack('BB', v2_scale_v/0x100, v2_scale_v%0x100)

        data_bin_array = data_bin_array + struct.pack('B', background_r)
        data_bin_array = data_bin_array + struct.pack('B', background_g)
        data_bin_array = data_bin_array + struct.pack('B', background_b)

        ser.write(data_bin_array)
        ser.flushInput()  

        time.sleep(0.1)
        #raw_input()
        #int_num =  int_num + 1
        osd_left = osd_left + 1
        osd_top = osd_top + 1
        if (osd_left > 1200):
            osd_left = 0
        if (osd_top > 300):
            osd_top = 0


def int2bcd(a):
    return (a/10)*16+ (a%10 & 0x0f)
    pass
     
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  


