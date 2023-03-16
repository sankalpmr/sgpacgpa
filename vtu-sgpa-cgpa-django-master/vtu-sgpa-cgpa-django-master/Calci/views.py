from django.shortcuts import render 

def gradepoints(mark):     #to find the gradepoints
    gp=0
    if(mark>=90):
        gp=10
    elif(mark>=80 and mark<90):
        gp=9
    elif(mark>=70 and mark<80):
        gp=8
    elif(mark>=60 and mark<70):
        gp=7
    elif(mark>=45 and mark<60):
        gp=6
    elif(mark>=40 and mark<45):
        gp=4
    else:
        gp=0
    return gp
    
def mypage(request):#ask sgpa or cgpa 
    return render(request,"cgpaorsgpa.html")

def sems(request):#render sgpa page
    return render(request,"sem.html")

def about(request):#render about page
    return render(request,"about.html")

def cgpa(request):#to find the cgpa
    finalans=0
    i=0
    try:
        s1=int(request.GET['sem1'])
        s2=int(request.GET['sem2'])
        s3=int(request.GET['sem3'])
        s4=int(request.GET['sem4'])
        s5=int(request.GET['sem5'])
        s6=int(request.GET['sem6'])
        s7=int(request.GET['sem7'])
        s8=int(request.GET['sem8'])
        if(s1>0):
            i=i+1
        if(s2>0):
            i=i+1
        if(s3>0):
            i=i+1
        if(s4>0):
            i=i+1
        if(s5>0):
            i=i+1
        if(s6>0):
            i=i+1
        if(s7>0):
            i=i+1
        if(s8>0):
            i=i+1
        finalans=(s1+s2+s3+s4+s5+s6+s7+s8)/i
    except:
        pass
    return render(request,"cgpa.html",{'output':finalans})

def sem1(request):#sem1 sgpa
    sum=0
    a1=0
    a2=0
    a3=0
    a4=0
    a4=0
    a5=0
    a6=0
    a7=0
    a8=0
    try:
        s1= int(request.GET['s1'] )
        s2= int(request.GET['s2'] )
        s3= int(request.GET['s3'] )
        s4= int(request.GET['s4'] )
        s5= int(request.GET['s5'] )
        s6= int(request.GET['s6'] )
        s7= int(request.GET['s7'] )
        s8= int(request.GET['s8'] )
        a1=gradepoints(s1)
        a2=gradepoints(s2)
        a3=gradepoints(s3)
        a4=gradepoints(s4)
        a5=gradepoints(s5)
        a6=gradepoints(s6)
        a7=gradepoints(s7)
        a8=gradepoints(s8)
        sum=((a1*4)+(a2*4)+(a3*3)+(a4*3)+(a5*3)+(a6*1)+(a7*1)+(a8*1))/20 
    except:
        pass
    return render(request,'sem1.html' , {'r1':sum})

def sem2(request):
    sum=0
    a1=0
    a2=0
    a3=0
    a4=0
    a4=0
    a5=0
    a6=0
    a7=0
    a8=0
    try:
        s1= int(request.GET['s1'] )
        s2= int(request.GET['s2'] )
        s3= int(request.GET['s3'] )
        s4= int(request.GET['s4'] )
        s5= int(request.GET['s5'] )
        s6= int(request.GET['s6'] )
        s7= int(request.GET['s7'] )
        s8= int(request.GET['s8'] )
        a1=gradepoints(s1)
        a2=gradepoints(s2)
        a3=gradepoints(s3)
        a4=gradepoints(s4)
        a5=gradepoints(s5)
        a6=gradepoints(s6)
        a7=gradepoints(s7)
        a8=gradepoints(s8)
        sum=((a1*4)+(a2*4)+(a3*3)+(a4*3)+(a5*3)+(a6*1)+(a7*1)+(a8*1))/20 
    except:
        pass
    return render(request,'sem2.html' , {'r2':sum})

def sem3(request):
    sum=0
    a1=0
    a2=0
    a3=0
    a4=0
    a4=0
    a5=0
    a6=0
    a7=0
    a8=0
    a9=0
    try:
        s1= int(request.GET['s1'] )
        s2= int(request.GET['s2'] )
        s3= int(request.GET['s3'] )
        s4= int(request.GET['s4'] )
        s5= int(request.GET['s5'] )
        s6= int(request.GET['s6'] )
        s7= int(request.GET['s7'] )
        s8= int(request.GET['s8'] )
        s9= int(request.GET['s9'] )
        a1=gradepoints(s1)
        a2=gradepoints(s2)
        a3=gradepoints(s3)
        a4=gradepoints(s4)
        a5=gradepoints(s5)
        a6=gradepoints(s6)
        a7=gradepoints(s7)
        a8=gradepoints(s8)
        a9=gradepoints(s9)
        sum=((a1*3)+(a2*4)+(a3*4)+(a4*3)+(a5*3)+(a6*3)+(a7*2)+(a8*2)+(a9*1))/25  
    except:
        pass
    return render(request,'sem3.html' , {'r3':sum})

def sem4(request):
    sum=0
    a1=0
    a2=0
    a3=0
    a4=0
    a4=0
    a5=0
    a6=0
    a7=0
    a8=0
    a9=0
    try:
        s1= int(request.GET['s1'] )
        s2= int(request.GET['s2'] )
        s3= int(request.GET['s3'] )
        s4= int(request.GET['s4'] )
        s5= int(request.GET['s5'] )
        s6= int(request.GET['s6'] )
        s7= int(request.GET['s7'] )
        s8= int(request.GET['s8'] )
        s9= int(request.GET['s9'] )
        a1=gradepoints(s1)
        a2=gradepoints(s2)
        a3=gradepoints(s3)
        a4=gradepoints(s4)
        a5=gradepoints(s5)
        a6=gradepoints(s6)
        a7=gradepoints(s7)
        a8=gradepoints(s8)
        a9=gradepoints(s9)
        sum=((a1*3)+(a2*4)+(a3*3)+(a4*3)+(a5*3)+(a6*3)+(a7*2)+(a8*2)+(a9*1))/25  
    except:
        pass
    return render(request,'sem4.html' , {'r4':sum})

def sem5(request):
    sum=0
    a1=0
    a2=0
    a3=0
    a4=0
    a4=0
    a5=0
    a6=0
    a7=0
    a8=0
    a9=0
    try:
        s1= int(request.GET['s1'] )
        s2= int(request.GET['s2'] )
        s3= int(request.GET['s3'] )
        s4= int(request.GET['s4'] )
        s5= int(request.GET['s5'] )
        s6= int(request.GET['s6'] )
        s7= int(request.GET['s7'] )
        s8= int(request.GET['s8'] )
        s9= int(request.GET['s9'] )
        a1=gradepoints(s1)
        a2=gradepoints(s2)
        a3=gradepoints(s3)
        a4=gradepoints(s4)
        a5=gradepoints(s5)
        a6=gradepoints(s6)
        a7=gradepoints(s7)
        a8=gradepoints(s8)
        a9=gradepoints(s9)
        sum=((a1*3)+(a2*4)+(a3*4)+(a4*3)+(a5*3)+(a6*3)+(a7*2)+(a8*2)+(a9*1))/25  
    except:
        pass
    return render(request,'sem5.html' , {'r5':sum})

def sem6(request):
    sum=0
    a1=0
    a2=0
    a3=0
    a4=0
    a4=0
    a5=0
    a6=0
    a7=0
    a8=0
    try:
        s1= int(request.GET['s1'] )
        s2= int(request.GET['s2'] )
        s3= int(request.GET['s3'] )
        s4= int(request.GET['s4'] )
        s5= int(request.GET['s5'] )
        s6= int(request.GET['s6'] )
        s7= int(request.GET['s7'] )
        s8= int(request.GET['s8'] )
        a1=gradepoints(s1)
        a2=gradepoints(s2)
        a3=gradepoints(s3)
        a4=gradepoints(s4)
        a5=gradepoints(s5)
        a6=gradepoints(s6)
        a7=gradepoints(s7)
        a8=gradepoints(s8)
        sum=((a1*4)+(a2*4)+(a3*4)+(a4*3)+(a5*3)+(a6*2)+(a7*2)+(a8*2))/24 
    except:
        pass
    return render(request,'sem6.html' , {'r6':sum})

def sem7(request):
    sum=0
    a1=0
    a2=0
    a3=0
    a4=0
    a4=0
    a5=0
    a6=0
    a7=0
    try:
        s1= int(request.GET['s1'] )
        s2= int(request.GET['s2'] )
        s3= int(request.GET['s3'] )
        s4= int(request.GET['s4'] )
        s5= int(request.GET['s5'] )
        s6= int(request.GET['s6'] )
        s7= int(request.GET['s7'] )
        a1=gradepoints(s1)
        a2=gradepoints(s2)
        a3=gradepoints(s3)
        a4=gradepoints(s4)
        a5=gradepoints(s5)
        a6=gradepoints(s6)
        a7=gradepoints(s7)
        sum=((a1*4)+(a2*4)+(a3*3)+(a4*3)+(a5*3)+(a6*2)+(a7*1))/20 
    except:
        pass
    return render(request,'sem7.html' , {'r7':sum})

def sem8(request):
    sum=0
    a1=0
    a2=0
    a3=0
    a4=0
    a4=0
    a5=0
    try:
        s1= int(request.GET['s1'] )
        s2= int(request.GET['s2'] )
        s3= int(request.GET['s3'] )
        s4= int(request.GET['s4'] )
        s5= int(request.GET['s5'] )
        a1=gradepoints(s1)
        a2=gradepoints(s2)
        a3=gradepoints(s3)
        a4=gradepoints(s4)
        a5=gradepoints(s5)
        sum=((a1*3)+(a2*3)+(a3*8)+(a4*1)+(a5*3))/18  
    except:
        pass
    return render(request,'sem8.html' , {'r8':sum})   