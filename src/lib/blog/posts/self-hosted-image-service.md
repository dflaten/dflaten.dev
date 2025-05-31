---
title: Self Hosting a Photo/Video System
date: 2025-02-28
published: false
---

I've started setting up a service to manage the storage of Photos/Videos for my family. Currently we are using Amazon Photos
which gets us unlimited photos (we have 40 GB worth) and 100 GB of Video (we are using 100 GB) for 20$ per year. I could
upgrade to get more video storage but it would cost 60$ per year for 1 TB of video.

Instead of doing this I'm moving to using a self hosted option where I will use my Ubuntu based server with a 2 TB drive to
store photos and videos with a backup to the could somewhere for long term storage. I evaluated two options for cloud storage:

1. S3 - Glacier Deep Archive for long term storage.
2. Backblaze - Backup Solution that has cheaper retrieval costs than pure S3.

## Basic Parts

I used immich[https://immich.app/] running on an Ubuntu Machine to handle the uploading and access of the images. An IOS and
Android App is provided which makes it easy to upload photos and videos from your phone. I bought an external hard drive and
mounted it using the `.env` [file](https://immich.app/docs/install/environment-variables/) to set the upload location for photos
and videos to the usb drive.

Every day a cron job will be run to upload the new images/videos to S3 via the `rclone` utility. [This repo](https://github.com/dflaten/photo-video-backup) is where those
scripts will live.

### Setup
1. First you will need docker so follow the instructions [on docker's docs page](https://docs.docker.com/engine/install/ubuntu/) to get
it installed on your Ubuntu machine. I reccomend the `apt-get` path so you can update in the future as needed. I needed to
start the service after install with `sudo service docker start`.

I first downloaded the repo on my Ubuntu machine then followed the instructions [here](https://immich.app/docs/install/docker-compose/#upgrading) for
install as well as upgrading.

### Problems Encountered
1. At first couldn't get the iphone app to work correctly because I didn't put my local ip address in exactly as required. You
need to put in the entire `http://numbers:port` in order for it to access correctly.

2. A backup incase local storage fails. I'm only using a 2 TB drive hooked to my server which could fail. I need redundency and 
will for now probably look to the cloud to provide.

3. If your machine is ever resarted and then you have trouble getting the clusters to start back up and connect to your devices there are
a few things you can try:
    * First try updating your server by running: `docker compose pull && docker compose up --force-recreate`
    * If you are using a different location than the default you may need to re mount the usb drive where your photos/videos are stored you can do
    a command like `sudo mount /dev/sdb1 /media/usb` to remount it. 

## Cloud Backup Cost Analysis
Backblaze costs ~ 6 dollars per month for a terrabyte of storage. This is more expensive than general AWS S3 storage but the
closer you get to 1TB the closer the costs come to evening out.

This is based on my current library of photos and videos. My rate of growth is probably less than 1,000 new videos and 100 new
photos every year and costs as you will see do not increase greatly. I can also explore Tiered S3 access or Glacier in the future
if I want to save on costs.

### Data Summary
    Photos: 21,000 files totaling 46 GB
    Videos: 1,900 files totaling 139 GB
    Total storage: 185 GB
    Region: us-east-2

### Storage Cost
* Price - First 50 TB: $0.023 per GB per month.
* 185 GB X $.023/GB = $4.26 per month.

#### Put Request for Initial Backup

* Total files: 21,000 photos + 1,900 videos = 22,900 files
* PUT requests: $0.005 per 1,000 requests
* 22,900 files ÷ 1,000 × $0.005 = $0.11

### Retrieval Costs
This gets a bit pricier but is not too bad:

* Total files: 21,000 photos + 1,900 videos = 22,900 files
* Total data to retrieve: 185 GB

####  Get Request Costs
* GET requests: $0.0004 per 1,000 requests (standard S3 GET pricing)
* 22,900 files ÷ 1,000 × $0.0004 = $0.01

#### Data Transfer Out Costs
* First 10 TB per month: $0.09 per GB
* 185 GB × $0.09/GB = $16.65

#### Data Processing Costs
* GET and SELECT data processing: $0.0015/GB
* 185 GB × $0.0015/GB = $0.28

**Total Cost:** $16.93 and that is only if I need to pull the photos back out of S3.

Due to the fact that I expect to very rarely thaw/access my photos I'm going to go with S3 for storage and if my access patterns
change will re-evaluate.
