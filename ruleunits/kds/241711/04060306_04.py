import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060306_04(RuleUnit): # KDS241711_04060306_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.3.6 (4)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-13'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '축방향철근 중심각 수평간격'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.6 결합나선철근
    (4)
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
    A[Title: 결합나선철근];
    B["KDS 24 17 11 4.6.3.6 (4)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 축방향철근 중심 각 수평간격/] ;
    VarIn2[/입력변수: 축방향철근/];
    end

      Python_Class ~~~ Variable_def -->D--> I

    D[" 200mm &ge; 축방향철근 중심간 수평간격 and 결합부분 축방향철근 배근 &ge; 4개"]
   	I([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def axial_reinforcing_bar(fIcahsar,fIlonrei) -> bool:
        """축방향철근 중심각 수평간격

        Args:
            fIcahsar (float): 축방향철근 중심간 수평간격
            fIlonrei (float): 축방향철근

        Returns:
            bool: 교량내진설계기준(한계상태설계법) 4.6.3.6 결합나선철근 (4)의 통과 여부
        """

        if fIcahsar <= 200 and fIlonrei >= 4:
          return "Pass"
        else:
          return "Fail"