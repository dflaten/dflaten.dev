
---
title: Creating and Alexa Replacement
date: 2025-03-14
published: false
---

A few months ago I decided Amazon had enough data from me collected via Alexa and there must be an open source or 
self hosted option to replace it. This led me to the [ESP Box 3](https://www.espressif.com/en/dev-board/esp32-s3-box-3-en),
a piece of hardware which can understand voice commands and execute code which you've uploaded to it. [Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/get-started/index.html) is good and can help you get started.

### What do you need to get started?
1. Toolchain to compile code. 
2. Build Tools - CMake and Ninja to build full Applications.
3. ESP-IDF that contains the api for ESP-32 and scripts to operate the Toolchain.

### Installing Dev tools on Linux Machine

[This page was really useful.](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/linux-macos-setup.html)

I'm using a Linux machine for my development work so I followed those instructions and installed the CLI version of the available
tooling. 

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
`/home/david/.espressif/v5.5.3/esp-idf` and then running `./install.fish esp32` which left me with: 


```
All done! You can now run:

  . /home/david/.espressif/v5.5.3/esp-idf/export.fish
```

To activate my environment I used:
`source /home/david/.espressif/v5.5.3/esp-idf/export.fish`

Which I created an alias for easy access: 
`alias get_idf='source /home/david/.espressif/v5.5.3/esp-idf/export.fish'`

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
[{"success":{"username":"WILL_BE_A_STRING_HERE"}}]⏎
```

Get your group number: 
```
curl -X GET http://192.168.68.60/api/5eYoU3esxjvjeSi2eyA76NwE3kRYuhmXBdnxxYgd/groups | jq
```


