import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS115040_020113_03(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 11 50 40 2.1.13 (3)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-15'
    title = '압축 정재하시험 시 반력장치와 시험말뚝과의 간격'

    # 건설기준문서항목 (분류체계정보)
    description = """
    말뚝재하시험
    2. 시험
    2.1 압축 정재하시험
    2.1.13 반력장치
    (3)
    """

    # 건설기준문서내용(text)
    content = """
        ####2.1.13 반력장치
        (3) 시험말뚝과 반력말뚝 또는 지반앵커와의 중심 간격, 혹은 시험말뚝 중심과 받침대의 간격은 시험말뚝 최대지름의 3배 혹은 1.5 m 이상을 원칙으로 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
        flowchart TD
        subgraph Python_Class
        A[Title: 압축 정재하시험 시 반력장치와 시험말뚝과의 간격];
        B["KCS 11 50 40 2.1.13 (3)"];
        B ~~~ A
        end

        KCS(["KCS 11 50 40 2.1.13 (3)"])

        subgraph Variable_def
        VarOut[/출력변수: 시험말뚝과의 간격/];
        VarIn1[/입력변수: 시험말뚝과 반력말뚝의 중심 간격/];
        VarIn2[/입력변수: 시험말뚝과 지반앵커와의 중심 간격/];
        VarIn3[/입력변수: 시험말뚝 중심과 받침대의 간격/];
        VarIn4[/입력변수: 시험말뚝 최대지름/];
        VarOut ~~~ VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
        end

        Python_Class ~~~ KCS
        KCS --> Variable_def
        Variable_def --> C{"시험말뚝과 반력말뚝의 중심 간격 \n & 시험말뚝과 지반앵커와의 중심 간격 \n& 시험말뚝 중심과 받침대의 간격 \n ≥ max(시험말뚝 최대지름*3.5, 1.5) \n."}
        C --> |True|Pass([Pass])
        C --> |False|Fail([Fail])
    """

    @rule_method
    def spacing_test_pile(fITesRea, fITesGro, fITesPed, fIDiaTes):
        """
        Args:
            fITesRea (float): 시험말뚝과 반력말뚝의 중심 간격
            fITesGro (float): 시험말뚝과 지반앵커와의 중심 간격
            fITesPed (float): 시험말뚝 중심과 받침대의 간격
            fIDiaTes (float): 시험말뚝 최대지름
        Returns:
            sOSpaTes (string): 말뚝의 허용오차
        """
        if fITesRea >= max(fIDiaTes*3, 1.5) and fITesGro >= max(fIDiaTes*3, 1.5) and fITesPed >= max(fIDiaTes*3, 1.5) :
            sOSpaTes = "Pass"
        else:
            sOSpaTes = "Fail"
        return sOSpaTes