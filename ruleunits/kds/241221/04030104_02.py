import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04030104_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.3.1.4 (2)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-12-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '차륜의 접지면'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.1 차량활하중 : LL
    4.3.1.4 바닥판과 바닥틀을 설계하는 경우의 설계차량활하중
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
        A[다차로 재하계수];
        B["KDS 24 12 21 4.3.1.2"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 다차로 재하계수/];
    VarIn1[/입력변수 : 재하차로의 수/];
    end
    Python_Class~~~Variable_def
    D{"재하차로의 수"};
    E["다차로 재하계수=1.0"];
    F["다차로 재하계수=0.9"];
    G["다차로 재하계수=0.8"];
    H["다차로 재하계수=0.7"];
    I["다차로 재하계수=0.65"];
    J(["다차로 재하계수"]);
    Variable_def--->D--1--->E--->J
    D--2--->F--->J
    D--3--->G--->J
    D--4--->H--->J
    D--5이상--->I--->J
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def multiple_lane_loading_coefficient(fOm,fINlane) -> float:
        """차륜의 접지면

        Args:
            fOm (float): 다차로 재하계수
            fINlane (float): 재하차로의 수

        Returns:
            float: 강교 설계기준(한계상태설계법)  4.3.1.2 활하중의 동시재하 의 값
        """
        if fINlane ==1:
          fOm = 1.0
        elif fINlane ==2:
          fOm = 0.9
        elif fINlane ==3:
          fOm = 0.8
        elif fINlane ==4:
          fOm = 0.7
        elif fINlane ==5:
          fOm = 0.65

        return(fOm)


# 

