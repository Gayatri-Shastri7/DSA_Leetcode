#Convert to letter 
#letter has asci value
#a=97 , 122-z 
#Subtract with 97 to get index value
#word in list(words)
#store in list of string value


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = []
        for word in words:
            morse = ""
            for char in word:
                morse += morse_code[ord(char) - 97]
            if morse not in res:
                res.append(morse)
        
        return(len(res))

        