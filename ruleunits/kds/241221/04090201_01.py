import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04090201_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.9.2.1 (1)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '유수에 의한 종방향 압력'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.9 정수압, 유수압, 부력, 파압: WA, BP, WP
    4.9.2 유수압
    4.9.2.1 종방향
    (1)
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
          A[하부구조물에 종방향으로 작용되는 유수에 의한 압력];
        B["KDS 24 12 21 4.9.2.1 (1)"];
        A ~~~ B
        end
      subgraph Variable_def
    VarOut[/출력변수 : 유수에 읳나 압력/];
    VarIn1[/입력변수 : 교각의 기하학적 형상에 따른 항력계수/];
    VarIn2[/입력변수 : 설계홍수시의 설계유속/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class~~~Variable_def
    D["<img src='https://latex.codecogs.com/svg.image?p=0.514C_{D}V^{2}'>-----------------"];
    E(["유수에 의한 압력"]);
    Variable_def--->D--->E
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Longitudinal_pressure_caused_by_running_water(fOp,fICD,fIV) -> float:
        """유수에 의한 종방향 압력

        Args:
            fOp (float): 유수에 의한 압력
            fICD (float): 교각의 기하학적 형상에 따른 항력계수
            fIV (float): 설계홍수시의 설계유속


        Returns:
            float: 강교 설계기준(한계상태설계법) 4.9.2.1 종방향 (1) 의 값
        """

        fOp = 0.514*fICD*fIV**2
        return(fOp)


# 
