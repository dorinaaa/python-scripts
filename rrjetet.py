import sys

ip = sys.argv[1]
sm = sys.argv[2]
octets = ip.split(".")
sm_octets = sm.split(".")
try:
    if len(octets) < 4 or len(octets) > 4 or len(sm_octets) < 4 or len(sm_octets) > 4:
        print("Enter a valid IP Adress/ Subnet Mask!")
        exit()
    for octet in octets:
        if float(octet) < 0:
            print("Enter a valid IP Adress!")
            exit()
    for sm_octet in sm_octets:
        if float(sm_octet) < 0:
            print("Enter a valid Subnet Mask!")
            exit()

except:
    print("Enter valid data!")
    exit()
print("IP: "+ip)
print("Subnet Mask: "+sm)
ip_class = float(octets[0])
if ip_class>=1 and ip_class <=126:
    print("Class : A")
    print("NetworkID : "+str(octets[0])+".0.0.0")
    print("Default SubnetMask : 255.0.0.0")
elif ip_class >= 128 and ip_class <=191:
    print("Class : B")
    print("NetworkID : " + str(octets[0])+"."+str(octets[1]) + ".0.0")
    print("Default SubnetMask : 255.255.0.0")
elif ip_class >=192 and ip_class <= 223:
    print("Class : C")
    print("NetworkID : " + str(octets[0]) +"."+ str(octets[1])+"."+str(octets[2]) + ".0")
    print("Default SubnetMask : 255.255.255.0")
else:
    print("Enter valid data!")
    exit()
s_id = [0,0,0,0]
for i in range(4):
    if int(sm_octets[i])==255:
        s_id[i]=octets[i]
    elif int(sm_octets[i])==0:
        s_id[i]=0
    elif int(sm_octets[i])!=255 and int(sm_octets[i])!=0:
        magic_number = 256 - int(sm_octets[i])
        multiples = [x for x in range(magic_number,256,magic_number)]
        min = 255
        for x in multiples:
            dif = abs(int(octets[i])-x)
            if dif < min:
                min =dif
                s_id[i]=x
b_id = [0,0,0,0]
for i in range(4):
    if int(sm_octets[i])==255:
        b_id[i]=octets[i]
    elif int(sm_octets[i])==0:
        b_id[i]=255
    elif int(sm_octets[i])!=255 and int(sm_octets[i])!=0:
        magic_number = 256 - int(sm_octets[i])
        b_id[i]=s_id[i]+magic_number-1

print("Subnet : "+str(s_id[0])+"."+str(s_id[1])+'.'+str(s_id[2])+"."+str(s_id[3]))
print("Broadcast : "+str(b_id[0])+"."+str(b_id[1])+'.'+str(b_id[2])+"."+str(b_id[3]))
print("Host Min : "+str(s_id[0])+"."+str(s_id[1])+'.'+str(s_id[2])+"."+str(s_id[3]+1))
print("Host Max : "+str(b_id[0])+"."+str(b_id[1])+'.'+str(b_id[2])+"."+str(b_id[3]-1))

