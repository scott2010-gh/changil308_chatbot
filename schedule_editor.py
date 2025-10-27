import tkinter as t
editor = t.Tk()
editor.title("일정 편집기")
editor.geometry('500x300')
global dr

#아래 경로를 일정이 저장될 json 파일 경로로 설정하시오
dr="/home/radxa/server-files/main/schedule_data.dat"
def edit(ymd,text):
    try:
        global dr
        data = open(dr,'r',encoding='UTF8')
        get = eval(data.readline())
        data.close()
        get[ymd]=text
        data = open(dr,'w',encoding='UTF8')
        data.write(str(get))
        data.close()
        print('success')
    except:
        print('err')

def remove(ymd):
    try:
        global dr
        data = open(dr,'r',encoding='UTF8')
        get = eval(data.readline())
        data.close()
        del get[ymd]
        data = open(dr,'w',encoding='UTF8')
        data.write(str(get))
        data.close()
        print('success')
    except:
        print('err')

def get():
    try:
        global dr
        data = open(dr,'r',encoding='UTF8')
        print(data.readline())
        data.close()
    except:
        print('err')

howto = t.Label(editor,text="- 날짜(YYYY/MM/DD)입력 후 내용 입력\n- 시험명은 중간/기말만 사용하며 반대로 입력")

ymd_input = t.Entry(editor)
text_input = t.Entry(editor)
ymd_input.place(x=190,y=100)
text_input.place(x=190,y=150)
apply = t.Button(editor,text="적용",command=lambda:edit(ymd_input.get(),text_input.get()))
apply.place(x=190,y=200)
getb = t.Button(editor,text="불러오기",command=get)
getb.place(x=235,y=200)
rb = t.Button(editor,text="제거",command=lambda:remove(ymd_input.get()))
rb.place(x=300,y=200)
howto.place(x=140,y=30)
editor.mainloop()
