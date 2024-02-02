import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_04060202_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.2.2 (2)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-27'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '바닥판의 해석방법 설계일반'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.2 바닥판의 해석방법
    4.6.2.2 설계일반
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
     A[철근콘크리트 바닥판에 사용하는 콘크리트 설계기준강도];
     B["KDS 24 10 11 4.6.2.2 (2)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarIn1[/입력변수 : 콘크리트의 설계기준강도/];
    end
    Python_Class~~~Variable_def
    D["콘크리트의 설계기준강도 &ge; 27MPa"];
    E(["Pass or Fail"]);
    Variable_def--->D--->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def specified_design_strength(fIfck) -> bool:
        """콘크리트의 설계기준강도가 KDS 24 10 11 4.6.2.2 (2)의 기준을 만족하는지 여부

        Args:
            fIfck (float): 콘크리트의 설계기준강도.

        Returns:
            bool: 교량 설계 일반사항(한계상태설계법) 콘크리트의 설계기준강도가 KDS 24 10 11 4.6.2.2 (2)의 기준을 만족하는지 여부
        """

        if fIfck>=27:
              return 'Pass'
        else:
              return 'Fail'


