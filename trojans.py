import os
import sys
import time

def mengetik(z):
            for e in z + "\n":
			  sys.stdout.write(e)
			  sys.stdout.flush()
			  time.sleep(0.1)

def nanya():
    nanya = raw_input("\033[92mApakah anda ingin mengirim virus trojans lagi? (Y/T) : ")
    if nanya =="Y" or nanya =="y":
         menu()
    elif nanya =="T" or nanya =="t":
         mengetik("\033[91mYaudah seterah lu aja ajg..............")
         time.sleep(0.1)
         sys.exit()
    elif nanya =="T" or nanya =="t":
         mengetik("jangan kosong ngab:v")
         time.sleep(0.1)
         nanya()
    else:
         mengetik("\033[91msalah masukkan input anda dengan benar !")
         time.sleep(0.1)
         nanya()

def menu():
       os.system("clear")
       time.sleep(0.2)
       print                         "\033[91mTROJANS"
       print "\033[96m[+]===========================================[+]"
       print    "\033[97m[*] Author : muhammad saiful galang"
       print    "\033[97m[*] youtube : nggak ada ngab:v"
       print    "\033[97m[*] facebook : nggak aja juga njir:v"
       print    "\033[97m[*] WhatsApp : +62 8214-6685-361"
       print    "\033[97m[*] github : https://github.com/MR-galang97"
       print "\033[96m[+]===========================================[+]"

       print

       nomor = raw_input("\033[90mMasukkan nomor target : ")
       jumlah = int(input("\033[90mMasukkan jumlah pengiriman : "))
       time.sleep(0.1)

       try:
           for i in range(jumlah):
	       print "\033[96mMengirim" "\033[91m Virus Trojans" "\033[96m Ke Nomor >""\033[93m",nomor,"\033[91mSukses"
               time.sleep(0.1)

       except KeyboardInterrupt:
           print "\033[96mMengirim Virus Trojans Ke Nomor Target Sukses"
       nanya()

menu()

#no record ajg
#record izin dl ngab:v
#coding by muhammad saiful galang
