# lhtwitterbot
Twitterbot implemented in Python3
# lhtwitterbot
Python Twitterbot implemented in Python3

Summary:

lhtwitterbot checks a Twitter account's direct message (DM) history at a given interval (5 minutes by default) and responds to a predetermined hotword with the external IP address of the host it is currently running on. To do this it makes a call to api.ipify.org to get the external IP and responds back with a DM to the same Twitter account as the originating query.

Requirements:

lhtwitterbot requires Python3 and the modules listed in the requirements.txt of this repository. If you intend to build and run this Python program as a podman container your environment will also require Podman 2.2.1 and Buildah 1.18.0.

You will need a Twitter Developer account in order to access the Twitter API. You can apply for a Twitter Developer account at: https://developer.twitter.com/en. Setting up a new application in your Twitter Developer Dashboard will provide you with four necessary keys, which must be passed to the Python program as environmental variables which will allow the program to authenticate with Twitter. They are the CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, and ACCESS_SECRET.

Procedure:

Prepare the script (container or non-container)

After cloning this repository, log into Twitter with the account you intend to run the bot with and send yourself a DM. Edit get_senderid.py and insert your 4 Twitter API keys into the 'Twitter Creds' section. Run get_senderid.py. This script will return an 18 digit number. This is your Twitter senderid. I've written filtering in main.py to only respond with your IP address when it sees a request with your chosen hotword and senderid to prevent malicious flooding. Insert your sender_id and a hotword of your choice into ln. 41 on main.py.

Running lhtwitterbot outside of a container:

If you intend to run lhtwitterbot outside of a container, install the additional required Python libraries with `pip3 install -r requirements.txt`. Make the 4 Twitter keys available to your environment with:

  export CONSUMER_KEY=aaaaBBBBccccDDDDeeeeffffGGGG
  
  export CONSUMER_SECRET=aaaaBBBBccccDDDDeeeeffffGGGG
  
  export ACCESS_KEY=aaaaBBBBccccDDDDeeeeffffGGGG
  
  export ACCESS_SECRET=aaaaBBBBccccDDDDeeeeffffGGGG

and then execute lhtwitterbot with `python3 main.py`.

Running lhtwitterbot inside of a container:

If you would like to build a container suitable for use with the Podman runtime, execute prebuild.sh to zip the necessary components, and then execute build_script.sh to call Buildah to create a Podman container in the localhost repository called localhost/lhwtitterbot:latest. You can now run:

  podman run -d --name \<name of your choosing\> -e CONSUMER_KEY=aaaaBBBBccccDDDDeeeeffffGGGG -e CONSUMER_SECRET=aaaaBBBBccccDDDDeeeeffffGGGG -e ACCESS_KEY=aaaaBBBBccccDDDDeeeeffffGGGG -e ACCESS_SECRET=aaaaBBBBccccDDDDeeeeffffGGGG localhost/lhtwitterbot

substituting your 4 Twitter API access keys for the examples above.

lhtwitterbot logs internally to /opt/log.txt in the container, and to <exec directory>/log.txt when executed outside of a container. Following which either of these fits your circumstances should result in output every 5 minutes after starting lhtwitterbot to let you know the program is active. The program will sit in an event loop until the container is stopped or a SIGINT is received. Test functionality by sending a DM to yourself via Twitter containing the hotword (I chose !ipaddress). On the next scheduled run the message containing the hotword will be deleted and replaced with the host's external IP address.

dcd 
