# secret-santa
#### Python-streamlit webapp to manage secret santa giftee assignments


This is a just-for-fun, remote, no-unintentional-cheat secret santa giftee assignment (assuming the Mod doesn't go rogue). 
How it works:
1. Spin up the webapp using `streamlit run secret-santa.py` command. 
2. Start a new instance after entering all player names separated by commas.
3. Click on `Generate SecretIds` button to assign a secretId for each player. The mod can view these secretIds on the console and share them privately with all players. 
4. Random match generation: Click on the `Randomly assign santa-giftee pairs` button to simulate the assignment of giftees. So the mod only views the secretIds for all the pairs, but not the pair assignments. 
5. Each player can go to the app, enter their secretId to view their match. 
