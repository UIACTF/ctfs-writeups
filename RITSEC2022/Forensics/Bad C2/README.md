# Bad C2
>Not very versatile malware
>
Here we are given a pcap file with 74 packets. All of them TCP and HTTP steams.
![wireshark1](https://user-images.githubusercontent.com/91279257/161536497-6e4907e8-0de7-42c1-9226-574e7ec0b5a4.png)<br>
What I like to do whenever there is HTTP packets is to look for a post request, because if you want to do something malicious you most likely have to send something to the site. To find all post reqiest we can apply this filter in wireshark: `http.request.method == "POST"`
![wireshark2](https://user-images.githubusercontent.com/91279257/161536501-d634bb63-389f-41f8-9250-a809934cc69a.png)<br>
This leves just one packet, now to see the content we can `Right Click > Follow > TCP Steam`
![tcpSteam](https://user-images.githubusercontent.com/91279257/161536502-a8960a3f-d95a-4f40-add2-c87cba7017aa.png)<br>
Here we can se someone sends `{"please": "false"}` to `maliciouspayload.delivery/get/secret` and the server answers `sorry, you didn't say please`. So from this we can gather that if we mabye send {"please": "true"} to the server it will give us the secret. Now you can do this in whatever web browser you want, but I beleve its easyest using the burpsuite repeater. All I have done here is to copy the exact request from the wireshark capture, and pasted it into the repeater and changed false to true.
![burp](https://user-images.githubusercontent.com/91279257/161536504-8f2dddc7-619e-4709-b4e8-1cde92688fd3.png)<br>
This gives us the flag: **RS{m4gic_word_is_4lw4ys_b31ng_p0lit3}**
