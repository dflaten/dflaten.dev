---
title: Managing Access for Personal AWS Account
date: 2025-03-09
published: true
---

AWS offers many of its services for free or up-to-a-point free so it can be nice to have a personal AWS account
setup to build things on. Setting up access in a secure manner is a prudent to prevent someone else from gaining
access and racking up unneccessary costs. In this post I'll outline the basic pieces you will want to setup with
your AWS Account to prevent unauthorized access while making it easy to do development.

I reccomend you use a password manager to generate/save the passwords for the users you will create as part of this
process. There are many ways to do this but I'll outline what worked for me.

By the end of this you will have:

1. Secure Credentials to Access the AWS console in your AWS account.
2. The ability to connect  via the CLI to AWS services.

### Steps to Create Secure Access

#### Set up the Account
1. First create your aws account [here](https://aws.amazon.com/). You will be assigned an account id and granted access to
a root user for the account.

2. The first thing you should do is log in with your root user and enable 2-Factor Authentication. There are lots of
options  here but we will go with using an authenticator app on your phone like [Duo  Mobile](https://duo.com/product/multi-factor-authentication-mfa/duo-mobile-app).
You will need to download the app on  your phone and log in to your root user.

3. Go to your user and enable MFA by clicking on the `Security Credentials` section. You will be able to add the App by
following the instructions as listed.
~[EnableMFA](./EnableMFA.jpg)

#### Create the Admin User

4. We will now create an Admin user which will be used to log in to the AWS account from now on. Root user should rarely be used
since it has such wide access to the account. To do so go to the `IAM Identity Center` in AWS and enable it. Then go to users and create a user.
I reccomend you create a `Admin` user first which has Admin permissions that is the `AdministratorAccess` permission. Then
enable MFA for this user and verify the email for it through the UI. Also make sure you assign the `Admin` user to your AWS account
under `AWS Accounts`.

#### Create the Developer User
5. After this you should log out of your `root` user and log in to your `Admin` user. Go back the `IAM Identity Center` and create a new
user with the name `my-name-developer` following the same process as the Admin user. This is the user you will use to do development in the account. You should only grant access
to this user the services you will use.

6. Now we need to download the aws cli so you can connect from your local machine. On mac you can do so using brew: `brew install aws`

7. Now configure the credentials by using `aws configure sso` this will start the setup process.

8. Go to your AWS console logged in as `Admin` and got to the `IAM Identity Center`. On the right you will see a URL
by the field, `AWS access portal URL` copy this URL. Now you need to either open another browser or user Firefox container
tables to access this URL because we are going to log in as the developer user. Follow the prompts to authenticate and you will
see a new screen with the AWS Account id you have access to. Click the `Access Keys` link on this page and follow the instructions
under `AWS IAM Identity Center credentials (Recommended)` to get the required fields to get aws access.

### Wrapping Up
You now have secure access to your AWS account and can make calls via the cli to AWS after authenticating. The nice
part about the Identify Center is it will automatically try to authenticate if you lose access.
