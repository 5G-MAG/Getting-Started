---
layout: default
title:  Testing with Postman
parent: Testing
grand_parent: 5G Downlink Media Streaming
has_children: false
nav_order: 4
---

# Testing with Postman
[Postman](https://www.postman.com/) is a popular API development and testing tool that allows users to create, send, and manage HTTP requests. It provides a user-friendly interface for building and testing API endpoints, making it easier for developers to collaborate and streamline the API development process. Postman comes in very handy when testing and working with the `M1` and `M5` interfaces of the Application Function.

# Importing the 5G-MAG Postman Collection
Postman provides an easy way to export and import a collection of REST calls. To facilitate getting started, you can download our pre-defined Postman collections and environment here: 

* [5G-MAG M1.postman_collection.json](https://github.com/5G-MAG/rt-5gms-application-function/files/14064359/5G-MAG.M1.postman_collection.json)
* [5G-MAG M5.postman_collection.json](https://github.com/5G-MAG/rt-5gms-application-function/files/14062693/5G-MAG.M5.postman_collection.json)
* [5G-MAG.postman_environment.json](https://github.com/5G-MAG/rt-5gms-application-function/files/14062716/5G-MAG.postman_environment.json)


After the download, open Postman and select `File->Import`. After a successful import, you should see two collections like this:

<img width="382" alt="Bildschirmfoto 2024-01-26 um 09 07 00" src="https://github.com/5G-MAG/rt-5gms-application-function/assets/2427039/80df62af-0f3c-4abd-bc83-8a4528cf48cc">

# Postman Configuration
A very useful feature of Postman is the possibility to define variables. These variables can afterward be used in any of our routes or payloads. The first variables we need to define are the `m1_url` and `m5_url` variables. For that reason, select `Environments` on the left side and then select the `5G-MAG` environment. Now you should see a list of variables similar to this:

<img width="1065" alt="Bildschirmfoto 2024-01-26 um 09 15 05" src="https://github.com/5G-MAG/rt-5gms-application-function/assets/2427039/1d0decc5-2c73-4f87-93cc-baad62c685fa">

Add the URL to the `M1` and the `M5` endpoint of your Application Function here. In the example above, we are running the Application Function in a local network. Note that both URLs also need to contain the port. The configuration options for the Application Function are documented [here](https://github.com/5G-MAG/rt-5gms-application-function/wiki/Configuring-the-Application-Function).

# Using M1
Now that we have defined the `M1` endpoint, we can start using it:

## Creating a Provisioning Session
Navigate to the `Provisioning Session` folder in the Postman Collection and select `Create Provisioning Session`. Check the URL on the top that we are sending the request to: `{{m1_url}}/3gpp-m1/v2/provisioning-sessions`. Here you can see that we are using the `m1_url` variable that we defined earlier. If the endpoint changes at some point we only need to change our variable instead of all the M1 calls in our Postman collection.

Click on `Send` on the top right. You should see a successful response (status code `201`) and the payload of the response on the bottom:

<img width="1066" alt="Bildschirmfoto 2024-01-26 um 09 28 04" src="https://github.com/5G-MAG/rt-5gms-application-function/assets/2427039/95422926-a2fb-4489-82c0-c07e39e4df86">


The response body contains the `provisioningSessionId` of our created provisioning session. The `provisioningSessionId` is an important identifier and used in many of the `M1` and `M5` endpoints. Consequently, it makes sense to assign the `provisioningSessionId` to a variable as well. Our collection contains a small script that automatically assigns the `provisioningSessionId` value of the response body to the `provisioning_session_id` variable:
  
````js
var responseBody = pm.response.json();
var provisioningSessionId = responseBody.provisioningSessionId;
pm.environment.set("provisioning_session_id", provisioningSessionId);
````

## Retrieving a Provisioning Session
Now that we have created a provisioning session and assigned its `provisioningSessionId` to our variable, we can directly call the `GET Provisioning Session` endpoint. As expected, our route contains the `m1_url` and the `provisioning_session_id` variable: `{{m1_url}}/3gpp-m1/v2/provisioning-sessions/{{provisioning_session_id}}`.

Sending this request should result in a response similar to this:
<img width="1069" alt="Bildschirmfoto 2024-01-26 um 09 36 19" src="https://github.com/5G-MAG/rt-5gms-application-function/assets/2427039/e5a21053-6a98-4bed-8695-f3b2a39d16dc">

## Deleting a Provisioning Session
Deleting a provisioning session is straight forward as well. As we already defined the required variables, you can simply execute the call and should receive a `202 Accepted` response.

## Consumption Reporting
To manage consumption reporting configurations, proceed similarly to managing provisioning sessions. Note that the `create` and `update` functions contain a `JSON` structure in the payload to define the required parameters.

## Policy Templates
To manage policy templates, proceed similarly to managing provisioning sessions. Note that the `create` and `update` functions contain a `JSON` structure in the payload to define the required parameters. Moreover, `open5gsIntegration` must be enabled in the configuration of the Application Function. For more details, refer to the [Configuration Guide](https://github.com/5G-MAG/rt-5gms-application-function/wiki/Configuring-the-Application-Function).

After successfully creating a policy template, the new `policyTemplateId` contained in the `Location` header is automatically assigned to the `policy_template_id` variable:

````js
var policyTemplateId = pm.response.headers.get("Location").split("/").pop()
pm.environment.set("policy_template_id", policyTemplateId);
````

# Using M5
The `M5` routes to query the Service Access Information, send a Consumption Report, create a Dynamic Policy resource and provision a new Network Assistance Session can be found in the `5G-MAG M5` folder. There is no additional configuration required, the routes for `M5` use the variables that we defined earlier as part of the configuration and the execution of `M1` endpoints. 
