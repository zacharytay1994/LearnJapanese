import random
import os
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear');
# ----- hiraganaClass -----
class Hiragana:
    # Vowels : a, i, u, e, o, n
    hiraganaVowels = ["あ", "い", "う", "え", "お", "ん"];
    hiraganaVowelsR = ["a", "i", "u", "e", "o", "n"];
    # b/p/h
    # "", "", "", "", ""
    hiraganaBPH = [["ば", "び", "ぶ", "べ", "ぼ"], #b
                   ["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"], #p
                   ["は", "ひ", "ふ", "へ", "ほ"]]; #h
    hiraganaBPHR = [["ba", "bi", "bu", "be", "bo"], #b
                   ["pa", "pi", "pu", "pe", "po"], #p
                   ["ha", "hi", "fu", "he", "ho"]]; #h
    # d/t
    hiraganaDT = [["だ", "ぢ", "づ", "で", "ど"], #d
                  ["た", "ち", "つ", "て", "と"]]; #t [1] = chi/tci [2] = tsu
    hiraganaDTR = [["da", "dji", "dzu", "de", "do"], #d
                  ["ta", "ti", "tsu", "te", "to"]]; #t [1] = chi/tci [2] = tsu

    # g/k
    hiraganaGK = [["が", "ぎ", "ぐ", "げ", "ご"], #g
                  ["か", "き", "く", "け", "こ"]]; #k
    hiraganaGKR = [["ga", "gi", "gu", "ge", "go"], #g
                  ["ka", "ki", "ku", "ke", "ko"]]; #k

    # m/n
    hiraganaMN = [["ま", "み", "む", "め", "も"], #m
                  ["な", "に", "ぬ", "ね", "の"]]; #n
    hiraganaMNR = [["ma", "mi", "mu", "me", "mo"], #m
                  ["na", "ni", "nu", "ne", "no"]]; #n

    # r/s
    hiraganaRS = [["ら", "り", "る", "れ", "ろ"], #r
                  ["さ", "し", "す", "せ", "そ"]]; #s
    hiraganaRSR = [["ra", "ri", "ru", "re", "ro"], #r
                  ["sa", "shi", "su", "se", "so"]]; #s

    # w/y/z
    hiraganaWYZ = [["わ", "ゐ", "", "ゑ", "を"], #w
                   ["や", "", "ゆ", "", "よ"], #y
                   ["ざ", "じ", "ず", "ぜ", "ぞ"]]; #z [2] = ji/zi
    hiraganaWYZR = [["wa", "wi", "", "we", "wo"], #w
                   ["ya", "", "yu", "", "yo"], #y
                   ["za", "ji", "zu", "ze", "zo"]]; #z [2] = ji/zi
    # by/py/hy
    hiraganaBPHy = [["びゃ", "びゅ", "びょ"], #by
                    ["ぴゃ", "ぴゅ", "ぴょ"], #py
                    ["ひゃ", "ひゅ", "ひょ"]]; #hy
    hiraganaBPHyR = [["bya", "byu", "byo"], #by
                    ["pya", "pyu", "pyo"], #py
                    ["hya", "hyu", "hyo"]]; #hy
    # gy/ky
    hiraganaGKy = [["ぎゃ", "ぎゅ", "ぎょ"], #gy
                   ["きゃ", "きゅ", "きょ"]]; #ky
    hiraganaGKyR = [["gya", "gyu", "gyo"], #gy
                   ["kya", "kyu", "kyo"]]; #ky
    # my/ny
    hiraganaMNy = [["みゃ", "みゅ", "みょ"], #my
                   ["にゃ", "にゅ", "にょ"]]; #ny
    hiraganaMNyR = [["mya", "myu", "myo"], #my
                   ["nya", "nyu", "nyo"]]; #ny
    #ry/sh
    hiraganaRSy = [["りゃ", "りゅ", "りょ"], #ry
                   ["しゃ", "しゅ", "しょ"]]; #sh
    hiraganaRSyR = [["rya", "ryu", "ryo"], #ry
                   ["sha", "shu", "sho"]]; #sh
    #ja/za
    hiraganaJZy = [["じゃ", "", "じゅ", "", "じょ"], #ja
                   ["ぢゃ", "", "ぢゅ", "", "ぢょ"]]; #za
    hiraganaJZyR = [["ja", "", "ju", "", "jo"], #ja
                   ["zha", "", "zhu", "", "zho"]]; #za
    # shi/chi/tsu/fu
    hiraganaOutliers = ["し", "ち", "つ" ,"ふ"]

    # Big Bad Hiragana Array
    hiraganaAll = [hiraganaBPH, hiraganaDT, hiraganaGK, hiraganaMN,
                   hiraganaRS, hiraganaWYZ, hiraganaBPHy, hiraganaGKy,hiraganaMNy, hiraganaRSy,
                   hiraganaJZy];
    hiraganaAllR = [hiraganaBPHR, hiraganaDTR, hiraganaGKR, hiraganaMNR,
                   hiraganaRSR, hiraganaWYZR, hiraganaBPHyR, hiraganaGKyR, hiraganaMNyR, hiraganaRSyR,
                   hiraganaJZyR];
###############################
    def hiraToWord(word):
        print ("hello world");
###############################
    def splitWord(self, word):
        holder = "";
        holderList = [];
        index = 0;
        for i in word:
            if (i == "a" or i == "i" or i == "u"
                or i == "e" or i == "o"):
                holder += i;
                holderList.append(holder);
                holder = "";
            elif ((i == "n"
                  and (index == len(word) - 1))
                  or (i == "n"
                  and (word[index+1] != "a" and word[index+1] != "i" and
                                word[index+1] != "u" and word[index+1] != "e" and word[index+1] != "o"))):
                holder += i;
                holderList.append(holder);
                holder = "";
            else:
                holder += i;
            index += 1;
        return holderList;
###############################
    def wordToHira(self, data):
        hiraganaArray = [];
        hiraganaHolder = "";
        firstChar = 0;
        secondChar = 0;
        for i in data:
            if len(i) == 1:
                if (i == "a"):
                    hiraganaHolder += self.hiraganaVowels[0];
                elif (i == "i"):
                    hiraganaHolder += self.hiraganaVowels[1];
                elif (i == "u"):
                    hiraganaHolder += self.hiraganaVowels[2];
                elif (i == "e"):
                    hiraganaHolder += self.hiraganaVowels[3];
                elif (i == "o"):
                    hiraganaHolder += self.hiraganaVowels[4];
                elif (i == "n"):
                    hiraganaHolder += self.hiraganaVowels[5];
            elif len(i) == 2:
                if (i[0] == "w" or i[0] == "y" or i[0] == "z"):
                    hiraganaArray = self.hiraganaWYZ;
                elif (i[0] == "b" or i[0] == "p" or i[0] == "h"):
                    hiraganaArray = self.hiraganaBPH;
                elif (i[0] == "d" or i[0] == "t"):
                    hiraganaArray = self.hiraganaDT;
                elif (i[0] == "g" or i[0] == "k"):
                    hiraganaArray = self.hiraganaGK;
                elif (i[0] == "m" or i[0] == "n"):
                    hiraganaArray = self.hiraganaMN;
                elif (i[0] == "r" or i[0] == "s"):
                    hiraganaArray = self.hiraganaRS;
                elif (i[0] == "j"):
                    hiraganaArray = self.hiraganaJZy;

                if (i[0] == "w" or i[0] == "b" or i[0] == "d" or i[0] == "g" or i[0] == "m" or i[0] == "r"
                    or i[0] == "j"):
                    
                    firstChar = 0;
                elif (i[0] == "y" or i[0] == "p" or i[0] == "t" or i[0] == "k" or i[0] == "n" or i[0] == "s"):
                    firstChar = 1;
                elif (i[0] == "z" or i[0] == "h"):
                    firstChar = 2;

                if (i[1] == "a"):
                    secondChar = 0;
                elif (i[1] == "i"):
                    secondChar = 1;
                elif (i[1] == "u"):
                    secondChar = 2;
                elif (i[1] == "e"):
                    secondChar = 3;
                elif (i[1] == "o"):
                    secondChar = 4;

                hiraganaHolder += hiraganaArray[firstChar][secondChar];
                
            elif len(i) == 3:
                if (i[0] == "b" or i[0] == "p" or i[0] == "h"):
                    hiraganaArray = self.hiraganaBPHy;
                elif (i[0] == "g" or i[0] == "k"):
                    hiraganaArray = self.hiraganaGKy;
                elif (i[0] == "m" or i[0] == "n"):
                    hiraganaArray = self.hiraganaMNy;
                elif (i[0] == "r" or i[0] == "s"):
                    hiraganaArray = self.hiraganaRSy;
                
                if (i[0] == "b" or i[0] == "g" or i[0] == "m" or i[0] == "r"):
                    firstChar = 0;
                elif (i[0] == "p" or i[0] == "k" or i[0] == "n" or i[0] == "s"):
                    firstChar = 1;
                elif (i[0] == "h"):
                    firstChar = 2;

                if (i[2] == "a"):
                    secondChar = 0;
                elif (i[2] == "u"):
                    secondChar = 1;
                elif (i[2] == "o"):
                    secondChar = 2;

                if (i == "shi"):
                    hiraganaHolder += "し";
                elif (i == "chi"):
                    hiraganaHolder += "ち";
                elif (i == "tsu"):
                    hiraganaHolder += "つ";
                elif (i == "fu"):
                    hiraganaHolder += "ふ";
                else:
                    hiraganaHolder += hiraganaArray[firstChar][secondChar];
                
        return hiraganaHolder;

    def randHiraganaArray(self):
        i = 0;
        randHiraHolder = [];
        while (i < 10):
            randNum = random.randint(0, len(self.hiraganaAll[i])-1);
            randNum2 = random.randint(0, len(self.hiraganaAll[i][randNum])-1);
            randHiraHolder.append(self.hiraganaAll[i][randNum][randNum2]);
            randHiraHolder.append(self.hiraganaAllR[i][randNum][randNum2]);
            randNum = random.randint(0, len(self.hiraganaAll[i])-1);
            randNum2 = random.randint(0, len(self.hiraganaAll[i][randNum])-1);
            randHiraHolder.append(self.hiraganaAllR[i][randNum][randNum2]);
            
            i += 1;
        returnHiraHolder = [randHiraHolder, self.hiraganaAllR];
        return returnHiraHolder;

    def randHiraganaArrayR(self):
        i = 0;
        randHiraHolderR = [];
        while (i < 10):
            randNum = random.randint(0, len(self.hiraganaAllR[i])-1);
            randNum2 = random.randint(0, len(self.hiraganaAllR[i][randNum])-1);
            randHiraHolderR.append(self.hiraganaAllR[i][randNum][randNum2]);
            randHiraHolderR.append(self.hiraganaAll[i][randNum][randNum2]);
            randNum = random.randint(0, len(self.hiraganaAllR[i])-1);
            randNum2 = random.randint(0, len(self.hiraganaAllR[i][randNum])-1);
            randHiraHolderR.append(self.hiraganaAll[i][randNum][randNum2]);
            
            i += 1;
        returnHiraHolderR = [randHiraHolderR, self.hiraganaAll];
        return returnHiraHolderR;
# ----- Test -----
class Test:
    def hiraganaIdentifyEasy(self, data):
        startTime = time.time();
        score = 0;
        i = 0;
        testArray = data;
        check = True;
        while (i < 10):
            print("- Hiragana Test (Easy) -");
            print("========================");
            print("Please identify:");
            print("================");
            print(testArray[0][i*3]);
            print("================");
            optionStorage = [];
            randNum = random.randint(0, 3);
            r = 0;
            while (r < 4):
                check = True;
                if (r == randNum):
                    print(str(r+1) + ". " + testArray[0][i*3+1]);
                    optionStorage.append(testArray[0][i*3+1]);
                    #print(testArray[0][i*3+1]);
                else:
                    while (check):
                        if (i < 7): # Number of 2 character questions
                            randAnswer = random.randint(0, len(testArray[1][i])-1);
                            randAnswer2 = random.randint(0, len(testArray[1][randAnswer])-1);
                            randAnswer3 = random.randint(0, len(testArray[1][randAnswer][randAnswer2])-1);
                            answer = testArray[1][randAnswer][randAnswer2][randAnswer3];
                            if (answer != testArray[0][i*3+1]):
                                print(str(r+1) + ". " + answer);
                                optionStorage.append(answer);
                                #print(answer);
                                check = False;
                        else: # Number of 3 character questions
                            randAnswer2 = random.randint(0, len(testArray[1][i])-1);
                            randAnswer3 = random.randint(0, len(testArray[1][i][randAnswer2])-1);
                            answer = testArray[1][i][randAnswer2][randAnswer3];
                            if (answer != testArray[0][i*3+1]):
                                print(str(r+1) + ". " + answer);
                                optionStorage.append(answer);
                                #print(answer);
                                check = False;                   
                r += 1;
            x = input();
            if (optionStorage[int(x)-1] == testArray[0][i*3+1]):
                outputAnswer = "Last question: Correct!";
                score += 1;
            else:
                outputAnswer = ("Last question: Wrong! The correct answer to "
                + testArray[0][i*3] + " is: " + testArray[0][i*3+1]);
                
            cls();
            print("========================");
            print(outputAnswer);
            print("Score: " + str(score));
            print("\n");
            i += 1;
        elapsedTime = time.time() - startTime;
        print("You took %.1f seconds to complete." %(elapsedTime));
        print("Your score is: " + str(score) + "/10");
        experienceGained = ((score/10)/elapsedTime)*10000;
        print("Experience Gained: %.1f" %(experienceGained));
        print("Press Any Enter To Continue");
        #if (experienceGained > int(highScore)):
        #    return round(experienceGained, 0);
        #else:
        #    return round(highScore, 0);
        z = input();
        
    def hiraganaIdentifyMedium(self, data):
        startTime = time.time();
        score = 0;
        i = 0;
        testArray = data;
        check = True;
        while (i < 10):
            print("- Hiragana Test (Medium) -");
            print("==========================");
            print("Please identify:");
            print("================");
            print(testArray[0][i*3]);
            print("================");
            optionStorage = [];
            randNum = random.randint(0, 3);
            r = 0;
            while (r < 4):
                check = True;
                if (r == randNum):
                    print(str(r+1) + ". " + testArray[0][i*3+1]);
                    optionStorage.append(testArray[0][i*3+1]);
                    #print(testArray[0][i*3+1]);
                else:
                    while (check):
                        if (i < 7): # Number of 2 character questions
                            randAnswer = random.randint(0, len(testArray[1][i])-1);
                            randAnswer2 = random.randint(0, len(testArray[1][randAnswer])-1);
                            randAnswer3 = random.randint(0, len(testArray[1][randAnswer][randAnswer2])-1);
                            answer = testArray[1][randAnswer][randAnswer2][randAnswer3];
                            if (answer != testArray[0][i*3+1]):
                                print(str(r+1) + ". " + answer);
                                optionStorage.append(answer);
                                #print(answer);
                                check = False;
                        else: # Number of 3 character questions
                            randAnswer2 = random.randint(0, len(testArray[1][i])-1);
                            randAnswer3 = random.randint(0, len(testArray[1][i][randAnswer2])-1);
                            answer = testArray[1][i][randAnswer2][randAnswer3];
                            if (answer != testArray[0][i*3+1]):
                                print(str(r+1) + ". " + answer);
                                optionStorage.append(answer);
                                #print(answer);
                                check = False;                   
                r += 1;
            x = input();
            if (optionStorage[int(x)-1] == testArray[0][i*3+1]):
                outputAnswer = "Last question: Correct!";
                score += 1;
            else:
                outputAnswer = ("Last question: Wrong! The correct answer to "
                + testArray[0][i*3] + " is: " + testArray[0][i*3+1]);
            #print(x);
            #print(optionStorage[0]);
            cls();
            print("==========================");
            print(outputAnswer);
            print("\n");
            i += 1;
        elapsedTime = time.time() - startTime;
        print("You took %.1f seconds to complete." %(elapsedTime));
        print("Your score is: " + str(score) + "/10");
        experienceGained = ((score/10)/elapsedTime)*10000;
        print("Experience Gained: %.1f" %(experienceGained));
        print("Press Any Enter To Continue");
        #if (experienceGained > int(highScore)):
        #    return round(experienceGained, 0);
        #else:
        #    return round(highScore, 0);
        z = input();

    def hiraganaIdentifyHard(self, data):
        i = 0;
        testArray = data;
        while (i < 10):
            print("- Hiragana Test (Hard) -");
            print("========================");
            print("Please identify:");
            print("================");
            print(testArray[0][i*3]);
            print("================");          
            x = input();
            if (x == testArray[0][i*3+1]):
                outputAnswer = "Last question: Correct!";
            else:
                outputAnswer = ("Last question: Wrong! The correct answer to "
                + testArray[0][i*3] + " is: " + testArray[0][i*3+1]);
            #print(x);
            #print(optionStorage[0]);
            cls();
            print("==========================");
            print(outputAnswer);
            print("\n");
            i += 1;
# ----- Menu -----
class Menu:
    def initMenuOne(self, h, t):
        x = 0;
        check = True;
        #file = open("score.txt", "r");
        #scoreOne = file.readline();
        #scoreTwo = file.readline();
        #scoreThree = file.readline();
        #file.close();
        while (check):
            cls();
            print("Welcome to the Japanese Study Session ~ ようこそ");
            print("===============================================");
            print("1. Take the Hiragana Test (Easy)")#, Highscore: %s" %(scoreOne));
            print("2. Take the Hiragana Test (Medium)")#, Highscore: %s" %(scoreTwo));
            print("3. Take the Hiragana Test (Hard)")#, Highscore: %s" %(scoreThree));
            x = input();

            if (int(x) == 1): 
                cls();
                test = h.randHiraganaArray();
                scoreOne = t.hiraganaIdentifyEasy(test);
            elif (int(x) == 2):
                cls();
                test = h.randHiraganaArrayR();
                scoreTwo = t.hiraganaIdentifyMedium(test);

            elif (int(x) == 3):
                cls();
                test = h.randHiraganaArray();
                t.hiraganaIdentifyHard(test);

            #file = open("score.txt", "w");
            #file.write(str(scoreOne));
            #file.close();
            #file = open("score.txt", "a");
            #file.write(str(scoreTwo));
            #file.write(str(scoreThree));
            #file.close();
# ----- Main -----
                                  
h = Hiragana(); # Init Hirgana
t = Test(); # Init Test
m = Menu(); # Init Menu
m.initMenuOne(h, t);
