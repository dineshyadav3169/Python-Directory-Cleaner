import os
import shutil
#input from user
input_file_path = input('Enter Directory Path :')
#file path join
pdf_join_path = os.path.join(input_file_path,'PDF')
video_join_path = os.path.join(input_file_path,'VIDEOS')
image_join_path = os.path.join(input_file_path,'IMAGES')
pptx_join_path = os.path.join(input_file_path,'PPT')
exe_join_path = os.path.join(input_file_path,'PROGRAM')
txt_join_path = os.path.join(input_file_path,'TEXT')

def pdf():
    location = os.listdir(input_file_path)
    len_location = len(location)
    for i in range(len_location):
        if 'pdf' in location[i]:
            file_name = location[i]
            total_file_path = os.path.join(input_file_path,file_name)
            total_new_file_path = os.path.join(pdf_join_path,file_name)
            shutil.move(total_file_path,total_new_file_path)


def mp4():
    location = os.listdir(input_file_path)
    len_location = len(location)
    for i in range(len_location):
        if 'mp4' in location[i]:
            file_name = location[i]
            total_file_path = os.path.join(input_file_path,file_name)
            total_new_file_path = os.path.join(video_join_path,file_name)
            shutil.move(total_file_path,total_new_file_path)

def mkv():
    location = os.listdir(input_file_path)
    len_location = len(location)
    for i in range(len_location):
        if 'mkv' in location[i]:
            file_name = location[i]
            total_file_path = os.path.join(input_file_path, file_name)
            total_new_file_path = os.path.join(video_join_path, file_name)
            shutil.move(total_file_path, total_new_file_path)

def jpg():
    location = os.listdir(input_file_path)
    len_location = len(location)
    for i in range(len_location):
        if 'jpg' in location[i]:
            file_name = location[i]
            total_file_path = os.path.join(input_file_path, file_name)
            total_new_file_path = os.path.join(image_join_path, file_name)
            shutil.move(total_file_path, total_new_file_path)

def jpeg():
    location = os.listdir(input_file_path)
    len_location = len(location)
    for i in range(len_location):
        if 'jpeg' in location[i]:
            file_name = location[i]
            total_file_path = os.path.join(input_file_path, file_name)
            total_new_file_path = os.path.join(image_join_path, file_name)
            shutil.move(total_file_path, total_new_file_path)

def png():
    location = os.listdir(input_file_path)
    len_location = len(location)
    for i in range(len_location):
        if 'png' in location[i]:
            file_name = location[i]
            total_file_path = os.path.join(input_file_path, file_name)
            total_new_file_path = os.path.join(image_join_path, file_name)
            shutil.move(total_file_path, total_new_file_path)

def pptx():
    location = os.listdir(input_file_path)
    len_location = len(location)
    for i in range(len_location):
        if 'pptx' in location[i]:
            file_name = location[i]
            total_file_path = os.path.join(input_file_path, file_name)
            total_new_file_path = os.path.join(pptx_join_path, file_name)
            shutil.move(total_file_path, total_new_file_path)

def exe():
    location = os.listdir(input_file_path)
    len_location = len(location)
    for i in range(len_location):
        if 'exe' in location[i]:
            file_name = location[i]
            total_file_path = os.path.join(input_file_path, file_name)
            total_new_file_path = os.path.join(exe_join_path, file_name)
            shutil.move(total_file_path, total_new_file_path)

def txt():
    location = os.listdir(input_file_path)
    len_location = len(location)
    for i in range(len_location):
        if 'txt' in location[i]:
            file_name = location[i]
            total_file_path = os.path.join(input_file_path,file_name)
            total_new_file_path = os.path.join(txt_join_path,file_name)
            shutil.move(total_file_path,total_new_file_path)


print('What do you want to move \n1.PDF   2.VIDEOS   3.IMAGES   4.PPTX   5.EXE   6.TEXT\n 0.All')
choice = int(input("Enter Your Choice Number :"))

def video_choice():
    if choice==2:
        check_Video_folder = os.path.exists(video_join_path)
        if check_Video_folder==False:
            os.makedirs(video_join_path)
            mp4()
            mkv()
        else:
            mp4()
            mkv()
    print('Done!!')
video_choice()
def image_choice():
    if choice==3:
        check_image_folder = os.path.exists(image_join_path)
        if check_image_folder==False:
            os.makedirs(image_join_path)
            jpeg()
            jpg()
            png()
        else:
            jpeg()
            jpg()
            png()
    print('Done!!')
image_choice()

def pdf_choice():
    if choice==1:
        check_pdf_folder = os.path.exists(pdf_join_path)
        if check_pdf_folder==False:
            os.makedirs(pdf_join_path)
            pdf()
        else:
            pdf()
    print('Done!!')
pdf_choice()

def pptx_choice():
    if choice==4:
        check_pptx_folder = os.path.exists(pptx_join_path)
        if check_pptx_folder == False:
            os.makedirs(pptx_join_path)
            pptx()
        else:
            pptx()
    print('Done!!')
pptx_choice()

def exe_choice():
    if choice==5:
        check_exe_folder = os.path.exists(exe_join_path)
        if check_exe_folder == False:
            os.makedirs(exe_join_path)
            exe()
        else:
            exe()
    print('Done!!')
exe_choice()

def txt_choice():
    if choice==6:
        check_txt_folder = os.path.exists(txt_join_path)
        if check_txt_folder == False:
            os.makedirs(txt_join_path)
            txt()
        else:
            txt()
    print('Done!!')
txt_choice()

if choice==0:
    for i in range(1,7):
        choice=i
        pdf_choice()
        video_choice()
        image_choice()
        pptx_choice()
        exe_choice()
        txt_choice()
    print("All Complete!!")