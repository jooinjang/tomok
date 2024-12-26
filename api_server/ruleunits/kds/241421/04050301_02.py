import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04050301_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.5.3.1 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '프리캐스트 콘크리트에서 철근의 수평 순간격'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.3 철근의 간격
    4.5.3.1 철근의 최소간격
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 프리캐스트 콘크리트에서 철근의 수평 순간격];
    B["KDS 24 14 21 4.5.3.1 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;

		VarIn1["철근의 수평 순간격"]
		VarIn2["철근 공칭지름"]
		VarIn3["굵은 골재의 최대치수"]

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.5.3.1 (2)"])
		C --> Variable_def

		Variable_def--->G & D & E--->F
		G{"철근의 수평 순각격≥철근 공칭지름"}
		D{"철근의 수평 순각격≥굵은 골재 최대치수X1.33"}
		E{"철근의 수평 순각격≥25mm"}
		F(["Pass or fail"])
    """

    @rule_method
    def Horizontal_moment_spacing_of_rebar_in_precast_concrete(fIhorins,fIrebnod,fImaxsco) -> RuleUnitResult:
        """프리캐스트 콘크리트에서 철근의 수평 순간격

        Args:
            fIhorins (float): 철근의 수평 순간격
            fIrebnod (float): 철근 공칭지름
            fImaxsco (float): 굵은 골재의 최대치수

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.5.3.1 철근의 최소간격 (2)의 판단 결과
        """

        assert isinstance(fIhorins, float)
        assert isinstance(fIrebnod, float)
        assert isinstance(fImaxsco, float)

        if fIhorins >= max(fIrebnod, fImaxsco*1.33, 25):
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