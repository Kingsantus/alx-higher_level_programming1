#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        result = np.matmul(np_a, np_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except Exception as e:
        raise type(e)(str(e))
