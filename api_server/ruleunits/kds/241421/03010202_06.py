import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010202_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.2 (6)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '시간에 따른 탄성계수'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.2 탄성변형
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 시간에 따른 탄성계수];
    B["KDS 24 14 21 3.1.2.2 (6)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 보통 콘크리트 탄성계수/];
    VarIn2[/입력변수: 강도 보정 계수/] ;
 	  VarOut1[/출력변수: 시간에 따른 탄성계수/];


	  VarOut1~~~VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.2 (6)"])
		C --> Variable_def

		Variable_def---->D-->G

		D["<img src='https://latex.codecogs.com/svg.image?&space;E_{c}(t)=\sqrt{\beta_{cc}}E_{c}'>--------------------------------------------------------"]

		G(["시간에 따른 탄성계수"]);
    """

    @rule_method
    def Youngs_modulus_as_a_function_of_time(fIEc,fIbetcct) -> RuleUnitResult:
        """시간에 따른 탄성계수

        Args:
            fIEc (float): 보통 콘크리트의 탄성계수
            fIbetcct (float): 강도 보정 계수

        Returns:
            fOEct (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.2 탄성변형 (6)의 값
        """

        assert isinstance(fIEc, float)
        assert isinstance(fIbetcct, float)
        assert fIbetcct > 0

        fOEct = fIbetcct**0.5 * fIEc

        return RuleUnitResult(
            result_variables = {
                "fOEct": fOEct,
            }
        )