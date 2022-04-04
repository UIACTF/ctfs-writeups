# Milking The Stream
>There is a rumor going around saying that there is a new APT stemming out of Rochester that uses the Broadband-Hamnet to send messages around the world. Is there anyway you can pull their messages out of this file for me?
>
In this task we are given a `.waw` file wich just sounds like noise. The first thing I do for audio files like this is to open them in audacity. 
![signal](https://user-images.githubusercontent.com/91279257/161536846-f43be639-9702-4bc6-b2a8-78db879d6ffa.png)
However not much interesting is revealed, the sound does remind of radio noise, so the next step is to fire up Universal Radio Hacker (https://github.com/jopohl/urh).<br><br>
Once here I like to let it autodetect parameters as its better at recognizing signal data then me. Now after doing this we can see some data is recognized, but its all nonsense. But the spectogram does look interesting.
![urh1](https://user-images.githubusercontent.com/91279257/161536848-3045a33e-5ce7-4ebd-abd9-979b9cc60bc0.png)
Now if we play with the FFT Window size and Data_min, Data_max and the zoom we get this:
![urh2](https://user-images.githubusercontent.com/91279257/161536852-730d8754-087f-49a9-b7f6-ecc9cec836df.png)
And the flag: **RS{YAAAA_BABY}**
