---
title: Learning Linux with Arch Linux
date: 2025-03-23
published: false
---

I had an extra computer arround the house and decided to try and install Arch Linux on it
because I heard it was a good version but "not for beginners". I wouldn't call myself
an expert in Linux but decided this could be a good way of learning more about it. After
starting the installation process it showed me how little I really understood about how
linux works.

### Installation process.

I found the [ISO on the ArchLinux site](https://archlinux.org/download/) and burned it into
a USB. Almost immediately upon loading it I ran into my first big problem.

During booting you are greeted with a screen like this:

![`First install screen.`](./learning-linux-with-arch-linux.jpg)

If I let the system attempt to boot up the live image on my pc it will start to load into RAM but my screen would go
to black.

Searching quickly brought be to the [Arch Linux Install Wiki](https://wiki.archlinux.org/title/Installation_guide#) which
looked like an excellent way to get things installed but brought no resolution for my issue. Further searching finally
led me to set the `nomodeset` option on the boot screen by precessing `e` and adding `nomodeset` to the end of the line.

My issue was due to the AMD GPU drivers not loading correctly and setting `nomodeset` prevented the Kernel from setting
setting up the video card, waiting for the OS to do so.

TODO: ADD MORE DETAILS ON NOMODESET resolution.

### Pieces Needed to setup Arch Linux

#### Installing the OS to your local drive

#### Formatting the Drive

#### Display Adapter

#### Network / Internet Connection

### User Setup (Root and dflaten)

#### GUI
