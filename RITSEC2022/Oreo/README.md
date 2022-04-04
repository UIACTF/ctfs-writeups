# Oreo
>yum, goes well with milk
>
Here we are given a tar with a lot of folders inside<br>
![folders](https://user-images.githubusercontent.com/91279257/161536212-00ae4eec-e6a1-43f3-8382-24ee9672da00.png)<br>
Now after looking a bit I find a file called Cookies, and considering the task title this file might be interesting and running strings on it gives this:<br>
![strings](https://user-images.githubusercontent.com/91279257/161536218-807a7d22-927c-405a-ab59-0b3e9a654fa7.png)<br>
This: `UlN7eXVteXVtX20xbGtfNGFuZF9jbzBraTNzX2Ywcl9kYXl6fQ==` looks like base64, so lets slap that into CyberChef
![chef](https://user-images.githubusercontent.com/91279257/161536219-512bde26-9f17-4c54-949a-79e83c321bc6.png)
There we have the flag: **RS{yumyum_m1lk_4and_co0ki3s_f0r_dayz}**


