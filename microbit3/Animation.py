from microbit import *
frame1 = Image("11111:11111:11111:11111:11111")																				
frame2 = Image("22222:22222:22222:22222:22222")																				
frame3 = Image("33333:33333:33333:33333:33333")																				
frame4 = Image("44444:44444:44444:44444:44444")																				
frame5 = Image("55555:55555:55555:55555:55555")
frame6 = Image("66666:66666:66666:66666:66666")																				
frame7 = Image("77777:77777:77777:77777:77777")																				
frame8 = Image("88888:88888:88888:88888:88888")																				
frame9 = Image("99999:99999:99999:99999:99999")

frames = [frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8,frame9]																				

while True:
	display.show(frames,delay = 200)
	sleep(2000)
	display.scroll("POWER UP!!!")
