__author__ = 'rodas'



def clean():
    with open('corpus/lsi-corpusR.txt', 'r') as f:
        lines = f.readlines()
    f= open("corpus/lsi-corpusR.txt", "wb")
    tmp = ['1[]','2[]','3[]','4[]','5[]','6[]','7[]','8[]','9[]','10[]','11[]','12[]','13[]','14[]','15[]','16[]',
           '17[]','18[]','19[]','20[]','21[]','22[]','23[]','24[]','25[]','26[]','27[]','28[]','29[]','30[]','31[]',
           '32[]','33[]','34[]','35[]','36[]','37[]','38[]','39[]','40[]','41[]','42[]','43[]','44[]']
    for l in lines:
        if( l.rstrip() not in tmp):
            f.writelines(l)
    f.close()

    with open('corpus/lsi-corpusR.txt', 'r') as f:
        lines = f.readlines()
    f= open("corpus/lsi-corpusR.txt", "wb")

    for l in lines:
        f.writelines(l.replace('), (','  '))
    f.close()

    with open('corpus/lsi-corpusR.txt', 'r') as f:
        lines = f.readlines()
    f= open("corpus/lsi-corpusR.txt", "wb")

    for l in lines:
        f.writelines(l.replace(',',':'))

    f.close()

    with open('corpus/lsi-corpusR.txt', 'r') as f:
        lines = f.readlines()
    f= open("corpus/lsi-corpusR.txt", "wb")

    for l in lines:
        f.writelines(l.replace('[(',' '))
    f.close()

    with open('corpus/lsi-corpusR.txt', 'r') as f:
        lines = f.readlines()
    f= open("corpus/lsi-corpusR.txt", "wb")

    for l in lines:
        f.writelines(l.replace(')]',''))

if __name__ == '__main__':
     clean()
