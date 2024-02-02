import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060303_05(RuleUnit): # KDS241711_04060303_05

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.3.3 (5)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-12'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '최대간격'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.3 축방향철근과 횡방향철근
    (5)
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
	A([축방향철근과 횡방향철근])
	B["KDS 24 17 11 4.6.3.3(4)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarIn1[/입력변수: 최대간격/]
	VarIn2[/입력변수: 부재 최소 단면치수/]
	VarIn3[/입력변수: 축방향철근지름/]
	end

	Python_Class ~~~ Variable_def--> I

I-->J
	I["min(부재 최소 단면치수x1/4,축방향철근지름x6) &ge; 최대간격"]
	J([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def maximum_spacing(fImaxspa,fImicsdm,fIaxredi) -> bool:
        """최대간격

        Args:
            fImaxspa (float): 최대간격
            fImicsdm (float): 부재 최소 단면치수
            fIaxredi (float): 축방향철근지름

        Returns:
            bool: 교량내진설계기준(한계상태설계법) 4.6.3.3 축방향철근과 횡방향철근 (5)의 통과 여부
        """

        if min(fImicsdm * 0.25, fIaxredi * 6) >= fImaxspa:
          return "Pass"
        else:
          return "Fail"