##import speech_recognition as sr
##
##r = sr.Recognizer()
##
##with sr.Microphone() as source:
##    print ('Say Something!')
##    audio = r.listen(source)
##    print ('Done!')
## 
##text = r.recognize_google(audio)
##
##print(text)
import speech_recognition as sr
 


sample_rate = 48000

chunk_size = 2048  #buffer size 


r = sr.Recognizer()
 

mic_list = sr.Microphone.list_microphone_names()

print(mic_list)
device_id = 1   #manually 



##for i, microphone_name in enumerate(mic_list):
##    if microphone_name == mic_name:
##        device_id = 1
 


with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                        chunk_size = chunk_size) as source:
  
    r.adjust_for_ambient_noise(source)
    print("Say Something")
    #listens for the user input
    audio = r.listen(source)
         
    try:
        text = r.recognize_google(audio)
        print("you said: " + text)
     
    
     
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
     
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
