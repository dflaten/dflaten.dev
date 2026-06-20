
---
title: Creating an Alexa Replacement with help from Codex
date: 2026-04-04
published: true 
---

A few months ago I decided Amazon had enough data from me collected via Alexa and there must be an open source or 
self hosted option to replace it. This led me to the [ESP Box 3](https://www.espressif.com/en/dev-board/esp32-s3-box-3-en),
a piece of hardware which can understand voice commands and execute code which you've uploaded to it. [Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/get-started/index.html) is good and can help you get started. This has been something
I've wanted to do for a while but I haven't had a lot of time and my rustiness with `C` prevented me from giving it a go. Thanks to coding agents though it has made building things much easier especially if you aren't familiar with the language.

I've learned a decent bit about the current state of coding Agents as a part of creating this project. Getting 90% there with a coding Agent is very easy but getting your application to be something that is maintainable, scalable, and understandable by others requires more than just letting the Agent take the wheel, at least for now.

Just like anything you are building it is best to start with a very basic idea and build upon it which is what I've done. There were some tricky bugs that took quite a few iterations with Codex to get solved and the firmware certainly isn't perfect yet but it does do the basics of what I need it to. 

[Here's the Firmware!](https://github.com/dflaten/box3-assistant) If you'd like to build your own follow the directions below!

## Getting Started Instructions 

I'll outline how I went about building the software for the assistant which could help you build something similar.

### We need a toolchain to build the firmware image and get it on the device.

This requires two things:
1. Build Tools - CMake and Ninja to build full Applications.
2. ESP-IDF that contains the api for ESP-32 and scripts to operate the Toolchain.

### Installing ESP-IDF on Linux Machine

I'm using a linux machine for development but the overall process is the same on Windows or Mac.

[This page was really useful.](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/linux-macos-setup.html)

I chose the the CLI version of the available tooling which has worked well with Codex for development.

Here's what the terminal looks like once it is finished:

```
Configuration saved successfully to config.toml
You have successfully installed ESP-IDF
for using the ESP-IDF tools inside the terminal, you will find activation scripts inside the base install folder
sourcing the activation script will setup environment in the current terminal session
============================================
to activate the environment, run the following command in your terminal:
       source "/home/my-user/.espressif/tools/activate_idf_v5.5.3.sh"
```

Now I am currently using Fish for my terminal instead of Z shell or Bash so I had to install the tooling by going here:
`/home/my_user/.espressif/v5.5.3/esp-idf` and then running `./install.fish esp32` which left me with: 


```
All done! You can now run:

  . /home/user_name/.espressif/v5.5.3/esp-idf/export.fish
```

To activate my environment I used:
`source /home/user_name/.espressif/v5.5.3/esp-idf/export.fish`

Which I created an alias for easy access: 
`alias get_idf='source /home/user_name/.espressif/v5.5.3/esp-idf/export.fish'`

### What's Next?

After tooling setup its time to start coding. Create a new GIT repo and try building a firmware version for the device using the libraries provided by ESP-IDF. It has been a while since I've used `C` but thanks to [Codex](https://developers.openai.com/codex/cli) 
I was able to get something working pretty quickly.

### Hue Controls
I started by creating a new project: 

```
idf.py create-project hue-controls
cd hue-controls
idf.py set-target esp32s3
```


Then I started coding the controls for my Hue Lights using the http client Hue has available.

Get a token from HUE:

```
❯ curl -X POST http://<IP_OF_BRIDGE>/api \
        -H "Content-Type: application/json" \
        -d '{"devicetype": "esp_s3_box#mydevice"}'
[{"success":{"username":"{USERNAME_STRING}"}}]⏎
```

Get your group number: 
```
curl -X GET http://192.168.68.60/api/{USERNAME_STRING}/groups | jq
```

### Deploying the project

curl -X GET http://192.168.XX.XX/api//groups | jq

```
idf.py reconfigure
idf.py build
```

Once you are ready to deploy set your target to your ESP Box 3: 
`idf.py set-target esp32s3`

If needed you can configure your WiFi:
```
idf.py menuconfig
# Navigate to: Example Connection Configuration
# Set: WiFi SSID
# Set: WiFi Password
# Save with S, quit with Q
```

### Polishing and Expanding
After getting my hue lights working with my ESP I decided to add basic weather information to the device. A couple of prompts to codex and a bit of direction and I was able to get todays current weather displayed on the device. 

### Some Other Helpful Information
Then figure out which port you're ESP is connected to: 
`ls /dev/tty*        # look for /dev/ttyUSB0 or /dev/ttyACM0`

Then run:
`idf.py -p /dev/ttyACM0 build flash monitor`

### Now What?
Now it's up to you! You can build your own firmware or fork mine if you like. Happy building!

