import os
print("\t------------------------------------------------------------")
print("\t\t\tTo Provide Elasticity to Data Node Storage")
print("\t------------------------------------------------------------")
print("""1.TO create a Physical Volume
         2.TO create a Volume Group 
         3.TO create a Logical Volume 
         4.To Extend the Storage Capacity of Data Node by 5GB 
         5.EXIT
    """)
while True:
    n=int(input("Select Option from 1-5 : "))
    if n==1:
        os.system("pvcreate /dev/sdc")
        os.system("pvcreate /dev/sdb")
        print("PV CREATED!!")
    elif n==2:
        os.system("vgcreate hadoopSto /dev/sdb /dev/sdc")
        print("VG CREATED!!")
    elif n==3:
        os.system("lvcreate --size 50G --name hadoopLV hadoopSto")
        os.system("mkfs.ext4 /dev/hadoopSto/hadoopLV")
        os.system("mkdir hadoopdrive")
        os.system("mount /dev/hadoopSto/hadoopLV /hadoopdrive")
    elif n==4:
        os.system("lvextend --size +5G /dev/hadoopSto/hadoopLV")
        os.system("resize2fs /dev/hadoopSto/hadoopLV")
    else:
        break
