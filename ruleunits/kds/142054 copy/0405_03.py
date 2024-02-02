import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_0405_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 20 54 4.5 (3)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-11-29'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단일 앵커 또는 앵커 그룹에서 개별 앵커의 계수 인장하중'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.5 인장력과 전단력의 동시 작용
    (3)
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
    A[인장력과 전단력의 동시 작용];
    B["KDS 14 20 54 4.5 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 단일 앵커 또는 앵커 그룹에 작용하는 계수전단하중/];
    VarIn2[/입력변수 : 공칭전단강도/];
    VarIn3[/입력변수 : 공칭인장강도/];
    VarIn4[/입력변수 : 단일 앵커 또는 앵커 그룹에서 개별 앵커의 계수인장하중/];
    VarIn1~~~ VarIn3
    VarIn2 ~~~ VarIn4
    end
    Python_Class~~~Variable_def
    D{"<img src='https://latex.codecogs.com/svg.image?\frac{N_{ua}}{\phi&space;N_{n}}\leq&space;0.2'>"};
    E["<img src='https://latex.codecogs.com/svg.image?V_{ua}\leq\phi&space;V_{n}'>"];
    F(["Pass or Fail"])
    Variable_def--->D--Yes--->E--->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Coefficient_shear_load_acting_on_a_single_anchor_or_group_of_anchors(fINua,fINn,fIVn,fIVua) -> float:
        """단일 앵커 또는 앵커 그룹에 작용하는 계수전단하중

        Args:
            fINua (float): 단일 앵커 또는 앵커 그룹에 작용하는 계수전단하중
            fINn (float): 공칭전단강도
            fIVn (float): 공칭인장강도
            fIVua (float): 단일 앵커 또는 앵커 그룹에서 개별 앵커의 계수인장하중

        Returns:
            float: 콘크리트용 앵커 설계기준  4.5 인장력과 전단력의 동시 작용 (3)의 통과 여부

        """

        if fINua/fINn <= 0.2
          if fIVn >= fIVua :
              return "Pass"
          else:
              return "Fail"


# 

