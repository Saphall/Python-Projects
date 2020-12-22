from tkinter import *
import requests
import json

root=Tk()
root.title('Weather app')
root.geometry('480x100')

#create zipcode lookup funciton:
def ziplookup():
    #zip.get()
    #ziplabel=Label(root,text=zip.get())
    #ziplabel.grid(row=1,column=0,columnspan=2)


    try:
        api_request=requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+zip.get()+'&distance=5&API_KEY=BD63D7FF-3FFB-4669-A8B0-9F13A29DC250')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality= api[0]["AQI"]
        category= api[0]['Category']["Name"]

        if category=='Good':
            weather_color='#0C0'
        elif category=='Moderate':
            weather_color='#FFFF00'
        elif category=='Unhealthy for Sensitive Groups':
            weather_color='#ff9900'
        elif category=='Unhealthy':
            weather_color='#FF0000'
        elif category=='Very Unhealthy':
            weather_color='#990066'
        elif category=='Hazardous':
            weather_color='#660000'

        root.configure(background=weather_color)

        my_label=Label(root,text=city + ' ' +'Air-quality:'+str(quality)+' '+ category,font=("Helvetica",20),background=weather_color)
        my_label.grid(row=1,column=0,columnspan=2)
    except Exception as e:
        api = "Error..."



zip=Entry(root)
zip.grid(row=0,column=0,stick=W+E+N+S)

zipButton=Button(root,text="Check Zipcode",command=ziplookup)
zipButton.grid(row=0,column=1,stick=W+E+N+S)
root.mainloop()
