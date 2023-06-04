#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """Validate if m_a is a list"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    """Validate if m_b is a list"""
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    """Validate if m_a is a list of lists"""
    if any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    """Validate if m_b is a list of lists"""
    if any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    """Validate if m_a is not empty"""
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")

    """Validate if m_b is not empty"""
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    """Validate if m_a contains only integers or floats"""
    if any(not isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")

    """Validate if m_b contains only integers or floats"""
    if any(not isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    """Validate if m_a and m_b are rectangles"""
    a_num_columns = len(m_a[0])
    if any(len(row) != a_num_columns for row in m_a):
        raise ValueError("each row of m_a must be of the same size")

    b_num_columns = len(m_b[0])
    if any(len(row) != b_num_columns for row in m_b):
        raise ValueError("each row of m_b must be of the same size")

    """Validate if m_a and m_b can be multiplied"""
    if a_num_columns != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """Perform matrix multiplication"""
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        result.append(row)

    return (result)
