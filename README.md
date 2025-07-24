# Devops_tutorial_by_tutedue

Microsoft Windows [Version 10.0.22631.5262]
(c) Microsoft Corporation. All rights reserved.

C:\Users\beher>wsl --install
Downloading: Ubuntu
Installing: Ubuntu
Distribution successfully installed. It can be launched via 'wsl.exe -d Ubuntu'
Launching Ubuntu...
Provisioning the new WSL instance Ubuntu
This might take a while...
Create a default Unix user account: beheramadhusudan607
New password:
Retype new password:
passwd: password updated successfully
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

beheramadhusudan607@Rajperlove:/mnt/c/Users/beher$ mkdir test_dir
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher$ ls
 -1.14-windows.xml       Desktop                   'Local Settings'                                                                                NetHood            SendTo               madhu
'3D Objects'             Documents                  Microsoft                                                                                      OneDrive          'Start Menu'          ntuser.dat.LOG1
 AppData                 Downloads                  Music                                                                                          PrintHood          Templates            ntuser.dat.LOG2
'Application Data'      'Epic Games Launcher.lnk'  'My Documents'                                                                                  PycharmProjects    Videos               ntuser.ini
 Autodesk                Favorites                  NTUSER.DAT                                                                                     Recent            'VirtualBox VMs'      pythonProject2
 Contacts                IdeaProjects               NTUSER.DAT{e000167e-46a4-11ed-920d-b3b3d63b076e}.TM.blf                                       'Rising Hell.url'   anaconda3            test_dir
 Cookies                 IntelGraphicsProfiles      NTUSER.DAT{e000167e-46a4-11ed-920d-b3b3d63b076e}.TMContainer00000000000000000001.regtrans-ms  'Saved Games'      'docker desktop'
'Creative Cloud Files'   Links                      NTUSER.DAT{e000167e-46a4-11ed-920d-b3b3d63b076e}.TMContainer00000000000000000002.regtrans-ms   Searches           example-voting-app
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher$ cd test_dir
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher/test_dir$ ls
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher/test_dir$ touch example.txt
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher/test_dir$ ls
example.txt
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher/test_dir$ mv example.txt renamed_example.txt
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher/test_dir$ ls
renamed_example.txt
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher/test_dir$ cat
^C
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher/test_dir$ cat/etc/passwd
bash: cat/etc/passwd: No such file or directory
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher/test_dir$ head -n 5 /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher/test_dir$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:996:996:systemd Time Synchronization:/:/usr/sbin/nologin
dhcpcd:x:100:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false
messagebus:x:101:101::/nonexistent:/usr/sbin/nologin
syslog:x:102:102::/nonexistent:/usr/sbin/nologin
systemd-resolve:x:991:991:systemd Resolver:/:/usr/sbin/nologin
uuidd:x:103:103::/run/uuidd:/usr/sbin/nologin
landscape:x:104:105::/var/lib/landscape:/usr/sbin/nologin
polkitd:x:990:990:User for polkitd:/:/usr/sbin/nologin
beheramadhusudan607:x:1000:1000:,,,:/home/beheramadhusudan607:/bin/bash
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher/test_dir$ tail -n /etc/passwd
tail: invalid number of lines: ‘/etc/passwd’
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher/test_dir$ tail -n 5 /etc/passwd
systemd-resolve:x:991:991:systemd Resolver:/:/usr/sbin/nologin
uuidd:x:103:103::/run/uuidd:/usr/sbin/nologin
landscape:x:104:105::/var/lib/landscape:/usr/sbin/nologin
polkitd:x:990:990:User for polkitd:/:/usr/sbin/nologin
beheramadhusudan607:x:1000:1000:,,,:/home/beheramadhusudan607:/bin/bash
beheramadhusudan607@Rajperlove:/mnt/c/Users/beher/test_dir$
