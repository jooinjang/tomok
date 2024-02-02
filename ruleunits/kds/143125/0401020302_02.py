import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0401020302_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.2.3.2 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '플러그용접을 위한 구멍의 직경'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.3 플러그 및 슬롯용접
    4.1.2.3.2 제한사항
    (2)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A([플러그용접을 위한 구멍의 직경])
	  B["KDS 14 31 25 4.1.2.3.2(2)"]
	  A ~~~ B
  	end

  	subgraph Variable_def
	  VarOut[/출력변수: 플러그용접을 위한 구멍의 직경/]
	  VarIn1[/입력변수: 구멍이 있는 판의 두께/]
	  VarIn2[/입력변수: 용접두께/]
	  VarIn3[/입력변수: 최소직경/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
  	end

	  Python_Class ~~~ Variable_def --> D --> F

  	D["구멍이 있는 판의 두께+8mm ≤ 플러그용접을 위한 구멍의 직경 ≤ 용접두께x2.25 or 최소직경+3mm"]
  	F(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def diameter_of_holes_for_plug_welding(fIdihopw,fIthpepl,fIwelthi,fImindia) -> bool:
        """플러그용접을 위한 구멍의 직경

        Args:
            fIdihopw (float): 플러그용접을 위한 구멍의 직경
            fIthpepl (float): 구멍이 있는 판의 두께
            fIwelthi (float): 용접 두께
            fImindia (float): 최소 직경

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.3.2 제한사항 (2)의 통과 여부
        """
        if (fIthpepl+8) <= fIdihopw <= (fIwelthi*2.25 or fImindia+3) :
          return "Pass"
        else:
          return "Fail"


# 

