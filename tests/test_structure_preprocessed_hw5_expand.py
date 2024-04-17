
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
@hide_errors('')
def test_structure_question1_a_float(run_compute):
    function_name = test_structure_question1_a_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(a)' not in correct_answer:
        explanation = "Key: '(a)' not found in instructor answer!\n"
        test_structure_question1_a_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a)']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(a)' not in student_answer:
        explanation = "Key: '(a)' not found in student answer!\n"
        test_structure_question1_a_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_float(student_answer, instructor_answer, rel_tol, abs_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question1_a_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question1_b_float(run_compute):
    function_name = test_structure_question1_b_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(b)' not in correct_answer:
        explanation = "Key: '(b)' not found in instructor answer!\n"
        test_structure_question1_b_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b)']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(b)' not in student_answer:
        explanation = "Key: '(b)' not found in student answer!\n"
        test_structure_question1_b_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_float(student_answer, instructor_answer, rel_tol, abs_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question1_b_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question1_c_float(run_compute):
    function_name = test_structure_question1_c_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(c)' not in correct_answer:
        explanation = "Key: '(c)' not found in instructor answer!\n"
        test_structure_question1_c_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c)']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(c)' not in student_answer:
        explanation = "Key: '(c)' not found in student answer!\n"
        test_structure_question1_c_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_float(student_answer, instructor_answer, rel_tol, abs_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question1_c_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question2_a_A_bool(run_compute):
    function_name = test_structure_question2_a_A_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(a) A' not in correct_answer:
        explanation = "Key: '(a) A' not found in instructor answer!\n"
        test_structure_question2_a_A_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) A']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(a) A' not in student_answer:
        explanation = "Key: '(a) A' not found in student answer!\n"
        test_structure_question2_a_A_bool.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question2_a_A_bool.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question2_a_B_bool(run_compute):
    function_name = test_structure_question2_a_B_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(a) B' not in correct_answer:
        explanation = "Key: '(a) B' not found in instructor answer!\n"
        test_structure_question2_a_B_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) B']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(a) B' not in student_answer:
        explanation = "Key: '(a) B' not found in student answer!\n"
        test_structure_question2_a_B_bool.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question2_a_B_bool.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question2_a_C_bool(run_compute):
    function_name = test_structure_question2_a_C_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(a) C' not in correct_answer:
        explanation = "Key: '(a) C' not found in instructor answer!\n"
        test_structure_question2_a_C_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) C']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(a) C' not in student_answer:
        explanation = "Key: '(a) C' not found in student answer!\n"
        test_structure_question2_a_C_bool.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question2_a_C_bool.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question2_a_D_bool(run_compute):
    function_name = test_structure_question2_a_D_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(a) D' not in correct_answer:
        explanation = "Key: '(a) D' not found in instructor answer!\n"
        test_structure_question2_a_D_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) D']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(a) D' not in student_answer:
        explanation = "Key: '(a) D' not found in student answer!\n"
        test_structure_question2_a_D_bool.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question2_a_D_bool.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question2_b_A_bool(run_compute):
    function_name = test_structure_question2_b_A_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(b) A' not in correct_answer:
        explanation = "Key: '(b) A' not found in instructor answer!\n"
        test_structure_question2_b_A_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) A']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(b) A' not in student_answer:
        explanation = "Key: '(b) A' not found in student answer!\n"
        test_structure_question2_b_A_bool.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question2_b_A_bool.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question2_b_B_bool(run_compute):
    function_name = test_structure_question2_b_B_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(b) B' not in correct_answer:
        explanation = "Key: '(b) B' not found in instructor answer!\n"
        test_structure_question2_b_B_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) B']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(b) B' not in student_answer:
        explanation = "Key: '(b) B' not found in student answer!\n"
        test_structure_question2_b_B_bool.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) B']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'bool'
    question_id = 'question2'
    subquestion_id = '(b) B'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question2_b_B_bool.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question2_b_C_bool(run_compute):
    function_name = test_structure_question2_b_C_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(b) C' not in correct_answer:
        explanation = "Key: '(b) C' not found in instructor answer!\n"
        test_structure_question2_b_C_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) C']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(b) C' not in student_answer:
        explanation = "Key: '(b) C' not found in student answer!\n"
        test_structure_question2_b_C_bool.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question2_b_C_bool.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question2_b_A_bool(run_compute):
    function_name = test_structure_question2_b_A_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(b) A' not in correct_answer:
        explanation = "Key: '(b) A' not found in instructor answer!\n"
        test_structure_question2_b_A_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) A']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(b) A' not in student_answer:
        explanation = "Key: '(b) A' not found in student answer!\n"
        test_structure_question2_b_A_bool.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_bool(student_answer)"
    msg_answer = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question2_b_A_bool.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question2_c_Weight_update_eval_float(run_compute):
    function_name = test_structure_question2_c_Weight_update_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(c) Weight update' not in correct_answer:
        explanation = "Key: '(c) Weight update' not found in instructor answer!\n"
        test_structure_question2_c_Weight_update_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) Weight update']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(c) Weight update' not in student_answer:
        explanation = "Key: '(c) Weight update' not found in student answer!\n"
        test_structure_question2_c_Weight_update_eval_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question2_c_Weight_update_eval_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question2_d_Weight_influence_float(run_compute):
    function_name = test_structure_question2_d_Weight_influence_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(d) Weight influence' not in correct_answer:
        explanation = "Key: '(d) Weight influence' not found in instructor answer!\n"
        test_structure_question2_d_Weight_influence_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) Weight influence']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(d) Weight influence' not in student_answer:
        explanation = "Key: '(d) Weight influence' not found in student answer!\n"
        test_structure_question2_d_Weight_influence_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_float(student_answer, instructor_answer, rel_tol, abs_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question2_d_Weight_influence_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question3_Agree_ques_str(run_compute):
    function_name = test_structure_question3_Agree_ques_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question3', 'i', **kwargs)
    if 'Agree?' not in correct_answer:
        explanation = "Key: 'Agree?' not found in instructor answer!\n"
        test_structure_question3_Agree_ques_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['Agree?']
    student_answer = run_compute('all_questions', 'question3', 's', **kwargs)
    if 'Agree?' not in student_answer:
        explanation = "Key: 'Agree?' not found in student answer!\n"
        test_structure_question3_Agree_ques_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['Agree?']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question3'
    subquestion_id = 'Agree?'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question3_Agree_ques_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question3_Explain_explain_str(run_compute):
    function_name = test_structure_question3_Explain_explain_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question3', 'i', **kwargs)
    if 'Explain' not in correct_answer:
        explanation = "Key: 'Explain' not found in instructor answer!\n"
        test_structure_question3_Explain_explain_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['Explain']
    student_answer = run_compute('all_questions', 'question3', 's', **kwargs)
    if 'Explain' not in student_answer:
        explanation = "Key: 'Explain' not found in student answer!\n"
        test_structure_question3_Explain_explain_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['Explain']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_explain_str(student_answer)"
    msg_answer = "assert_utilities.check_answer_explain_str(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'explain_str'
    question_id = 'question3'
    subquestion_id = 'Explain'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question3_Explain_explain_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question4_a_e_0_dot_5_comma_independent_bool(run_compute):
    function_name = test_structure_question4_a_e_0_dot_5_comma_independent_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question4', 'i', **kwargs)
    if '(a) e=0.5, independent' not in correct_answer:
        explanation = "Key: '(a) e=0.5, independent' not found in instructor answer!\n"
        test_structure_question4_a_e_0_dot_5_comma_independent_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) e=0.5, independent']
    student_answer = run_compute('all_questions', 'question4', 's', **kwargs)
    if '(a) e=0.5, independent' not in student_answer:
        explanation = "Key: '(a) e=0.5, independent' not found in student answer!\n"
        test_structure_question4_a_e_0_dot_5_comma_independent_bool.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question4_a_e_0_dot_5_comma_independent_bool.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question4_b_comma_independent_bool(run_compute):
    function_name = test_structure_question4_b_comma_independent_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question4', 'i', **kwargs)
    if '(b), independent' not in correct_answer:
        explanation = "Key: '(b), independent' not found in instructor answer!\n"
        test_structure_question4_b_comma_independent_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b), independent']
    student_answer = run_compute('all_questions', 'question4', 's', **kwargs)
    if '(b), independent' not in student_answer:
        explanation = "Key: '(b), independent' not found in student answer!\n"
        test_structure_question4_b_comma_independent_bool.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question4_b_comma_independent_bool.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question4_c_identical_bool(run_compute):
    function_name = test_structure_question4_c_identical_bool
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question4', 'i', **kwargs)
    if '(c) identical' not in correct_answer:
        explanation = "Key: '(c) identical' not found in instructor answer!\n"
        test_structure_question4_c_identical_bool.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) identical']
    student_answer = run_compute('all_questions', 'question4', 's', **kwargs)
    if '(c) identical' not in student_answer:
        explanation = "Key: '(c) identical' not found in student answer!\n"
        test_structure_question4_c_identical_bool.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question4_c_identical_bool.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question5_a_str(run_compute):
    function_name = test_structure_question5_a_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question5', 'i', **kwargs)
    if '(a)' not in correct_answer:
        explanation = "Key: '(a)' not found in instructor answer!\n"
        test_structure_question5_a_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a)']
    student_answer = run_compute('all_questions', 'question5', 's', **kwargs)
    if '(a)' not in student_answer:
        explanation = "Key: '(a)' not found in student answer!\n"
        test_structure_question5_a_str.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['i', 'ii', 'iii', 'iv']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question5'
    subquestion_id = '(a)'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question5_a_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question5_b_str(run_compute):
    function_name = test_structure_question5_b_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question5', 'i', **kwargs)
    if '(b)' not in correct_answer:
        explanation = "Key: '(b)' not found in instructor answer!\n"
        test_structure_question5_b_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b)']
    student_answer = run_compute('all_questions', 'question5', 's', **kwargs)
    if '(b)' not in student_answer:
        explanation = "Key: '(b)' not found in student answer!\n"
        test_structure_question5_b_str.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['i', 'ii', 'iii', 'iv']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question5'
    subquestion_id = '(b)'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question5_b_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question5_c_str(run_compute):
    function_name = test_structure_question5_c_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question5', 'i', **kwargs)
    if '(c)' not in correct_answer:
        explanation = "Key: '(c)' not found in instructor answer!\n"
        test_structure_question5_c_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c)']
    student_answer = run_compute('all_questions', 'question5', 's', **kwargs)
    if '(c)' not in student_answer:
        explanation = "Key: '(c)' not found in student answer!\n"
        test_structure_question5_c_str.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['i', 'ii', 'iii', 'iv']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question5'
    subquestion_id = '(c)'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question5_c_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question5_d_str(run_compute):
    function_name = test_structure_question5_d_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question5', 'i', **kwargs)
    if '(d)' not in correct_answer:
        explanation = "Key: '(d)' not found in instructor answer!\n"
        test_structure_question5_d_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d)']
    student_answer = run_compute('all_questions', 'question5', 's', **kwargs)
    if '(d)' not in student_answer:
        explanation = "Key: '(d)' not found in student answer!\n"
        test_structure_question5_d_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d)']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['i', 'ii', 'iii', 'iv']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question5'
    subquestion_id = '(d)'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question5_d_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question6_a_C1_minus_TPR_eval_float(run_compute):
    function_name = test_structure_question6_a_C1_minus_TPR_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(a) C1-TPR' not in correct_answer:
        explanation = "Key: '(a) C1-TPR' not found in instructor answer!\n"
        test_structure_question6_a_C1_minus_TPR_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) C1-TPR']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(a) C1-TPR' not in student_answer:
        explanation = "Key: '(a) C1-TPR' not found in student answer!\n"
        test_structure_question6_a_C1_minus_TPR_eval_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question6_a_C1_minus_TPR_eval_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question6_a_C2_minus_TPR_eval_float(run_compute):
    function_name = test_structure_question6_a_C2_minus_TPR_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(a) C2-TPR' not in correct_answer:
        explanation = "Key: '(a) C2-TPR' not found in instructor answer!\n"
        test_structure_question6_a_C2_minus_TPR_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) C2-TPR']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(a) C2-TPR' not in student_answer:
        explanation = "Key: '(a) C2-TPR' not found in student answer!\n"
        test_structure_question6_a_C2_minus_TPR_eval_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question6_a_C2_minus_TPR_eval_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question6_a_C1_minus_FPR_eval_float(run_compute):
    function_name = test_structure_question6_a_C1_minus_FPR_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(a) C1-FPR' not in correct_answer:
        explanation = "Key: '(a) C1-FPR' not found in instructor answer!\n"
        test_structure_question6_a_C1_minus_FPR_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) C1-FPR']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(a) C1-FPR' not in student_answer:
        explanation = "Key: '(a) C1-FPR' not found in student answer!\n"
        test_structure_question6_a_C1_minus_FPR_eval_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question6_a_C1_minus_FPR_eval_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question6_a_C2_minus_FPR_eval_float(run_compute):
    function_name = test_structure_question6_a_C2_minus_FPR_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(a) C2-FPR' not in correct_answer:
        explanation = "Key: '(a) C2-FPR' not found in instructor answer!\n"
        test_structure_question6_a_C2_minus_FPR_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) C2-FPR']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(a) C2-FPR' not in student_answer:
        explanation = "Key: '(a) C2-FPR' not found in student answer!\n"
        test_structure_question6_a_C2_minus_FPR_eval_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question6_a_C2_minus_FPR_eval_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question6_b_C2_better_classifier_than_C1_ques_str(run_compute):
    function_name = test_structure_question6_b_C2_better_classifier_than_C1_ques_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(b) C2 better classifier than C1?' not in correct_answer:
        explanation = "Key: '(b) C2 better classifier than C1?' not found in instructor answer!\n"
        test_structure_question6_b_C2_better_classifier_than_C1_ques_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) C2 better classifier than C1?']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(b) C2 better classifier than C1?' not in student_answer:
        explanation = "Key: '(b) C2 better classifier than C1?' not found in student answer!\n"
        test_structure_question6_b_C2_better_classifier_than_C1_ques_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) C2 better classifier than C1?']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['yes', 'no']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question6'
    subquestion_id = '(b) C2 better classifier than C1?'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question6_b_C2_better_classifier_than_C1_ques_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question6_b_C2_better_classifier_than_C1_ques_Explain_explain_str(run_compute):
    function_name = test_structure_question6_b_C2_better_classifier_than_C1_ques_Explain_explain_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(b) C2 better classifier than C1? Explain' not in correct_answer:
        explanation = "Key: '(b) C2 better classifier than C1? Explain' not found in instructor answer!\n"
        test_structure_question6_b_C2_better_classifier_than_C1_ques_Explain_explain_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) C2 better classifier than C1? Explain']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(b) C2 better classifier than C1? Explain' not in student_answer:
        explanation = "Key: '(b) C2 better classifier than C1? Explain' not found in student answer!\n"
        test_structure_question6_b_C2_better_classifier_than_C1_ques_Explain_explain_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) C2 better classifier than C1? Explain']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_explain_str(student_answer)"
    msg_answer = "assert_utilities.check_answer_explain_str(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'explain_str'
    question_id = 'question6'
    subquestion_id = '(b) C2 better classifier than C1? Explain'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question6_b_C2_better_classifier_than_C1_ques_Explain_explain_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question6_c_Which_metric_ques_str(run_compute):
    function_name = test_structure_question6_c_Which_metric_ques_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(c) Which metric?' not in correct_answer:
        explanation = "Key: '(c) Which metric?' not found in instructor answer!\n"
        test_structure_question6_c_Which_metric_ques_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) Which metric?']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(c) Which metric?' not in student_answer:
        explanation = "Key: '(c) Which metric?' not found in student answer!\n"
        test_structure_question6_c_Which_metric_ques_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) Which metric?']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['TPR/FPR', 'precision/recall']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question6'
    subquestion_id = '(c) Which metric?'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question6_c_Which_metric_ques_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question6_c_explain_explain_str(run_compute):
    function_name = test_structure_question6_c_explain_explain_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question6', 'i', **kwargs)
    if '(c) explain' not in correct_answer:
        explanation = "Key: '(c) explain' not found in instructor answer!\n"
        test_structure_question6_c_explain_explain_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) explain']
    student_answer = run_compute('all_questions', 'question6', 's', **kwargs)
    if '(c) explain' not in student_answer:
        explanation = "Key: '(c) explain' not found in student answer!\n"
        test_structure_question6_c_explain_explain_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) explain']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_explain_str(student_answer)"
    msg_answer = "assert_utilities.check_answer_explain_str(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'explain_str'
    question_id = 'question6'
    subquestion_id = '(c) explain'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question6_c_explain_explain_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question7_i_Best_classifier_ques_str(run_compute):
    function_name = test_structure_question7_i_Best_classifier_ques_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(i) Best classifier?' not in correct_answer:
        explanation = "Key: '(i) Best classifier?' not found in instructor answer!\n"
        test_structure_question7_i_Best_classifier_ques_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(i) Best classifier?']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(i) Best classifier?' not in student_answer:
        explanation = "Key: '(i) Best classifier?' not found in student answer!\n"
        test_structure_question7_i_Best_classifier_ques_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(i) Best classifier?']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['C1', 'C2', 'None']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question7'
    subquestion_id = '(i) Best classifier?'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question7_i_Best_classifier_ques_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question7_i_Best_classifier_comma_explain_explain_str(run_compute):
    function_name = test_structure_question7_i_Best_classifier_comma_explain_explain_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(i) Best classifier, explain' not in correct_answer:
        explanation = "Key: '(i) Best classifier, explain' not found in instructor answer!\n"
        test_structure_question7_i_Best_classifier_comma_explain_explain_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(i) Best classifier, explain']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(i) Best classifier, explain' not in student_answer:
        explanation = "Key: '(i) Best classifier, explain' not found in student answer!\n"
        test_structure_question7_i_Best_classifier_comma_explain_explain_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(i) Best classifier, explain']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_explain_str(student_answer)"
    msg_answer = "assert_utilities.check_answer_explain_str(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'explain_str'
    question_id = 'question7'
    subquestion_id = '(i) Best classifier, explain'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question7_i_Best_classifier_comma_explain_explain_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question7_ii_appropriate_metric_pair_str(run_compute):
    function_name = test_structure_question7_ii_appropriate_metric_pair_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(ii) appropriate metric pair' not in correct_answer:
        explanation = "Key: '(ii) appropriate metric pair' not found in instructor answer!\n"
        test_structure_question7_ii_appropriate_metric_pair_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(ii) appropriate metric pair']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(ii) appropriate metric pair' not in student_answer:
        explanation = "Key: '(ii) appropriate metric pair' not found in student answer!\n"
        test_structure_question7_ii_appropriate_metric_pair_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(ii) appropriate metric pair']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['TPR-FPR', 'precision-recall-F1-Measure']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question7'
    subquestion_id = '(ii) appropriate metric pair'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question7_ii_appropriate_metric_pair_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question7_ii_appropriate_metric_pair_comma_explain_explain_str(run_compute):
    function_name = test_structure_question7_ii_appropriate_metric_pair_comma_explain_explain_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(ii) appropriate metric pair, explain' not in correct_answer:
        explanation = "Key: '(ii) appropriate metric pair, explain' not found in instructor answer!\n"
        test_structure_question7_ii_appropriate_metric_pair_comma_explain_explain_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(ii) appropriate metric pair, explain']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(ii) appropriate metric pair, explain' not in student_answer:
        explanation = "Key: '(ii) appropriate metric pair, explain' not found in student answer!\n"
        test_structure_question7_ii_appropriate_metric_pair_comma_explain_explain_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(ii) appropriate metric pair, explain']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_explain_str(student_answer)"
    msg_answer = "assert_utilities.check_answer_explain_str(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'explain_str'
    question_id = 'question7'
    subquestion_id = '(ii) appropriate metric pair, explain'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question7_ii_appropriate_metric_pair_comma_explain_explain_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question7_iii_preferred_classifier_ques_str(run_compute):
    function_name = test_structure_question7_iii_preferred_classifier_ques_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(iii) preferred classifier?' not in correct_answer:
        explanation = "Key: '(iii) preferred classifier?' not found in instructor answer!\n"
        test_structure_question7_iii_preferred_classifier_ques_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(iii) preferred classifier?']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(iii) preferred classifier?' not in student_answer:
        explanation = "Key: '(iii) preferred classifier?' not found in student answer!\n"
        test_structure_question7_iii_preferred_classifier_ques_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(iii) preferred classifier?']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['C1', 'C2', 'C3']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question7'
    subquestion_id = '(iii) preferred classifier?'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question7_iii_preferred_classifier_ques_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question7_iii_best_classifier_comma_explain_explain_str(run_compute):
    function_name = test_structure_question7_iii_best_classifier_comma_explain_explain_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(iii) best classifier, explain' not in correct_answer:
        explanation = "Key: '(iii) best classifier, explain' not found in instructor answer!\n"
        test_structure_question7_iii_best_classifier_comma_explain_explain_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(iii) best classifier, explain']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(iii) best classifier, explain' not in student_answer:
        explanation = "Key: '(iii) best classifier, explain' not found in student answer!\n"
        test_structure_question7_iii_best_classifier_comma_explain_explain_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(iii) best classifier, explain']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_explain_str(student_answer)"
    msg_answer = "assert_utilities.check_answer_explain_str(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'explain_str'
    question_id = 'question7'
    subquestion_id = '(iii) best classifier, explain'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question7_iii_best_classifier_comma_explain_explain_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question8_a_precision_for_C0_eval_float(run_compute):
    function_name = test_structure_question8_a_precision_for_C0_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(a) precision for C0' not in correct_answer:
        explanation = "Key: '(a) precision for C0' not found in instructor answer!\n"
        test_structure_question8_a_precision_for_C0_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) precision for C0']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(a) precision for C0' not in student_answer:
        explanation = "Key: '(a) precision for C0' not found in student answer!\n"
        test_structure_question8_a_precision_for_C0_eval_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question8_a_precision_for_C0_eval_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question8_a_recall_for_C0_eval_float(run_compute):
    function_name = test_structure_question8_a_recall_for_C0_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(a) recall for C0' not in correct_answer:
        explanation = "Key: '(a) recall for C0' not found in instructor answer!\n"
        test_structure_question8_a_recall_for_C0_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) recall for C0']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(a) recall for C0' not in student_answer:
        explanation = "Key: '(a) recall for C0' not found in student answer!\n"
        test_structure_question8_a_recall_for_C0_eval_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question8_a_recall_for_C0_eval_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question8_b_F_minus_measure_of_C0_eval_float(run_compute):
    function_name = test_structure_question8_b_F_minus_measure_of_C0_eval_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(b) F-measure of C0' not in correct_answer:
        explanation = "Key: '(b) F-measure of C0' not found in instructor answer!\n"
        test_structure_question8_b_F_minus_measure_of_C0_eval_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) F-measure of C0']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(b) F-measure of C0' not in student_answer:
        explanation = "Key: '(b) F-measure of C0' not found in student answer!\n"
        test_structure_question8_b_F_minus_measure_of_C0_eval_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question8_b_F_minus_measure_of_C0_eval_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question8_C1_better_than_random_ques_str(run_compute):
    function_name = test_structure_question8_C1_better_than_random_ques_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if 'C1 better than random?' not in correct_answer:
        explanation = "Key: 'C1 better than random?' not found in instructor answer!\n"
        test_structure_question8_C1_better_than_random_ques_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['C1 better than random?']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if 'C1 better than random?' not in student_answer:
        explanation = "Key: 'C1 better than random?' not found in student answer!\n"
        test_structure_question8_C1_better_than_random_ques_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['C1 better than random?']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['yes', 'no', 'unknown']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question8'
    subquestion_id = 'C1 better than random?'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question8_C1_better_than_random_ques_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question8_p_minus_range_float(run_compute):
    function_name = test_structure_question8_p_minus_range_float
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if 'p-range' not in correct_answer:
        explanation = "Key: 'p-range' not found in instructor answer!\n"
        test_structure_question8_p_minus_range_float.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['p-range']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if 'p-range' not in student_answer:
        explanation = "Key: 'p-range' not found in student answer!\n"
        test_structure_question8_p_minus_range_float.explanation = explanation
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
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_float(student_answer)"
    msg_answer = "assert_utilities.check_answer_float(student_answer, instructor_answer, rel_tol, abs_tol)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
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
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question8_p_minus_range_float.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question9_i_metrics_dict_lbrack_str_comma_float_rbrack(run_compute):
    function_name = test_structure_question9_i_metrics_dict_lbrack_str_comma_float_rbrack
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question9', 'i', **kwargs)
    if '(i) metrics' not in correct_answer:
        explanation = "Key: '(i) metrics' not found in instructor answer!\n"
        test_structure_question9_i_metrics_dict_lbrack_str_comma_float_rbrack.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(i) metrics']
    student_answer = run_compute('all_questions', 'question9', 's', **kwargs)
    if '(i) metrics' not in student_answer:
        explanation = "Key: '(i) metrics' not found in student answer!\n"
        test_structure_question9_i_metrics_dict_lbrack_str_comma_float_rbrack.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(i) metrics']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    dict_float_choices = {}
    local_namespace['dict_float_choices'] = dict_float_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_dict_str_float(student_answer, instructor_answer, keys)"
    msg_answer = "assert_utilities.check_answer_dict_str_float(student_answer, instructor_answer, rel_tol, keys, dict_float_choices, partial_score_frac_l)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'dict[str,float]'
    question_id = 'question9'
    subquestion_id = '(i) metrics'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question9_i_metrics_dict_lbrack_str_comma_float_rbrack.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question9_i_best_metric_ques_str(run_compute):
    function_name = test_structure_question9_i_best_metric_ques_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question9', 'i', **kwargs)
    if '(i) best metric?' not in correct_answer:
        explanation = "Key: '(i) best metric?' not found in instructor answer!\n"
        test_structure_question9_i_best_metric_ques_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(i) best metric?']
    student_answer = run_compute('all_questions', 'question9', 's', **kwargs)
    if '(i) best metric?' not in student_answer:
        explanation = "Key: '(i) best metric?' not found in student answer!\n"
        test_structure_question9_i_best_metric_ques_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(i) best metric?']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['recall', 'precision', 'F-measure', 'accuracy']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question9'
    subquestion_id = '(i) best metric?'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question9_i_best_metric_ques_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question9_i_worst_metric_ques_str(run_compute):
    function_name = test_structure_question9_i_worst_metric_ques_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question9', 'i', **kwargs)
    if '(i) worst metric?' not in correct_answer:
        explanation = "Key: '(i) worst metric?' not found in instructor answer!\n"
        test_structure_question9_i_worst_metric_ques_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(i) worst metric?']
    student_answer = run_compute('all_questions', 'question9', 's', **kwargs)
    if '(i) worst metric?' not in student_answer:
        explanation = "Key: '(i) worst metric?' not found in student answer!\n"
        test_structure_question9_i_worst_metric_ques_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(i) worst metric?']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['recall', 'precision', 'F-measure', 'accuracy']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question9'
    subquestion_id = '(i) worst metric?'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question9_i_worst_metric_ques_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question9_ii_Explain_your_choices_of_best_and_worst_metrics_explain_str(run_compute):
    function_name = test_structure_question9_ii_Explain_your_choices_of_best_and_worst_metrics_explain_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question9', 'i', **kwargs)
    if '(ii) Explain your choices of best and worst metrics' not in correct_answer:
        explanation = "Key: '(ii) Explain your choices of best and worst metrics' not found in instructor answer!\n"
        test_structure_question9_ii_Explain_your_choices_of_best_and_worst_metrics_explain_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(ii) Explain your choices of best and worst metrics']
    student_answer = run_compute('all_questions', 'question9', 's', **kwargs)
    if '(ii) Explain your choices of best and worst metrics' not in student_answer:
        explanation = "Key: '(ii) Explain your choices of best and worst metrics' not found in student answer!\n"
        test_structure_question9_ii_Explain_your_choices_of_best_and_worst_metrics_explain_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(ii) Explain your choices of best and worst metrics']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_explain_str(student_answer)"
    msg_answer = "assert_utilities.check_answer_explain_str(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'explain_str'
    question_id = 'question9'
    subquestion_id = '(ii) Explain your choices of best and worst metrics'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question9_ii_Explain_your_choices_of_best_and_worst_metrics_explain_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question10_a_better_test_based_on_F_minus_measure_ques_str(run_compute):
    function_name = test_structure_question10_a_better_test_based_on_F_minus_measure_ques_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(a) better test based on F-measure?' not in correct_answer:
        explanation = "Key: '(a) better test based on F-measure?' not found in instructor answer!\n"
        test_structure_question10_a_better_test_based_on_F_minus_measure_ques_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) better test based on F-measure?']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(a) better test based on F-measure?' not in student_answer:
        explanation = "Key: '(a) better test based on F-measure?' not found in student answer!\n"
        test_structure_question10_a_better_test_based_on_F_minus_measure_ques_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) better test based on F-measure?']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['T1', 'T2']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question10'
    subquestion_id = '(a) better test based on F-measure?'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question10_a_better_test_based_on_F_minus_measure_ques_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question10_b_better_test_based_on_TPR_slash_FPR_ques_str(run_compute):
    function_name = test_structure_question10_b_better_test_based_on_TPR_slash_FPR_ques_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(b) better test based on TPR/FPR?' not in correct_answer:
        explanation = "Key: '(b) better test based on TPR/FPR?' not found in instructor answer!\n"
        test_structure_question10_b_better_test_based_on_TPR_slash_FPR_ques_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) better test based on TPR/FPR?']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(b) better test based on TPR/FPR?' not in student_answer:
        explanation = "Key: '(b) better test based on TPR/FPR?' not found in student answer!\n"
        test_structure_question10_b_better_test_based_on_TPR_slash_FPR_ques_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) better test based on TPR/FPR?']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['T1', 'T2']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question10'
    subquestion_id = '(b) better test based on TPR/FPR?'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question10_b_better_test_based_on_TPR_slash_FPR_ques_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question10_c_Which_evaluation_measure_to_use_between_the_two_tests_ques_str(run_compute):
    function_name = test_structure_question10_c_Which_evaluation_measure_to_use_between_the_two_tests_ques_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(c) Which evaluation measure to use between the two tests?' not in correct_answer:
        explanation = "Key: '(c) Which evaluation measure to use between the two tests?' not found in instructor answer!\n"
        test_structure_question10_c_Which_evaluation_measure_to_use_between_the_two_tests_ques_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) Which evaluation measure to use between the two tests?']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(c) Which evaluation measure to use between the two tests?' not in student_answer:
        explanation = "Key: '(c) Which evaluation measure to use between the two tests?' not found in student answer!\n"
        test_structure_question10_c_Which_evaluation_measure_to_use_between_the_two_tests_ques_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) Which evaluation measure to use between the two tests?']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    remove_spaces = False
    local_namespace['remove_spaces'] = remove_spaces
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_str(student_answer, choices)"
    msg_answer = "assert_utilities.check_answer_str(student_answer, instructor_answer, str_choices, remove_spaces)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = ['F1', 'TPR/FPR']
    local_namespace['choices'] = choices
    answer_type = 'str'
    question_id = 'question10'
    subquestion_id = '(c) Which evaluation measure to use between the two tests?'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question10_c_Which_evaluation_measure_to_use_between_the_two_tests_ques_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question10_c_Which_evaluation_measure_ques_Explain_explain_str(run_compute):
    function_name = test_structure_question10_c_Which_evaluation_measure_ques_Explain_explain_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(c) Which evaluation measure? Explain' not in correct_answer:
        explanation = "Key: '(c) Which evaluation measure? Explain' not found in instructor answer!\n"
        test_structure_question10_c_Which_evaluation_measure_ques_Explain_explain_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) Which evaluation measure? Explain']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(c) Which evaluation measure? Explain' not in student_answer:
        explanation = "Key: '(c) Which evaluation measure? Explain' not found in student answer!\n"
        test_structure_question10_c_Which_evaluation_measure_ques_Explain_explain_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) Which evaluation measure? Explain']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_explain_str(student_answer)"
    msg_answer = "assert_utilities.check_answer_explain_str(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'explain_str'
    question_id = 'question10'
    subquestion_id = '(c) Which evaluation measure? Explain'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question10_c_Which_evaluation_measure_ques_Explain_explain_str.explanation = explanation
    assert is_success


@hide_errors('')
def test_structure_question10_d_Example_scenario_where_you_would_reverse_choise_in_c_explain_str(run_compute):
    function_name = test_structure_question10_d_Example_scenario_where_you_would_reverse_choise_in_c_explain_str
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(d) Example scenario where you would reverse choise in (c)' not in correct_answer:
        explanation = "Key: '(d) Example scenario where you would reverse choise in (c)' not found in instructor answer!\n"
        test_structure_question10_d_Example_scenario_where_you_would_reverse_choise_in_c_explain_str.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) Example scenario where you would reverse choise in (c)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(d) Example scenario where you would reverse choise in (c)' not in student_answer:
        explanation = "Key: '(d) Example scenario where you would reverse choise in (c)' not found in student answer!\n"
        test_structure_question10_d_Example_scenario_where_you_would_reverse_choise_in_c_explain_str.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d) Example scenario where you would reverse choise in (c)']
    local_namespace = {}
    exclude_indices = []
    local_namespace['exclude_indices'] = exclude_indices
    include_indices = []
    local_namespace['include_indices'] = include_indices
    rel_tol = 0.01
    abs_tol = 0.01
    str_choices = []
    local_namespace['str_choices'] = str_choices
    local_namespace['rel_tol'] = rel_tol
    local_namespace['abs_tol'] = abs_tol
    keys = None
    msg_structure = "assert_utilities.check_structure_explain_str(student_answer)"
    msg_answer = "assert_utilities.check_answer_explain_str(student_answer, instructor_answer)"
    local_namespace.update({'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'keys':keys})
    choices = []
    local_namespace['choices'] = choices
    answer_type = 'explain_str'
    question_id = 'question10'
    subquestion_id = '(d) Example scenario where you would reverse choise in (c)'
    partial_score_frac_l = [0.]
    local_namespace['partial_score_frac_l'] = partial_score_frac_l
    function_name.answer_type = answer_type
    function_name.question_id = question_id
    function_name.subquestion_id = subquestion_id
    function_name.partial_score_frac = partial_score_frac_l[0]
    is_success, explanation_structure = eval(msg_structure, {'__builtins__':{}}, local_namespace)
    explanation = '\n'.join(['==Structure tests==:', explanation_structure])
    test_structure_question10_d_Example_scenario_where_you_would_reverse_choise_in_c_explain_str.explanation = explanation
    assert is_success


