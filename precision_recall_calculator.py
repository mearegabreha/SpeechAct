__author__ = 'meareg'

'''Example usage from command prompt enter:
  python3.4 precision_recall_calculator c:/testfile, c:/output '''

from sys import argv, exit
import os.path

def exit_with_help(argv):
	print("""\
Usage:{0} testfile, {1} predicted_output

testfile : the testfile(along its root path)
predicted_outputfile : the predicted values' output file (which is output when the probabilities estimates '-b 1' is used with svm-train.""")
	print(argv[0])
	exit(1)

def precision_recall_calc(testfile, predictfile):
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']
    label_count_in_predicted = 0
    label_count_in_test = 0
    TPs = []
    FNs = []
    FPs = []
    predicted_labels = []
    
#Copy the predicted values into a list
    with open(predictfile) as output:
        for line in output:
            line = line[:2]
            predicted_labels.append(line)
        output.close()
    
# Calculate the True Positives (TP) for each class/label
    for index in range(0, len(labels)):
        TP = 0
        i = -1
        with open(testfile) as fp:
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
        with open(testfile) as test:
            label_count_in_test = 0
            for line in test:
                line = line[:2]
                if line == labels[i]:
                    label_count_in_test += 1
        FN = label_count_in_test - TPs[i]
        FNs.append(FN)
        FN= 0
        test.close()
    print ("False negatives for each class")
    print(FNs)

# Calculate Precision (Precision = TP/(FP+TP)) for each class/label
    precisions = []
    for i in range (0, len(labels)):
        TPFP = TPs[i]+FPs[i]
        if TPFP > 0:
            precision = (TPs[i]/TPFP)*100
            precisions.append(precision)
    print("Precision per class")
    print (precisions)

# Calculate Recall (Recall = TP/(FN+TP)) for each class/label
    recalls = []
    for i in range (0, len(labels)):
        TPFN = FNs[i]+TPs[i]
        if TPFN > 0:
            recall = (TPs[i]/TPFN)*100
            recalls.append(recall)
    print("Recall per class")
    print (recalls)
    return labels, precisions, recalls


def main(argv):
    if len(argv) != 3:
        exit_with_help(argv)
    test_dataset = argv[1]
    predicted = argv[2]
    if not os.path.exists(test_dataset):
        print("dataset {0} not found".format(test_dataset))
        exit(1)
    if not os.path.exists(predicted):
        print("Predicted output {1} not found".format(predicted))
        exit(1)
    precision_recall_calc(test_dataset, predicted)
        
if __name__ == '__main__':
        main(argv)
