import requests,json
class check:
	def Instagram(self,user):
		response = requests.post("https://www.instagram.com/accounts/web_create_ajax/attempt/",headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7','content-length': '61','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/emailsignup/','sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36','x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M','x-instagram-ajax': '72bda6b1d047','x-requested-with': 'XMLHttpRequest'},data={'email' : 'a@gmail.com','username': f'{user}','first_name': 'AA','opt_into_one_tap': 'false'}).text
		if ('{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}') in response:
			status = "404"
		else:
			status = "200"
		return status
		pass
	def Tiktok(self,user):	
		response=requests.get(f'https://www.tiktok.com/@{user}',headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36","Connection": "close","Host": "www.tiktok.com","Accept-Encoding": "gzip, deflate","Cache-Control": "max-age=0"}).status_code
		return response
		pass
	def Snapchat(self,user):
		response=requests.get(f"https://story.snapchat.com/@{user}",headers={'Host': 'story.snapchat.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document'}).status_code
		return response	
		pass
	def Telegram(self,user):
		response=requests.get(f"https://t.me/{user}")
		if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
			status = "404"
		else:
			status = "200"
		return status			
		pass
	def Tellonym(self,user):
		response=requests.get(f"https://tellonym.me/{user}",headers={'Host': 'tellonym.me','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document'}).status_code
		return response
		pass
	def Twitch(self,user):
		response=requests.get(f"https://m.twitch.tv/{user}",headers={'Host': 'm.twitch.tv','Connection': 'keep-alive','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','Save-Data': 'on','Upgrade-Insecure-Requests': '1','User-Agent': generate_user_agent(),'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Sec-Fetch-Site': 'none','Sec-Fetch-Mode': 'navigate','Sec-Fetch-User': '?1','Sec-Fetch-Dest': 'document'}).status_code
		return response
	def Xbox(self,user):
		response=requests.get(f"https://xboxgamertag.com/search/{user}",headers={'Host': 'xboxgamertag.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','user-agent': generate_user_agent(),'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document'}).status_code
		return response
	def Like(self,user):
		response=requests.get(f"https://likee.video/@{user}/",headers={'Host': 'likee.video','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1'}).status_code
		return response
	def Github(self,user):
		response=requests.get(f"https://github.com/{user}",headers={'Host': 'github.com','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document'}).status_code
		return response
	def Reddit(self,user):		
		response=requests.get("https://www.reddit.com/api/username_available.json",headers={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.3"},data={"user": f"{user}"}).text
		if response == True:
			status ="404"
		else:
			status ="200"			
		return status
		pass
	def Gmail(self,user):
		response=requests.post('https://android.clients.google.com/setup/checkavail',data=json.dumps({'username':user,'version':'3','firstName':'AbaLahb','lastName':'AbuJahl'}),headers={'Content-Length':'98','Content-Type':'text/plain; charset=UTF-8','Host':'android.clients.google.com','Connection':'Keep-Alive','user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}).json()
		if response['status'] == 'USERNAME_UNAVAILABLE':
			status ="200"
		elif response['status'] == 'SUCCESS':
			status ="404"
		return status						
		pass
	def Hotmail(self,user):
		response = requests.get("https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + user + "&_=1604288577990", data={}, headers={"Accept": "*/*","Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36","Connection": "close","Host": "odc.officeapps.live.com","Accept-Encoding": "gzip, deflate","Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0","Accept-Language": "ar,en-US;q=0.9,en;q=0.8","canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c","uaid": "d06e1498e7ed4def9078bd46883f187b","Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"})
		if 'MSAccount' in response.text:
			status ="200"
		else:
			status ="404"
		return status	
	def Yahoo(self,user):
		response = requests.post("https://login.yahoo.com/?.lang=en-US&src=homepage&.done=https%3A%2F%2Fwww.yahoo.com%2F&pspid=2023538075&activity=ybar-signin",data={'browser-fp-data': '{"language":"ar","colorDepth":24,"deviceMemory":2,"pixelRatio":1,"hardwareConcurrency":4,"timezoneOffset":-180,"timezone":"Asia/Riyadh","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"dc94ea3045345a33f2917ca98bae1ab9"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":33,"hash":"edeefd360161b4bf944ac045e41d0b21"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"738","h":"1366"},"ts":{"serve":1619968366391,"render":1619968365898}}','crumb': 'zX6Y8DzwyGQ','acrumb': '5akNJNuE','sessionIndex': 'Qg--','displayName': '','deviceCapability': '{"pa":{"status":false}}','username': user,'signin': 'Next','persistent': 'y'},headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en','content-length': '1412','Connection': 'keep-alive','content-type': 'application/x-www-form-urlencoded','cookie': 'B=bm9vuddg8p2ga&b=3&s=j7; GUC=AQEBAQFgjdtglkIiMgTF; A1=d=AQABBAqKjGACEOq_YSZwHJ4WhPmUJWv-J7sFEgEBAQHbjWCWYAAAAAAA_eMAAAcICoqMYGv-J7s&S=AQAAAlzh2dn91k2zbdtc0u-1yz0; A3=d=AQABBAqKjGACEOq_YSZwHJ4WhPmUJWv-J7sFEgEBAQHbjWCWYAAAAAAA_eMAAAcICoqMYGv-J7s&S=AQAAAlzh2dn91k2zbdtc0u-1yz0; APID=UP85920d6e-ab40-11eb-ba37-02c2cb9988ce; APIDTS=1619957920; A1S=d=AQABBAqKjGACEOq_YSZwHJ4WhPmUJWv-J7sFEgEBAQHbjWCWYAAAAAAA_eMAAAcICoqMYGv-J7s&S=AQAAAlzh2dn91k2zbdtc0u-1yz0&j=WORLD; cmp=t=1619968264&j=0; AS=v=1&s=5akNJNuE&d=A6090128c|qq4wynn.2SqVWiOIp_VpNh3Lzyo2y4pBKLL55CSEwUHFlHFRTYTY2pItAkUYdMsJ5E9ADnF_3DKxmP6lx9Uscl__5prHetfu2Qh2oRcHzy2BeMxLMeiRzY0hcEWq.fN.hUvax.VaEAwbPfSiKSBWTBUfa7UH0EhDzWDyWNt.dDk8bJgCtg.1Oat3dAR8O0HMeOLqcHQQQRHekavlNIWXTf01LB2NCPMpGSDasrtFwYHtTpgcgOLLexxDVd_PoGwrWbkpYnU.Irhlctu8UXQs4gQFCSaY3RH.oQQSI9QJ8595Fvj15m0f2c6KQ5ee8EhwwH1bTZddt6vDwQAOLWkkRP86a1A5GYnD0erV43CksOZNZPUHcqHQEkQ0iwKM84VVPQuG_0ARsK9DYKQGyPpKpPOSQm5jzORPFBCJaiCmLeQozRCxHJ8caSjGIXSiiyh6w_pA1RoP9A7EW5TKiMPbB0TUVqf3ZBtRP.wvA9lVLJ0Mhyo0OSlMzRKBJ4cpDtZJfogCuH_muuJcP0AN0CPD.wJ_q7w.dW_bWyssJfXVdwvD8RyyyWBZD9XcLo5vDWkktS80IoXhDWEo_abFn0ZDdIHvHWlaSP_hm6TqdAqdSNvgIsE302fewn4IM2GOA.v6pbkUf5XpUwHD2Ho5DwFY2VNRTm584fLpGpV8Gbn_0JIR719qzqZZX07Gk2mHNcDKKDgtM6j_FTpzwK9kK.4QvZSVs0oZqrwwrzTwkXDAI2X82c6Gyk0HWR9d9VDfPszYX6CzH6iS1OWjPIGDrgIyTSv.qVW_croFa9B8kaYRF_E9NJ6PsZtWcZGeSHE8jXDBTXV0yViEFIIlnRLRhlEPiiDFKG93v58AP69q2MWNDGLLgys-~A|B609012ee|681uFX3.2Sp2V6jxkaRhaqPw4DcbOoHDf9swSs78fSdPp0kwXejzGWDqWJAYUfVCM2hIyMGwspszur7ubvnLOQvQICPbRCMIPTC1u_gxhLjD2CRZwAdpOYPgQ2T71Gt9ZUjKs_xKpNTJiT_ISmTN6ig.JUGgdwKgY8SPN07.qHtVaeQmBX0O5DMMs982JPBqCQR2mG7VtGOSkHyg8NCYBJaMcj9vyveuxp355iHol1FQAkfscDG20zKnzzCS97coC8LN_us5bqHLHNy4ZuCbs3V2Aaa76PZdBAlRE0m6bNCZln_786EJHltYd5acCgFViRTLVk3b5oFdO8kcdr0i8iJ_iDTVXfxJ6MjclHN1L1wgjsJpLRS.5H_5h9UIqzTq2UOIrUJjLLYmu1uL9PiSI1M0uvxZL.Ul7Ca7U3aGTbCHylA8uc6SdLf6SUhISILtP67Q0AY_EkxPCRz0rP8WJJzDdFozMhd_oqDfCiZ1SIaNRDNlOgnRSLTeMW_q.J6kydyTrLqQskzbtPZdx_baU6GFd_KIQTVLNjBWoT8AN_7X5yr62Y5E2rixlpvfP_KQcyOkLTOhA666zGvjYqTqBw.QHKLejuYxNM5Nhrw7VaIexUVsRTVbU7VNtPCO3qihfJOyjLC_OeFvFu.r.r_C6mDi33w5z9bNUzyyXmvT7fuSi8_0b07VEDx6GO6.98Imyq6VyPbqWGBn7pPSJhTaWAkwwaIX2gfo1bWxKqbmFZu1Uc3tP1F2h7OxuY02XK5SsJWcyHkj.IL08ZVZUydBq6VkCFl0I0oyK5iaCSZ.PJ0VvzFIuz792O71HlQhDO5SLIXZdSF_Fs1zbdVsmsp8qmb4n1mKlLXD7HXtjBAsUyQ-~A','origin': 'https://login.yahoo.com','referer': 'https://login.yahoo.com/','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51','x-csrftoken': 'yv0DVF5FiI9VNdvDd6HEy3IAU0wKson5','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': '822bad258fea','x-requested-with': 'XMLHttpRequest'}).json()
		if 'isDisabledUserName' in response:
			status ="404"
		else:
			status ="200"
		return response				
	def Sony(self,uesr):
		response=requests.post("https://psnid.world/api/check?tag=gg",headers={'Host': 'psnid.world','content-length': '0','sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1',
'save-data': 'on','user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36','sec-ch-ua-platform': '"Android"','content-type': 'application/json','accept': '*/*','origin': 'https://psnid.world','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://psnid.world/'}).text
		if "Search again to try and find an available name" in response:
			status ="200"
		else:
			status ="404"
		return status
	def Steam(self,uesr):
		response=requests.get("https://steamcommunity.com/id/{uesr}",headers={'Host': 'steamcommunity.com','Connection': 'keep-alive','Cache-Control': 'max-age=0','sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','Save-Data': 'on','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Sec-Fetch-Site': 'none','Sec-Fetch-Mode': 'navigate','Sec-Fetch-User': '?1','Sec-Fetch-Dest': 'document'}).text
		if "<title>Steam Community :: Error</title>" in response:
			status ="404"
		else:
			status ="200"
		return status
		pass
	def Tamtam(self,uesr):
		try:
			response=requests.get(f"https://tamtam.chat/{uesr}",headers={'Host': 'steamcommunity.com','Connection': 'keep-alive','Cache-Control': 'max-age=0','sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','Save-Data': 'on','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Sec-Fetch-Site': 'none','Sec-Fetch-Mode': 'navigate','Sec-Fetch-User': '?1','Sec-Fetch-Dest': 'document'}).status_code			
			status ="200"
		except:
			status ="404"	
		return status
				