import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0304_10_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.4 (10) ③'
    ref_date = '2022-02-23'
    doc_date = '2023-11-15'
    title = '이동식 사다리의 설치'

    description = """
    작업발판 및 통로
    3. 시공
    3.4 사다리
    (10)
    ③
    """

    content = """
    #### 3.4 사다리
    (10) 이동식 사다리는 다음 항에 적합하여야 한다.
    ③ 사다리 폭은 300mm 이상이어야 하며, 발 받침대 간격은 250mm ∼ 350mm 이내로 하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 이동식 사다리의 설치];
    B["KCS 21 60 15 3.4 (10) ③"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.4 (10) ③"])

    subgraph Variable_def
    VarIn1[/입력변수: 사다리 폭/];
    VarIn2[/입력변수: 발 받침대 간격/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"사다리 폭 >= 300mm"}
    Variable_def --> C2{"250mm <= 발 받침대 간격 <= 350mm"}
    C1 & C2 --> D(["Pass or Fail"]);
    """

    @rule_method
    def Length_of_Portable_Ladder(fIWidLad, fISpaFoo) -> bool:
        """ 이동식 사다리의 설치
        Args:
        fIWidLad (float): 사다리 폭
        fISpaFoo (float): 발 받침대 간격

        Returns:
        pass_fail (bool): 작업발판 및 통로 3.4 사다리 (10) ③의 판단 결과
        """
        assert isinstance(fIWidLad, float)
        assert isinstance(fISpaFoo, float)

        if fIWidLad >= 300 and 250 <= fISpaFoo <= 350:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )