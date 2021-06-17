import random
class WordGame:
    gameWord='UNDERSTOOD'
    l=3
    
    def randomWord(self): 
        rW=['sathyaa','sooryaa','ramya','jayanthi','vengat']
        return (random.choice(rW))

    def verifyWord(self, inputWord):
        if(inputWord==self.gameWord):
            return True
        else:
            return False
        
   
    def verifyLetter(self,a,encryptedWord):
        
        gW=self.gameWord
        newEncryptedWord=''
        if a in self.gameWord:
            for i in range(0,len(gW)):
            
                if (gW[i]==a):
                    newEncryptedWord=newEncryptedWord+gW[i]
                else:
                    newEncryptedWord=newEncryptedWord+encryptedWord[i]
                    

            return newEncryptedWord
        else:
            
            return encryptedWord
    
    def encryptWord(self):
        
        gW=self.gameWord
        encryptedWord=''
        for i in range(0,len(gW)):
            if (i%2==0) or (i==len(gW)-1):
                encryptedWord=encryptedWord+gW[i]
            else:
                encryptedWord=encryptedWord+'_'
                

        return encryptedWord
        
        

    def startGame(self,a):
        
        if(a!='RANDOM'):
            self.gameWord=a
        else:
            self.gameWord=self.randomWord()
        i=3
        newEncryptedWord=''
        print("Guess the below word:")
        print(self.encryptWord())
        print("__________\n|       |\n|\n|\n|\n|\n|__________")
        a=input("guess letter:")
        
        
        print (self.verifyLetter(a,self.encryptWord()))
        newEncryptedWord=self.verifyLetter(a,self.encryptWord())
        if (newEncryptedWord==self.encryptWord()):
            self.l=self.l-1
            print("try again ",self.l,"chances remaining")
        else:
            print("correct!try again,", self.l,"chance remaining")
       
        
        while(self.l!=0):
               
            if(self.verifyWord(newEncryptedWord)):
                print("Congrats!! you guessed it right")
                break
            else:
                #print("try again",i," chances remaining")
                chance=input("enter:")
                print(self.verifyLetter(chance,newEncryptedWord))
                newEncryptedWords=self.verifyLetter(chance,newEncryptedWord)
                if (newEncryptedWord==newEncryptedWords):
                    if(self.l-1==0):
                        print("Sorry you lost the game \nGAME OVER")
                        break
                    self.l=self.l-1
                    print("try again ",self.l,"chances remaining")
                   
                else:
                   
                    if(self.verifyWord(self.verifyLetter(chance,newEncryptedWords))):
                        print("Congrats!! you guessed it right\n GAME OVER")
                        break
                    newEncryptedWord=self.verifyLetter(chance,newEncryptedWords)
                    print("correct!try again",self.l,"chance remaining")
                if (self.l==3):
                    print("__________\n|       |\n|\n|\n|\n|\n|__________")
                    
                elif (self.l==2):
                        print("__________\n|       |\n|      (.)\n|\n|\n|\n|__________")
                elif (self.l==1):
                        print("__________\n|       |\n|      (.)\n|      /|\ \n|\n|\n|__________")
                elif (self.l==0):
                        print("__________\n|       |\n|      (.)\n|      /|\ \n|      / \ \n|\n|__________")        
                    
                
            
            
                
    

game=WordGame()
game.startGame(game.randomWord())

        
        
        
