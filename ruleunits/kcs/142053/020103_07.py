import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142053_020103_07(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 14 20 53 2.1.3 (7)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '그라우트의 물-결합재비'

    # 건설기준문서항목 (분류체계정보)
    description = """
    프리스트레스트 콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 프리스트레스트 콘크리트용 그라우트
    (7)
    """

    # 건설기준문서내용(text)
    content = """
    ####(7) 그라우트의 물-결합재비는 45 % 이하로 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 그라우트의 물-결합재비];
    B["KCS 14 20 53 2.1.3 (7)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 2.1.3 (7)"])

    subgraph Variable_def
    VarOut[/출력변수: 그라우트의 물-결합재비/];
    VarIn1[/입력변수: 그라우트의 물-결합재비/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C["그라우트의 물-결합재비 ≤ 45"]
    C --> |True|Pass(["Pass"])
    C --> |True|Fail(["Fail"])
    """

    @rule_method
    def water_binder_ratio(fIWatRat):
        """
        Args:
            fIWatRat (float): 그라우트의 물-결합재비
        Returns:
            sOWatRat (sting): 그라우트의 물-결합재비
        """
        if fIWatRat <= 45:
            sOWatRat = "Pass"
        else:
            sOWatRat = "Fail"
        return sOWatRat