# KangarooHybrid
KangarooHybrid to help solve the 100 BTC Bitcoin Challenge

This version is a combination of Jean Luc's VanitySearch and Alek76's KangarooHybrid; with small tweaks made by me to speed up the process of finding the private key.

I am setting this up to help capture the 100 BTC Bitcoin challenge ( https://bitcointalk.org/index.php?topic=5218972.0 ) using GPUs only, no CPU function at this time. Also, only Nvidia GPUs work and I only compiled for Windows users. 

For right now, the only challenges we are going after are the ones that have their bitcoin public key exposed (#120, #125, #130, etc....using a version of Pollard's Kangaroo method with distinguished points. 

With many people helping, we should be able to break the #120 puzzle rather quickly, which is worth 1.20 Bitcoins. Members will be paid for the percentage of work they submit. Think of it like a mining pool, but without the automation. I am not a programmer by trade and therefore I do not have the skillsets to set up a server, WITH VALIDATION, to capture everyone's work/submissions.

But it is rather simple to get started and help out and earn some Bitcoin.
  
Step 1: Go to the "Releases" section and download the .exe program, the solver-all.py file, the check1.txt file, the check2.txt file, and the batch (.bat) files.

Step 2: Add all of those files into one folder on your PC.

Step 3: Adjust the batch file to how many GPUs you have or will use. 
Example: 
-gpuId represents the devices. If you are using one GPU, use -gpuId 0; if you use two GPUs 
-gpuId 0,1; if you use three GPUs -gpuid 0,1,2; etc.

Step 4: Double-click/start the batch file and let the program run. You will see tame and wild text files start filling up in the same folder.

Step 5: Once you are ready to submit work, stop the .exe file from running and send me the tame and wild text files (via DM on Discord; DM me and I will send you email address). I have included example batch files to combine your wild and tame files so you only have to send one tame file and one wild file. You will need to adjust the folder path in the wild and tame combine files.

Step 6: Rinse and repeat Steps 4 and 5.

More information here:
https://discord.gg/6ysgcHbC
