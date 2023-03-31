def fun():
    
    try:
        print("Mode 1 for continuous incremental Question numbers \nMode 2 for custom sequence of numbers ")
        init=int(input('MODE : '))
        return(init)
    except:
        fun()
def qnum():
    qnumber=[]
    mode=fun()

    if mode == 1:
        start=int(input("START: "))
        end=int(input("END : "))
        for i in range(start,end+1):
            qnumber.append(i)
        print(end='\r')
        print('press "ctrl + Space" to start \npress "space" to change to next question')
        return(qnumber)
    else:
        question_sequence=input("QUESTION SEQUENCE : ")
        question_sequence_processed=question_sequence.split(' ')
        try:
            if int(question_sequence_processed[-1])>0:
                for i in question_sequence_processed:
                    qnumber.append(int(i))
        except:
            del question_sequence_processed[-1]
            for i in question_sequence_processed:
                qnumber.append(int(i))
        print(end='\r')
        print('press "ctrl + Space" to start \npress "space" to change to next question')
        return(qnumber)