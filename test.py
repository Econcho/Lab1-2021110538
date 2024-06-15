import pytest
import WordGraph
import coverage


def test_queryBridgeWords():
    f = WordGraph.WordGraph()
    f.generateGraph('./test.txt')

    # 1-2-3
    case_1 = ['explor', 'strange']
    assert f.queryBridgeWords(case_1[0], case_1[1]) == -1

    # 1-2-4-5
    case_2 = ['new', 'lif']
    assert f.queryBridgeWords(case_2[0], case_2[1]) == -2

    # 1-2-4-6-7-8-9-10-11-12-13
    case_3 = ['seek', 'new']
    assert f.queryBridgeWords(case_3[0], case_3[1]) == ['out']

    # 1-2-4-6-7-8-9-10-7-8-10-11-12-13
    case_4 = ['out', 'life']
    assert f.queryBridgeWords(case_4[0], case_4[1]) == ['new']

    # 1-2-4-6-7-8-9-10-11-6-7-8-10-11-12-13
    case_5 = ['To', 'strange']
    assert f.queryBridgeWords(case_5[0], case_5[1]) == ['explore']

    # 1-2-4-6-7-8-10-11-12-14
    case_6 = ['worlds', 'out']
    assert f.queryBridgeWords(case_6[0], case_6[1]) == -3

    # 1-2-4-6-7-8-10-11-6-7-8-10-11-12-14
    case_7 = ['to', 'new']
    assert f.queryBridgeWords(case_7[0], case_7[1]) == -3



