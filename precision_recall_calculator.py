__auther__ = '''Meareg'''
labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']
label_count_in_predicted = 0
label_count_in_test = 0
TPs = []
FNs = []
FPs = []
predicted_labels = []


#Copy the predicted values into a list
with open('predicted1') as output:
    for line in output:
        line = line[:2]
        predicted_labels.append(line)
    output.close()

# Calculate the True Positives (TP) for each class/label
for index in range(0, len(labels)):
    TP = 0
    i = -1
    with open('test1') as fp:
        for line in fp:        
            i+=1    
            if str(line[:2]) == predicted_labels[i] == labels[index]:
                TP += 1
    TPs.append(TP)
    fp.close()
print("True Positives")    
print(TPs)

# Calculate the False Positive (FP) for each class/label
FP = 0
label_count_in_predicted = 0
for i in range(0, len(labels)):
    for index in range(0, len(predicted_labels)):            
        if predicted_labels[index] == labels[i]:
                label_count_in_predicted += 1
    FP = label_count_in_predicted - TPs[i]
    FPs.append(FP)
    FP = 0
print ("False positives for each class")
print (FPs)

# Calculate the False Negative (FN) for each class/label
FN = 0
for i in range(0, len(labels)):
    with open('test1') as testfile:
        label_count_in_test = 0
        for line in testfile:
            line = line[:2]
            if line == labels[i]:
                label_count_in_test += 1
    FN = label_count_in_test - TPs[i]
    FNs.append(FN)
    FN= 0
    testfile.close()
print ("False negatives for each class")
print(FNs)

# Calculate Precision (Precision = TP/(FP+TP)) for each class/label
class_precision = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10':0, '11':0, '12':0, '13':0, '14':0, '15':0, '16':0, '17':0, '18':0, '19':0, '20':0, '21':0, '22':0, '23':0, '24':0, '25':0, '26':0, '27':0, '28':0, '29':0, '30':0, '31':0, '32':0, '33':0, '34':0, '35':0, '36':0, '37':0, '38':0, '39':0, '40':0, '41':0, '42':0, '43':0}

precisions = []
for i in range (1, len(class_precision)+1):
    TPFP = TPs[i-1]+FPs[i-1]
    if TPFP > 0:
        precision = TPs[i-1]/TPFP
        precisions.append(precision)
print("Precisions")
print (precisions)

# Calculate Recall (Recall = TP/(FN+TP)) for each class/label
recalls = []
for i in range (0, len(class_precision)):
    TPFN = FNs[i]+TPs[i]
    if TPFN > 0:
        recall = TPs[i]/TPFN
        recalls.append(recall)
print("Recalls")
print (recalls)




        #class_precision[str[i]] = TPs[i]/TPFP
        #print (class_precision[str[i]])
#class_pre = {'c1':0, 'c2':0, 'c3':0, 'c4':0, 'c5':0, 'c6':0, 'c7':0, 'c8':0, 'c9':0, 'c10':0, 'c11':0, 'c12':0, 'c13':0, 'c14':0, 'c15':0, 'c16':0, 'c17':0, 'c18':0, 'c19':0, 'c20':0, 'c21':0, 'c22':0, 'c23':0, 'c24':0, 'c25':0, 'c26':0, 'c27':0, 'c28':0, 'c29':0, 'c30':0, 'c31':0, 'c32':0, 'c33':0, 'c34':0, 'c35':0, 'c36':0, 'c37':0, 'c38':0, 'c39':0, 'c40':0, 'c41':0, 'c42':0, 'c43':'0'}

