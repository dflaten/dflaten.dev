---
title: Self Hosting My Photo/Video Storage
date: 2025-02-28
published: false
---

I've started setting up a service to manage the storage of Photos/Videos for my family. Currently we are using Amazon Photos
which gets us unlimited photos (we have 40 GB worth) and 100 GB of Video (we are using 100 GB) for 20$ per year. I could
upgrade to get more video storage but it would cost 60$ per year for 1 TB of video.

Instead of doing this I'm moving to using a self hosted option where I will use my Ubuntu based server with a 2 TB drive to
store photos and videos with a backup to the could somewhere. I evaluated two options for cloud storage:

1. S3 Glacier - Deep Archive for long term storage.
2. Backblaze

At ~500 GB of storage S3 will charge me $21.60 per year to store the photos/videos. However when I need to restore the
backup the S3 retrieval costs would be ~100 dollars for 1 TB. See [pricing info here](https://aws.amazon.com/s3/pricing/).

Backblaze costs ~ 6 dollars per month for a terrabyte of storage. This is cheaper than general AWS S3 storage but more expensive
(if you aren't thawing often) than S3 Glacial.

Due to the fact that I expect to very rarely thaw/access my photos I'm going to go with S3 for storage and if my access patterns
change will re-evaluate.

### Basic Parts

Will use immich[https://immich.app/] running on an Ubuntu Machine to handle the uploading and access of the images in general.

Every day a cron job will be run to upload the new images/videos to S3 via the `rclone` utility. [This repo](https://github.com/dflaten/photo-video-backup) is where those
scripts will live.

### Setup
I first downloaded the repo on my Ubuntu

### Problems Encountered
1. At first couldn't get the iphone app to work correctly because I didn't put my local ip address in exactly as required.
