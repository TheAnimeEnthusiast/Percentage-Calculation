# Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. Find the percentage he got?

mathScore = float(input("What did you score in maths?"))
scienceScore = float(input("What did you score in science?"))
hindiScore = float(input("What did you score in Hindi?"))
englishScore = float(input("What did you score in english?"))

totalAverage = mathScore + scienceScore + hindiScore + englishScore

print(f"Your total average is {totalAverage/4}")