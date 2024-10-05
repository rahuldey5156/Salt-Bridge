Step 1. Generate the salt bridge datafiles using VMD
Step 2. Run the salt_bridge_1.py to get the total salt bridge values at each frame. It will create a datafile named total_salt_bridge.dat
Step 3. Make a directory named 'final_salt_bridge' inside the present directory
Step 4. Run the salt_bridge_2.py to generate a sh file
Step 5. Run the sh file. This will move the datafiles to 'final_salt_bridge' directory which has highest salt bridge values. (Top 40 datafiles with highest value of salt bridge)
Step 6. In the 'final_salt_bridge' directory, run the 'intra.sh' and 'inter.sh' scripts.
Step 7. Inside the 'inter' directory, run the inter.py script to generate a datafile that will have the sorted order of files with high value of salt bridge.
Step 8. Inside the 'intra' directory, run the intra.py script to generate a datafile that will have the sorted order of files with high value of salt bridge.
