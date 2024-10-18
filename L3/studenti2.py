import json
import numpy


def ex1hard(jsonFile):
    data=json.load(open(jsonFile, 'r'))
    count = 0
    for elev, details in data.items():
        # print(elev)
        seminariiMean = numpy.mean(details['seminarii'])
        seminariiPoints = 0
        for i in details['seminarii']:
            seminariiPoints += i

        #print('SP+PP',seminariiPoints + details['proiect'])
        #print('Elevul ', elev, seminariiMean)
        projectGrade = (details['proiect'] / 7)
        #print('PG',projectGrade)
        # teste 30% fiecare. Seminar + proiect 20%
        finalGrade = 0.3 * details['partial']/10 + 0.3 * details['curs']/10 + seminariiMean*0.2 + projectGrade * 0.2
        print('FG', finalGrade)
        if finalGrade >= 4.5:
            count += 1
    return count



if __name__ == '__main__':
    print(ex1hard('studenti.json'))