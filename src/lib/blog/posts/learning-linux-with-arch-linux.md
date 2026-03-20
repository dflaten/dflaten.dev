---
title: Learning Linux with Arch Linux
date: 2026-01-25
published: true 
---

I had an extra computer around the house and decided to try and install Arch Linux on it
because I heard it was a good version but "not for beginners". I wouldn't call myself
an expert in Linux but decided this could be a good way of learning more about it. After
starting the installation process it showed me how little I really understood about how
Linux works.

### Installation process
The Arch wiki has an installation guide that is fairly good even if you don't have much experience with Linux. I used that to get through most of the issues I encountered.

#### ISO Creation
I found the [ISO on the ArchLinux site](https://archlinux.org/download/) and burned it into
a USB. Almost immediately upon loading it I ran into my first big problem.

#### Booting Problems...

During booting you are greeted with a screen like this:

![`First install screen.`](./arch_linux_first_install_screen.png)

If I let the system attempt to boot up the live image on my pc it will start to load into RAM but my screen would go to black.

Searching quickly brought be to the [Arch Linux Install Wiki](https://wiki.archlinux.org/title/Installation_guide#) which
looked like an excellent way to get things installed but brought no resolution for my issue. Further searching finally
led me to set the `nomodeset` option on the boot screen by precessing `e` and adding `nomodeset` to the end of the line.

My issue was due to the AMD GPU drivers not loading correctly and setting `nomodeset` prevented the Kernel from setting up the video card, waiting for the OS to do so.

The `nomodeset` option did allow me to continue with the setup. Next I moved on to setting up network connections.

#### Network / Internet Connection
I used `ip link` and  `iwd` to get connected to the internet. 

#### Formatting the Drive
Next I formatted the disk with `fdisk` setting up the `/boot` partition. I learned about mounting drives with commands like `mount /dev/root_partition /mnt`. 

#### Installing the OS to your local drive
`pacstrap -K /mnt base linux linux-firmware` got the system installed on my machine.

#### User Setup (Root and user)
Next I switched my root to the new install since up to this point I had been working off the USB drive. `arch-chroot /mnt`

I set up a user account here and then tried to Reboot. This is where I ran into the same problem that I did with the USB booting. The drivers for the video card on my machine did not install correctly and I was required to set the `nomodeset` value by default on my machine to keep using it. 

### Calling it Quits
Due to the fact that I wanted to test gaming on this PC this is where I decided it wasn't worth going further with this machine. I did learn some interesting things about how Linux is setup from it's core and how to get Arch up and running on a machine. I may come back to this in the future but for now will call this learning experience complete!
