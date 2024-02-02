import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040402_08 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.4.2 (8)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-10-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '앵커가 정착되는 부재 두께 (앵커 축과 평행한 방향)'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도
    (8)
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
    A[수정계수];
    B["KDS 14 20 54 4.4.2 (8)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 수정계수/];
    VarIn1[/입력변수 : 앵커가 정착되는 부재 두께:앵커축과평행한 방향/];
    VarIn2[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지의 거리/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class~~~Variable_def
    D{"<img src='https://latex.codecogs.com/svg.image?h_{a}<1.5c_{a1}'>인 부재에 사용되는 앵커인 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{h,V}=\sqrt{\frac{1.5c_{a1}}{h_{a}}}(\geq&space;1)'>------------------------------"];
    F(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{h,V}'>"]);
    Variable_def--->D--->E--->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def thickness_of_the_member_to_which_the_anchor_is_anchored(fIha,fIcaone,fOpsihV) -> float:
        """앵커가 정착되는 부재 두께 (앵커 축과 평행한 방향)

        Args:
            fIha (float): 앵커가 정착되는 부재 두께(앵커축과평행한방향)
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트 단부까지의 거리
            fOpsihV (float): 수정계수

        Returns:
            float: 콘크리트용 앵커 설계기준  4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도 (8)의 값
        """

        if fIha < 1.5*fIcaone:
          fOpsihV = max((1.5 * fIcaone / fIha)**0.5, 1.0)
          return fOpsihV


