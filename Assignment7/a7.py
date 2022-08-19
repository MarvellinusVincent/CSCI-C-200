################################
# PROBLEM 1
################################
# In this starter code (different from the pdf), we have also
# added a blank `get` function but you are free to remove it or name it
# differently (but appropriately) to implement the functionality.
# A `get` function is used to obtain the value for objects of a given class.
# For example, in this case since it's Fractions so if I call get on an object of this class
# then the get function should retiurn the reduced representation for that Fraction.
# This could come handy for implementing other related functions in this class.
class Fraction:
    def __init__(self, numerator, denominator):
        for i in range (min(numerator,denominator),0,-1):
            if numerator % i == 0 and denominator % i == 0:
                numerator /= i
                denominator /= i
        self.n = int(numerator)
        self.d = int(denominator)

    def get(self):
        pass

    def __add__(self,other):
        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return Fraction(n,d)
    
    def __mul__(self,other):
        n = self.n * other.n
        d = self.d * other.d
        return Fraction(n,d)

    def __repr__(self):
        string = "frac("
        if self.d > self.n:
            string += str(self.n) + "," + str(self.d) + ")"
        else:
            a = int(self.n/self.d)
            b = self.n % self.d
            c = self.d
            string += str(a) + "," + str(b) + "/" + str(c) + ")"
        return string

    def __eq__(self,other):
        if self.n == other.n and self.d == other.d:
            return True
        return False


################################
# PROBLEM 2
# You likely will need some additional functions
################################

#INPUT takes a letter and shift
#RETURN new letter shifted 
def encrypt(letter, n):
    if letter == "{" or letter == " ":
        return "a"
    enc = ord(letter.lower())
    shift_letter = ((enc - 97 + n) % 27) + 97
    return chr(shift_letter)

#INPUT takes a letter and shift
#RETURN original letter
def decrypt(letter, n):
    if letter == "a":
        return "{"
    dec = ord(letter.lower())
    original_letter = ((dec - 97 - n) % 27) + 97
    return chr(original_letter)

#INPUT takes a sentence of lowercase letters and spaces and shift
#RETURN caeser cypher
def encrypt_sentence(sentence, shift):
    sentence = sentence.replace(" ", "{")
    encrypted_sentence = ""
    for i in sentence:
        encrypted_sentence += encrypt (i,shift)
    return encrypted_sentence

#INPUT takes an encrypted sentence and shift
#RETURN decrypted sentence
def decrypt_sentence(sentence, shift):
    decrypted_sentence = ""
    for i in sentence:
        decrypted_sentence += decrypt(i,shift)
    decrypted_sentence = decrypted_sentence.replace("{"," ")
    return decrypted_sentence





################################
# PROBLEM 3
################################

#the dictionary for the transation
aa_d = {}
#the FASTA file
DNA_d = []

#the translation
actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"


# INPUT path and file name of amino acid file
# RETURN a dictionary 
# Key is a tuple (c0, c1, ... , cn) where ci are codons
# Value is a pair [name, abbreviation] for the amino acid
def get_amino_acids(path,name):
    pass


# INPUT path and file name of amino acid file
# RETURN a list [header, DNA]
# header is first line in the file
# DNA is a string of letters from remainder of file
# no whitespace
def get_DNA(path,name):
    pass  


#INPUT FAST file
#RETURN a string representing the protein
#using the dictionary
def translate(DNA_d):
    pass

# Here is how we set the path and file name as function arguments
# This is done assuming that you run the code from within Assignment7 directory.
# Based on differences in our paths (could be differet based on how VSC is configured on your system), y
# you may or may not need to modify the path i.e. 'Assignment7'. We suggest that you try this asap and
# if file could not be found then, you revise the File IO concepts from lectures/labs
# to properly set the path in these functions.
aa_d = get_amino_acids("Assignment7", "amino_acids.txt")
DNA_d = get_DNA("Assignment7", "DNA.txt")
protein = translate(DNA_d)



################################
# PROBLEM 4
################################
class Function:
    def __init__(self,expression):
        self.Function = eval("lambda x:" + expression)

    def point(self,x):
        return self.Function(x)

    def integral(self,x,y):
        h = (y-x)/4
        d = [x,x+h,x+(2*h),x+(3*h),x+(4*h)]
        return (h/3)*(Function.point(self,d[0]) + Function.point(self,d[4]) + 4*(Function.point(self,d[1]) + Function.point(self,d[3])) + 2*Function.point(self,d[2]))

    def derivative_at_point(self,x):
        return (self.point(x+0.000005)-self.point(x-0.000005))/(2*0.000005)

    def __repr__(self):
        return self.Function




if __name__ == "__main__":
    
    #PROBLEM 1
    # x = 2*3*5
    # y = 2*3*7
    # a = Fraction(x,y)
    # print(a)
    # b = Fraction(1,2)
    # c = Fraction(4,5)
    # d = b + c
    # e = b*c
    # print(f"{b} + {c} = {d}")
    # print(f"{b} * {c} = {e}")
    # print(Fraction(6,2))
    # zz = Fraction(2,4)
    # print(zz,b)
    # print(zz == b)
    # print(b + b == b)


    #PROBLEM 2
    # sentence = "this is a secret message about the class"
    # shift = 5
    # secret = encrypt_sentence(sentence, shift)
    # decode_secret = decrypt_sentence(secret, shift)
    
    # print(f"original: {sentence}")
    # print(f"encrypted: {secret}")
    # print(f"decrypted: {decode_secret}")

    #PROBLEM 3
    # print("Dictionary")
    # print(aa_d)
    # print("FASTA file")
    # print(DNA_d)
    # print("Translations match:", str(protein == actual))

    # # should return "PLHS"    
    # print(translate(["nothing", "CCACTGCACTCA"]))

    # # should returns "D-"
    # print(translate(["nothing", "GACTAA"]))

    #PROBLEM 4
    
    # f0 = Function("1/x")
    # f1 = Function("x**2 - x")
    # f2 = Function("x**2")

    # print(f0)
    # print(f1)
    # print(f2)

    # print(f0.point(10))
    # print(f1.point(2))
    # print(f2.point(3))

    # print(f0.derivative_at_point(10))
    # print(f1.derivative_at_point(2))
    # print(f2.derivative_at_point(3))

    # print(f0.integral(1,2))
    # print(f1.integral(1,4))
    # print(f2.integral(0,3))
    pass
