import i_utils as u
import pytest
from all_questions import *
from tqdm import tqdm
import matplotlib
import pickle



def question1():
    answers = {}

    # type: float
    answers['(a)'] = 0.0288

    # type: float
    answers['(b)'] = 0.002

    # type: float
    answers['(c)'] = 0.008

    return answers
#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: bool
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: bool
    answers['(c) Weight update'] = '0.5*math.log((1-p)/p)'

    # type: bool
    answers['(d) Weight influence'] = 1.5275252316519468

    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    # type: explain_string
    answers['Explain'] = """
        No, because the ensemble of base classifiers gets a better 
        classification performance only when at least some of the 
        base classifiers are better than a random classifier. In 
        this case, all the base classifiers (the coin tosses) are 
        random and therefore, their ensemble would not do any better 
        than any other random classifier. 
    """

    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False

    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'

    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = 'p'

    # type: eval_float
    answers['(a) C2-TPR'] = '2*p'

    # type: eval_float
    answers['(a) C1-FPR'] = 'p'

    # type: eval_float
    answers['(a) C2-FPR'] = '2*p'

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = """
        No, when p takes continuous value in the range [0, 1], both ROC 
        curves of C1 and C2 are the same with the random guess line, 
        which is TPR=FPR.
    """

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) explain'] = """
        Since C1 and C2 are both random classifiers, expected precision 
        for both of them are always the same, so precision contains 
        no information here. Besides, the recall will make C2 a winner, 
        but recall evaluation is just comparing the random probabilities, 
        which is apparently meaningless. In practice, C1 and C2 are 
        equivalent because they are both randomly guessing, so using 
        {TPR and FPR} is more proper for their relative performance.
    """


    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = "None"

    # type: explain_string
    answers['(i) Best classifier, explain'] = """
        None of C1 and C2 is better than the other.  The two classifiers 
        are random, as shown by their TPR/FPR (C1= 0.1/0.1; C2=0.5/0.5), 
        which lies on the random guess line of ROC curve. 
    """

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = "TPR-FPR"

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair, explain'] = """
        Higher F-1 measure might be caused by C2 having a higher 
        probability of assigning an instance to (+) class, which 
        causes more instances to be classified as (+) (but does 
        not mean that those + predictions are accurate)
    """

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = "C3"

    # type: explain_string
    answers['(iii) best classifier, explain'] = """
        C3 is the best classifier because it has the highest TPR/FPR=2. 
        TPR / FPR provides a better evaluation % of a model across 
        different population distribution. So, if C3 is better than C2 
        and C1 based on TPR / % FPR on this dataset, it will still perform 
        similarly when tested on different population with a different 
        distribution.
    """

    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    # String with valid python expression
    answers['(a) precision for C0'] = '1/10'

    # type: eval_float
    # String with valid python expression
    answers['(a) recall for C0'] = 'p'

    # type: eval_float
    # String with valid python expression
    answers['(b) F-measure of C0'] = "(2*p/10) / (p + 1/10)"

    # type: string
    # String with valid python expression
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = "unknown"

    # type: float
    answers['p-range'] = 0.3

    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    answers['(i) metrics'] = {
            'recall':0.53, 
            'precision':0.62, 
            'F-measure':0.57, 
            'accuracy':0.88
        }

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = "F-measure"

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = "accuracy"

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = """
        Accuracy is a poor metric because there is a class imbalance 
        problem (the sunshine (+) class is the minority), so accuracy 
        is not a good indicator in this situation while the 
        F-measure is an appropriate metric.
    """

    return answers

#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = "T1"

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = "T2"

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = """
        In this case, T2 is strictly better than T1 since both have the 
        same TPR and T2 has lower FPR.  Hence for any data set 
        (irrespective of skew), T2 will outperform T1 on any reasonable 
        measures.” Note that the value of F-measure depends on the skew of 
        the data that is being used for evaluation.  In particular, a given 
        classifier will have different F-scores on two different datasets 
        that have different ratio of positive and negative classes. Hence 
        F-score should be used to compare two classifiers only if they 
        are being tested on data sets with similar skew.  For this 
        specific question, if classifiers T1 and T2 were both tested 
        on the same data set (or on two data sets that have identical 
        skew), then T2 will have higher F-score than T1.  The problem 
        arises when we compare the F-score of T1 with F-score T2 but 
        these scores are computed on data sets with different skew.
        The value of TPR/FPR is independent of the skew in the data.  
        Still, it can’t be used as a measure of choice in all situations. 
        In fact, depending on the actual skew in the data, a classifier 
        C1 with better TPR/FPR than C2 can have worse F-score relative 
        to C2.   However, if both classifiers have identical TPR 
        (or FPR), then TPR/FPR can be used to select the best classifier 
        (i.e., classifier with higher TPR/FPR will be superior according 
        to any reasonable measure when the two classifiers are tested 
        on the exact same data set).
    """

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = """
        In a  scenario where you know the skew in the target population 
        matches that in the confusion matrix,  the F measure can be preferred 
        over {TPR/FPR}, as it captures both precision and recall for the target 
        population, and thus allows you to identify a test that does not 
        compromise one of these for the other.
    """

    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
