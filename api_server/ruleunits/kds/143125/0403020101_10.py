import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020101_10(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.1.1 (10)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '강재의 항복강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.1 적용한계
    (10)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 강재의 항복강도]
	  B["KDS 14 31 25 4.3.2.1.1 (10)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 강재의 항복강도/]
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.1.1 (10)"])
		C --> Variable_def

	  D{"<img src='https://latex.codecogs.com/svg.image?F_{y}\leq&space;360MPa'>----------------------------------------------"} ;
		Variable_def --> D --> F(["PASS or Fail"])
    """

    @rule_method
    def Yield_strength_of_steel(fIFy) -> RuleUnitResult:
        """강재의 항복강도

        Args:
            fIFy (float): 강재의 항복강도

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1.1 적용한계 (10)의 판단 결과
        """

        assert isinstance(fIFy, float)

        if fIFy <= 360:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )