# THE_PATTERN
TO PRINT ANY WORD IN PATTERN    AND "IMPORTANT !! ONLY CAPITAL WORDS CAN BE PRINTED"



{*The program will run from pattern=input()
*first we define a function gk()
in that function we use for loop to go throgh each alphabet in that for we take range of len(pattern)beacause we want to print a word 
(IF LEN(PATERN)CONTAINS 2 ALPHABETS IT WILL RUN 2 TIMES)

such that when in len(pattern) if a word is GK then it will take (0 as i and 1 as i)so when i=G it will print G simillarly when i!=G IT WILL GO FOR NEXT ALPHABET FOR THIS WE USE IF AND ELIF

ALSO THE NO OF ROWS AND COL TO PRINT THE PATTERNS HAS TO BE SAME THRUOUT EACH ALPHABET

INSTEAD OF PRINTING THE PATTERN WE STORE IN ROW AND COL
then we store that in NESTED list(print_a,the nested list differs for each alphabet) THEN WE CHECK EACH ALPHABET AND the nested list is  APPEND IT TO THE list
the list contains the final output

AFTER THE LOOP COMPLETES IT WILL RETURN list whch is outside of the loop


when the enter word does not satifies the if elif condition it will use else and pirnt invalid
 
**we use list[] to store each alphabet
**we use lst2[]to call the function gk() and print the pattern

IN LAST FOR PRINTING OUR INPUT WE TAKE A FOR LOOP 
IN WHICH FIRST WE TAKE i for range ROW THEN j for range LEN(list2)index and k for range col
then we use print(list2[j][i][k])
and use end="" for space 
and last prin()for new line }
