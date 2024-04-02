# import utils as u


def question1():
    answers = {}
    answers["(a)"] = ""
    answers["(b)"] = ""
    answers["(c)"] = ""
    answers["(d)"] = ""
    return answers


def question2():
    answers = {}
    return answers


def question3():
    answers = {}
    answers["(a)"] = ""
    answers["(b)"] = ""
    answers["(c)"] = ""
    return answers


def question4():
    answers = {}
    answers["(a)"] = ["", ""]
    answers["(b)"] = ["", ""]
    answers["(c)"] = ["", ""]
    answers["(d)"] = ["", ""]
    answers["(e)"] = ["", ""]
    answers["(f)"] = ["", ""]
    return answers


def question5():
    answers = {}
    answers["(a)"] = [""]
    answers["(a) explain"] = [""]
    answers["(b)"] = [""]
    answers["(b) explain"] = [""]
    return answers


def question7():
    answers = {}
    answers["(a)"] = {""}
    answers["(a) explain"] = {""}
    answers["(b)"] = {""}
    answers["(b) explain"] = {""}
    answers["(c)"] = {""}
    answers["(c) explain"] = {""}
    answers["(d)"] = {""}
    answers["(d) explain"] = {""}
    return answers


def question8():
    answers = {}
    #  "yes" or "no"
    answers["(a) dependent"] = ""

    # "yes" or "no"
    answers["(b) conditionally independent"] = ""

    # float
    answers["(c) P(X1=1|+)"] = 0.0
    answers["(c) P(X1=1|-)"] = 0.0
    answers["(c) P(X2=1|+)"] = 0.0
    answers["(c) P(X2=1|-)"] = 0.0
    answers["(c) P(X3=1|+)"] = 0.0
    answers["(c) P(X3=1|-)"] = 0.0

    # class label: "+" or "-"
    answers["(d) example 111 "] = ""
    answers["(d) example 100 "] = ""
    answers["(d) example 010 "] = ""
    answers["(d) example 000 "] = ""

    # float in range [0, 1]
    answers["(d) training error rate "] = 0.0
    return answers


def question9():
    answers = {}

    # integer: 1, 5, or 50
    answers["(a)"] = 0
    answers["(b)"] = 0
    return answers


def question10():
    answers = {}
    # float
    answers["(a) P(A=1|+)"] = 0.0
    # string
    answers["(a) P(A=1|+) explain"] = ""
    # float
    answers["(a) P(B=1|+)"] = 0.0
    answers["(a) P(C=1|+)"] = 0.0
    answers["(a) P(A=1|-)"] = 0.0

    # float
    answers["(b) P(R|+)"] = 0.0
    answers["(b) P(R|-)"] = 0.0
    # string
    answers["(b) label"] = ""

    # float
    answers["(c) P(A=1)"] = 0.0
    answers["(c) P(B=1)"] = 0.0
    answers["(c) P(A=1,B=1)"] = 0.0
    # string "independent" or "dependent"
    answers["(c) Relationship between A and B"] = ""

    # Repeat analysis of part C. Choose the correct keys for answer.
    answers["(d) P(A=1)"] = 0.0
    answers["(d) P(B=0)"] = 0.0
    answers["(d) P(A=1,B=0)"] = 0.0
    # string "independent" or "dependent"
    answers["(d) Relationship between A and B"] = ""

    # float
    answers["(e) P(A=1, B=1|Class=+)"] = 0.0
    answers["(e) P(A=1|Class=+)"] = 0.0
    answers["(e) P(B=1|Class=+)"] = 0.0
    # string: "yes" or "no"
    answers["(e) A and B conditionally independent"] = ""
    answers["(e) A and B conditionally independent, explain"] = ""
    return answers


# ----------------------------------------------------------------------
if __name__ == "__main__":
    answers = {}
    answers["question1"] = question1()
    answers["question2"] = question2()
    answers["question3"] = question3()
    answers["question4"] = question4()
    answers["question5"] = question5()
    answers["question6"] = question6()
    answers["question7"] = question7()
    answers["question8"] = question8()
    answers["question9"] = question9()
    answers["question10"] = question10()
