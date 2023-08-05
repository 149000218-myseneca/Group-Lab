# Group-Lab 

**Group Member 1: Priyank Yogesh Panchal (149000218)**  
**Group Member 2: Darshit Parimal Patel (148634215)**  
**Group Member 3: Dev Patel**  

============================================================  
### [Role Assigned](#header)   
============================================================  

**Group Member 1: Priyank Yogesh Panchal (149000218)**  
-- Will execute and design python code and works as python developer. He performs the task assigned and suggest by QA Tester and take care of performing code in proper executable manner according to workflow.  

**Group Member 2: Darshit Parimal Patel (148634215)**  
-- Will act as a QA Tester of the game, will figure out issues, suggest how to make sure it works fine and helps in developing python code. He will design the workflow and guides in the process of step-by-step execution.  

**Group Member 3: Dev Patel**  
-- Will perform the QA Testing#2 and design the workflow, handles the github submission. Also, Helps in developing python code.  
 
============================================================  
### [Algorithmic Explanation of how the Game Works](#header)   
============================================================  

**1) Initialize Options:-**  
-- Have to create a list called "option" containing the strings "rock","paper" and "scissors"

**2) Game Loop:-**  
-- Start loop to keep game running until the player decides to exit

**3) Computer's Choice**   
-- Use the 'random.choice(options)' function to select a random choice from any rock, paper or scissor

**4) Player's Turn**  
-- Print Welcome Message & Prompt player to choose their choice (Not Case Sensitive)

**5) Comparison & Outcome**  
-- Compare both the choices of player and computer  
--> If they are equal, print "Its a Tie" and End the game loop.  
--> Otherwise, Proceed to determine winner based on the rules like :-  
    --> If player choose "rock"  
        --> If the computer choose "scissors", print "You Win"   
        --> If computer choose "paper", print "Computer Wins"  
    --> If player choose "paper"  
        --> If computer choose "rock", print "You Win"  
        --> If computer choose "scissors", print "Computer Wins"  
    --> If player choose "scissors"  
        --> If computer choose "paper", print "You Win"  
        --> If computer choose "rock", print "Computer Wins"  

**6) Play Again:-**  
-- Ask Player to choose if they want to play another round or not by parameters of "Yes" or "No"  
    --> If user choose "yes", return to the player's turn  
    --> If user choose "no", end the loop  

**7) End of Game**  
-- Print final "GoodBye" message  

============================================================  
### Design
### [Flowchart/WorkFlow of Game](#header)   
============================================================  

<img src="https://github.com/149000218-myseneca/Group-Lab/blob/8fd123ffee9b540fc857ced953f3fbf9dc4a2291/Diagram.jpeg"></img>  

============================================================  
### Development - Iteration #1  
============================================================  

**1) Proof of cloning repository**  

Command Used  
``` git clone https://github.com/149000218-myseneca/Group-Lab.git```

Screenshot :-

<img src="https://github.com/149000218-myseneca/Group-Lab/blob/99afcff5fdf6452dc07d9aae06526549bec9e89a/SS-1.png"></img>  

**2) Command used to create new branch**  

Command Used  
``` git checkout -b Iteration1 ```  

Screenshot :-  

<img src="https://github.com/149000218-myseneca/Group-Lab/blob/4c61062ea69d2ca4f5a7288ac5d1bbf48322ce57/SS-2.png"></img>  

**3) Command used to switch branch**  

Command Used  
``` git checkout ```   
``` git branch ```  

Screenshot :-  

<img src="https://github.com/149000218-myseneca/Group-Lab/blob/4c61062ea69d2ca4f5a7288ac5d1bbf48322ce57/SS-2.png"></img>  

**4) Commiting changes to Iteration1**  

Command Used  
``` git add MainGame.py ```  
``` git commit -m "Rock, Paper, Scissor Game" ```  

Screenshot :-  

<img src="https://github.com/149000218-myseneca/Group-Lab/blob/4c61062ea69d2ca4f5a7288ac5d1bbf48322ce57/SS-3.png"></img>  

**5) Pushing changes to Iteration1 Branch**  

Command Used  
``` git push origin Iteration1 ```

Screenshot :-  

<img src="https://github.com/149000218-myseneca/Group-Lab/blob/4c61062ea69d2ca4f5a7288ac5d1bbf48322ce57/SS-4.png"></img> 

============================================================  
### QA Testing #1 
============================================================ 

**1) Errors Faced**  

Screenshot :-  
<img src="https://github.com/149000218-myseneca/Group-Lab/blob/4c61062ea69d2ca4f5a7288ac5d1bbf48322ce57/SS-5.png"></img>  

**2) Issue Created**

Screenshot :-  
<img src="https://github.com/149000218-myseneca/Group-Lab/blob/4c61062ea69d2ca4f5a7288ac5d1bbf48322ce57/SS-6.png"></img> 

============================================================  
### Development - Iteration #2
============================================================ 

**1) Creating New Branch Iteration2** 

Command Used  
```git checkout -b Iteration2 ```  
``` git branch```  

Screenshot  
<img src="https://github.com/149000218-myseneca/Group-Lab/blob/4c61062ea69d2ca4f5a7288ac5d1bbf48322ce57/SS-7.png"></img>  

**2) Swtich to new branch**  

Command Used  
``` git branch```  

**3) Commiting changes to Iteration2**  

Command Used  
```git add MainGame.py ```  
```git commit -m "Updated exit loop in game " ```  

Screenshot
<img src="https://github.com/149000218-myseneca/Group-Lab/blob/4c61062ea69d2ca4f5a7288ac5d1bbf48322ce57/SS-8.png"></img>

**4) Pushing Changes to Iteration2**  

Command Used  
``` git push origin Iteration2```

Screenshot
<img src="https://github.com/149000218-myseneca/Group-Lab/blob/4c61062ea69d2ca4f5a7288ac5d1bbf48322ce57/SS-9.png"></img>  

============================================================  
### QA Testing :- #2
============================================================ 

**1) Successfully run the game**  

Screenshot  
<img src="https://github.com/149000218-myseneca/Group-Lab/blob/4c61062ea69d2ca4f5a7288ac5d1bbf48322ce57/SS-10.png"></img>  

**2) Close Issue**  

Screenshot  
<img src="https://github.com/149000218-myseneca/Group-Lab/blob/89421a2ce47446952d093c60b32fe82379fad538/SS-12.png"></img>  

============================================================  
### Deploy
============================================================ 

**1) Successfully Merged and Pushed to main Branch**  

Command used to merge & push  
``` git checkout main``` for changing branch from Iteration2 to "main"  
``` git merge Iteration2 ``` to merge updated file successfully
``` git push origin main``` to push files on GitHub

Screenshot   
<img src="https://github.com/149000218-myseneca/Group-Lab/blob/4c61062ea69d2ca4f5a7288ac5d1bbf48322ce57/SS-11.png"></img>  
