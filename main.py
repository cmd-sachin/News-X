import random
import speech_recognition as sr
import sounddevice
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import datetime as dt
from tkinter import *
from tkinter import  ttk
from tkinter import messagebox
from playsound3 import playsound
import webbrowser
from PIL import ImageTk,Image
import smtplib
import subprocess

colors=["#99BC85","#F2F597","#000000","#86A7FC","#7FC7D9","#DC84F3","#304D30","#FFAD84","#E7BCDE","#B99470","#FEFAE0","#265073","#9ADE7B","#FF4B91","#F3D7CA"]
recognizer = sr.Recognizer()


def help():
    subprocess.run(["open","/Users/DELL/Desktop/DAILY NEWS READER/DOCUMENTATION.pdf"])
def mail_window():
    global var,ns,email_,na
    win=Toplevel()
    win.geometry("1880x1315")
    win.title("Mail Service")
    b=PhotoImage(file="mail_bg.png")
    background=Label(win,image=b)
    background.place(relwidth=1,relheight=1)
    label_1=Label(win,text="NAME",font=("Cosmic Sans MS",25,'bold'),fg="#40A2D8",bg="#365486")
    label_1.place(x=500,y=200)

    na = StringVar()
    n=Entry(win,width=25,bg="#365486",font=("Cosmic Sans MS",28,'bold'),textvariable=na)
    n.place(x=600, y=200)

    var=IntVar()
    ENG=Radiobutton(win,text="ENGLISH",variable=var,value=1,font=("Cosmic Sans MS",25,'normal'),fg="#40A2D8",bg="#365486").place(x=500,y=300)
    TAM=Radiobutton(win,text="TAMIL",variable=var,value=2,font=("Cosmic Sans MS",25,'normal'),fg="#40A2D8",bg="#365486").place(x=500,y=350)
    KAN=Radiobutton(win,text="KANNADA", variable=var, value=3,font=("Cosmic Sans MS",25,'normal'),fg="#40A2D8",bg="#365486").place(x=500,y=400)
    HIN=Radiobutton(win,text="HINDI",variable=var,value=4,font=("Cosmic Sans MS",25,'normal'),fg="#40A2D8",bg="#365486").place(x=500,y=450)
    MAL=Radiobutton(win,text="MALAYALAM",variable=var,value=5,font=("Cosmic Sans MS",25,'normal'),fg="#40A2D8",bg="#365486").place(x=500,y=500)


    label_2 = Label(win, text="CHOOSE OPTIONS", font=("Cosmic Sans MS", 25, 'bold'), fg="#40A2D8", bg="#365486")
    label_2.place(x=500, y=600)

    ns = StringVar()
    news_spec = ttk.Combobox(win, width=25, textvariable=ns)
    news_spec['values'] = (' National News (ENG)',
                              ' World News (ENG)',
                              ' Sports News (ENG)',
                              ' Opinions (ENG)',
                              ' National News (TAMIL)',
                              ' World News (TAMIL)',
                              ' Sports News (TAMIL)',
                              ' State News (TAMIL)',
                              ' National News (HINDI)',
                              ' World News (HINDI)',
                              ' Sports News (HINDI)',
                              ' National News (KANNADA)',
                              ' World News (KANNADA)',
                              ' Sports News (KANNADA)',
                              ' State News (KANNADA)',
                              ' National News (MALAYALAM)',
                              ' World News (MALAYALAM)',
                              ' Sports News (MALAYALAM)',
                              ' State News (MALAYALAM)')

    news_spec.place(x=750, y=605)
    news_spec.current()

    label_3 = Label(win, text="E-Mail Address", font=("Cosmic Sans MS", 25, 'bold'), fg="#40A2D8", bg="#365486")
    label_3.place(x=500, y=650)

    email_=StringVar()
    e = Entry(win, width=25, bg="#365486", font=("Cosmic Sans MS", 28, 'bold'),textvariable=email_)
    e.place(x=700,y=650)

    submit = Button(win, text="SUBMIT",command=win.destroy, relief="flat", bd=0)
    submit.place(x=800, y=900)
    win.mainloop()
    send_mail()

def send_mail():
    global content
    lang_list=["english","tamil","kannada","hindi","malayalam"]
    to= email_.get()
    spec = ns.get().lower()
    lang = lang_list[int(var.get())-1]
    print(to)
    print(spec)
    print(lang)
    if lang == "english":
        if "national" in spec:
            content = eng_get_news(url="https://www.thehindu.com/news/national/")

        elif "world" in spec:
            content = eng_get_news(url='https://www.thehindu.com/news/international/')
        elif "sports" in spec:
            content = eng_get_news(url="https://www.thehindu.com/sport/")
        elif "opinions" in spec:
            content = eng_get_news(url="https://www.thehindu.com/opinion/")

    elif lang == "tamil":
        if "national" in spec:
            content = tamil_get_news(url="https://www.dailythanthi.com/News/India")
        elif "world" in spec:
            content = tamil_get_news(url='https://www.dailythanthi.com/News/World')
        elif "sports" in spec:
            content = tamil_get_news(url="https://www.dailythanthi.com/sports")
        elif "state" in spec:
            content = tamil_get_news(url='https://www.dailythanthi.com/News/State')

    elif lang == "kannada":
        if "national" in spec:
            content = kan_get_news('https://kannada.news18.com/national-international/',"jsx-bcef60bca6506e85 hd")
        elif "world" in spec:
            content = kan_get_news('https://kannada.news18.com/tag/world-news/',"jsx-2436636446 hd")
        elif "sports" in spec:
            content = kan_get_news('https://kannada.news18.com/sports/',"jsx-bcef60bca6506e85 hd")
        elif "state" in spec:
            content = kan_get_news('https://kannada.news18.com/state/',"jsx-bcef60bca6506e85 hd")

    elif lang == "hindi":
        if "national" in spec:
            content = kan_get_news("https://ndtv.in/india#pfrom=home-khabar_nav")
        elif "world" in spec:
            content = kan_get_news("https://ndtv.in/world-news")
        elif "sports" in spec:
            content = kan_get_news("https://ndtv.in/sports-news")

    elif lang == "malayalam":
        """if "national" in spec:
            content = m_get_news('https://kannada.news18.com/national-international/', "jsx-bcef60bca6506e85 hd")
        elif "world" in spec:
            content = m_get_news('https://kannada.news18.com/tag/world-news/', "jsx-2436636446 hd")
        elif "sports" in spec:
            content = m_get_news('https://kannada.news18.com/sports/', "jsx-bcef60bca6506e85 hd")
        elif "state" in spec:
            content = m_get_news('https://kannada.news18.com/state/', "jsx-bcef60bca6506e85 hd")"""

    message=f"Subject:Heyy {na.get()}\n\n"
    for i in content:
        message+="\t\t"
        message+=i
        message+="\n"

    connect=smtplib.SMTP(host="smtp.gmail.com",port=587)
    connect.starttls()
    connect.login(user="--",password="--")
    connect.sendmail(from_addr="--",to_addrs=to,msg=message)
    connect.close()
    messagebox.showinfo(title="Mail",message=f"Mail Sent To {to}")


def record_audio(code_):
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    recognize_speech(audio,code_)

def recognize_speech(audio,code_):
    try:
        text = recognizer.recognize_google(audio,language=code_)
        if text.lower() == "english":
            english_reader()
        elif text.lower() == "tamil":
            tamil_reader()
        elif text.lower() == "kannada":
            kannada_reader()
        elif text.lower() == "national news":
            e_national_news()
        elif text.lower() == "world news":
            e_world_news()
        elif text.lower() == "sports news":
            e_sports_news()
        elif text.lower() == "opinions":
            e_opinion()
        elif text == "மாநில செய்தி":
            t_state_news()
        elif text == "தேசிய செய்தி":
            t_national_news()
        elif text == "உலக செய்தி":
            t_world_news()
        elif text == "விளையாட்டு செய்தி":
            t_sports_news()

    except:
        pass



def review():
    webbrowser.open("https://forms.gle/wFL5oMpHUg99q43g7")

#Tamil
def t_state_news():
    news = tamil_get_news('https://www.dailythanthi.com/News/State')
    news.insert(0,"மாநில செய்தி")
    tamil_news_reader(news)
def t_national_news():
    news = tamil_get_news('https://www.dailythanthi.com/News/India')
    news.insert(0,"தேசிய செய்தி")
    tamil_news_reader(news)
def t_sports_news():
    news = tamil_get_news('https://www.dailythanthi.com/sports')
    news.insert(0,"விளையாட்டு செய்தி")
    tamil_news_reader(news)
def t_world_news():
    news = tamil_get_news('https://www.dailythanthi.com/News/World')
    news.insert(0,"உலக செய்தி")
    tamil_news_reader(news)

#English
def e_national_news():
    news = eng_get_news("https://www.thehindu.com/news/national/")
    news.insert(0,"National News")
    eng_news_reader(news)
def e_world_news():
    news = eng_get_news("https://www.thehindu.com/news/international/")
    news.insert(0, "World News")
    eng_news_reader(news)
def e_sports_news():
    news = eng_get_news("https://www.thehindu.com/sport/")
    news.insert(0, "Sports News")
    eng_news_reader(news)
def e_opinion():
    news = eng_get_news("https://www.thehindu.com/opinion/")
    news.insert(0, "Opinions")
    eng_news_reader(news)

#Kannada
def k_state_news():
    news = kan_get_news('https://kannada.news18.com/state/',"jsx-bcef60bca6506e85 hd")
    news.insert(0,"ರಾಜ್ಯ ಸುದ್ದಿ")
    kannada_news_reader(news)
def k_national_news():
    news = kan_get_news('https://kannada.news18.com/national-international/',"jsx-bcef60bca6506e85 hd")
    news.insert(0,"ರಾಷ್ಟ್ರೀಯ ಸುದ್ದಿ")
    kannada_news_reader(news)
def k_sports_news():
    news = kan_get_news('https://kannada.news18.com/sports/',"jsx-bcef60bca6506e85 hd")
    news.insert(0,"ಕ್ರೀಡಾ ಸುದ್ದಿ")
    kannada_news_reader(news)
def k_world_news():
    news = kan_get_news('https://kannada.news18.com/tag/world-news/',"jsx-2436636446 hd")
    news.insert(0,"ವಿಶ್ವದ ಸುದ್ದಿ")
    kannada_news_reader(news)

def h_national_news():
    news = hindi_get_news("https://ndtv.in/india#pfrom=home-khabar_nav")
    news.insert(0,"राष्ट्रीय समाचार")
    hindi_news_reader(news)

def h_world_news():
    news = hindi_get_news("https://ndtv.in/world-news")
    news.insert(0,"विश्व समाचार")
    hindi_news_reader(news)

def h_sports_news():
    news = hindi_get_news("https://ndtv.in/sports-news")
    news.insert(0, "खेल समाचार")
    hindi_news_reader(news)

#Webscraping
def hindi_get_news(url):
    try:
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text,features="html.parser")
        data = soup.find_all(name="h2",class_="newsHdng")
        data_final = [i.find("a").text  for i in data]
        news = data_final
        news.append("धन्यवाद, शुभ दिन")
        return news
    except:
        playsound("error.mp3")
        messagebox.showerror(title="Error", message="Check Your Internet Connection")
        quit()


def kan_get_news(url,clas,n='div'):
    try:
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text,features="html.parser")
        data = soup.find_all(name=n,class_=clas)
        news = []
        for i in data:
            news.append(i.get_text())
        news.append("ಧನ್ಯವಾದಗಳು")
        return news
    except:
        playsound("error.mp3")
        messagebox.showerror(title="Error", message="Check Your Internet Connection")
        quit()
def eng_get_news(url):
    try:
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text,features="html.parser")
        data = soup.find_all(name="h3",class_="title")
        news = []
        for i in data:
            news.append(i.get_text())
        news.append("Thanks,Have a nice day.")
        return news
    except:
        playsound("error.mp3")
        messagebox.showerror(title="Error", message="Check Your Internet Connection")
        quit()
def tamil_get_news(url):
    try:
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, features="html.parser")
        data = soup.find_all(name="h3")[:-3]
        news = []
        for i in data:
            news.append(i.get_text())
        return news
    except:
        playsound("error.mp3")
        messagebox.showerror(title="Error",message="Check Your Internet Connection")
        quit()

#gtts readers

def hindi_news_reader(news):
    for i in news:
        voice = gTTS(text=i,lang="hi")
        voice.save("play.mp3")
        playsound("play.mp3")
def kannada_news_reader(news):
    news.append("ಓದಿದ್ದಕ್ಕಾಗಿ ಧನ್ಯವಾದಗಳು, ನಿಮ್ಮ ಹಾರ್ಸಾಕ್ ಡೆವಲಪರ್‌ಗಳು")
    for i in news:
        voice = gTTS(text=i,lang="kn")
        voice.save("play.mp3")
        playsound("play.mp3")
def eng_news_reader(news):
    for i in news:
        voice = gTTS(text=i)
        voice.save("play.mp3")
        playsound("play.mp3")

def tamil_news_reader(news):
    news.append("நன்றி, செய்திகள் வாசிப்பது , உங்கள் ஹார்சாக் டெவலப்பர்ஸ்")
    for i in news:
        voice = gTTS(text=i,lang="ta")
        voice.save("play.mp3")
        playsound("play.mp3")

#UI
def english_reader():
    playsound("english.mp3")
    record_audio(code_='en-IN')
    window = Toplevel()
    x = (1680 - 800) // 2
    y = (1115 - 600) // 2
    window.geometry(f"800x600+{x}+{y}")
    window.title("News Reader Bot")
    window.config(bg="#79AC78")
    window.resizable(height=None,width=None)

    # labels
    logo = PhotoImage(file="logo.png")
    title = Label(window, image=logo, bg="#79AC78")
    title.place(x=-30, y=-60)
    header = Label(window, text="News Reader", font=("Ubuntu", 20, "bold"), bg="#79AC78", fg="#B0D9B1")
    header.place(x=340, y=30)
    date = Label(window, text=str(dt.datetime.now().date()), font=("Ubuntu", 25, "bold"), bg="#79AC78", fg="#B0D9B1")
    date.place(x=580, y=30)
    # BUTTON IMAGES
    n = PhotoImage(file="NATIONAL NEWS.png")
    w = PhotoImage(file="WORLD NEWS.png")
    s = PhotoImage(file="SPORTS.png")
    o = PhotoImage(file="OPINIONS.png")

    button = Button(window, text="QUIT", width=10,
                    command=window.destroy)
    button.place(x=340, y=550)

    q = Label(window, text="Press ESC To Quit When Audio Is Not Playing", bg="#79AC78", font=("Stencil Std", 25, "bold"), fg="#B0D9B1")
    q.place(x=130, y=550)

    national = Button(window, image=n, highlightthickness=5, highlightbackground="#D0E7D2",
                      command=e_national_news)
    national.place(x=140, y=90)

    world = Button(window, image=w, highlightthickness=5, highlightbackground="#D0E7D2",
                   command=e_world_news)
    world.place(x=140, y=320)

    sports = Button(window, image=s, highlightthickness=5, highlightbackground="#D0E7D2",
                    command=e_sports_news)
    sports.place(x=460, y=90)

    opinion = Button(window, image=o, highlightthickness=5, highlightbackground="#D0E7D2", command=e_opinion)
    opinion.place(x=460, y=320)

    window.bind('<Escape>', lambda event: window.destroy())

    window.mainloop()
def tamil_reader():
    playsound("tamil.mp3")
    record_audio(code_="ta-IN")
    window = Toplevel()
    x = (1680 - 800) // 2
    y = (1115 - 600) // 2
    window.geometry(f"800x600+{x}+{y}")
    window.title("News Reader Bot")

    window.config(bg="#967de8")
    # labels
    logo = PhotoImage(file="logo.png")
    title = Label(window,image=logo, bg="#967de8")
    title.place(x=-30, y=-60)
    header = Label(window,text="News Reader", font=("Ubuntu", 20, "bold"), bg="#967de8",fg="#756AB6")
    header.place(x=340, y=30)
    date = Label(window,text=str(dt.datetime.now().date()), font=("Ubuntu", 25, "bold"), bg="#967de8",fg="#756AB6")
    date.place(x=580, y=30)
    # BUTTON IMAGES
    n = PhotoImage(file="t_national.png")
    w = PhotoImage(file="t_world.png")
    s = PhotoImage(file="t_state.png")
    sport = PhotoImage(file="t_sports.png")


    quit = Label(window,text="Press ESC To Quit When Audio Is Not Playing", bg="#967de8",
                 font=("Stencil Std", 25, "bold"), fg="#756AB6")
    quit.place(x=130, y=550)

    national = Button(window,image=n, highlightthickness=5, highlightcolor="#E0AED0",
                      command=t_national_news)
    national.place(x=140, y=90)

    world = Button(window,image=w, highlightthickness=5, highlightcolor="#E0AED0",
                   command=t_world_news)
    world.place(x=140, y=320)

    sports = Button(window,image=sport, highlightthickness=5, highlightcolor="#E0AED0",
                    command=t_sports_news)
    sports.place(x=460, y=90)

    state = Button(window,image=s, highlightthickness=5, highlightcolor="#E0AED0",command=t_state_news)
    state.place(x=460, y=320)

    window.bind('<Escape>', lambda event: window.destroy())
    window.mainloop()

def kannada_reader():
    window = Toplevel()
    window.title("News Reader Bot")
    x = (1680 - 800) // 2
    y = (1115 - 600) // 2
    window.geometry(f"800x600+{x}+{y}")

    window.config(bg="#C4DFDF")
    # labels
    logo = PhotoImage(file="logo.png")
    title = Label(window, image=logo, bg="#C4DFDF")
    title.place(x=-30, y=-60)
    header = Label(window, text="News Reader", font=("Ubuntu", 20, "bold"), bg="#C4DFDF", fg="#80BCBD")
    header.place(x=340, y=30)
    date = Label(window, text=str(dt.datetime.now().date()), font=("Ubuntu", 25, "bold"), bg="#C4DFDF", fg="#80BCBD")
    date.place(x=580, y=30)
    # BUTTON IMAGES
    n = PhotoImage(file="k_national.png")
    w = PhotoImage(file="k_world.png")
    s = PhotoImage(file="k_state.png")
    sport = PhotoImage(file="k_sports.png")


    quit = Label(window, text="Press ESC To Quit When Audio Is Not Playing", bg="#C4DFDF",
                 font=("Stencil Std", 25, "bold"), fg="#80BCBD")
    quit.place(x=130, y=550)

    national = Button(window, image=n, highlightthickness=5, highlightbackground="#92C7CF",
                      command=k_national_news)
    national.place(x=140, y=90)

    world = Button(window, image=w, highlightthickness=5, highlightbackground="#92C7CF",
                   command=k_world_news)
    world.place(x=140, y=320)

    sports = Button(window, image=sport, highlightthickness=5, highlightbackground="#92C7CF",
                    command=k_sports_news)
    sports.place(x=460, y=90)

    state = Button(window, image=s, highlightthickness=5, highlightbackground="#92C7CF", command=k_state_news)
    state.place(x=460, y=320)

    window.bind('<Escape>', lambda event: window.destroy())
    window.mainloop()

def hindi_reader():
    window = Toplevel()
    window.title("News Reader Bot")
    x = (1680 - 800) // 2
    y = (1115 - 600) // 2
    window.geometry(f"800x600+{x}+{y}")

    window.config(bg="#C4DFDF")
    # labels
    logo = PhotoImage(file="logo.png")
    title = Label(window, image=logo, bg="#C4DFDF")
    title.place(x=-30, y=-60)
    header = Label(window, text="News Reader", font=("Ubuntu", 20, "bold"), bg="#C4DFDF", fg="#80BCBD")
    header.place(x=340, y=30)
    date = Label(window, text=str(dt.datetime.now().date()), font=("Ubuntu", 25, "bold"), bg="#C4DFDF", fg="#80BCBD")
    date.place(x=580, y=30)
    # BUTTON IMAGES
    n = PhotoImage(file="h_national.png")
    w = PhotoImage(file="h_world.png")
    sport = PhotoImage(file="h_sports.png")


    quit = Label(window, text="Press ESC To Quit When Audio Is Not Playing", bg="#C4DFDF",
                 font=("Stencil Std", 25, "bold"), fg="#80BCBD")
    quit.place(x=130, y=550)

    national = Button(window, image=n, highlightthickness=5, highlightbackground="#92C7CF",
                      command=h_national_news)
    national.place(x=140, y=90)

    world = Button(window, image=w, highlightthickness=5, highlightbackground="#92C7CF",
                   command=h_world_news)
    world.place(x=460, y=90)

    sports = Button(window, image=sport, highlightthickness=5, highlightbackground="#92C7CF",
                    command=h_sports_news)
    sports.place(x=300, y=320)

    window.bind('<Escape>', lambda event: window.destroy())
    window.mainloop()

def home_win():
    global home
    home = Tk()
    home.title("NEWS READER")
    home.geometry('2880x1864')
#Menu Bar
    menubar = Menu(home, relief='ridge')
    home.config( menu=menubar)
    bg=PhotoImage(file="background.png")
    background_label = Label(home, image=bg)
    background_label.place(relwidth=1, relheight=1)
    file_menu=Menu(menubar,tearoff=0)
    mail_service=Menu(menubar,tearoff=0)

    menubar.add_cascade(label="File", font=("Cosmic Sans MS", 15, 'bold'),menu=file_menu)
    file_menu.add_command(label="Review",font=("Cosmic Sans MS", 15, 'bold'),command=review)
    file_menu.add_command(label="Help",font=("Cosmic Sans MS", 15, 'bold'),command=help)
    file_menu.add_command(label="Exit", font=("Cosmic Sans MS", 15, 'bold'), command=home.destroy)
    menubar.add_cascade(label="Mail Services",font=("Cosmic Sans MS", 15, 'bold'),menu=mail_service)
    mail_service.add_command(label="Mail News",font=("Cosmic Sans MS",15,'bold'),command=mail_window)

    ta = PhotoImage(file='Tamil.png')

    tamil = Button(home, image=ta, bg='#dfc9af', highlightbackground='#0a0908', highlightthickness=5, command=tamil_reader,relief="flat",bd=0)
    tamil.place(x=500,y=200)

    en = PhotoImage(file='English.png')
    english = Button(home, image=en, bg='#dfc9af', highlightbackground='#0a0908', highlightthickness=5, command=english_reader,relief="flat",bd=0)
    english.place(x=1000,y=200)

    ka = PhotoImage(file="kannada.png")
    kannada = Button(home,image=ka,bg='#dfc9af', highlightbackground='#0a0908', highlightthickness=5, command=kannada_reader,relief="flat",bd=0)
    kannada.place(x=500,y=600)

    hi = PhotoImage(file="hindi.png")
    hindi = Button(home, image=hi, bg='#dfc9af', highlightbackground='#0a0908', highlightthickness=5,command=hindi_reader, relief="flat", bd=0)
    hindi.place(x=1000, y=600)
    playsound("options.mp3")
    record_audio(code_='en-IN')

    home.mainloop()


home_win()




