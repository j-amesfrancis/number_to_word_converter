from django.shortcuts import render
from gtts import gTTS


# Create your views here.
def home(request):
    if request.method == "POST":
        number = int(request.POST['number'])
        word = convert(number)
        speech = gTTS(text=word, lang='en')
        speech.save('converter/static/speech.mp3')
        return render(request, 'index.html', {"word": word, "number": number})
    return render(request, 'index.html')


def convertToDigit(n, suffix):
    X = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ",
         "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
         "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
         "Seventeen ", "Eighteen ", "Nineteen "]

    Y = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ",
         "Sixty ", "Seventy ", "Eighty ", "Ninety "]

    if n == 0:
        return ""

    # split n if it is more than 19
    if n > 19:
        return Y[n // 10] + X[n % 10] + suffix
    else:
        return X[n] + suffix


# Function to convert a given number (max 9-digits) into words
def convert(n):
    if n == 0:
        return "Zero"

    result = convertToDigit((n // 10000000) % 100, "Crore ")

    # add digits at hundred thousands & one millions place
    result += convertToDigit(((n // 100000) % 100), "Lakh ")

    # add digits at thousands & tens thousands place
    result += convertToDigit(((n // 1000) % 100), "Thousand ")

    # add digit at hundreds place
    result += convertToDigit(((n // 100) % 10), "Hundred ")

    if n > 100 and n % 100:
        result += "and "

    # add digits at ones & tens place
    result += convertToDigit((n % 100), "")

    return result
