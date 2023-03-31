import time
import threading
import tkinter
import customtkinter
import qnum as qnum
class timmer:
    def __init__(self) :
        
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.app=customtkinter.CTk()
        self.app.geometry('1920x1080')
        self.app.title('LAPPER')
        self.question_sequence=qnum.qnum()
        self.qlen=len(self.question_sequence)
        self.question_sequence.append(00)
        self.start_flag=False
        self.index=0
        self.count=0
        self.time_stamp=[]
        

        self.end_flag=False
        self.kill=False

        self.qlabel=tkinter.Label(master=self.app,text='Q.NO : '+'xx',bg='#3a7ebf',font=("Arial",22))
        self.qlabel.place(relx=0.05,rely=0.05,anchor=tkinter.CENTER)

        self.label = tkinter.Label(master=self.app,bg='#3a7ebf', text=self.count,font=("Arial", 150))
        self.label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.button = customtkinter.CTkButton(master=self.app, text="SUBMIT", font=("Arial", 22),command=self.end,width=50,fg_color='transparent')
        self.button.place(anchor=tkinter.CENTER,relx=.93, rely=.9)

        self.app.bind("<Control-space>",lambda event:self.start_thread())
        self.app.bind("<space>",lambda event:self.lapper())

        
        self.app.mainloop()
    def start_thread(self):
        self.start_flag=True
        t1=threading.Thread(target=self.counter)

        t1.start()
    def counter(self):
        while self.start_flag is True and self.index<self.qlen and self.end_flag is False:
            time.sleep(1)
            self.count+=1
            if len(self.time_stamp)==0:
                timerunner1=self.count
                
                timerunner1_formated=str(divmod(timerunner1,60)[0])+':'+str(divmod(timerunner1,60)[1])




                q_formated1='Q.NO :{0:2d}'.format(self.question_sequence[self.index])
                self.qlabel.config(text=q_formated1,bg='#242424',fg='white')
                self.label.config(text=timerunner1_formated,bg='#242424',fg='white')
            else:

                timerunner=self.count-self.time_stamp[self.index-1]
                timerunner_formated=str(divmod(timerunner,60)[0])+':'+str(divmod(timerunner,60)[1])
                self.label.config(text=timerunner_formated,bg='#242424',fg='white')
                q_formated='Q.NO :{0:2d}'.format(self.question_sequence[self.index])
                self.qlabel.config(text=q_formated,bg='#242424',fg='white') 


        if self.index==self.qlen:

            self.end()
    def end(self):
        print('RESULT:')
        self.end_flag=True
        time.sleep(0.01)
        self.time_stamp.append(self.count)
        time_stamp_processed=[self.time_stamp[0]]

        for i in range(len(self.time_stamp)-1):

            time_stamp_processed.append(self.time_stamp[i+1]-self.time_stamp[i])



        if self.index<self.qlen:
            for i in range(self.index+1):
                print('{0:2d}         {1:4d}   {2:2d}:{3:2d}'.format(self.question_sequence[i],time_stamp_processed[i],divmod(time_stamp_processed[i],60)[0],divmod(time_stamp_processed[i],60)[1]))

        else:
             for i in range(self.index):
                print('{0:2d}         {1:4d}   {2:2d}:{3:2d}'.format(self.question_sequence[i],time_stamp_processed[i],divmod(time_stamp_processed[i],60)[0],divmod(time_stamp_processed[i],60)[1]))

        timeformater=str(divmod(divmod(self.count,60)[0],60)[0])+':'+str(divmod(divmod(self.count,60)[0],60)[1])+':'+str(divmod(self.count,60)[1])
        print('TOTAL TIME : ',timeformater)
        a=int(self.count/self.qlen)
        avg=str(divmod(a,60)[0])+':'+str(divmod(a,60)[1])
        print('AVG : ',avg)
        
        
    def lapper(self):
        if self.index<self.qlen and self.start_flag is True:
            self.time_stamp.append(self.count)
            self.index+=1

        
  



timmer()