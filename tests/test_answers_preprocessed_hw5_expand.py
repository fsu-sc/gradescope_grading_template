
from pytest_utils.decorators import max_score, visibility, hide_errors
import assert_utilities  # <<< SHOULD be specified in config
from my_fixtures import *   
#import my_fixtures
import numpy as np
import yaml
# pytest might change the python path. Make sure to import it last. 
# import pytest

with open('type_handlers.yaml', 'r') as f:
    type_handlers = yaml.safe_load(f)

@max_score(20)
@hide_errors('')
def test_answers_question1_a_float(run_compute):
    function_name = test_answers_question1_a_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(a)' not in correct_answer:
        explanation = "Key: '(a)' not found in instructor answer!\n"
        test_answers_question1_a_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a)']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(a)' not in student_answer:
        explanation = "Key: '(a)' not found in student answer!\n"
        test_answers_question1_a_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a)']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_float(student_answer, instructor_answer, rel_tol, abs_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    note = 'Calculate the probability.'
    function_name.note = note
    answer_type = 'float'
    question_id = 'question1'
    subquestion_id = '(a)'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question1_a_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question1_b_float(run_compute):
    function_name = test_answers_question1_b_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(b)' not in correct_answer:
        explanation = "Key: '(b)' not found in instructor answer!\n"
        test_answers_question1_b_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b)']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(b)' not in student_answer:
        explanation = "Key: '(b)' not found in student answer!\n"
        test_answers_question1_b_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b)']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_float(student_answer, instructor_answer, rel_tol, abs_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    note = 'Calculate the probability.'
    function_name.note = note
    answer_type = 'float'
    question_id = 'question1'
    subquestion_id = '(b)'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question1_b_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question1_c_float(run_compute):
    function_name = test_answers_question1_c_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(c)' not in correct_answer:
        explanation = "Key: '(c)' not found in instructor answer!\n"
        test_answers_question1_c_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c)']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(c)' not in student_answer:
        explanation = "Key: '(c)' not found in student answer!\n"
        test_answers_question1_c_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c)']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_float(student_answer, instructor_answer, rel_tol, abs_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    note = 'Calculate the probability.'
    function_name.note = note
    answer_type = 'float'
    question_id = 'question1'
    subquestion_id = '(c)'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question1_c_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question2_a_A_bool(run_compute):
    function_name = test_answers_question2_a_A_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(a) A' not in correct_answer:
        explanation = "Key: '(a) A' not found in instructor answer!\n"
        test_answers_question2_a_A_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) A']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(a) A' not in student_answer:
        explanation = "Key: '(a) A' not found in student answer!\n"
        test_answers_question2_a_A_bool.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) A']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_note = 'Boosting reduces bias by focusing more on the instances that previous  models misclassified. This is achieved by assigning higher weights to  the misclassified instances, ensuring they are given more importance  in subsequent models.\n'
    function_name.answer_note = answer_note
    answer_type = 'bool'
    question_id = 'question2'
    subquestion_id = '(a) A'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question2_a_A_bool.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question2_a_B_bool(run_compute):
    function_name = test_answers_question2_a_B_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(a) B' not in correct_answer:
        explanation = "Key: '(a) B' not found in instructor answer!\n"
        test_answers_question2_a_B_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) B']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(a) B' not in student_answer:
        explanation = "Key: '(a) B' not found in student answer!\n"
        test_answers_question2_a_B_bool.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) B']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_note = 'Boosting does not employ parallel model training; it is an iterative  process where each model is trained sequentially, with each model  learning from the errors of its predecessors.\n'
    function_name.answer_note = answer_note
    answer_type = 'bool'
    question_id = 'question2'
    subquestion_id = '(a) B'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question2_a_B_bool.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question2_a_C_bool(run_compute):
    function_name = test_answers_question2_a_C_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(a) C' not in correct_answer:
        explanation = "Key: '(a) C' not found in instructor answer!\n"
        test_answers_question2_a_C_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) C']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(a) C' not in student_answer:
        explanation = "Key: '(a) C' not found in student answer!\n"
        test_answers_question2_a_C_bool.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) C']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_note = 'Boosting does not increase model diversity by training each model on  a random subset of the dataset. This description more accurately fits  bagging techniques, such as Random Forest, where each model is trained  independently on a random subset of the data. In contrast, boosting focuses  on instances that are harder to classify, adjusting weights after each iteration.\n'
    function_name.answer_note = answer_note
    answer_type = 'bool'
    question_id = 'question2'
    subquestion_id = '(a) C'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question2_a_C_bool.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question2_a_D_bool(run_compute):
    function_name = test_answers_question2_a_D_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(a) D' not in correct_answer:
        explanation = "Key: '(a) D' not found in instructor answer!\n"
        test_answers_question2_a_D_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) D']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(a) D' not in student_answer:
        explanation = "Key: '(a) D' not found in student answer!\n"
        test_answers_question2_a_D_bool.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) D']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_note = 'Boosting assigns weights to each training instance, adjusting these weights  after each round to prioritize harder-to-classify instances in subsequent models.  This dynamic weighting is a fundamental aspect of boosting, enabling it to  focus iteratively on the instances that previous models misclassified.\n'
    function_name.answer_note = answer_note
    answer_type = 'bool'
    question_id = 'question2'
    subquestion_id = '(a) D'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question2_a_D_bool.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question2_b_A_bool(run_compute):
    function_name = test_answers_question2_b_A_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(b) A' not in correct_answer:
        explanation = "Key: '(b) A' not found in instructor answer!\n"
        test_answers_question2_b_A_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) A']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(b) A' not in student_answer:
        explanation = "Key: '(b) A' not found in student answer!\n"
        test_answers_question2_b_A_bool.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) A']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_note = "Boosting can significantly increase the model's variance due to the high weight it may place on outliers. In boosting, misclassified instances are given higher weights in subsequent rounds. If an outlier is consistently misclassified, it may receive an increasingly high weight, causing the model to overfit to that specific instance. This can lead to increased variance and reduced generalization performance on unseen data."
    function_name.answer_note = answer_note
    answer_type = 'bool'
    question_id = 'question2'
    subquestion_id = '(b) A'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question2_b_A_bool.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question2_b_B_False(run_compute):
    function_name = test_answers_question2_b_B_False
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(b) B' not in correct_answer:
        explanation = "Key: '(b) B' not found in instructor answer!\n"
        test_answers_question2_b_B_False.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) B']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(b) B' not in student_answer:
        explanation = "Key: '(b) B' not found in student answer!\n"
        test_answers_question2_b_B_False.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) B']
    print('type False NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question2_b_C_bool(run_compute):
    function_name = test_answers_question2_b_C_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(b) C' not in correct_answer:
        explanation = "Key: '(b) C' not found in instructor answer!\n"
        test_answers_question2_b_C_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) C']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(b) C' not in student_answer:
        explanation = "Key: '(b) C' not found in student answer!\n"
        test_answers_question2_b_C_bool.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) C']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_note = 'The sequential nature of boosting can lead to increased training times compared to bagging. In boosting, each model is trained sequentially, with the weights of the instances being adjusted based on the performance of the previous models. This sequential process can be computationally expensive, especially when dealing with large datasets or complex models. In contrast, bagging can be parallelized since each model is trained independently on a bootstrap sample of the data.'
    function_name.answer_note = answer_note
    answer_type = 'bool'
    question_id = 'question2'
    subquestion_id = '(b) C'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question2_b_C_bool.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question2_b_A_bool(run_compute):
    function_name = test_answers_question2_b_A_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(b) A' not in correct_answer:
        explanation = "Key: '(b) A' not found in instructor answer!\n"
        test_answers_question2_b_A_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) A']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(b) A' not in student_answer:
        explanation = "Key: '(b) A' not found in student answer!\n"
        test_answers_question2_b_A_bool.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) A']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_note = "Boosting's focus on reducing bias does not necessarily make it less susceptible to overfitting compared to other ensemble methods. While boosting is effective at reducing bias, it can still overfit to the training data if not properly regularized. The high weights assigned to misclassified instances, especially outliers, can lead to overfitting. Techniques like early stopping, regularization, or using a validation set can help mitigate overfitting in boosting. Other ensemble methods, such as bagging or random forests, can be less prone to overfitting due to their randomization techniques."
    function_name.answer_note = answer_note
    answer_type = 'bool'
    question_id = 'question2'
    subquestion_id = '(b) A'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question2_b_A_bool.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question2_c_Weight_update_eval_float(run_compute):
    function_name = test_answers_question2_c_Weight_update_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(c) Weight update' not in correct_answer:
        explanation = "Key: '(c) Weight update' not found in instructor answer!\n"
        test_answers_question2_c_Weight_update_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) Weight update']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(c) Weight update' not in student_answer:
        explanation = "Key: '(c) Weight update' not found in student answer!\n"
        test_answers_question2_c_Weight_update_eval_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) Weight update']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_eval_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_eval_float(student_answer, instructor_answer, local_vars_dict, rel_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    local_vars_dict = {'p': [0.2, 0.4]}
    local_namespace['local_vars_dict'] = local_vars_dict
    choices = []
    local_namespace['choices'] = choices
    note = "The formulas should only use the variable 'p'. The formulas should be a valid Python expression. Use the functions in the math module as required."
    function_name.note = note
    answer_type = 'eval_float'
    question_id = 'question2'
    subquestion_id = '(c) Weight update'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question2_c_Weight_update_eval_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question2_d_Weight_influence_float(run_compute):
    function_name = test_answers_question2_d_Weight_influence_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(d) Weight influence' not in correct_answer:
        explanation = "Key: '(d) Weight influence' not found in instructor answer!\n"
        test_answers_question2_d_Weight_influence_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) Weight influence']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(d) Weight influence' not in student_answer:
        explanation = "Key: '(d) Weight influence' not found in student answer!\n"
        test_answers_question2_d_Weight_influence_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d) Weight influence']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_float(student_answer, instructor_answer, rel_tol, abs_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    note = 'the answer should be correct to 3 significant digits'
    function_name.note = note
    answer_type = 'float'
    question_id = 'question2'
    subquestion_id = '(d) Weight influence'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question2_d_Weight_influence_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question3_Agree_ques_string(run_compute):
    function_name = test_answers_question3_Agree_ques_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question3', 'i', **kwargs)
    if 'Agree?' not in correct_answer:
        explanation = "Key: 'Agree?' not found in instructor answer!\n"
        test_answers_question3_Agree_ques_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['Agree?']
    student_answer = run_compute('all_questions', 'question3', 's', **kwargs)
    if 'Agree?' not in student_answer:
        explanation = "Key: 'Agree?' not found in student answer!\n"
        test_answers_question3_Agree_ques_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['Agree?']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question3_Explain_explain_string(run_compute):
    function_name = test_answers_question3_Explain_explain_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question3', 'i', **kwargs)
    if 'Explain' not in correct_answer:
        explanation = "Key: 'Explain' not found in instructor answer!\n"
        test_answers_question3_Explain_explain_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['Explain']
    student_answer = run_compute('all_questions', 'question3', 's', **kwargs)
    if 'Explain' not in student_answer:
        explanation = "Key: 'Explain' not found in student answer!\n"
        test_answers_question3_Explain_explain_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['Explain']
    print('type explain_string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question4_a_e_0_dot_5_comma_independent_bool(run_compute):
    function_name = test_answers_question4_a_e_0_dot_5_comma_independent_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question4', 'i', **kwargs)
    if '(a) e=0.5, independent' not in correct_answer:
        explanation = "Key: '(a) e=0.5, independent' not found in instructor answer!\n"
        test_answers_question4_a_e_0_dot_5_comma_independent_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) e=0.5, independent']
    student_answer = run_compute('all_questions', 'question4', 's', **kwargs)
    if '(a) e=0.5, independent' not in student_answer:
        explanation = "Key: '(a) e=0.5, independent' not found in student answer!\n"
        test_answers_question4_a_e_0_dot_5_comma_independent_bool.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) e=0.5, independent']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'bool'
    question_id = 'question4'
    subquestion_id = '(a) e=0.5, independent'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question4_a_e_0_dot_5_comma_independent_bool.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question4_b_comma_independent_bool(run_compute):
    function_name = test_answers_question4_b_comma_independent_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question4', 'i', **kwargs)
    if '(b), independent' not in correct_answer:
        explanation = "Key: '(b), independent' not found in instructor answer!\n"
        test_answers_question4_b_comma_independent_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b), independent']
    student_answer = run_compute('all_questions', 'question4', 's', **kwargs)
    if '(b), independent' not in student_answer:
        explanation = "Key: '(b), independent' not found in student answer!\n"
        test_answers_question4_b_comma_independent_bool.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b), independent']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'bool'
    question_id = 'question4'
    subquestion_id = '(b), independent'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question4_b_comma_independent_bool.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question4_c_identical_bool(run_compute):
    function_name = test_answers_question4_c_identical_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question4', 'i', **kwargs)
    if '(c) identical' not in correct_answer:
        explanation = "Key: '(c) identical' not found in instructor answer!\n"
        test_answers_question4_c_identical_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) identical']
    student_answer = run_compute('all_questions', 'question4', 's', **kwargs)
    if '(c) identical' not in student_answer:
        explanation = "Key: '(c) identical' not found in student answer!\n"
        test_answers_question4_c_identical_bool.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) identical']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'bool'
    question_id = 'question4'
    subquestion_id = '(c) identical'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question4_c_identical_bool.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question5_a_string(run_compute):
    function_name = test_answers_question5_a_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question5', 'i', **kwargs)
    if '(a)' not in correct_answer:
        explanation = "Key: '(a)' not found in instructor answer!\n"
        test_answers_question5_a_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a)']
    student_answer = run_compute('all_questions', 'question5', 's', **kwargs)
    if '(a)' not in student_answer:
        explanation = "Key: '(a)' not found in student answer!\n"
        test_answers_question5_a_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a)']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question5_b_string(run_compute):
    function_name = test_answers_question5_b_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question5', 'i', **kwargs)
    if '(b)' not in correct_answer:
        explanation = "Key: '(b)' not found in instructor answer!\n"
        test_answers_question5_b_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b)']
    student_answer = run_compute('all_questions', 'question5', 's', **kwargs)
    if '(b)' not in student_answer:
        explanation = "Key: '(b)' not found in student answer!\n"
        test_answers_question5_b_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b)']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question5_c_string(run_compute):
    function_name = test_answers_question5_c_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question5', 'i', **kwargs)
    if '(c)' not in correct_answer:
        explanation = "Key: '(c)' not found in instructor answer!\n"
        test_answers_question5_c_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c)']
    student_answer = run_compute('all_questions', 'question5', 's', **kwargs)
    if '(c)' not in student_answer:
        explanation = "Key: '(c)' not found in student answer!\n"
        test_answers_question5_c_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c)']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question5_d_string(run_compute):
    function_name = test_answers_question5_d_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question5', 'i', **kwargs)
    if '(d)' not in correct_answer:
        explanation = "Key: '(d)' not found in instructor answer!\n"
        test_answers_question5_d_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d)']
    student_answer = run_compute('all_questions', 'question5', 's', **kwargs)
    if '(d)' not in student_answer:
        explanation = "Key: '(d)' not found in student answer!\n"
        test_answers_question5_d_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d)']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question6_a_C1_minus_TPR_eval_float(run_compute):
    function_name = test_answers_question6_a_C1_minus_TPR_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(a) C1-TPR' not in correct_answer:
        explanation = "Key: '(a) C1-TPR' not found in instructor answer!\n"
        test_answers_question6_a_C1_minus_TPR_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) C1-TPR']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(a) C1-TPR' not in student_answer:
        explanation = "Key: '(a) C1-TPR' not found in student answer!\n"
        test_answers_question6_a_C1_minus_TPR_eval_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) C1-TPR']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_eval_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_eval_float(student_answer, instructor_answer, local_vars_dict, rel_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    local_vars_dict = {'p': [0.1, 0.9]}
    local_namespace['local_vars_dict'] = local_vars_dict
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'eval_float'
    question_id = 'question6'
    subquestion_id = '(a) C1-TPR'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question6_a_C1_minus_TPR_eval_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question6_a_C2_minus_TPR_eval_float(run_compute):
    function_name = test_answers_question6_a_C2_minus_TPR_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(a) C2-TPR' not in correct_answer:
        explanation = "Key: '(a) C2-TPR' not found in instructor answer!\n"
        test_answers_question6_a_C2_minus_TPR_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) C2-TPR']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(a) C2-TPR' not in student_answer:
        explanation = "Key: '(a) C2-TPR' not found in student answer!\n"
        test_answers_question6_a_C2_minus_TPR_eval_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) C2-TPR']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_eval_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_eval_float(student_answer, instructor_answer, local_vars_dict, rel_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    local_vars_dict = {'p': [0.1, 0.9]}
    local_namespace['local_vars_dict'] = local_vars_dict
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'eval_float'
    question_id = 'question6'
    subquestion_id = '(a) C2-TPR'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question6_a_C2_minus_TPR_eval_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question6_a_C1_minus_FPR_eval_float(run_compute):
    function_name = test_answers_question6_a_C1_minus_FPR_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(a) C1-FPR' not in correct_answer:
        explanation = "Key: '(a) C1-FPR' not found in instructor answer!\n"
        test_answers_question6_a_C1_minus_FPR_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) C1-FPR']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(a) C1-FPR' not in student_answer:
        explanation = "Key: '(a) C1-FPR' not found in student answer!\n"
        test_answers_question6_a_C1_minus_FPR_eval_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) C1-FPR']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_eval_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_eval_float(student_answer, instructor_answer, local_vars_dict, rel_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    local_vars_dict = {'p': [0.1, 0.9]}
    local_namespace['local_vars_dict'] = local_vars_dict
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'eval_float'
    question_id = 'question6'
    subquestion_id = '(a) C1-FPR'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question6_a_C1_minus_FPR_eval_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question6_a_C2_minus_FPR_eval_float(run_compute):
    function_name = test_answers_question6_a_C2_minus_FPR_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(a) C2-FPR' not in correct_answer:
        explanation = "Key: '(a) C2-FPR' not found in instructor answer!\n"
        test_answers_question6_a_C2_minus_FPR_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) C2-FPR']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(a) C2-FPR' not in student_answer:
        explanation = "Key: '(a) C2-FPR' not found in student answer!\n"
        test_answers_question6_a_C2_minus_FPR_eval_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) C2-FPR']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_eval_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_eval_float(student_answer, instructor_answer, local_vars_dict, rel_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    local_vars_dict = {'p': [0.1, 0.9]}
    local_namespace['local_vars_dict'] = local_vars_dict
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'eval_float'
    question_id = 'question6'
    subquestion_id = '(a) C2-FPR'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question6_a_C2_minus_FPR_eval_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question6_b_C2_better_classifier_than_C1_ques_string(run_compute):
    function_name = test_answers_question6_b_C2_better_classifier_than_C1_ques_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(b) C2 better classifier than C1?' not in correct_answer:
        explanation = "Key: '(b) C2 better classifier than C1?' not found in instructor answer!\n"
        test_answers_question6_b_C2_better_classifier_than_C1_ques_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) C2 better classifier than C1?']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(b) C2 better classifier than C1?' not in student_answer:
        explanation = "Key: '(b) C2 better classifier than C1?' not found in student answer!\n"
        test_answers_question6_b_C2_better_classifier_than_C1_ques_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) C2 better classifier than C1?']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question6_b_C2_better_classifier_than_C1_ques_Explain_explain_string(run_compute):
    function_name = test_answers_question6_b_C2_better_classifier_than_C1_ques_Explain_explain_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(b) C2 better classifier than C1? Explain' not in correct_answer:
        explanation = "Key: '(b) C2 better classifier than C1? Explain' not found in instructor answer!\n"
        test_answers_question6_b_C2_better_classifier_than_C1_ques_Explain_explain_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) C2 better classifier than C1? Explain']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(b) C2 better classifier than C1? Explain' not in student_answer:
        explanation = "Key: '(b) C2 better classifier than C1? Explain' not found in student answer!\n"
        test_answers_question6_b_C2_better_classifier_than_C1_ques_Explain_explain_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) C2 better classifier than C1? Explain']
    print('type explain_string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question6_c_Which_metric_ques_string(run_compute):
    function_name = test_answers_question6_c_Which_metric_ques_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(c) Which metric?' not in correct_answer:
        explanation = "Key: '(c) Which metric?' not found in instructor answer!\n"
        test_answers_question6_c_Which_metric_ques_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) Which metric?']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(c) Which metric?' not in student_answer:
        explanation = "Key: '(c) Which metric?' not found in student answer!\n"
        test_answers_question6_c_Which_metric_ques_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) Which metric?']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question6_c_explain_explain_string(run_compute):
    function_name = test_answers_question6_c_explain_explain_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(c) explain' not in correct_answer:
        explanation = "Key: '(c) explain' not found in instructor answer!\n"
        test_answers_question6_c_explain_explain_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) explain']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(c) explain' not in student_answer:
        explanation = "Key: '(c) explain' not found in student answer!\n"
        test_answers_question6_c_explain_explain_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) explain']
    print('type explain_string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question7_i_Best_classifier_ques_string(run_compute):
    function_name = test_answers_question7_i_Best_classifier_ques_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(i) Best classifier?' not in correct_answer:
        explanation = "Key: '(i) Best classifier?' not found in instructor answer!\n"
        test_answers_question7_i_Best_classifier_ques_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(i) Best classifier?']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(i) Best classifier?' not in student_answer:
        explanation = "Key: '(i) Best classifier?' not found in student answer!\n"
        test_answers_question7_i_Best_classifier_ques_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(i) Best classifier?']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question7_i_Best_classifier_comma_explain_explain_string(run_compute):
    function_name = test_answers_question7_i_Best_classifier_comma_explain_explain_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(i) Best classifier, explain' not in correct_answer:
        explanation = "Key: '(i) Best classifier, explain' not found in instructor answer!\n"
        test_answers_question7_i_Best_classifier_comma_explain_explain_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(i) Best classifier, explain']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(i) Best classifier, explain' not in student_answer:
        explanation = "Key: '(i) Best classifier, explain' not found in student answer!\n"
        test_answers_question7_i_Best_classifier_comma_explain_explain_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(i) Best classifier, explain']
    print('type explain_string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question7_ii_appropriate_metric_pair_string(run_compute):
    function_name = test_answers_question7_ii_appropriate_metric_pair_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(ii) appropriate metric pair' not in correct_answer:
        explanation = "Key: '(ii) appropriate metric pair' not found in instructor answer!\n"
        test_answers_question7_ii_appropriate_metric_pair_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(ii) appropriate metric pair']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(ii) appropriate metric pair' not in student_answer:
        explanation = "Key: '(ii) appropriate metric pair' not found in student answer!\n"
        test_answers_question7_ii_appropriate_metric_pair_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(ii) appropriate metric pair']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question7_ii_appropriate_metric_pair_comma_explain_explain_string(run_compute):
    function_name = test_answers_question7_ii_appropriate_metric_pair_comma_explain_explain_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(ii) appropriate metric pair, explain' not in correct_answer:
        explanation = "Key: '(ii) appropriate metric pair, explain' not found in instructor answer!\n"
        test_answers_question7_ii_appropriate_metric_pair_comma_explain_explain_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(ii) appropriate metric pair, explain']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(ii) appropriate metric pair, explain' not in student_answer:
        explanation = "Key: '(ii) appropriate metric pair, explain' not found in student answer!\n"
        test_answers_question7_ii_appropriate_metric_pair_comma_explain_explain_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(ii) appropriate metric pair, explain']
    print('type explain_string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question7_iii_preferred_classifier_ques_string(run_compute):
    function_name = test_answers_question7_iii_preferred_classifier_ques_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(iii) preferred classifier?' not in correct_answer:
        explanation = "Key: '(iii) preferred classifier?' not found in instructor answer!\n"
        test_answers_question7_iii_preferred_classifier_ques_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(iii) preferred classifier?']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(iii) preferred classifier?' not in student_answer:
        explanation = "Key: '(iii) preferred classifier?' not found in student answer!\n"
        test_answers_question7_iii_preferred_classifier_ques_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(iii) preferred classifier?']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question7_iii_best_classifier_comma_explain_explain_string(run_compute):
    function_name = test_answers_question7_iii_best_classifier_comma_explain_explain_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(iii) best classifier, explain' not in correct_answer:
        explanation = "Key: '(iii) best classifier, explain' not found in instructor answer!\n"
        test_answers_question7_iii_best_classifier_comma_explain_explain_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(iii) best classifier, explain']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(iii) best classifier, explain' not in student_answer:
        explanation = "Key: '(iii) best classifier, explain' not found in student answer!\n"
        test_answers_question7_iii_best_classifier_comma_explain_explain_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(iii) best classifier, explain']
    print('type explain_string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question8_a_precision_for_C0_eval_float(run_compute):
    function_name = test_answers_question8_a_precision_for_C0_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(a) precision for C0' not in correct_answer:
        explanation = "Key: '(a) precision for C0' not found in instructor answer!\n"
        test_answers_question8_a_precision_for_C0_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) precision for C0']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(a) precision for C0' not in student_answer:
        explanation = "Key: '(a) precision for C0' not found in student answer!\n"
        test_answers_question8_a_precision_for_C0_eval_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) precision for C0']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_eval_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_eval_float(student_answer, instructor_answer, local_vars_dict, rel_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    local_vars_dict = {'p': [0.01, 0.99]}
    local_namespace['local_vars_dict'] = local_vars_dict
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'eval_float'
    question_id = 'question8'
    subquestion_id = '(a) precision for C0'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question8_a_precision_for_C0_eval_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question8_a_recall_for_C0_eval_float(run_compute):
    function_name = test_answers_question8_a_recall_for_C0_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(a) recall for C0' not in correct_answer:
        explanation = "Key: '(a) recall for C0' not found in instructor answer!\n"
        test_answers_question8_a_recall_for_C0_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) recall for C0']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(a) recall for C0' not in student_answer:
        explanation = "Key: '(a) recall for C0' not found in student answer!\n"
        test_answers_question8_a_recall_for_C0_eval_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) recall for C0']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_eval_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_eval_float(student_answer, instructor_answer, local_vars_dict, rel_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    local_vars_dict = {'p': [0.01, 0.99]}
    local_namespace['local_vars_dict'] = local_vars_dict
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'eval_float'
    question_id = 'question8'
    subquestion_id = '(a) recall for C0'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question8_a_recall_for_C0_eval_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question8_b_F_minus_measure_of_C0_eval_float(run_compute):
    function_name = test_answers_question8_b_F_minus_measure_of_C0_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(b) F-measure of C0' not in correct_answer:
        explanation = "Key: '(b) F-measure of C0' not found in instructor answer!\n"
        test_answers_question8_b_F_minus_measure_of_C0_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) F-measure of C0']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(b) F-measure of C0' not in student_answer:
        explanation = "Key: '(b) F-measure of C0' not found in student answer!\n"
        test_answers_question8_b_F_minus_measure_of_C0_eval_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) F-measure of C0']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_eval_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_eval_float(student_answer, instructor_answer, local_vars_dict, rel_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    local_vars_dict = {'p': [0.01, 0.99]}
    local_namespace['local_vars_dict'] = local_vars_dict
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'eval_float'
    question_id = 'question8'
    subquestion_id = '(b) F-measure of C0'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question8_b_F_minus_measure_of_C0_eval_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question8_C1_better_than_random_ques_string(run_compute):
    function_name = test_answers_question8_C1_better_than_random_ques_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if 'C1 better than random?' not in correct_answer:
        explanation = "Key: 'C1 better than random?' not found in instructor answer!\n"
        test_answers_question8_C1_better_than_random_ques_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['C1 better than random?']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if 'C1 better than random?' not in student_answer:
        explanation = "Key: 'C1 better than random?' not found in student answer!\n"
        test_answers_question8_C1_better_than_random_ques_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['C1 better than random?']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question8_p_minus_range_float(run_compute):
    function_name = test_answers_question8_p_minus_range_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if 'p-range' not in correct_answer:
        explanation = "Key: 'p-range' not found in instructor answer!\n"
        test_answers_question8_p_minus_range_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['p-range']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if 'p-range' not in student_answer:
        explanation = "Key: 'p-range' not found in student answer!\n"
        test_answers_question8_p_minus_range_float.explanation = explanation
        assert False
    else:
        student_answer = student_answer['p-range']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_float(student_answer, instructor_answer, rel_tol, abs_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    note = 'What is the range of p for which C1 is better than random?  What is "?" in the expression "p > ?"\n'
    function_name.note = note
    answer_note = 'Simply equate F to p.'
    function_name.answer_note = answer_note
    answer_type = 'float'
    question_id = 'question8'
    subquestion_id = 'p-range'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    if is_success:
        is_success, explanation_answer    = eval(msg_answer,    {'__builtins__':{}}, local_namespace)
        if is_success is True:
            function_name.partial_score_frac = 1.0
        else:
            function_name.partial_score_frac = partial_score_frac_l[0]
    else: 
        explanation_answer = 'Failed structural tests, No grade for answer component\n.' 
        explanation_answer += f'Instructor answer: {repr(correct_answer)}\n'
        explanation_answer += f'Student answer: {repr(student_answer)}'
        function_name.partial_score_frac = partial_score_frac_l[0]
        print(f'FAILURE, partial score: {function_name.partial_score_frac}')
    explanation = '\n'.join(['==Structure tests==:', explanation_structure, '==Answer tests==:', explanation_answer])
    test_answers_question8_p_minus_range_float.explanation = explanation
    assert is_success



@max_score(20)
@hide_errors('')
def test_answers_question9_i_metrics_dict_lbrack_string_comma_float_rbrack(run_compute):
    function_name = test_answers_question9_i_metrics_dict_lbrack_string_comma_float_rbrack
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question9', 'i', **kwargs)
    if '(i) metrics' not in correct_answer:
        explanation = "Key: '(i) metrics' not found in instructor answer!\n"
        test_answers_question9_i_metrics_dict_lbrack_string_comma_float_rbrack.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(i) metrics']
    student_answer = run_compute('all_questions', 'question9', 's', **kwargs)
    if '(i) metrics' not in student_answer:
        explanation = "Key: '(i) metrics' not found in student answer!\n"
        test_answers_question9_i_metrics_dict_lbrack_string_comma_float_rbrack.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(i) metrics']
    print('type dict[string,float] NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question9_i_best_metric_ques_string(run_compute):
    function_name = test_answers_question9_i_best_metric_ques_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question9', 'i', **kwargs)
    if '(i) best metric?' not in correct_answer:
        explanation = "Key: '(i) best metric?' not found in instructor answer!\n"
        test_answers_question9_i_best_metric_ques_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(i) best metric?']
    student_answer = run_compute('all_questions', 'question9', 's', **kwargs)
    if '(i) best metric?' not in student_answer:
        explanation = "Key: '(i) best metric?' not found in student answer!\n"
        test_answers_question9_i_best_metric_ques_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(i) best metric?']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question9_i_worst_metric_ques_string(run_compute):
    function_name = test_answers_question9_i_worst_metric_ques_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question9', 'i', **kwargs)
    if '(i) worst metric?' not in correct_answer:
        explanation = "Key: '(i) worst metric?' not found in instructor answer!\n"
        test_answers_question9_i_worst_metric_ques_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(i) worst metric?']
    student_answer = run_compute('all_questions', 'question9', 's', **kwargs)
    if '(i) worst metric?' not in student_answer:
        explanation = "Key: '(i) worst metric?' not found in student answer!\n"
        test_answers_question9_i_worst_metric_ques_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(i) worst metric?']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question9_ii_Explain_your_choices_of_best_and_worst_metrics_explain_string(run_compute):
    function_name = test_answers_question9_ii_Explain_your_choices_of_best_and_worst_metrics_explain_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question9', 'i', **kwargs)
    if '(ii) Explain your choices of best and worst metrics' not in correct_answer:
        explanation = "Key: '(ii) Explain your choices of best and worst metrics' not found in instructor answer!\n"
        test_answers_question9_ii_Explain_your_choices_of_best_and_worst_metrics_explain_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(ii) Explain your choices of best and worst metrics']
    student_answer = run_compute('all_questions', 'question9', 's', **kwargs)
    if '(ii) Explain your choices of best and worst metrics' not in student_answer:
        explanation = "Key: '(ii) Explain your choices of best and worst metrics' not found in student answer!\n"
        test_answers_question9_ii_Explain_your_choices_of_best_and_worst_metrics_explain_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(ii) Explain your choices of best and worst metrics']
    print('type explain_string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question10_a_better_test_based_on_F_minus_measure_ques_string(run_compute):
    function_name = test_answers_question10_a_better_test_based_on_F_minus_measure_ques_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(a) better test based on F-measure?' not in correct_answer:
        explanation = "Key: '(a) better test based on F-measure?' not found in instructor answer!\n"
        test_answers_question10_a_better_test_based_on_F_minus_measure_ques_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) better test based on F-measure?']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(a) better test based on F-measure?' not in student_answer:
        explanation = "Key: '(a) better test based on F-measure?' not found in student answer!\n"
        test_answers_question10_a_better_test_based_on_F_minus_measure_ques_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) better test based on F-measure?']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question10_b_better_test_based_on_TPR_slash_FPR_ques_string(run_compute):
    function_name = test_answers_question10_b_better_test_based_on_TPR_slash_FPR_ques_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(b) better test based on TPR/FPR?' not in correct_answer:
        explanation = "Key: '(b) better test based on TPR/FPR?' not found in instructor answer!\n"
        test_answers_question10_b_better_test_based_on_TPR_slash_FPR_ques_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) better test based on TPR/FPR?']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(b) better test based on TPR/FPR?' not in student_answer:
        explanation = "Key: '(b) better test based on TPR/FPR?' not found in student answer!\n"
        test_answers_question10_b_better_test_based_on_TPR_slash_FPR_ques_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) better test based on TPR/FPR?']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question10_c_Which_evaluation_measure_to_use_between_the_two_tests_ques_string(run_compute):
    function_name = test_answers_question10_c_Which_evaluation_measure_to_use_between_the_two_tests_ques_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(c) Which evaluation measure to use between the two tests?' not in correct_answer:
        explanation = "Key: '(c) Which evaluation measure to use between the two tests?' not found in instructor answer!\n"
        test_answers_question10_c_Which_evaluation_measure_to_use_between_the_two_tests_ques_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) Which evaluation measure to use between the two tests?']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(c) Which evaluation measure to use between the two tests?' not in student_answer:
        explanation = "Key: '(c) Which evaluation measure to use between the two tests?' not found in student answer!\n"
        test_answers_question10_c_Which_evaluation_measure_to_use_between_the_two_tests_ques_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) Which evaluation measure to use between the two tests?']
    print('type string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question10_c_Which_evaluation_measure_ques_Explain_explain_string(run_compute):
    function_name = test_answers_question10_c_Which_evaluation_measure_ques_Explain_explain_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(c) Which evaluation measure? Explain' not in correct_answer:
        explanation = "Key: '(c) Which evaluation measure? Explain' not found in instructor answer!\n"
        test_answers_question10_c_Which_evaluation_measure_ques_Explain_explain_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) Which evaluation measure? Explain']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(c) Which evaluation measure? Explain' not in student_answer:
        explanation = "Key: '(c) Which evaluation measure? Explain' not found in student answer!\n"
        test_answers_question10_c_Which_evaluation_measure_ques_Explain_explain_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) Which evaluation measure? Explain']
    print('type explain_string NOT HANDLED!')



@max_score(20)
@hide_errors('')
def test_answers_question10_d_Example_scenario_where_you_would_reverse_choise_in_c_explain_string(run_compute):
    function_name = test_answers_question10_d_Example_scenario_where_you_would_reverse_choise_in_c_explain_string
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(d) Example scenario where you would reverse choise in (c)' not in correct_answer:
        explanation = "Key: '(d) Example scenario where you would reverse choise in (c)' not found in instructor answer!\n"
        test_answers_question10_d_Example_scenario_where_you_would_reverse_choise_in_c_explain_string.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) Example scenario where you would reverse choise in (c)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(d) Example scenario where you would reverse choise in (c)' not in student_answer:
        explanation = "Key: '(d) Example scenario where you would reverse choise in (c)' not found in student answer!\n"
        test_answers_question10_d_Example_scenario_where_you_would_reverse_choise_in_c_explain_string.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d) Example scenario where you would reverse choise in (c)']
    print('type explain_string NOT HANDLED!')


